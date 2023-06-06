# Web Portal (Open OnDemand)

[Open OnDemand](https://openondemand.org) (OOD) is platform for accessing the clusters that only requires a web browser.
This web-portal provides a shell, file browser, and graphical interface for certain apps (like Jupyter or MATLAB).

## Access

If you access Open OnDemand installed on YCRC clusters from off campus, you will need to first connect to the Yale [VPN](https://docs.ycrc.yale.edu/clusters-at-yale/access/vpn). 

Open OnDemand is available on each cluster using your NetID credentials (CAS login). The Yale CAS login is configured with the DUO authentication. We recommend that you click "Remember me for 90 days" when you are prompted to choose an authentication menthod for DUO. This will simplified the login process.

| Cluster                        | OOD site                                                         |
|--------------------------------|------------------------------------------------------------------|
| [Grace](/clusters/grace)       | [ood-grace.hpc.yale.edu](https://ood-grace.hpc.yale.edu)         |
| [McCleary](/clusters/mccleary) | [ood-mccleary.ycrc.yale.edu](https://ood-mccleary.ycrc.yale.edu) |
| [Milgram](/clusters/milgram)   | [ood-milgram.hpc.yale.edu](https://ood-milgram.hpc.yale.edu)     |
| [Ruddle](/clusters/ruddle)     | [ood-ruddle.hpc.yale.edu](https://ood-ruddle.hpc.yale.edu)       |

The above four URLs are also called cluster OOD URLs. They are available to any user with a research account (also called a lab account) on the clusters. Your research account is the same as your NetID. 

### OOD for Courses

Each course on the YCRC clusters has its own URL to access OOD on the cluster. The URL is unique to each course and is also called course OOD. 
Course OODs all follow the same naming convention: <b>coursename.ycrc.yale.edu</b>. 'courename' is an abbreviated name given to the course by YCRC. 
Students must use the course URL to log in to OOD. They will with their NetID to log in but work under their student account on the cluster while they are in OOD. 

Course OOD and cluster OOD have different URLs, even if they use the same physical machine. 
Student accounts can only log in to OOD through a course OOD URL, and a regular account (same as your NetID) can only log in through the cluster OOD URL.

!!! warning 
    If you only have a student account, but try to log in through the cluster OOD URL, you will get an error in the browser:
    ```
    Error -- can't find user for cpsc424_test
    Run 'nginx_stage --help' to see a full list of available command line options.
    ```
    Use the URL for your course OOD will resolve the problem.

Additional information about course OOD can be found at [academic support](https://research.computing.yale.edu/services/academic-support).

## The Dashboard

On login you will see the OOD dashboard.

![welcome](/img/ood_welcome.png){: .large}

Along the top are pull-down menus for various Apps, including File Managers, Job Composer, a Shell, a list of Interactive Apps, etc.

## File Browser

![file_browser](/img/ood_filebrowser.png){: .medium}

The file browser is a graphical interface to manage, upload, and download files from the clusters. You can use the built-in file editor to view and edit files from your browser without having to download and upload scripts.

You can also drag-and-drop to download and upload files and directories, and move files between directories using this interface.

#### Customize Favorite Paths

Users are allowed to customize favorite paths in the file manager. Using the scripts below to add, remove, and list customized paths:

``` bash
  ood_add_path
  ood_remove_path
  ood_list_path
```
When you run `ood_add_path` from a shell command line, it will prompt you to add one path at a time, until you type 'n' to discontinue. All the paths added by you will be shown in the OOD pull-down menu for the file manager, as well as the left pane when the file manager is opened. 

`ood_remove_path` allows you to remove any of the paths added by you and `ood_list_path` will list all the paths added by you. 

After you have customized the path configuration from a shell, go to the OOD dashbaord and click `Develop`->`Restart Web Server` on the top menu bar to make the change effective immediately.  

## Shell

You can launch a traditional command-line interface to the cluster using the Shell pull-down menu.
This opens a terminal in a web-browser that you can use in the exact same way as when logging into the cluster via SSH.

This is a convenient way to access the clusters when you don't have access to an ssh client or do not have your ssh keys.

## Interactive Apps

We have deployed a selection of common graphical programs as Interactive Apps on Open OneDemand. Currently, we have apps for Remote Desktop, MATLAB, Mathematica, RStudio Desktop, RStudio Server, and Jupyter Notebook, etc.

!!! warning
    You are limited to 4 interactive app instances (of any type) at one time. 
    Additional instances will be rejected until you delete older open instances. 
    Closing the window does not terminate the interactive app job.
    To terminate the job, click the "Delete" button in your "My Interactive Apps" page in the web portal.

### Remote Desktop

Occasionally, it is helpful to use a graphical interface to explore data or run certain programs.
In the past your options were to use [VNC](/clusters-at-yale/access/vnc) or [X11 forwarding](/clusters-at-yale/access/x11). These tools can be complex to setup or suffer from reduced performance. The Remote Desktop app from OOD simplifies the configuration of a VNC desktop session on a compute node. The MATLAB, Mathematica, and RStudio Desktop Apps are special versions of this app. To get started choose Remote Desktop (or another desktop app) from the Interactive Apps menu on the dashboard.

Use the form to request resources and decide what partition your job should run on. Use `devel` (`interactive` on Milgram and Ruddle) or your lab's partition.

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

Make sure that you chose the right Conda environment for you from the drop-down menu. If you have not yet set one up, [follow our instructions](/clusters-at-yale/guides/jupyter) on how to create a new one. After specifying the required resources (number of CPUs/GPUs, amount of RAM, etc.), you can submit the job. When it launches you can open the standard Jupyter interface where you can start working with notebooks.

#### Root directory

The Jupyter root directory is set to your Home when started. Project and Scratch can be accessed via their respective symlinks in Home. If you want to access a directory that cannot be acessed through your home directory, for example Gibbs, you need to create a symlink to that directory in your home directory. 

#### ycrc_default

The `ycrc_default` conda environment will be automatically built when you select it for the first time from Jupyter. You can also build your own Jupyter and make it available to OOD:

```bash
module load miniconda
conda create -n env_name jupyter jupyter-lab
ycrc_conda_env.list build  
```

Once created, `ycrc_default` will not be updated by OOD automatically. It must be updated by the user manually. To update `ycrc_default`, run the following command from a shell command line:
```bash
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

To fix the problem, you need to configure your RStudio session to use `Cairo` for plotting. 
You can do it in your code as follows: 

```bash
options(bitmapType='cairo')
```

Alternatively, you can put the above code in `.Rprofile` in your home directory and the option will be picked up automatically. 

#### Clean RStudio
If RStudio becomes slow to respond or completely stops responding, please stop the RStudio session and then run the following script at a shell command line:

```
clean_rstudio.sh
```

This will remove any temporary files created by RStudio and allow it to start anew.

### Troubleshoot OOD

#### An OOD session is started and then completed immediately

1. Check if your quota is full
2. Reset your `.bashrc` and `.bash_profile` to their original contents (you can backup the startup files before resetting them. Add the changes back one at a time to see if one or more of the changes would affect OOD from starting properly)  
3. Remove the default module collection file `$HOME/.lmod.d/default.cluster-rhel7` (cluster is one of the following: grace, ruddle, milgram) or `$HOME/.lmod.d/default.mccleary-rhel8` for McCleary.

#### Remote Desktop (or MATLAB, Mathematica, etc) cannot be started properly
1. Make sure there is no initialization left by `conda init` in your `.bashrc`. Clean it with 
```bash
sed -i.bak -ne '/# >>> conda init/,/# <<< conda init/!p' ~/.bashrc
```
2. Run `dbus-launch` and make sure you see the following output:
```bash
[pl543@grace1 ~]$ which dbus-launch
/usr/bin/dbus-launch
```
#### Jupyter cannot be started properly
1.  If you are trying to launch `jupyter-notebook`, make sure it is available in your jupyter conda environment:
```bash
(ycrc_default)[pl543@grace1 ~]$ which jupyter-notebook
/gpfs/gibbs/project/support/pl543/conda_envs/ycrc_default/bin/jupyter-notebook
```
2.  If you are trying to launch `jupyter-lab`, make sure it is available in your jupyter conda environment:
```bash
(ycrc_default)[pl543@grace1 ~]$ which jupyter-lab
/gpfs/gibbs/project/support/pl543/conda_envs/ycrc_default/bin/jupyter-notebook
```
#### RStudio with Conda R
If you see `NOT_FOUND` in "Conda R Environment", it means your Conda R environment has not been properly installed. You may need to reinstall your Conda R environment and make sure `r-base r-essentials` are both included.
#### RStudio Server does not respond
If you encounter a grey screen after clicking the "Connect to RStudio Server" button, please stop the RStudio session and run `clean-rstudio.sh` at a shell command line.
