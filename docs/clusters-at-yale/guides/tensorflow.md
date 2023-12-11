#Tensorflow

Tensorflow and tensorflow-gpu are now the same package since tensorflow 2 was released. We do have some modules of tensorflow available for use with existing programs. You can find tensorflow versions using the command:


```bash
module avail tensorflow
```

#Installing Tensorflow
If you need a specific version of tensorflow or are working with specific python packages in a miniconda environment, then you will likely need to install your own version of tensorflow. Each version of tensorflow requires a specific version of CUDA and cudnn to be installed. You can refer to this [website](https://www.tensorflow.org/install/source#tested_build_configurations).


This table outlines how to install each version of tensorflow from 2.15-2.11:

--8<-- "snippets/tensorflowinstall.md"

#Test tensorflow gpu detection
If tensorflow is installed correctly, then it should be able to detect any GPUs that are allocated. You can test your tensorflow installation using these steps:


```bash

#####request compute allocation with a gpu node
salloc --partition=gpu_devel --cpus-per-task=1 --gpus=1 -t 4:00:00

#####load tensorflow miniconda environment

module load miniconda
conda activate YOUR_TF_ENVIRONMENT

#####run tensorflow validation test
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

This should print out a line of text that lists the recognized GPU. If this fails, please reach out to YCRC support for further assistance.
