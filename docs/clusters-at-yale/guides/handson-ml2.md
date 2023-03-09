# Practical Example: Python+TensorFlow

Notes on installing and testing [tensorflow](https://www.tensorflow.org/install/pip) for YCRC clusters [Grace](/clusters/grace/) & [McCleary](/clusters/mccleary/)

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
    salloc -c 2 -p interactive
    ```

    | `salloc` Argument  | Description |
    | ---------------- | ----------- |
    | `-c 2`           | Allocate two CPU cores (and default 5GiB RAM per core) |
    | `-p interactive` | Start the job on the `interactive` partition (meant for work like this) |

1. Create the [Conda](/clusters-at-yale/guides/conda/) environment for tensorflow, index it for the YCRC [Open Ondemand](/clusters-at-yale/access/ood/) web dashboard.

    ``` bash
    module load miniconda
    mamba create --name tf2 python=3.9 cudatoolkit=11.2.2 cudnn=8.1.0 jupyter jupyterlab
    # environment creation will take a few minutes
    conda activate tf2
    # Do not install tensorflow with conda, it is no longer supported
    pip install tensorflow==2.11.*
    # configure system paths to point to python libraries
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    #run command to add to list of jupyter note book environments
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
apptainer build tf_model_server.sif docker://tensorflow/serving

export ML_PATH=$HOME/repos/handson-ml2
apptainer run --containall -B "$ML_PATH/my_mnist_model:/models/my_mnist_model" \
    --env MODEL_NAME=my_mnist_model tf_model_server.sif
```

- Only need to build `.sif` file when you would run `docker pull`
- Don't need to forward ports out of container
- `--containall` makes apptainer run more like docker, allows finer control of what files container sees

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
