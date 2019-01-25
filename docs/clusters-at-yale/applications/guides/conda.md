# Conda

For researchers who have Python package requirements beyond the most common packages (Numpy, Scipy, Pandas), we recommend using [Anaconda Python](https://www.anaconda.com/what-is-anaconda/). Using Conda environments, you can manage which packages and even which versions of Python you are using for different projects.

Many other software packages have also started to use Conda as an installation tool. If you see a Conda as a suggested installation method, you can use the `miniconda` module to manage your software in your own directories.

## The Miniconda Module

For your convenience, we provide a relatively recent version of [Miniconda](https://conda.io/miniconda.html) (a base for Anaconda) as a module. It serves to bootstrap your personal environments. By using this module, you do not need to download your own copy of Anaconda, which will prevent unnecessary file and storage usage in your directories.

Note: If you are on Milgram and run out of space in your home directory for Conda, you can either reinstall your environment in your project space (see below) or contact us at [hpc@yale.edu](mailto:hpc@yale.edu) for help with your home quota.

## Setup Your Environment

### Load the Miniconda Module

``` bash
# Grace, Omega
module load Tools/miniconda

# all Others
module load miniconda
```

You can save this to your default module collection by using `module save`. See our [module documentation](/clusters-at-yale/applications/modules) for more details.

### Install to Your Project Directory

conda will look in the directory/directories specified in the environment variable `CONDA_ENVS_PATH` for places to find and install environments. If you want your environments stored in a directory where your quotas are higher, for example, `~/project/conda_envs`, you would need to set this variable to something like.

``` bash
echo "export CONDA_ENVS_PATH=~/project/conda_envs:$CONDA_ENVS_PATH" >> ~/.bashrc
source ~/.bashrc
```

### Create a `conda` Environment

Next, you will create a conda environment (saved by default to `~/.conda/envs`) so that you can install any Python packages that you need.

You can name your environment with any name that is meaningful to you.

You might want multiple environments if you have packages that have conflicting prerequisites. If so, just rerun the following commands to setup each environment as needed.

#### Installing Python

If you will be using your Conda environment ofr Python, specify your chosen version when creating the environment.

``` bash
conda create -n my_project python=2.7
```

``` bash
conda create -n my_project python=3.6
```

#### Installing Other Software

To start, you just create a blank environment with a name of your choosing.

``` bash
conda create -n gmt
```

### Activate & Customize Your Environment

You must first load your Conda environment before installing or using the packages in it. You only need to install packages once per environment.

``` bash
source activate my_project

# install packages, e.g. numpy
conda install numpy
# or, if not available in conda, e.g. ansible
pip install ansible
```

Or for non-python packages, like GMT

```
source activate gmt
conda install gmt=5.4.4 --channel conda-forge 
```

### Using Your Environment

#### Interactive

Your conda environments will **not** follow you into job allocations, so make sure to activate them after your interactive job begins. To re-enter your environment at any time, you just need the following:

``` bash
source activate my_project
```

#### In a Submission Script

To make sure that you are running in your project environment in a submission script, make sure to include the following lines in your submission script before running any other commands or scripts (but after your [Slurm directives](/clusters-at-yale/job-scheduling#directives)):

``` bash
# Grace, Omega
module load Tools/miniconda

# All other clusers
module load miniconda

source activate my_project

python <MY PYTHON SCRIPT HERE>
```

## Troubleshoot

### "Permission Denied"

If you get a permission denied error while trying to conda or pip install a package, make sure you have created an environment or activated an existing one first.

### "-bash: activate: No such file or directory"

If you get the above error, it is likely that you don't have the necessary module file loaded. Try loading the appropriate module and rerunning your `source activate my_project` command.

### "could not find environment:"

This error means that the version of Anaconda/Miniconda you have loaded doesn't recognize the environment name you have supplied. Make sure you have the Miniconda module loaded (and not a different Python module) and have previously created this environment. You can see a list of previously created environments by running:

```
conda info --envs
```

## Additional Conda Commands

### List Installed Packages

```
source activate my_project
conda list
```

### Delete a Conda Environment

```
conda env remove --name my_project
```

### Share your Conda Environment

If you want to share or back up a conda environment, you can export it to a file. To do so you need to run the following, replacing `my_project` with the desired environment.

``` bash
source activate my_project
conda env export > my_project_environment.yml
# on another machine or account, run
conda env create -f my_project_environment.yml
```

## Conda Documentation

Please see the excellent [Conda documentation](https://docs.anaconda.com/anaconda/user-guide/) on the official Anaconda website for some additional troubleshooting information and features provided by conda.