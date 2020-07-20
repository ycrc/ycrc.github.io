# GPUs and CUDA

There are GPUs available for general use on [Grace](/clusters-at-yale/clusters/grace) and [Farnam](/clusters-at-yale/clusters/farnam). See cluster pages for hardware and queue/partition specifics. Please do not use nodes with GPUs unless your application or job can make use of them. Any jobs submitted to a GPU partition without having requested a GPU may be terminated without warning.

## Requesting GPU Nodes

To access the GPU nodes you must request them with slurm. Here is an example command to request a 2 hour interactive job for testing or developing code interactively:

``` bash
srun --pty -p gpu_devel -c 2 -t 2:00:00 --gres=gpu:1 bash
```

or, if the `gpu_devel` and `gpu` partitions are busy, try to scavenge some private GPUs:

``` bash
srun --pty -p scavenge_gpu -c 2 -t 2:00:00 --gres=gpu:1 bash
```

!!! note
    The `--gres` option specifies resources **per node**, not per task or core. In a two node job, `--gres=gpu:2` would result in a total of four GPUs allocated to you.

### Specific GPUs

To request a specific type of GPU (e.g. a P100) for each node in your job, you specify the GPU type in the `--gres` flag.

``` bash
#SBATCH --gres=gpu:p100:1
```

Some applications require double-precision capable GPUs. If applicable, you can request any node with a compatible GPU by using the `doubleprecision` feature (e.g. K80, P100 or V100).

``` bash
#SBATCH -C doubleprecision
```

Conversely, you can use the `singleprecision` feature to request nodes that have single-precision only GPUs (e.g. GTX 1080, RTX 2080).

## Monitor Activity and Drivers

The CUDA libraries you load will allow you to compile code against them. To run CUDA-enabled code you must also be running on a node with a gpu allocated and a compatible driver installed. The minimum driver versions are listed on [this nvidia developer site](https://docs.nvidia.com/deploy/cuda-compatibility/index.html).

You can check the available GPUs, their current usage, installed version of the nvidia drivers, and more with the command [`nvidia-smi`](https://developer.nvidia.com/nvidia-system-management-interface). Either in an interactive job or after connecting to a node running your job with `ssh`,  `nvidia-smi` output should look something like this:

``` bash
[user@gpu01 ~]$ nvidia-smi
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.87.00    Driver Version: 418.87.00    CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 108...  On   | 00000000:02:00.0 Off |                  N/A |
| 23%   34C    P8     9W / 250W |      1MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

Here we see that the node `gpu01` is running driver version 418.87.00 and CUDA version 10.1\. There are no processes using the GPU allocated to this job.

## Software

### CUDA and cuDNN modules

We have seen varying degrees of success in using the runtime CUDA and cuDNN libraries supplied by various conda channels. If that works for you there may be no need to load additional modules. If not, find the corresponding CUDA and cuDNN combination for your desired environment and load or request those modules. To list all the CUDA and cuDNN modules available:

``` bash
module avail cuda/
module avail cudnn/
```

### Tensorflow

You can find hints about the correct version of Tensorflow from their [tested build configurations](https://www.tensorflow.org/install/source#tested_build_configurations). You can also test your install with a simple script that imports Tensorflow (run on a GPU node). If you an `ImportError` that mentions missing libraries like `libcublas.so.9.0`, for example, that means that Tensorflow is probably expecting CUDA v 9.0 but cannot find it.

### PyTorch

As with Tensorflow, sometimes the conda-supplied CUDA libraries are sufficient for the version of PyTorch you are installing. If not make sure you have the version of cuda referenced on the PyTorch site [in their install instructions](https://pytorch.org/get-started/locally/). They also provide [instructions on installing previous versions](https://pytorch.org/get-started/previous-versions/) compatible with older versions of CUDA.

### Create an Example Tensorflow-GPU Environment

``` bash
# example modules for tensorflow 1.12
module purge
module load cuDNN/7.1.4-CUDA-9.0.176
module load miniconda
```

Then save your modules as a collection.

``` bash
# save module environment
module save cuda90
```

Now create a virtual environment for your GPU enabled code. For more details on Conda environments, see our [Conda documentation](/clusters-at-yale/guides/conda).

``` bash
# create conda environment for deep learning/neural networks
conda create -y -n tensorflow112 python=3.6 anaconda
source activate tensorflow112

#install libraries
pip install keras tensorflow-gpu==1.12
```

## Use Your Environment

To re-enter your environment you only need the following:

``` bash
module restore cuda90
source activate tensorflow112
```

## Compile `.c` or `.cpp` Files with CUDA code

By default, `nvcc` expects that host code is in files with a `.c` or `.cpp` extension, and device code is in files with a `.cu` extension. When you mix device code in a `.c` or `.cpp` file with host code, the device code will not be recoganized by `nvcc` unless you add this flag: `-x cu`.  

``` bash
nvcc -x cu mycuda.cpp -o mycuda.exe
```     
