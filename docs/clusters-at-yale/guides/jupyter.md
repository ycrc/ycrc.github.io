# Jupyter Notebooks

We provide a simple way to start [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/) interfaces for Python and R using [Open OnDemand](/clusters-at-yale/access/ood/).
Jupyter notebooks provide a flexible way to interactively work with code and plots presented in-line together.
To get started choose Jupyter Notebook from the OOD Interactive Apps menu or click on the link on the dashboard.

Before you get started, you will need to be on campus or logged in to the [Yale VPN](/clusters-at-yale/access/vpn) and you will need to set up a Jupyter environment.

## Set up an environment

We recommend you use [miniconda](/clusters-at-yale/guides/conda) to manage your Jupyter environments.
You can create Conda environments from the OOD shell interface or from a terminal-based login to the clusters.
For example, if you want to create an environment with many commonly used scientific computing Python packages you would run:

``` bash
module load miniconda
conda create -y -n notebook_env python jupyter numpy pandas matplotlib
```

## Specify your resource request

![jupyter_ood](/img/ood_jupyter.png){: .medium}

You can use the `ycrc_default` environment or chose one of your own from the drop-down menu.
After specifying the required resources (number of CPUs/GPUs, amount of RAM, etc.), you can submit the job.
When it launches you can open the standard Jupyter interface where you can start working with notebooks.

!!! tip
    If you have installed and want to use [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/index.html) click the `Start JupyterLab` checkbox.

<br><br> **If there is a specific workflow which OOD does not satisfy, let us know and we can help.**
