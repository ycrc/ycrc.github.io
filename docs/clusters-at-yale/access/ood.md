# Open OnDemand

[Open OnDemand](https://openondemand.org) (OOD) is platform for accessing the clusters that only requires a web browser.
This web-portal provides a shell, file browser, and graphical interface for certain apps (like Jupyter or MATLAB).

## Access

If you access Open OnDemand installed on YCRC clusters from off campus, you will need to first connect to the Yale [VPN](https://docs.ycrc.yale.edu/clusters-at-yale/access/vpn). 

Open OnDemand is available on the following clusters using your NetID credentials (CAS login). 

| Cluster                                         | OOD site                                                   |
|-------------------------------------------------|------------------------------------------------------------|
| [Grace](/clusters-at-yale/clusters/grace)       | [ood-grace.hpc.yale.edu](https://ood-grace.hpc.yale.edu)   |
| [Farnam](/clusters-at-yale/clusters/farnam)     | [ood-farnam.hpc.yale.edu](https://ood-farnam.hpc.yale.edu) |
| [Milgram](/clusters-at-yale/clusters/milgram) | [ood-milgram.hpc.yale.edu](https://ood-milgram.hpc.yale.edu) |
| [Ruddle](/clusters-at-yale/clusters/ruddle)   | [ood-ruddle.hpc.yale.edu](https://ood-ruddle.hpc.yale.edu) |

The above four URLs are also called cluster OOD URLs. They are available to any user with a research account (also called a lab account) on the clusters. Your research account is the same as your NetID. 

## Course Open OnDemand Web Portals

Courses on the clusters have their own course-specific OOD URLs, also called course OOD web portals. Through the course OOD URLs, students will sign in with their NetID but work under their student account. The course URLs all follow the same naming convention: `coursename.ycrc.yale.edu`. More information about course OODs can be found at [academic support](https://research.computing.yale.edu/services/academic-support).

!!! warning 
    If you only have a student account, but try to sign in through the cluster OOD URL, you will get an error in the browser:
    ```
    Error -- can't find user for cpsc424_test
    Run 'nginx_stage --help' to see a full list of available command line options.
    ```
    Instead, use the course OOD URL.

## The Dashboard

On login you will see the OOD dashboard.

![welcome](/img/ood_welcome.png){: .large}

Along the top are pull-down menus for various Apps, including File Managers, Job Composer, a Shell, a list of Interactive Apps, etc.

## File Browser

![file_browser](/img/ood_filebrowser.png){: .medium}

The file browser is a graphical interface to manage, upload, and download files from the clusters. You can use the built-in file editor to view and edit files from your browser without having to download and upload scripts.

You can also drag-and-drop to download and upload files and directories, and move files between directories using this interface.

#### Customize Favorite Paths

Users are allowed to customize favorite paths in the file manager. Using the scripts below to add, remove, and list custmozed favorite paths:

``` bash
  ood_add_path
  ood_remove_path
  ood_list_path
```

The scripts are self explanatory and will prompt you to add or remove paths to the Files pull-down menue, as well as the left pane when the file manager is opened.

## Shell

You can launch a traditional command-line interface to the cluster using the Shell pull-down menu.
This opens a terminal in a web-browser that you can use in the exact same way as when logging into the cluster via SSH.

This is a convenient way to access the clusters when you don't have access to an ssh client or do not have your ssh keys.

## Interactive Apps

We have deployed a selection of common graphical programs as Interactive Apps on Open OneDemand. Currently, we have apps for Remote Desktop, MATLAB, Mathematica, RStudio Desktop, RStudio Server, and Jupyter Notebook, etc.

### Remote Desktop

Occasionally, it is helpful to use a graphical interface to explore data or run certain programs.
In the past your options were to use [VNC](/clusters-at-yale/access/vnc) or [X11 forwarding](/clusters-at-yale/access/x11). These tools can be complex to setup or suffer from reduced performance. The Remote Desktop app from OOD simplifies the configuration of a VNC desktop session on a compute node. The MATLAB, Mathematica, and RStudio Desktop Apps are special versions of this app. To get started choose Remote Desktop (or another desktop app) from the Interactive Apps menu on the dashboard.

Use the form to request resources and decide what partition your job should run on (use `interactive` or your lab's partition).

![remote_desktop](/img/ood_remote.png){: .medium}

Once you launch the job, you will be presented with a notification that your job has been queued.
Depending on the resources requested, you may need to wait for a bit. When the job starts you will see the option to launch the Remote Desktop:

![starting](/img/ood_remote_starting.png){: .medium}

Note you can share a view only link for your session if you would like to share your screen. After you click on Launch Remote Desktop, a standard desktop interface will open in a new tab. 

#### Copy/Paste

In some browsers, you may have to use a special text box to copy and paste from the Remote Desktop App. Click the arrow on the left side of your window for a menu, then click the clipboard icon to get access to your Remote Desktop's clipboard.

![clipboard](/img/ood_remote_clipboard.png){: .medium}


### Jupyter 

One of the most common uses of Open OnDemand is the Jupyter interface for Python and R. You can choose either Jupyter Notebook or Jupyter Lab. By default, this app will try to launch Jupyter Notebook, unless the `Start JupyterLab` checkbox is selected. 

![jupyter_form](/img/ood_jupyter_form.png){: .medium}

Make sure that you chose the right Conda environment for your from the drop-down menu. If you have not yet set one up, [follow our instructions](/clusters-at-yale/guides/jupyter) on how to create a new one. After specifying the required resources (number of CPUs/GPUs, amount of RAM, etc.), you can submit the job. When it launches you can open the standard Jupyter interface where you can start working with notebooks.

#### ycrc_default

The `ycrc_default` conda environment will be automatically built when you select it for the first time from Jupyter. You can also build your own Jupyter with:

```
module load miniconda
conda create -n env_name jupyter jupyter-lab
```

Once created, `ycrc_default` will not be updated unless you do it manually. To update `ycrc_default`, please run the following command from a shell command line:
```
module load miniconda
conda update -n  ycrc_default jupyter jupyter-lab
```

### RStudio Server

#### Change User R Package Path
To change the default path where packages installed by the user are stored, you need to add the following line of code in your `$HOME/.bashrc`:

```bash
export R_LIBS_USER=path_to_your_local_r_packages
```

#### Configure the Graphic Device
When you plot in a RStudio session, you may encounter the following error:

``` bash
Error in RStudioGD() : 
  Shadow graphics device error: r error 4 (R code execution error)
In addition: Warning message:
In grDevices:::png("/tmp/RtmpcRxRaB/4v3450e3627g4432fa27f516348657267.png",  :
  unable to open connection to X11 display ''
```

To fix the problem, you need to configure RStudio Server to use `Cairo` 
as the graphic device backend. To do so, first click `Tools` from the top menu bar on 
the RStudio Server GUI, and then select `Global options` from the pull down menu. An option window will be opened. 
In the window, click `general` on the left panel and then click `Graphics` on the right. Choose `Cairo` 
from the `backend` list. 

Once done, it sets `Cairo` as the default drawing device. You only need to configure the device once 
unless you have cleaned up your RStudio configuration files.

![rstudio_cairo](/img/ood_rstudio_cairo.png){: .medium}
