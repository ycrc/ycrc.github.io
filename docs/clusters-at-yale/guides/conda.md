# Conda

For researchers who have Python package requirements beyond the most common packages (Numpy, Scipy, Pandas), we recommend using [Anaconda Python](https://www.anaconda.com/what-is-anaconda/). Using Anaconda's [Conda](https://conda.io/projects/conda/en/latest/index.html) package manager, you can create and manage packages and environments. These allow you to easily switch between versions of Python libraries and applications for different projects.

Many other software applications have also started to use Conda as a package manager. It has become a popular choice for managing pipelines that involve several tools, especially with multiple languages.

## The Miniconda Module

For your convenience, we provide a relatively recent version of [Miniconda](https://conda.io/miniconda.html) (a minimal set of Anaconda libraries) as a module. It serves to bootstrap your personal environments. By using this module, you do not need to download your own copy of Conda, which will prevent unnecessary file and storage usage in your directories.

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

Conda will look in the directory/directories specified in the environment variable `CONDA_ENVS_PATH` for places to find and install environments. If you want your environments stored in a directory where your quotas are higher, for example, `~/project/conda_envs`, you would need to set this variable to something like. We set this by default for you on Farnam and Ruddle.

To match this behavior on Grace:

``` bash
echo "export CONDA_ENVS_PATH=~/project/conda_envs:$CONDA_ENVS_PATH" >> ~/.bashrc
source ~/.bashrc
```

### Create a `conda` Environment

To create an environment (saved to the first location in `$CONDA_ENVS_PATH` or to `~/.conda/envs`) use the [`conda create`](https://docs.conda.io/projects/conda/en/latest/commands/create.html) command. You should give your environments names that are meaningful to you, so you can more easily keep track of which serves which project or purpose. You can also use environments manage groups of packages that have conflicting prerequisites.

Because dependency resolution is hard and messy, we find specifying as many packages as possible at environment creation time can help minimize broken dependencies. Although often unavoidable, we also recommend against heavily mixing the use of `conda` and `pip` to install applications. If needed, try to get as much installed with `conda`, then use `pip` to get the rest of the way to your desired environment.

!!! tip
    For added reproducibility and control, specify versions of packages to be installed using `conda` with `packagename=version` syntax. E.g. `numpy=1.14`

For example, if you have a legacy application that needs Python 2 and OpenBLAS:

``` bash
conda create -n legacy_application python=2.7 openblas
```

If you want a good starting point for interactive development of scientific Python scripts:

``` bash
conda create -n py37_dev python=3.7 numpy scipy pandas matplotlib ipython jupyter
```

### Conda Channels

There are also community-lead collections of unofficial packages that you can use with `conda` called channels. A few popular examples are [Conda Forge](https://conda-forge.org/) and [Bioconda](https://bioconda.github.io/). 

You could use the Conda Forge channel to install [Brian2](http://briansimulator.org/)

``` bash
conda create -n brian2 --channel conda-forge brian2
```

Bioconda provides recent versions of various bioinformatics tools, for example:

``` bash
conda create -n bioinfo --channel bioconda biopython bedtools bowtie2 repeatmasker
```

### Using Your Environment

To use the applications in your environment, make sure you have the `miniconda` module loaded then run the following:

``` bash
source activate env_name
```

#### Interactive

Your conda environments will **not** follow you into job allocations, so make sure to activate them after your [interactive job](/clusters-at-yale/job-scheduling/#interactive-jobs) begins.

#### In a Job Script

To make sure that you are running in your project environment in a submission script, make sure to include the following lines in your submission script before running any other commands or scripts (but after your [Slurm directives](/clusters-at-yale/job-scheduling#directives)):

``` bash_
#!/bin/bash
#SBATCH --partition=general
#SBATCH --job-name=my_conda_job
#SBATCH --cpus-per-task 4
#SBATCH --mem-per-cpu=6000

# Grace, Omega
module load Tools/miniconda

# All other clusters
module load miniconda

source activate env_name
python analyses.py
```

## Troubleshoot

### "Permission Denied"

If you get a permission denied error while trying to conda or pip install a package, make sure you have created an environment or activated an existing one first.

### "-bash: activate: No such file or directory"

If you get the above error, it is likely that you don't have the necessary module file loaded. Try loading the appropriate module and rerunning your `source activate env_name` command.

### "could not find environment:"

This error means that the version of Anaconda/Miniconda you have loaded doesn't recognize the environment name you have supplied. Make sure you have the Miniconda module loaded (and not a different Python module) and have previously created this environment. You can see a list of previously created environments by running:

```
conda info --envs
```

## Additional Conda Commands

### List Installed Packages

```
source activate env_name
conda list
```

### Delete a Conda Environment

```
conda env remove --name env_name
```

### Share your Conda Environment

If you want to share or back up a conda environment, you can export it to a file. To do so you need to run the following, replacing `env_name` with the desired environment.

``` bash
source activate env_name
conda env export > env_name_environment.yml
# on another machine or account, run
conda env create -f env_name_environment.yml
```