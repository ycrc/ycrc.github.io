# Python

[Python](https://www.python.org/about/) is a language and free software distribution that is used for websites, system administration, security testing, and scientific computing, to name a few. On the Yale Clusters there are a couple ways in which you can set up Python environments. The default python provided is the minimal install of Python 2.7 that comes with Red Hat Enterprise Linux 7. Unless your Python scripts only use Python's standard library, you will probably want to use one of the methods below to set up your own python environment.

## The Python Module

We provide a Python as a [software module](/clusters-at-yale/applications/modules). We include frozen versions of many common packages used for scientific computing.

### Find and Load Python

Find the available versions of Python version 3 with:

``` bash
module avail Python/3
```

To load version 3.7.0:

``` bash
module load Python/3.7.0-foss-2018b
```

To show installed Python packages and their versions for the `Python/3.7.0-foss-2018b` module:

``` bash
module help Python/3.7.0-foss-2018b
```

### Install Packages

We recommend _*against*_ installing python packages with `pip` after having loaded the Python module. Doing so installs them to your home directory in a way that does not make it clear to other python installs what environment the packages you installed belong to. Instead we recommend using [virtualenv](https://docs.python.org/3/library/venv.html) or [Conda](/clusters-at-yale/guides/conda/) environments. We like conda because of all the additional pre-compiled software it makes available.

## Conda-based Python Environments

You can easily set up multiple Python installations side-by-side using the `conda` command. With Conda you can manage your own packages and dependencies for Python, R, etc. See our guide for more detailed instructions. 

``` bash
# install once
module load miniconda
conda create -n py3_env python=3 numpy scipy matplotlib ipython jupyter jupyterlab
# use later
module purge && module load miniconda
conda activate py3_env
```

## Run Python

We will kill Python jobs on the login nodes that are using excessive resources. To be a good cluster citizen, launch your computation in jobs. See our [Slurm documentation](/clusters-at-yale/job-scheduling) for more detailed information on submitting jobs.

### Interactive Job

To run Python interactively, first launch an interactive job on a compute node. If your Python sessions will need up to 10 GiB of RAM and up to 4 hours, you would submit you job with:

``` bash
srun --pty -p interactive --mem=10G -t 4:00:00 bash
```

Once your interactive session starts, you can load the appropriate module or Conda environment (see above) and start `python` or `ipython` on your command prompt. If you are happy with your Python commands, save them to a file which can then be submitted and run as a batch job.

### Batch Mode

To run Python in batch mode, create a plain-text batch script to submit. In that script, you call your Python script. In this case `myscript.py` is in the same directory as the batch script, batch script contents shown below.

``` bash
#!/bin/bash
#SBATCH -J my_python_program
#SBATCH --mem=10G
#SBATCH -t 4:00:00

module load miniconda
conda activate py3_env
python myscript.py
```

To actually submit the job, run `sbatch my_py_job.sh` where the batch script above was saved as `my_py_job.sh`.

### Jupyter Notebooks

You can run Jupyter notebooks & JupyterLab by submitting your notebook server as a job. See our [page dedicated to Jupyter](/clusters-at-yale/guides/jupyter) for more info.


