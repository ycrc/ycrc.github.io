# Access the Web Portal

[Open OnDemand](https://openondemand.org) (OOD) is a platform for accessing the clusters that only requires a web browser.
This web portal provides a shell, file browser, and graphical interface for many apps (such as Jupyter, RStudio or MATLAB).

## Access

Open OnDemand is available on each cluster using your NetID credentials (CAS login) and [DUO MFA](/clusters-at-yale/access/mfa).

!!! warning
    To access Open OnDemand from off campus, you need to connect to the Yale [VPN](https://docs.ycrc.yale.edu/clusters-at-yale/access/vpn). 

| Cluster                        | OOD site                                                         |
|--------------------------------|------------------------------------------------------------------|
| [Grace](/clusters/grace)       | [ood-grace.ycrc.yale.edu](https://ood-grace.ycrc.yale.edu)         |
| [McCleary](/clusters/mccleary) | [ood-mccleary.ycrc.yale.edu](https://ood-mccleary.ycrc.yale.edu) |
| [Milgram](/clusters/milgram)   | [ood-milgram.ycrc.yale.edu](https://ood-milgram.ycrc.yale.edu)     | 



### Web Portal for Courses

Each [academic course](/clusters-at-yale/access/courses) on the YCRC clusters has its own unique URL to access the web portal on the cluster. 
Course web portal URLs are <b>courseID.ycrc.yale.edu</b>, where 'courseID' is the unique abbreviation given to the course. 
Course members must use the course URL to log in to course accounts on Open OnDemand--the normal cluster portals are not accessible to course accounts. 
You will then authenticate using your standard NetID (without the courseid prefix) and password.
Additional information about courses and the associate web portal can be found at [academic support](/clusters-at-yale/access/courses).

## The Dashboard

On login you will see the OOD dashboard.
Along the top are pull-down menus for various Apps, including a file browser, a terminal, a variet of interactive apps.

![welcome](/img/ood_welcome.png){: .large}

## File Browser

![file_browser](/img/ood_filebrowser.png){: .medium}

The file browser, accessible via the `Files` pull-down menu, is a graphical interface to manage, upload, and download files from the clusters.
You can drag-and-drop to download and upload files and directories, and move files between directories using this interface.

You can also use the built-in file editor to view and edit files from your browser without having to download and upload scripts.

### Customize Favorite Paths

You are able to customize favorite paths in the file browser. Use the scripts below to add, remove, and list customized paths:

``` bash
  ood_add_path
  ood_remove_path
  ood_list_path
```

When you run `ood_add_path` from a terminal command line, it will prompt you to add one path at a time, until you type `n` to discontinue. 
`ood_remove_path` allows you to remove any of the paths added by you and `ood_list_path` will list all the paths added by you. 

All the paths added will be shown in the pull-down menu for the file browser, as well as the left pane when the file browser is opened. After you have customized the path configuration from a terminal, go to the OOD dashbaord and click `</> Develop`->`Restart Web Server` on the top right corner navigation bar to make the change effective immediately.

## Terminal

You can launch a traditional command-line interface on the cluster by selecting `Clusters` -> `Shell Access` in the top navigation bar.

This is a convenient way to access the clusters when you don't have access to an ssh client or do not have your ssh keys.

## Interactive Apps

We have deployed a selection of common graphical programs, such as Remote Desktop, Jupyter, RStudtio, and MATLAB, as Interactive Apps on the Web Portal.

!!! warning
    You are limited to 4 interactive app instances (of any type) at one time. 
    Additional instances will be rejected until you delete older open instances. 
    Closing the window does not terminate the interactive app job.
    To terminate the job, click the "Delete" button in your "My Interactive Apps" page in the web portal.

### Launch an Interactive App

Select an app either from the Dashboard or the "Interactive Apps" pull down menu. 
Use the form to request resources and decide what partition your job should run on. 
We recommend either `devel` or, if applicable, your group's private partition.

![remote_desktop](/img/ood_remote.png){: .medium}

Once you launch the job, you will be presented with a notification that your job has been queued.
Depending on the resources requested, you may need to wait for a bit. When the job starts you will see the option to launch the interactive app.
After you click on Launch Remote Desktop (for example), your interactive app will open in a new tab. 

![starting](/img/ood_remote_starting.png){: .medium}

For additional information on specific Interactive Apps, see the following documentation. A full list of available apps can viewed by selecting the "Interactive Apps" pull-down menu.

- [Remote Desktop](/clusters-at-yale/access/ood-remote-desktop)
- [Jupyter](/clusters-at-yale/access/ood-jupyter)
- [RStudio](/clusters-at-yale/access/ood-rstudio)
- [VSCode](/clusters-at-yale/access/ood-vscode)

## User Portal

The User Portal, located under the "Utilities" pull-down menu on the navigation bar, provides a variety of useful information about your recent jobs, the groups that you are a part of, compute and storage utilization, and support and documentation for the use of the clusters.
The User Portal also hosts a cost calculator for jobs submitted to [Priority Tier](/clusters-at-yale/job-scheduling/priority-tier) partitions.
For more information on specific tools in the User Portal, check out the following documentation:

- [Monitor Overall Slurm Usage](/clusters-at-yale/job-scheduling/getusage/#open-ondemand-web-app)
- [Job Performance Monitoring](/clusters-at-yale/job-scheduling/jobstats/)

## Troubleshoot the Web Portal

### An OOD session is started and then completed immediately

<<<<<<< HEAD
1. Check if your quota is full by running the `getquota` command or checking the [User Portal](#user-portal).
=======
![jupyter_form](/img/ood_jupyter_form.png){: .medium}

Make sure that you chose the right Conda environment for you from the drop-down menu. If you have not yet set one up, [follow our instructions](/clusters-at-yale/guides/jupyter) on how to create a new one. After specifying the required resources (number of CPUs/GPUs, amount of RAM, etc.), you can submit the job. When it launches you can open the standard Jupyter interface where you can start working with notebooks.

#### Root directory

The Jupyter root directory is set to your Home when started. Project and Scratch can be accessed via their respective symlinks in Home. If you want to access a directory that cannot be acessed through your home directory, for example Gibbs, you need to create a symlink to that directory in your home directory. 

#### ycrc_default

The `ycrc_default` conda environment will be automatically built when you select it for the first time from Jupyter. You can also build your own Jupyter and make it available to OOD:

```bash
module load miniconda
conda create -n env_name jupyter jupyter-lab
ycrc_conda_env.sh update
```

Once created, `ycrc_default` will not be updated by OOD automatically. It must be updated by the user manually. To update `ycrc_default`, run the following command from a shell command line:
```bash
module load miniconda
conda update -n  ycrc_default jupyter jupyter-lab
```

### VSCode Server

[Visual Studio Code](https://code.visualstudio.com) is a popular development tool that is widely used by our researchers.
While there are several extensions that allow users to connect to remote servers over SSH, these are imperfect and often drop connection. 
Additionally, these remote sessions connect to the clusters' login nodes, where resources are limited.

Instead, we recommend that you run VSCode on a cluster node, within OOD.  There are two ways to do that:

#### As an OOD app
We have developed an application for OOD that launches VSCode in a job on a compute node and opens in a web-browser. 
This application is called `code_server` and is available on all clusters.  This is the simpler method and is the best for most users.

#### Manually within an OOD remote desktop session
This allows more control over the environment, and can be useful if the first method runs into problems.
The steps are:

1. Create an OOD remote desktop session
1. In a terminal in that session, do: `module load VSCode; vscode`


#### Steps for configuring a conda environment within VSCode

1. Install the ms-python and ms-python debugger extensions.
1. Click settings (the gear icon) and search for conda.  Use the the Remote tab for the code_server app or the User tab for a manually started VSCode.  Enter the full path
to your conda executable, e.g. /vast/palmer/apps/avx2/software/miniconda/24.7.1/bin/conda.
1. Open a python file in the file browser.
1. At the bottom right, click on the python version number.  You should see all of the python interpreters in your conda envs.  Choose the interpreter for the env you want.



### RStudio Server

RStudio Server works with R from an R module or from an R Conda environment. Selected R modules on the cluster (ususally the two most recent versions installed on the cluster)
are available in the user form. If you want to use Conda R, you need to run `ycrc_conda_env.sh update` to have it listed in the user form. 


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
ycrc_clean_rstudio.sh
```

This will remove any temporary files created by RStudio and allow it to start anew.

#### Run RStudio in Remote Desktop

While we don't generally encourage our users to run a production R code in RStudio, there are cases that it could be benificial. 
For example, when a user needs to monitor the R code's progress constantly.

RStudio Server is not user friendly for long-running R code. When your CAS session timeout, you won't be able to reconnect
while the code is running. You'll need to wait until the code finishes before
you can connect to the same session again. 

If you need to monitor your R code's progress continuously within the same R session without concerns about disconnection, 
you can run RStudio Desktop within a Remote Desktop environment.

##### Using R module with RStudio Desktop

First, start a Remote Desktop instance in OOD. From the terminal in the Remote Desktop, run the following commands:

```bash
module load R
module load RStudio
rstudio
```

##### Using R Conda with RStudio Desktop

If you want to use R in a Conda environment, start a Remote Desktop instance in OOD first. 
From the terminal in the Remote Desktop, please don't load the modules for R and RStudio. 
Instead, please install 'rstudio-desktop' into your R Conda environment if you haven't done so, 
and then call `rstudio`.  

```bash
module load miniconda
conda activate my_r_env
conda install rstudio-desktop
rstudio
```

### Troubleshoot OOD

#### An OOD session is started and then completed immediately

1. Check if your quota is full by running `getquota` or checking the [User Portal](#user-portal).
2. Reset your `.bashrc` and `.bash_profile` to their original contents (you can backup the startup files before resetting them. Add the changes back one at a time to see if one or more of the changes would affect OOD from starting properly).
3. Remove the default module collection file `$HOME/.lmod.d/default.cluster-rhel8.

### Remote Desktop (or MATLAB, Mathematica, etc) cannot be started properly
1. Make sure there is no initialization left by `conda init` in your `.bashrc`. Clean it with 
```bash
sed -i.bak -ne '/# >>> conda init/,/# <<< conda init/!p' ~/.bashrc
```
2. Run `dbus-launch` and make sure you see the following output:
```bash
[pl543@grace1 ~]$ which dbus-launch
/usr/bin/dbus-launch
```
