#Python Package Installation Procedures for AI/ML workflows

##Current Recipes Available

Some Python Packages for AI/ML workflows do not install easily into YCRC systems. Due to this, we have developed and published 
installation recipes for commonly requested python packages. As of now, those packages include:

- [flash attention](https://docs.ycrc.yale.edu/clusters-at-yale/ai/pythonpackages/#flash-attention)
- [vllm](https://docs.ycrc.yale.edu/ai/pythonpackages/#vllm)
- [esmfold](https://docs.ycrc.yale.edu/ai/pythonpackages/#esmfold)

If you do not see a recipe for a package you need help with, please [contact us](https://docs.ycrc.yale.edu/#get-help) for
help installing the package/program.

##Common Error Associated with AI/ML Packages

If installing a python package/program for your AI/ML workflow and run into the error:

```bash
glibc 2.32+ not found
```

Then please [contact us](https://docs.ycrc.yale.edu/#get-help) for help installing the package. This error is a result of the
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

##vllm
```bash
###create initial environment (make sure to request a compute node with [miniconda](https://docs.ycrc.yale.edu/clusters-at-yale/guides/conda/)
conda create -n vllm python=3.10.* uv setuptools-scm cmake cuda-nvcc=12.4 cuda-version=12.4 pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 pytorch-cuda=12.4 cuda-toolkit=12.4 cuda-cudart-dev=12.4 cuda-runtime=12.4 gcc=12 gxx=12 -c pytorch -c nvidia -y

###store location of CUDA libraries and executables
export CUDA_HOME=$CONDA_PREFIX

###download repository for vllm to install from source
git clone https://github.com/vllm-project/vllm

cd vllm

uv pip install -e . --no-build-isolation
```

##esmfold
```bash
###create initial environment using [miniconda](https://docs.ycrc.yale.edu/clusters-at-yale/guides/conda/) on a compute node

conda create -n test python=3.10 scipy deepspeed=0.15 biopython einops dm-tree ml-collections   omegaconf=2.3 hydra-core=1.3 modelcif ninja compilers cmake   cuda-compiler=12.4 cuda-cudart-dev=12.4 cuda-nvcc=12.4 nvidia::cuda-libraries-dev=12.4 -y
conda activate test

###set variables to find cuda libraries and executables
export CUDA_HOME="$CONDA_PREFIX"
export CUDACXX="$CONDA_PREFIX/targets/x86_64-linux/bin/nvcc"
export PATH="$CONDA_PREFIX/targets/x86_64-linux/bin:$PATH"
export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"
mkdir -p "$CONDA_PREFIX/targets/x86_64-linux/lib64"
ln -sfn "$CONDA_PREFIX/lib" "$CONDA_PREFIX/targets/x86_64-linux/lib64"

#1 setup openfold, key dependency for esmfold
cd "$CONDA_PREFIX"
git clone https://github.com/aqlaboratory/openfold.git
cd openfold
git checkout v1.0.1
sed -i 's/-std=c++14/-std=c++17/g' setup.py

###install pytorch
pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0   --index-url https://download.pytorch.org/whl/cu124

###tell pytorch what CUDA architectures we are building for
export PYTORCH_NVCC_FLAGS="-gencode=arch=compute_80,code=sm_80 -gencode=arch=compute_86,code=sm_86 -gencode=arch=compute_89,code=sm_89 -gencode=arch=compute_90,code=sm_90"

# 2) drop any explicit '-gencode' occurrences to force openfold to build with our designated architectures
sed -i -E "/-gencode/d" setup.py
sed -i -E "/arch=compute_.*code=sm_.*/d" setup.py

###correct compiler in openfold, paste whole segment at one time
python - <<'PY'
import re
p="setup.py"
s=open(p,"r",encoding="utf-8").read()
s=re.sub(r"('nvcc'\s*:\s*)\[[^\]]*\]",
         r"\1['-O3','--use_fast_math','-std=c++17'] + _get_cuda_arch_flags()",
         s, flags=re.S)
open(p,"w",encoding="utf-8").write(s)
print("setup.py patched")
PY

###Tell compiler what CUDA architectures to build for (includes up to h200 right now)
export TORCH_CUDA_ARCH_LIST="7.5;8.0;8.6;8.9;9.0"

###installs openfold, key dependency of esmfold
python -m pip install . --no-build-isolation --no-deps -v

###installs esmfold
pip install fair-esm
```
