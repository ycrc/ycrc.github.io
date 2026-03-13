# CryoSPARC on the YCRC Clusters

!!! info
    As of February, 2026, the YCRC is transitioning to a new CryoSPARC workflow. The instructions below are for use with this new workflow. If you would like assistance with an alternative configuration, please [contact us](/#get-help). 

!!! info
    To start using the new workflow, you will need to do two things: (1) [install cryosparc](#install) if you haven't done so already (your existing installation should work fine) (2) [update your cryosparc port](#obtaining-your-unique-cryosparc-port) - this is very important to avoid conflicts with other cryosparc users.

## Running the YCRC cryosparc workflow

To use the new cryosparc workflow, follow the steps below:

1. **To start your cryosparc server**, submit the 'cryosparc-cluster-master.sh' script using:
    ```
    sbatch /apps/services/cryosparc/cryosparc-cluster-master.sh

    # To override the default runtime and partition, which may be useful for shorter runs,
    #  add the corresponding flags before the script name in your sbatch command, i.e.:
    sbatch -t 6:00:00 -p devel /apps/services/cryosparc/cryosparc-cluster-master.sh
    ```
    Please note, in contrast to our previous cryosparc workflow, this batch script *does not use GPUs* and requires only minimal resources to run the 'master' cryosparc process. The default batch script parameters specify 7 days on the 'week' partition, with 1 CPU and 32 GB of RAM.

2. **To interact with your cryosparc server**, launch a minimal [OnDemand Remote Desktop](/clusters-at-yale/access/ood-remote-desktop) session; 1 CPU, 8GB RAM on the 'devel' partition should suffice. There is no need to request more time than you expect to use your browser for, as the cryosparc server continues running as a separate batch job and you can always launch another Remote Desktop and get back to where you were.

3. **Submit job** : Once you start the job submission process by clicking on 'Submit job' in the job builder, the cryosparc GUI will prompt you to choose a compute lane that individual jobs will be submitted to. YCRC has set up the following lanes for your use: 'cpu', 'gpu', 'gpu_devel' as well as 'priority_cpu' and 'priority_gpu' if you have purchased [priority tier access](/clusters-at-yale/job-scheduling/priority-tier/). 

4. **Specify the job runtime** (important): after selecting the compute lane, you must explicitly give a suitable slurm runtime. **Currently this option is hidden at the bottom of the submission pane** (tab on the right-hand side of the window, titled 'Queue P*xxx* J*xxx*'). Click on the purple box beneath your selected compute lane, labeled 'Cluster submission script variables'. The box will expand to reveal two additional options. Click on 'Maximum runtime' and give your value in hours:minutes:seconds format (i.e. 1:00:00).
    The runtime should be generous, otherwise your job may be terminated prematurely; on the other hand, if you significantly overestimate the runtime, this may cause delays in when your job actually starts running. You may need to experiment to get a sense of what works best for your particular use cases. Please share any info you learn on this, so we can help make cryosparc easier for users to manage.

5. **Optionally specify a 'memory multiplier** : When cryosparc submits your job to slurm, it will try to guess the amount of memory required; however, for certain job types such as 2D classification and template matching we have found that this guess can underestimate the memory requirements, **leading to memory-related job failures**. If a job crashes unexpectedly, find the job ID in the cryosparc log and run jobstats to pinpoint the problem (see the [troubleshooting cryosparc jobs]() section below).

    To fix this type of memory issue, set the 'RAM multiplier' to a value larger than one; a value of 4 is quite conservative and should almost always work, while 2 may suffice for many cases. 'RAM multiplier' is found in the 'Cluster submission script variables' along with 'Maximum runtime' (described above).

6. **Click 'Submit to lane'** : the YCRC slurm scheduler will assign your task to an available compute node. It will be helpful to monitor your job not only in the cryosparc GUI, but also using the YCRC slurm tools (i.e. 'User Portal' from the OOD Utilities menu, or the terminal command 'squeue --me').

    Note, if you change your mind about job runtime after you submit to a lane, but before it starts running, you may use the following bash terminal command to adjust it, for example:

    ``` bash
    scontrol update JobId=1234567 TimeLimit=6:00:00
    ```

    You may also use slurm to change the partition a job runs in (again, you need to do this before the job starts running):
    
    ``` bash
    scontrol update JobId=1234567 Partition=priority_gpu
    ```

## Obtaining Your Unique Cryosparc Port

To use cryosparc with the YCRC cluster workflow, you need to obtain a unique 'port' value that cryosparc uses for displaying web pages, etc. We provide a script for doing this that you can run from a terminal, as follows:

    ```
    # Experimental script, development in progress
    /apps/services/cryosparc/ycrc_get_cryosparc_port.sh    
    ```
## Install

Before you get started, you will need to request a license from Structura [from 
their website](https://cryosparc.com/download/). These instructions are somewhat modified from the [official CryoSPARC documentation](https://cryosparc.com/docs/reference/install/). 

1. **Set up Environment** : First, log onto a CPU compute node, either as an [interactive session](/clusters-at-yale/job-scheduling/#interactive-jobs) or an [Open Ondemand Remote Desktop](/clusters-at-yale/access/ood/#remote-desktop). ('devel' is fine for initial cryosparc master installation).

    Then choose a location for installing the software, such as under your project directory.

    ``` bash
    export install_path=${HOME}/project/cryosparc
    mkdir -p ${install_path}
    ```

2. **Set up Directories, Download installers** :

    ``` bash
    export LICENSE_ID=Your-cryosparc-license-code-here

    #go get the installers
    cd $install_path
    curl -L https://get.cryosparc.com/download/master-latest/$LICENSE_ID -o cryosparc_master.tar.gz
    curl -L https://get.cryosparc.com/download/worker-latest/$LICENSE_ID -o cryosparc_worker.tar.gz

    tar -xf cryosparc_master.tar.gz
    tar -xf cryosparc_worker.tar.gz
    ```

3. **Install the Master** :

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

4. **Add the cryosparc commands to your system PATH (optional?)** :

    !!!warning
     The installer will likely prompt you with, i.e., 'Add bin directory to your ~/.bashrc ?',
     but this doesn't fully work in recent cryosparc installer script versions, at least on the YCRC clusters.
     You can check ~/.bashrc first and see if the paths are already added at the end ('# Added by cryosparc').
     If one or both are missing (typically we find only the 'master' path and not the 'worker' path), do the following:
     
    ``` bash
    echo export PATH="${install_path}/cryosparc_master/bin:\$PATH" >> ~/.bashrc
    echo export PATH="${install_path}/cryosparc_worker/bin:\$PATH" >> ~/.bashrc
    ```

5. **Install the worker software on a GPU node** : 
     
    Exit the above interactive session, and start an interactive session in a GPU partition (e.g., gpu_devel), requesting one GPU.

    cd YourCryosparcDirectory

    ``` bash
    cd cryosparc_worker

    $(grep LICENSE ../cryosparc_master/config.sh)
    ```

    ``` bash
    ./install.sh --license $CRYOSPARC_LICENSE_ID --yes
    ```

    Exit the interactive session. Master and worker software should now be ready.
     
    !!!warning
         If you are installing a version of CryoSPARC older than 4.4.0, the instructions are somewhat different. [Contact us](/#get-help) for assistance.
         
## Topaz Support

[Topaz](https://cb.csail.mit.edu/cb/topaz/) is a pipeline for particle picking in cryo-electron microscopy images using
convolutional neural networks. It can optionally be used from inside CryoSPARC using our cluster module.

1. **In a running CryoSPARC instance, add the executable '<PATH-TO/topaz.sh' to the General settings** :
    ![](/img/TopazCryosparc.png)

2. **Consult the [CryoSPARC guide](https://guide.cryosparc.com/processing-data/all-job-types-in-cryosparc/deep-picking/topaz)** for details on using Topaz with CryoSPARC.

## Troubleshooting (general)

1. **Leftover lock files** : If your submitted cryosparc master job is running but unable to start a new CryoSPARC instance, the likeliest reason is leftover files from a previous run that was not shut down properly. Login to the compute node of your cryosparc master job and check if cryosparc is running with 'cryosparcm status', and check your cryosparc master cluster logfile for errors related to the cryosparc data base and/or 'mongo'. If a cryosparcm has failed to run and/or you see signs of a database problem, check /tmp and /tmp/${USER} on the compute node for the existence of a `cryosparc*.sock` file or a `mongo*.sock` file.  If they are owned by you, you can just remove them and restart the cryosparc master process with 'cryosparcm start'. If these files are present but are not owned by you, then it is likely due to another user's interrupted job.  Contact YCRC staff for assistance.

    If your database won't start and *_you're sure_* there isn't another server running, you can remove lock files and try again.

    ``` bash
    # rm -f $CRYOSPARC_DB_PATH/WiredTiger.lock $CRYOSPARC_DB_PATH/mongod.lock
    ```

2. **Database corruption** : Occasionally a crash or other interrupted task may damage cryosparc's 'mongo' database. If it cannot be repaired, you can make use of our [daily project folder snapshots](/data/backups/#retrieve-data-from-snapshots) to restore a previous version of the 'cryosparc_database' folder from the past several days. This can avoid a long and painful troubleshooting process with minimal loss of work.

## Troubleshooting cryosparc jobs

Unfortunately, information needed to diagnose cryosparc job failures in cluster lanes can be a bit tedious to track down. Luckily, we have found that most job failures have simple explanations and solutions. The main causes are:

1. **Insufficient memory** : this is probably most common source of cryosparc job failures, but sadly provides little to no diagnostic information within cryosparc itself. If you do not see an obvious source for the job failure within cryosparc, check for a memory failure using our [jobstats tools](/clusters-at-yale/job-scheduling/jobstats/). You will first need find the slurm ID of the failed job; you can find this in the job log file by clicking 'Show from top' and scrolling down to the output lines describing the job submission. If you identify a memory issue as the source of the job crash, fix by changing the 'mem_multiplier' parameter (see above sections under [Running](#running-the-ycrc-cryosparc-workflow)).

2. **Resource requests do not match the requested partition** : if you see a 'Job violates accounting/QOS policy' error message and/or a job submission fails immediately (before the process even starts running) this indicates the requested job runtime (or, possibly, memory) may exceed the allowed user limit in a given partition. To fix, switch partitions or change the 'Maximum runtime' parameter (see above sections under [Running](#running-the-ycrc-cryosparc-workflow)).

3. **Drilling down further** : Within the cryosparc interface, find the job location (located in a text box) and copy it by clicking on it. Then, in a terminal, navigate to this folder where you will find a number of useful files, including log files (i.e., `P1_J2_slurm.log`, `P1_J2_slurm.err`, `job.log`) and also a copy of the slurm submission script (`queue_sub_script.sh`). A useful debugging technique is to create a copy of queue_sub_script.sh outside the job folder, edit and manually submit it. If the target YCRC partition is busy, you can accelerate your diagnosis by giving the script 'lightweight' slurm parameters and specifying the gpu_devel partition. In this way you can quickly get the job started on slurm, allowing trivial errors to be quickly spotted.
