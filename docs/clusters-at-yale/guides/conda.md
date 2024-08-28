# Conda

[Conda](https://conda.io/projects/conda/en/latest/index.html) is a package, dependency, and environment manager. It allows you to maintain different, often incompatible, sets of applications side-by-side. It has become a popular choice for managing pipelines that involve several tools, especially when multiple languages are involved. These sets of applications and their dependencies are kept in Conda environments, which you can switch between as your work dictates. Compared to the [modules](/applications/modules) that we provide, there are often newer and more varied packages available that you can manage yourself, but they may not be as well optimized for the clusters. See [Conda's official command-line reference](https://docs.conda.io/projects/conda/en/latest/commands.html) and [the offical docs for managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for detailed instructions. Here we present essential instructions and site-specific info.

!!! Warning
    Mixing modules and conda-managed software is almost never a good idea. When constructing an environment for your work you should load either modules or a conda environment. If you get stuck, you [can always ask us for help](/#get-help).

## The Miniconda Module

For your convenience, we provide a relatively recent version of [Miniconda](https://conda.io/miniconda.html) as a module. This is a read-only environment from which you can create your own. We set some defaults for you in this module, and we keep it relatively up-to-date so you don't have to. If you are using Conda-installed packages, this should be the only module you load in your jobs.

Note: If you are on Milgram and run out of space in your home directory for Conda, you can either reinstall your environment in your project space (see below) or [contact us](/#web-and-email-support) for help with your home quota.

## Defaults We Set

On all clusters, we set the `CONDA_ENVS_PATH` and `CONDA_PKGS_DIRS` environment variables to `conda_envs` and `conda_pkgs` in your project directory where there is more quota available. Conda will install to and search in these directories for environments and cached packages.

Starting with minconda module version 4.8.3 we set the default channels (the sources to find packages) to [`conda-forge`](https://conda-forge.org/#about) and [`bioconda`](https://bioconda.github.io/), which provide a wider array of packages than the default channels do. We have found it saves a lot of typing. If you would like to override these defaults, see the [Conda docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html) on managing channels. Below is the `.condarc` for the miniconda module.

``` yaml
env_prompt: '({name})'
auto_activate_base: false
channels:
  - conda-forge
  - bioconda
  - defaults
```

## Setup Your Environment

### Load the `miniconda` Module

``` bash
module load miniconda
```

You can save this to your default module collection by using `module save`. See our [module documentation](/applications/modules) for more details.

### Create a `conda` Environment

To create an environment use the [`conda create`](https://docs.conda.io/projects/conda/en/latest/commands/create.html) command. Environment files are saved to the first path in `$CONDA_ENVS_PATH`, or where you specify with the `--prefix` option. You should give your environments names that are meaningful to you, so you can more easily keep track of their purposes.

Because dependency resolution is hard and messy, we find specifying as many packages as possible at environment creation time can help minimize broken dependencies. Although sometimes unavoidable for Python, we recommend against heavily mixing the use of `conda` and `pip` to install applications. If needed, try to get as much installed with `conda`, then use `pip` to get the rest of the way to your desired environment.

!!! tip
    For added reproducibility and control, specify versions of packages to be installed using `conda` with `packagename=version` syntax. E.g. `numpy=1.14`

!!! Warning
    You will need to request an [interactive job](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/#interactive-jobs) with the `salloc` command when you create a new `conda` environment or install packages into an existing `conda` environment.   

For example, if you have a legacy application that needs Python 2 and OpenBLAS:

``` bash
module load miniconda
conda create -n legacy_application python=2.7 openblas
```

If you want a good starting point for interactive data science in R/Python Jupyter Notebooks:

``` bash
module load miniconda
conda create -n ds_notebook python numpy scipy pandas matplotlib ipython jupyter r-irkernel r-ggplot2 r-tidyverse
```

Note that you can also install jupyterlab instead of, or alongside jupyter. 

### Conda Channels

Community-lead collections of packages that you can install with `conda` are provided with channels. Some labs will provide their own software using this method. A few popular examples are [Conda Forge](https://conda-forge.org/) and [Bioconda](https://bioconda.github.io/), which we set for you by default. See the [Conda docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html) for more info about managing channels.

You can create a new environment called `brian2` (specified with the `-n` option) and install [Brian2](http://briansimulator.org/) into it with the following:

``` bash
module load miniconda
conda create -n brian2 brian2
# normally you would need this:
# conda create -n brian2 --channel conda-forge brian2
```

You can also install packages from Bioconda, for example:

``` bash
module load miniconda
conda create -n bioinfo biopython bedtools bowtie2 repeatmasker
# normally you would need this:
# conda create -n bioinfo --channel conda-forge --channel bioconda biopython bedtools bowtie2 repeatmasker
```

## Use Your Environment

To use the applications in your environment, run the following:

``` bash
module load miniconda
conda activate env_name
```

!!! warning
    We recommend _against_ putting `source activate` or `conda activate` commands in  your `~/.bashrc` file. This can lead to issues in interactive or batch jobs. If you have issues with an environment, trying re-loading the environment by calling `conda deactivate` before rerunning `conda activate env_name`.

#### Interactive

Your Conda environments **will not follow you** into job allocations. Make sure to activate them after your [interactive job](/clusters-at-yale/job-scheduling/#interactive-jobs) begins.

#### In a Job Script

To make sure that you are running in your project environment in a submission script, make sure to include the following lines in your submission script before running any other commands or scripts (but after your [Slurm directives](/clusters-at-yale/job-scheduling#directives)):

``` bash
#!/bin/bash
#SBATCH --partition=general
#SBATCH --job-name=my_conda_job
#SBATCH --cpus-per-task 4
#SBATCH --mem-per-cpu=6000


module load miniconda

conda activate env_name
python analyses.py
```

### Find and Install Additional Packages

You can search [Anaconda Cloud](https://anaconda.org/) or use [`conda search`](https://docs.conda.io/projects/conda/en/latest/commands/search.html) to find the names of packages you would like to install:

``` bash
module load miniconda
conda search numpy
```

### Compiling Codes

You may need to compile codes in a conda environment, for example, installing an R package in a conda R env. This requires you to have the GNU C compiler and its development libraries installed in the conda env before compiling any codes:

``` bash
conda install gcc_linux-64
```  

Without `gcc_linux-64`, the code will be compiled using the system compiler and libraries. You will experience run-time errors when running the code in the conda environment. 

## Troubleshoot

### Conda version doesn't match the module loaded

If you have run `conda init` in the past, you may be locked to an old version of `conda`. You can run the following to fix this:

``` bash
sed -i.bak -ne '/# >>> conda init/,/# <<< conda init/!p' ~/.bashrc
```

### Permission Denied

If you get a permission denied error when running `conda install` or `pip install` for a package, make sure you have created an environment and activated it or activated an existing one first.

### bash: conda: No such file or directory

If you get the above error, it is likely that you don't have the necessary module file loaded. Try loading the `minconda` module and rerunning your `conda activate env_name` command.

### Could not find environment

This error means that the version of miniconda you have loaded doesn't recognize the environment name you have supplied. Make sure you have the `miniconda` module loaded (and not a different Python module) and have previously created this environment. You can see a list of previously created environments by running:

``` bash
module load miniconda
conda info --envs
```

## Additional Conda Commands

### List Installed Packages

``` bash
module load miniconda
conda list --name env_name
```

### Delete a Conda Environment

``` bash
module load miniconda
conda remove --name env_name --all
```

### Save and Export Environments


There are two concepts for rebuilding conda environments:

1. a copy of an existing environment, with identical versions of each package
2. a fresh build following the same steps taken to creat the first environment (letting unspecified versions float)

This short doc will walk through recommended approaches to both styles of exporting and rebuilding a generic environment named `test` containing python, jupyter, numpy, and scipy.


#### Full Export Including Dependencies

To export the exact versions of each package installed (including all dependencies) run:

```sh
module load miniconda
conda env export --no-builds --name test | grep -v prefix > test_export.yaml

```

This yaml file is ~230 lines long and contains every package that is installed in the `test` environment.

The conda export command includes information about the path where it was installed (i.e. the `prefix`).
To remove this hard-coded path, we need to remove the line in this print out related to the "prefix".


#### Export Only Specified Packages

If we simply wish to rebuild the environment using the steps previously employed to create it, we can replace `--no-builds` with `--from-history`.
```sh
module load miniconda
conda env export --from-history --name test | grep -v prefix > test_export.yaml

```

This is a much smaller file, ~10 lines, and only lists the packages explicitly installed:

```yml
name: test
channels:
  - conda-forge
  - defaults
  - bioconda
dependencies:
  - scipy
  - numpy=1.21
  - jupyter
  - python=3.8

```

In this environment, the versions of python and numpy were pinned during installation, but scipy and jupyter were left to get the most recent compatible version.



#### Build a New Environment

To create a new environment using all the enumerated pacakges:

```sh
module load miniconda
conda env create --file test_export.yaml

```

This will create a new environment with the same name `test`.
The yaml file can be edited to change the name of the new environment.
