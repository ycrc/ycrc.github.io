# Practical Example: Python+TensorFlow

Notes on [handson-ml2](https://github.com/ageron/handson-ml2) for YCRC clusters [Grace](/clusters/grace/) & [Farnam](/clusters/farnam/)

## Prerequisites

- Basic understanding of command line shell commands and syntax
- A Yale NetID
- An active [Yale VPN](https://yale.service-now.com/it?id=service_offering&sys_id=c4684dcd6fbb31007ee2abcf9f3ee4f2) connection
- A YCRC [Cluster account](https://research.computing.yale.edu/support/hpc/account-request)

## Setup

1. Log in to [OOD](/clusters-at-yale/access/ood/) for the cluster you have an account on with NetID and Password.

1. Start a new interactive shell.

    "Shell" > "Clustername Shell Access"

    ![shell navigation menu](/img/handson-ml2_00.png)

1. Start an [interactive job](/clusters-at-yale/job-scheduling/#interactive-jobs).

    ``` bash
    srun --pty -c 2 -p interactive bash
    ```

    | `srun` Argument  | Description |
    | ---------------- | ----------- |
    | `--pty`          | Start a pseudo terminal in the job |
    | `-c 2`           | Allocate two CPU cores (and default 5GiB RAM per core) |
    | `-p interactive` | Start the job on the `interactive` partition (meant for work like this) |
    | `bash`           | Run the bash shell |

1. Clone the repo from [GitHub](/clusters-at-yale/guides/github/).

    ``` bash
    mkdir -p ~/repos
    cd ~/repos
    git clone https://github.com/ageron/handson-ml2.git
    ```

1. Create the [Conda](/clusters-at-yale/guides/conda/) environment used in the book, index it for the YCRC [Open Ondemand](/clusters-at-yale/access/ood/) web dashboard.

    ``` bash
    module load miniconda
    cd ~/repos/handson-ml2
    # environment creation will take a few minutes
    conda env create -f environment.yml
    conda activate tf2
    # swap out tf with gpu-enabled tf
    pip uninstall tensorflow
    pip install tensorflow-gpu==2.4.1
    ycrc_conda_env.list build
    ```

## Start a Notebook

1. Log in to [OOD](/clusters-at-yale/access/ood/) for the cluster you have an account on with NetID and Password.

1. Navigate to the Jupyter job submission form.

    "Interactive Apps" > "Jupyter Notebook"

    ![interactive apps navigation menu](/img/handson-ml2_01.png)

1. Set up the request.

    !!! warning "GPUs and their needs"
        Not all partitions have GPUs, they must be requested explicitly, and you need to load the right version of CUDA + cuDNN.

    To make this environment work properly in your jupyter job you need to

    - Choose your `tf2` environment from the "Environment Setup" dropdown

        ![conda environment choice](/img/handson-ml2_notebook01.png)

    - Set "Number of GPUs per node" to at least 1.

        ![GPU choice](/img/handson-ml2_notebook02.png)

    - Set a partition with GPUs available.

        ![GPU partition](/img/handson-ml2_notebook03.png)

    - Load the right cuDNN module (will also load a CUDA module). For this environment, that's `cuDNN/8.0.5.39-CUDA-11.1.1` .

        ![cuDNN module choice](/img/handson-ml2_notebook04.png)

        !!! tip "What version of CUDA?"
            If you are not installing things for yourself or don't know what CUDA version you need, try importing GPU-enabled `tensorflow` and look at the output:
            ``` python
            Python 3.7.10 | packaged by conda-forge | (default, Feb 19 2021, 16:07:37)
            [GCC 9.3.0] on linux
            Type "help", "copyright", "credits" or "license" for more information.
            >>> import tensorflow as tf
            2021-03-26 08:50:40.092738: W tensorflow/stream_executor/platform/default/dso_loader.cc:60] Could not load dynamic library'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
            2021-03-26 08:50:40.092780: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do nothave a GPU set up on your machine.
            ```
            Notice it complains about not finding `libcudart.so.11.0`. The numbers at the end of this shared object usually correspond ot a CUDA version, so here we will use CUDA 11.

    Then click the Launch button. Depending on how busy the cluster is your job may need to wait in the queue.

1. Connect to the Jupyter Server.

    ![Jupyter job connection button](/img/handson-ml2_notebook05.png)

## Containers - `tensorflow/serving`

You can use TensorFlow Serving to serve multiple versions of models but examples given use Ubuntu packages or Docker. YCRC clusters are RHEL and do not allow Docker, so instead we use [Apptainer](/clusters-at-yale/guides/containers)

``` bash
docker pull tensorflow/serving

export ML_PATH=$HOME/ml # or wherever this project is
docker run -it --rm -p 8500:8500 -p 8501:8501 \
   -v "$ML_PATH/my_mnist_model:/models/my_mnist_model" \
   -e MODEL_NAME=my_mnist_model \
   tensorflow/serving
```

``` bash
singularity build tf_model_server.sif docker://tensorflow/serving

export ML_PATH=$HOME/repos/handson-ml2
singularity run --containall -B "$ML_PATH/my_mnist_model:/models/my_mnist_model" \
    --env MODEL_NAME=my_mnist_model tf_model_server.sif
```

- Only need to build `.sif` file when you would run `docker pull`
- Don't need to forward ports out of container
- `--containall` makes singularity run more like docker, allows finer control of what files container sees

## Heterogeneous Job Layouts

If you want to allocate multiple node types in a single job, e.g. a larger first task/worker for a tf "chief" or a CPU-only parameter server. 

``` bash
#!/bin/bash
#SBATCH --partition=gpu --time=1- --ntasks=1 --cpus-per-task=4
#SBATCH --mem-per-cpu=8G --gpus-per-task=1 --job-name=tf2-cluster-chief
#SBATCH hetjob
#SBATCH --ntasks=8 --cpus-per-task=2 
#SBATCH --mem-per-cpu=16G --gpus-per-task=1

module load miniconda cuDNN/8.0.5.39-CUDA-11.1.1
conda activate tf2

# this python process will start on a node in the gpu partition with 4 CPUs & 1 GPU
python cluster_tf.py
```

``` bash
#!/bin/bash
#SBATCH --partition=day --time=1- --ntasks=1 --cpus-per-task=2
#SBATCH --mem-per-cpu=8G --job-name=tf2-cluster-par-serv
#SBATCH hetjob
#SBATCH --partition=gpu --ntasks=8 --cpus-per-task=2 
#SBATCH --mem-per-cpu=16G --gpus-per-task=1

module load miniconda cuDNN/8.0.5.39-CUDA-11.1.1
conda activate tf2

# this python process will start on a node in the day partition with 2 CPUs
python cluster_tf.py

```
