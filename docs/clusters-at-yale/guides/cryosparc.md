# CryoSPARC on the YCRC Clusters

!!! info
    As of February, 2026, the YCRC is transitioning to a new CryoSPARC workflow. The instructions below are for use with this new workflow. If you would like assistance with an alternative configuration, please [contact us](/#get-help). 

## Install

Before you get started, you will need to request a license from Structura [from 
their website](https://cryosparc.com/download/). These instructions are somewhat modified from the [official CryoSPARC documentation](https://cryosparc.com/docs/reference/install/). 

### 1. Set up Environment

First, log onto a CPU compute node, either as an [interactive session](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/#interactive-jobs) or an [Open Ondemand Remote Desktop](https://docs.ycrc.yale.edu/clusters-at-yale/access/ood/#remote-desktop). ('devel' is fine for initial cryosparc master installation).

Then choose a location for installing the software, such as under your project directory.

``` bash
export install_path=${HOME}/project/cryosparc
mkdir -p ${install_path}
```

### 2. Set up Directories, Download installers

``` bash
export LICENSE_ID=Your-cryosparc-license-code-here

 #go get the installers
cd $install_path
curl -L https://get.cryosparc.com/download/master-latest/$LICENSE_ID -o cryosparc_master.tar.gz
curl -L https://get.cryosparc.com/download/worker-latest/$LICENSE_ID -o cryosparc_worker.tar.gz

tar -xf cryosparc_master.tar.gz
tar -xf cryosparc_worker.tar.gz
```

### 3. Install the Master

``` bash
# Define temporary password, database location, and server port number
export cryosparc_passwd=Password123

export db_path=${install_path}/cryosparc_database
export port_number="Insert a number from 39000 to 65535 here"

# Run the installation script
cd ${install_path}/cryosparc_master

./install.sh --license $LICENSE_ID \
             --hostname <master_hostname> \
             --dbpath $db_path \
             --port $port_number

# Start CryoSPARC
./bin/cryosparcm start

# Create the first (administrative) user
./bin/cryosparcm createuser --email "<user email>" \
                      --password $cryosparc_password \
                      --username ${USER} \
                      --firstname "<given name>" \
                      --lastname "<surname>"

# Load the environment
source ~/.bashrc

# Stop the master
./bin/cryosparcm stop
```

### 5. Add the cryosparc commands to your system PATH (optional?)

!!!warning
     The installer will likely prompt you with, i.e., 'Add bin directory to your ~/.bashrc ?',
     but this doesn't always work in recent cryosparc installer script versions, at least on the YCRC clusters.
     You can check ~/.bashrc first and see if the paths are already added.  If not, do the following:
     
``` bash
     echo export PATH="${install_path}/cryosparc_master/bin:\$PATH" >> ~/.bashrc
     echo export PATH="${install_path}/cryosparc_worker/bin:\$PATH" >> ~/.bashrc
```

### 6. Install the worker software on a GPU node
     
Exit the above interactive session, and start an interactive session in a GPU partition (e.g., gpu_devel), requesting one GPU.

cd YourCryosparcDirectory

``` bash
cd cryosparc_worker

`grep LICENSE ../cryosparc_master/config.sh`
```
Note that the above command is enclosed in **single left quotes**.

``` bash
./install.sh --license $CRYOSPARC_LICENSE_ID --yes
```

Exit the interactive session. Master and worker software should now be ready.
     
!!!warning
     If you are installing a version of CryoSPARC older than 4.4.0, the instructions are somewhat different. [Contact us](/#get-help) for assistance.
     
## Run (2/10/2026 - Experimental)

Copy /apps/services/cryosparc/cryosparc-cluster-master.sh to your working directory.

Please note, in contrast to our previous cryosparc workflow, the new method *does not use GPU's in the batch script*. Required resources for the script `cryosparc-cluster-master.sh` are minimal and should not be modified. The only change to the #SBATCH directives that may be needed are the running time and partition. Also note, 'worker' nodes are no longer part of this workflow.

To use the new cryosparc workflow, follow the steps below:

1. **To start your cryosparc server**, submit the 'cryosparc-cluster-master.sh' script using `sbatch cryosparc-cluster-master.sh`. With the script, you may (optionally) change the '#SBATCH -t <time>' and '#SBATCH -p <partition>' directive lines to specify the running time and slurm partition to reflect how long you expect your workflow to take. The default request of 7 days on the 'week' partition, with 1 CPU and 8GB of RAM, should be fine.

2. **To interact with your cryosparc server**, launch a minimal [OnDemand Remote Desktop](/clusters-at-yale/access/ood-remote-desktop) session; 1 CPU, 8GB RAM on the 'devel' partition should suffice. There is no need to request more time than you expect to use your browser for, as you can always launch another Remote Desktop and get back to where you were with no information loss.

3. **When submitting analysis tasks on your cryosparc server**, please note that you will now have several compute lanes to choose from, including 'cpu', 'gpu' and (if you have purchased access) 'priority_cpu' and 'priority_gpu'. The cryosparc GUI will prompt you to select one of these choices once you start the job submission process by clicking 'submit job'. **You must then give a job runtime (see below)**

!!!warning
    **You must specify an appropriate runtime upper limit** for your job, prior to clicking 'submit to lane'; otherwise, **your job may be terminated prematurely**. For jobs than run very quickly like micrograph imports, one hour ('1:00:00') is a safe value. However, for long jobs whose durations are uncertain, we suggest 24 hours ('24:00:00'). If you have a safe and reasonable guess that is smaller, this will help your job start sooner.

    **Currently this option is hidden at the bottom of the submission pane** (right-hand side of the window titled 'Queue P*xxx* J*xxx*'). Scroll to the bottom and click on the purple box that says 'Cluster submission script variables'.  The box will expand to reveal additional options, where you can click on 'Maximum runtime'.

    After you click 'Submit to lane', the YCRC slurm scheduler will assign your task to an available compute node. You may then monitor your job not only through cryosparc itself, but also through the YCRC slurm tools (i.e. 'User Portal' from the OOD Utilities menu, or by the terminal command 'squeue --me').

!!!note
    The cryosparc slurm scheduler tries to guess the amount of memory required for a job, which depends on a variety of factors. If you encounter memory-related failures, you may set the 'RAM multiplier' value under 'Cluster submission script variables' to a value greater than one.

!!!note
    **If you change your mind about job runtime** after you submit to a lane, but before it starts running, you may use the following bash terminal command to adjust it, for example:

    ``` bash
    scontrol update JobId=1234567 TimeLimit=6:00:00
    ```

    You may also use slurm to change the partition a job runs in (again, you need to do this before the job starts running):
    
    ``` bash
    scontrol update JobId=1234567 Partition=priority_gpu
    ```
    
## Topaz support (Optional)

[Topaz](https://cb.csail.mit.edu/cb/topaz/) is a pipeline for particle picking in cryo-electron microscopy images using
convolutional neural networks. It can optionally be used from inside CryoSPARC using our cluster module.

### 1. In an interactive cluster session, prepare an executable bash script 'topaz.sh' that loads our topaz module and runs topaz:

```
#!/usr/bin/env bash
if command -v conda > /dev/null 2>&1; then
    conda deactivate > /dev/null 2>&1 || true  # ignore any errors
    conda deactivate > /dev/null 2>&1 || true  # ignore any errors
fi
unset _CE_CONDA
unset CONDA_DEFAULT_ENV
unset CONDA_EXE
unset CONDA_PREFIX
unset CONDA_PROMPT_MODIFIER
unset CONDA_PYTHON_EXE
unset CONDA_SHLVL
unset PYTHONPATH
unset LD_PRELOAD
unset LD_LIBRARY_PATH

module load topaz/0.2.5-fosscuda-2020b
exec topaz $@
```

### 2. Make the topaz.sh script executable:
```
chmod a+x <PATH-TO>/topaz.sh
```
   
### 3. In a running CryoSPARC instance, add the executable '<PATH-TO/topaz.sh' to the General settings:
![](/img/TopazCryosparc.png)

### 4. Consult the [CryoSPARC guide](https://guide.cryosparc.com/processing-data/all-job-types-in-cryosparc/deep-picking/topaz)
for details on using Topaz with CryoSPARC.

## Troubleshoot

If you are unable to start a new CryoSPARC instance, the likeliest reason is leftover files from a previous run that was not shut down properly. Check /tmp and /tmp/${USER} for the existence of a cryosparc*.sock file or a mongo*.sock file.  If they are owned by you, you can just remove them, and CryoSPARC should start normally.  If they are not owned by you, and you have reserved the GPUs, then it is likely due to another user's interrupted job.  Contact YCRC staff for assistance.


If your database won't start and *_you're sure_* there isn't another server running, you can remove lock files and try again.

``` bash
# rm -f $CRYOSPARC_DB_PATH/WiredTiger.lock $CRYOSPARC_DB_PATH/mongod.lock
```
