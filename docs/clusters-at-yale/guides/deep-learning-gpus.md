# Deep Learning with GPUs

In order to get your job set up properly and test your environment, you will want to allocate a compute node that has a GPU. Here are a couple examples:

``` bash
srun --pty -p gpu -c 2 -t 12:00:00 --gres=gpu:1 bash
```

or, if the `gpu` queue is busy, try to scavenge some private GPUs:

``` bash
srun --pty -p scavenge -c 2 -t 12:00:00 --gres=gpu:1 bash
```

Next, we'll walk though the setup and activation of your environment.

## One time Setup

### Modules

Load the appropriate modules for either Farnam or Grace.

``` bash
# load modules for Farnam
module purge
module load GCC/7.3.0-2.30
module load cuDNN/7.1.4-CUDA-9.0.176
module load Python/miniconda

# or load modules for Grace
module purge
module load Langs/GCC/5.2.0
module load GPU/cuDNN/9.0-v7
module load Langs/Python/miniconda
```

Then save your modules as a collection.

``` bash
# save module environment
module save cuda
module purge
```

### Create Your Python Environment

You will want to create a virtual environment for your GPU enabled code. For more details on Conda environments, see our [Conda documentation](/clusters-at-yale/guides/conda).

``` bash
# create conda environment for deep learning/neural networks
conda create -y -n dlnn python=3.6 anaconda
source activate dlnn

#install libraries
pip install --force --upgrade setuptools
pip install keras
pip install Theano
pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.8.0-cp36-cp36m-linux_x86_64.whl
pip install http://download.pytorch.org/whl/cu90/torch-0.4.0-cp36-cp36m-linux_x86_64.whl
pip install torchvision
```

## Use Your Environment

Now, to re-enter your Deep Neural Network environment, you just need the following:

``` bash
module restore cuda
source activate dlnn
```