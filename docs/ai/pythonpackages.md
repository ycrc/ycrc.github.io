#Python Package Installation Procedures for AI/ML workflows

##Current Recipes available

Some Python Packages for AI/ML workflows do not install easily into YCRC systems. Due to this, we have developed 
installation recipes for commonly requested python packages. As of now, those packages include:

- [flash attention](https://docs.ycrc.yale.edu/clusters-at-yale/ai/pythonpackages/#flash-attention)

If you do not see a recipe for a package you need help with, please contact research.computing@yale.edu for
help installing the package/program.

##Common error associated with AI/ML packages.

If installing a python package/program for your AI/ML workflow and run into the error:

```bash
glibc 2.32+ not found
```

Then please contact research.computing@yale.edu for help installing the package. This error is a result of the
operating system available on YCRC Computing Systems and will require building the program/package from source.

##Flash Attention
```bash
###request a compute node on day for 24 hours with 200 GB of memory and 20 cpus
salloc --partition=day --mem=200G --time=1- --cpus-per-task=20

##create initial environment
module load miniconda

conda create -n test python=3.12.* uv ninja packaging cuda-version=12.8 cuda-nvcc=12.8 psutil -c nvidia 

conda activate test

###install pytorch with cuda 12.8 (12.8 is necessary to match B200 architecture)
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu128

###Load YCRC Cuda 12.8 module for nvcc detection
module load CUDA/12.8

###get flash attention package and setup for install
git clone https://github.com/Dao-AILab/flash-attention

cd flash-attention 

git submodule update --init --recursive

###make some cluster settings to install only for specific GPU architectures available (B200s, H200s, A100s, etc)
export TORCH_CUDA_ARCH_LIST="8.9;9.0,10.0"

###stop install from overthreading/overcommitting memory
export MAX_JOBS=8
export CMAKE_BUILD_PARALLEL_LEVEL=8

##install package
python setup.py install
```
