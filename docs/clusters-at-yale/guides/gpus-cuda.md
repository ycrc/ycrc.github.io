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

You can find hints about the correct version of Tensorflow from their [tested build configurations](https://www.tensorflow.org/install/source#tested_build_configurations). You can also test your install with a simple script that imports Tensorflow (run on a GPU node). If you an `ImportError` that mentions missing libraries like `libcublas.so.9.0`, for example, that means that Tensorflow is probably expecting CUDA v 9.0 but cannot find it.

### Tensorflow-gpu 
Tensorflow-gpu is now depreciated for newer versions of CUDA and cuDNN and has been combined with the original tensorflow. Any version of tensorflow 2.* contains gpu capabilities and should be installed instead of attempting to install tensorflow-gpu.

#### Create an Example Tensorflow Environment

To create a conda environment with Tensorflow and uses the module CUDA:

```bash
# load modules, including the system CUDA and cuDNN
module load miniconda CUDAcore/11.2.2 cuDNN/8.1.1.33-CUDA-11.2.2
# save module collection for future use
module save cuda11

#create environment with required dependencies
conda create --name tf-modulecuda python numpy pandas matplotlib jupyter -c conda-forge 

# activate environment
conda activate tf-modulecuda

# use pip to install tensorflow
pip install tensorflow
```
The most up to date instructions for creating your own cuda/tensorflow environment can be found [here](https://www.tensorflow.org/install/pip). 

To create a conda environment with your own versions of Cuda and tensorflow:

For tensorflow 2.12+:

```bash
module load miniconda
conda create --name tf-condacuda python numpy pandas matplotlib jupyter cudatoolkit=11.8.0 
conda activate tf-condacuda
pip install nvidia-cudnn-cu11==8.6.0.163

# Store system paths to cuda libraries for gpu communication
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

#install tensorflow
pip install tensorflow==2.12.*

```

For tensorflow 2.11.*

```bash
module load miniconda
conda create --name tf-condacuda python numpy pandas matplotlib jupyter cudatoolkit=11.3.1 cudnn=8.2.1
conda activate tf-condacuda

# Store system paths to cuda libraries for gpu communication
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

#install tensorflow
pip install tensorflow==2.11.*

```

#### Use Your Environment

To re-enter your environment you only need the following:

```bash
module load miniconda
conda activate tf-condacuda

```
Or if using the module-installed CUDA:

``` bash
module restore cuda11
conda activate tf-modulecuda
```

### PyTorch

As with Tensorflow, sometimes the conda-supplied CUDA libraries are sufficient for the version of PyTorch you are installing. 
If not make sure you have the version of CUDA referenced on the PyTorch site [in their install instructions](https://pytorch.org/get-started/locally/).
They also provide [instructions on installing previous versions](https://pytorch.org/get-started/previous-versions/) compatible with older versions of CUDA.

Following the instructions on their site, create a PyTorch environment using `conda`:

```bash
module load miniconda
conda create --name pytorch_env pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia

```


## Compile `.c` or `.cpp` Files with CUDA code

By default, `nvcc` expects that host code is in files with a `.c` or `.cpp` extension, and device code is in files with a `.cu` extension. When you mix device code in a `.c` or `.cpp` file with host code, the device code will not be recoganized by `nvcc` unless you add this flag: `-x cu`.  

``` bash
nvcc -x cu mycuda.cpp -o mycuda.exe
```     
