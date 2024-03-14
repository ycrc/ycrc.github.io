# GPUs and CUDA

There are GPUs available for general use on the YCRC clusters. In order to use them, you must [request them for your job](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus). See the [Grace](/clusters/grace), [McCleary](/clusters/mccleary), and [Milgram](/clusters/milgram) pages for hardware and partition specifics. Please do not use nodes with GPUs unless your application or job can make use of them. Any jobs submitted to a GPU partition without having requested a GPU may be terminated without warning.

## Monitor Activity and Drivers

The CUDA libraries you load will allow you to compile code against them. To run CUDA-enabled code you must also be running on a node with a gpu allocated and a compatible driver installed. The minimum driver versions are listed on [this nvidia developer site](https://docs.nvidia.com/deploy/cuda-compatibility/index.html).

You can check the available GPUs, their current usage, installed version of the nvidia drivers, and more with the command [`nvidia-smi`](https://developer.nvidia.com/nvidia-system-management-interface). Either in an interactive job or after connecting to a node running your job with `ssh`,  `nvidia-smi` output should look something like this:

``` bash
[user@gpu01 ~]$ nvidia-smi
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
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

Here we see that the node `gpu01` is running driver version 460.32.03 and is compatible with CUDA version 11.2. There are no processes using the GPU allocated to this job.

## Software

###Cuda, cuDNN, tensorflow, and pytorch availability on cluster

We have built certain versions of CUDA, cuDNN, tensorflow, and pytorch on all the clusters YCRC maintains. If one of the versions of these modules aligns with the version needed for your research, then there may be no need to install these programs yourself. To list all the modules available for these programs:

``` bash
module avail cuda/
module avail cudnn/
module avail tensorflow
module avail pytorch
```

### Tensorflow

Instructions for installing tensorflow on our clusters can be found [here](https://docs.ycrc.yale.edu/clusters-at-yale/guides/tensorflow/)


### PyTorch

Instructions for installing tensorflow on our clusters can be found [here](https://docs.ycrc.yale.edu/clusters-at-yale/guides/pytorch/)

## Compile `.c` or `.cpp` Files with CUDA code

By default, `nvcc` expects that host code is in files with a `.c` or `.cpp` extension, and device code is in files with a `.cu` extension. When you mix device code in a `.c` or `.cpp` file with host code, the device code will not be recoganized by `nvcc` unless you add this flag: `-x cu`.  

``` bash
nvcc -x cu mycuda.cpp -o mycuda.exe
```     
