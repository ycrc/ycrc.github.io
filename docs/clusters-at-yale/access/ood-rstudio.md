# RStudio

A graphical RStudio is available through our cluster [Web Portals](/clusters-at-yale/access/ood).
Information on accessing the web portal is available on [Access the Web Portal](/clusters-at-yale/access/ood)) documentation page.

## RStudio Server

The RStudio Server app is available on our cluster [Web Portals](/clusters-at-yale/access/ood). 
To get started, connect to one of cluster [Web Portals](/clusters-at-yale/access/ood) and choose Rstudio from the Interactive Apps menu or the dashboard and then follow the instructions for [launching an interactive app](/clusters-at-yale/access/ood/#launch-an-interactive-app).
In the submission form, you can alos select between a number of R versions.

### Change User R Package Path
To change the default path where packages installed by the user are stored, you need to add the following line of code in your `$HOME/.bashrc`:

```bash
export R_LIBS_USER=path_to_your_local_r_packages
```

### Configure the Graphic Device
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

## Troubleshoot: RStudio Server does not respond

We have been observing that users' RStudio server app files seem to become corrupted from time to time; this may cause RStudio to become sluggish or even completey stop responding. We are working to track down the cause of the issue(s); a possible trigger could be ungraceful termination of a previous RStudio session, for example crashing due to a memory error, rather than exiting normally.

To recover from such behavior, terminate any running or pending RStudio sessions and then run the following command in a [terminal](/clusters-at-yale/access/ood#terminal):

```
ycrc_clean_rstudio.sh

# or, if the above fails to fix the problem, do:

ycrc_clean_rstudio.sh -f

# (enter 'y' to the prompt after confirming no RStudio sessions are running)
```

This will remove any temporary files created by RStudio and allow it to start anew.

The second option will basically delete all previous OOD records of your RStudio sessions; this shouldn't be a problem since these records are rarely if ever useful.

## Updating the conda drop-down menu in RStudio Server app

If you have created R conda environments (i.e, in the [terminal](/clusters-at-yale/access/ood#terminal))
then you can make these available within RStudio Server app. From the terminal, execute the following command:

``` bash
ycrc_conda_env.sh update
```


## Run RStudio in Remote Desktop

!!!warning
    The following methods are depracated and no longer work as is; if you need alternative methods for running RStudio, please contact us by email ([hpc@yale.edu](mailto:hpc@yale.edu)) or online ([help.ycrc.yale.edu](https://help.ycrc.yale.edu))

While we don't generally encourage our users to run a production R code in RStudio, there are cases that it could be beneficial. 
For example, when a user needs to monitor the R code's progress continuously.

RStudio Server is not user friendly for long-running R code.
When your CAS session timeout, you won't be able to reconnect
while the code is running.
You will need to wait until the code finishes before you can connect to the same session again. 

If you need to monitor your R code's progress continuously within the same R session without concerns about disconnection, 
you can run RStudio Desktop within a Remote Desktop environment.

### Using R module with RStudio Desktop

First, start a Remote Desktop instance in the web portal. From the terminal in the Remote Desktop, run the following commands:

```bash
module load R
module load RStudio
rstudio
```

### Using R Conda with RStudio Desktop

If you want to use R in a Conda environment, start a Remote Desktop instance in the web portal first. 
From the terminal in the Remote Desktop, do *not* load the modules for R and RStudio. 
Instead, install 'rstudio-desktop' into your R Conda environment if you have not done so, 
and then call `rstudio`.  

```bash
module load miniconda
conda activate my_r_env
conda install rstudio-desktop
rstudio
```

## Troubleshoot: RStudio with Conda R

If you see `NOT_FOUND` in "Conda R Environment", it means your Conda R environment has not been properly installed. You may need to reinstall your Conda R environment, making sure `r-base r-essentials` are both included; then
