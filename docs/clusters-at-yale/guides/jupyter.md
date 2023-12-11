# Jupyter Notebooks

## Open OnDemand

We provide a simple way to start [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/) interfaces for Python and R using [Open OnDemand](/clusters-at-yale/access/ood/).
Jupyter notebooks provide a flexible way to interactively work with code and plots presented in-line together.
To get started choose Jupyter Notebook from the OOD Interactive Apps menu or click on the link on the dashboard.

Before you get started, you will need to be on campus or logged in to the [Yale VPN](/clusters-at-yale/access/vpn) and you will need to set up a Jupyter environment.

### Set up an environment

We recommend you use [miniconda](/clusters-at-yale/guides/conda) to manage your Jupyter environments.
You can create Conda environments from the OOD shell interface or from a terminal-based login to the clusters.
For example, if you want to create an environment with many commonly used scientific computing Python packages you would run:

``` bash
module load miniconda
conda create -y -n notebook_env python jupyter numpy pandas matplotlib
```

### Specify your resource request

![jupyter_ood](/img/ood_jupyter.png){: .medium}

You can use the `ycrc_default` environment or chose one of your own from the drop-down menu.
After specifying the required resources (number of CPUs/GPUs, amount of RAM, etc.), you can submit the job.
When it launches you can open the standard Jupyter interface where you can start working with notebooks.

!!! tip
    If you have installed and want to use [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/index.html) click the `Start JupyterLab` checkbox.

<br><br> **If there is a specific workflow which OOD does not satisfy, let us know and we can help.**

## Command-Line Execution of Jupyter Notebooks

Many scientific workflows start as interactive Jupyter notebooks, and our Open OnDemand portal has dramatically simplified deploying these notebooks on cluster resources.  However, the step from running notebooks interactively to running jobs as a batch script can be challenging and is often a barrier to migrating to using `sbatch` to run workflows non-interactively.

To help solve this problem, there are a handful of utilities that can execute a notebook as if you were manually hitting "shift-Enter" for each cell. Of note is [Papermill](https://papermill.readthedocs.io/en/latest/) which provides a powerful set of tools to bridge between interactive and batch-mode computing.

To get started, install papermill into your `conda` environments:

```
module load miniconda
conda activate my_env
conda install papermill
```

Then you can simply evaluate a notebook, preserving figures and output inside the notebook, like this:

```
papermill /path/to/notebook.ipynb /path/to/output.ipynb
```

This can be run inside a batch job that might look like this:

```
#!/bin/bash
#SBATCH -p day
#SBATCH -c 1
#SBATCH -t 6:00:00

module purge
module load miniconda
conda activate my_env
papermill /path/to/notebook.ipynb /path/to/output.ipynb

```

Variables can also be parameterized and passed in as command-line options so that you can run multiple copies simultaneously with different input variables. For more information see the [Papermill docs pages](https://papermill.readthedocs.io/).
