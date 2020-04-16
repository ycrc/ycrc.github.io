# Open OnDemand

We have recently built a new way to access the clusters called [Open OnDemand](https://openondemand.org) (OOD).
This is a web-portal that provides a shell, file browser, and graphical interface for certain apps (like Jupyter or MATLAB).
Currently, this is only available for Farnam and Grace.

## Access

Open OnDemand is available on the following clusters using your NetID credentials (CAS login).

| Cluster                                     | OOD site                                                   |
|---------------------------------------------|------------------------------------------------------------|
| [Farnam](/clusters-at-yale/clusters/farnam) | [ood-grace.hpc.yale.edu](https://ood-grace.hpc.yale.edu)   |
| [Grace](/clusters-at-yale/clusters/grace)   | [ood-farnam.hpc.yale.edu](https://ood-farnam.hpc.yale.edu) |
| [Ruddle](/clusters-at-yale/clusters/ruddle)\* | [ood-ruddle.hpc.yale.edu](https://ood-ruddle.hpc.yale.edu) |

### DUO Everywhere for OOD Ruddle

If you want access to ood-ruddle, you must enroll in the early pilot of DUO Everywhere. Enrollment will force [Multi-Factor Authentication](/clusters-at-yale/access/mfa) (MFA) for CAS on every login, even on-campus.

To enroll in DUO Everywhere, please email [netal.patel@yale.edu](mailto:netal.patel@yale.edu) indicating you want to use OnDemand on Ruddle. Include your your NetID and your desired deployment date. The deployment date should be any day from Monday to Thursday.

## The Dashboard

On login you will then be greeted with a welcome page showing the standard message of the day.

![welcome](/img/ood_welcome.png)

Along the top are a pull-down menus for a File Browser, a Job Builder, a list of Interactive Apps, and a Shell.

## File Browser

![file_browser](/img/ood_filebrowser.png)

The file browser is a graphical interface to manage, upload, and download files from the clusters. You can use the built-in file editor to view and edit files from your browser without having to download and upload scripts, etc.

You can also drag and drop files, download entire directories, and move files between directories using this interface.

## Shell

You can launch a traditional command-line interface to the cluster using the Shell pull-down menu.
This opens a terminal in a web-browser that you can use in the exact same way as when logging into the cluster via SSH.

This is a convenient way to access the clusters when you don't have access to an ssh client or do not have your ssh keys.
## Interactive Apps

We have deployed a selection of common graphical programs as Interactive Apps on Open OneDemand. Currently, we have apps for Remote Desktop, Matlab, RStudio, Jupyter Notebook, and Mathematica.

### Remote Desktop

Occasionally, it is helpful to use a graphical interface to explore data or run certain programs.
In the past your options were to use [VNC](/clusters-at-yale/access/vnc) or [X11 forwarding](docs/clusters-at-yale/access/x11). These tools can be complex to setup or suffer from reduced performance. The Remote Desktop app from OOD simplifies the configuration of a VNC desktop session on a compute node. The Matlab, Mathematica, and RStudio Desktop Apps are special versions of this app. To get started choose Remote Desktop (or another desktop app) from the Interactive Apps menu on the dashboard.

Use the form to request resources and decide what partition your job should run on (use `interactive` or your lab's partition).

![remote_desktop](/img/ood_remote.png)

Once you launch the job, you will be presented with a notification that your job has been queued.
Depending on the resources requested, you may need to wait for a bit. When the job starts you will see the option to launch the Remote Desktop:

![starting](/img/ood_remote_starting.png)

Note you can share a view only link for your session if you would like to share your screen. After you click on Launch Remote Desktop, a standard desktop interface will open in a new tab. You can find the terminal application (for loading modules and launching programs) in the "Applications" > "System Tools" menu.

![terminal](/img/ood_remote_terminal.png)

#### Copy/Paste

Because of the way modern borowsers protect your computer's clipboard you have to use a special text box to copy and paste from the Remote Desktop App. Click the arrow on the left side of your window for a menu, then click the clipboard icon to get access to your Remote Desktop's clipboard.

![clipboard](/img/ood_remote_clipboard.png)

### Jupyter Notebooks

One of the most common uses of Open OnDemand is the Jupyter Notebook interface for Python and R.
[Jupyter Notebooks](https://jupyter-notebook.readthedocs.io/en/stable/) provide a flexible way to interactively work with code and plots presented in-line together. To get started choose Jupyter Notebook from the Interactive Apps menu on the dashboard.

![jupyter_form](/img/ood_jupyter_form.png)

Make sure that you chose the right conda environment for your from the drop-down menu. If you have not yet set one up, [follow our instructions](/guides/jupyter.md) on how to create a new one. After specifying the required resources (number of CPUs/GPUs, amount of RAM, etc.), you can submit the job. When it launches you can open the standard Jupyter interface where you can start working with notebooks.

!!! tip
    If you have installed and want to use [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/index.html) replace `/tree?` with `/lab` in the url to your Jupyter job.
