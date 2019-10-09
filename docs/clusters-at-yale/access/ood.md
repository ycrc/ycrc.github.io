# Open OnDemand

We have recently built a new way to access the clusters called [Open OnDemand](https://openondemand.org).
This is a web-portal that provides a shell, file browser, and graphical interface for certain apps (like Jupyter or MATLAB).
Currently, this is only available for Farnam and Grace.

To get started, navigate to either

```
ood-grace.hpc.yale.edu
ood-farnam.hpc.yale.edu
```

and CAS authenticate with your netID/password.
You will then be greeted with a welcome page showing the standard Message of the Day:

![welcome](/img/ood_welcome.png)

Along the top are a pull-down menus for a File Browser, a Job Builder, a list of Interactive Apps, and a Shell.

## File Browser
![file_browser](/img/ood_filebrowser.png)
The file browser is a graphical interface to manage, upload, and download files from the clusters.
You can drag and drop files, download entire directories, and also move files between directories all from within the web browser.

## Remote Desktop
Occasionally, it is helpful to use a graphical interface to explore data or manage certain programs.
In this case, users have typically utilized VNC or X11 forwarding.
Both of these tools have complications, either in complexity of setup or in performance.
The Remote Desktop option from OOD simplifies the configuration of a VNC desktop session on a compute node.

First, you request resources (similar to the command-line interface to SLURM) and decide what partition your job should run on (`interactive` is the most common).

![remote_desktop](/img/ood_remote.png)

Once you launch the job, you will be presented with a notification that your job has been queued.
Depending on the resources requested, your job should be scheduled in a minute or so.
Then you will see the option to launch the Remote Desktop:

![starting](/img//ood_remote_starting.png)

After you click on Launch Remote Desktop, a standard desktop interface will open in a new tab:

![desktop](/img//ood_remote_desktop.png)

From here you can launch any graphical program that you might need.

## Interactive apps

We have deployed a selection of common graphical programs as Interactive Apps on Open OneDemand.
Currently, we have apps for Matlab, Jupyter Notebook, and Mathematica.
We are working to develop more apps in the future.
The process for launching each of these is very similar, so we will focus on one of them (Jupyter Notebooks) as an example.

### Jupyter Notebooks

One of the most common uses of Open OnDemand is the Jupyter Notebook interface for Python and R.
[Jupyter Notebooks](https://jupyter-notebook.readthedocs.io/en/stable/) are a flexible way to interactively work with code and plots presented in-line together.

To launch a Jupyter session through Open OnDemand, click on the Interactive Apps pull-down menu and select Jupyter Notebook:

![interactive](/img/ood_interactive.png)

Then you will be presented with a set of options to request resources for your job.
The first option is a pull-down menu listing the available Conda environments for your account.
Make sure to select one that has jupyter installed (follow the steps [here](../guides/jupyter.md) to set up the environment.)

![jupyter_request](/img/ood_jupyter.png)

After specifying the required resources (number of CPUs/GPUs, amount of RAM, etc.), the job will be scheduled and will launch when it's ready.
This will open the standard Jupyter interface where you can start working with notebooks.

![jupyter_running](/img/ood_jupyter_running.png)
