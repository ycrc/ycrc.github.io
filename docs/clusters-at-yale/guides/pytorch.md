#Pytorch

Pytorch is an open source Machine Learning (ML) framework based on the python programming language.

#Pytorch module

Some pytorch versions are already available on the clusters at yale as modules and will not require any user modification to run successfully. You can search for these versions using the module avail command:

``` bash
module avail pytorch
```


#Installing Pytorch in a miniconda environment

If you find that there is not a module available on the cluster for the version of pytorch you need, and/or you are using a complex miniconda environment as part of your workflow, then you may benefit from installing pytorch yourself inside a miniconda environment.

Click this link, [installing pytorch](https://pytorch.org/get-started/locally/), to be directed to the pytorch website to install the latest version of pytorch.


You will be greeted with a table like the one below:

![pytorch](/img/pytorch_start_locally.png)

Please make sure your selections match the image above, i.e., Stable, linux, conda, and Python. Either CUDA version will work on the clusters, and CPU should be selected if you do not plan on using GPUs with your pytorch installation.

Then copy the install command to install pytorch into your existing environment. Please make sure you are off the login node or the install will fail.

If building a new environment, you can instead use the conda create command as outlined at this [site](https://docs.ycrc.yale.edu/clusters-at-yale/guides/conda/).

#Installing older versions of pytorch

To install older versions of pytorch, you can find instructions at this [site](https://pytorch.org/get-started/previous-versions).
