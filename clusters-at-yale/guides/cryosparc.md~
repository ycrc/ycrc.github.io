# CryoSPARC on the YCRC Clusters

CryoSPARC is widely used and powerful structural biology tool. The YCRC has developed a workflow to facilitate use of this software on our clusters. Instructions on how to install and use cryoSPARC on YCRC clusters are given below.

_(June 2026): We have newly streamlined our cryoSPARC workflow, both for installation and running the app._

!!! Note
    CryoSPARC can be tricky to debug. If/when you encounter problems, please check our growing list of [troubleshooting tips](#troubleshooting) that are shared at the bottom of this page. Please do not hesitate to [contact us](https://docs.ycrc.yale.edu/#web-and-email-support) if you encounter difficulties running this program.

## Install

To operate cryoSPARC on a YCRC cluster, please use our installer script following the steps below. This automates the procedure described in the [official cryoSPARC documentation](https://cryosparc.com/docs/reference/install/), and integrates the installation within our YCRC HPC framework.

**Please do steps 1 and 2 below right away**, as they are quick and easy, and it could take up to a day to get the needed responses.

1. **Request a cryoSPARC License** : Visit the Structura website and [fill out the License Request Form](https://cryosparc.com/download/).

2. **Request a YCRC cryoSPARC Port Number** : Start a terminal shell on the desired cluster (login node is fine, no need to use a compute node) and paste the following command:
    ```
    /apps/services/cryosparc/ycrc_get_cryosparc_port.sh    
    ```

    - A message will be printed, confirming that an email request has been sent to the YCRC. We will do the assignment by the next working day, and you will be automatically notified by email when this is completed.
                                            
3. **Run the Installer** : Once you have received your cryoSPARC license and YCRC port number, run the installer by pasting the following command in a cluster terminal (again, login node is fine):

    ``` bash
    /apps/services/cryosparc/ycrc_prepare_cryosparc.sh <your-cryosparc-license>
    ```

    - The script will launch a pair of batch jobs in the background and print helpful info. You will receive confirmation emails upon completion of the jobs.

    - If the installation fails, for example if you do not have enough space available in your project account, please [contact us](https://docs.ycrc.yale.edu/#web-and-email-support) for assistance.

    !!! Note
        **Older cryoSPARC versions** : Please note that our script installs the latest version of cryoSPARC. If you wish to use an older version of CryoSPARC, please follow [these instructions](https://guide.cryosparc.com/setup-configuration-and-management/software-system-guides/guide-updating-to-cryosparc-v5#downgrade-from-cryosparc-v5-to-v4) to downgrade cryoSPARC after the YCRC installation script has finished.
    
## Run the YCRC cryosparc workflow
To use the new cryosparc workflow, follow the steps below.

**Please note** : if you have already been using an older cryoSPARC workflow, you may be notified that a 'YCRC cryoSPARC port' has been requested. It is fine to use your old workflow in the meantime, while you wait for email notification that your port has been assigned.

1. **Launch your cryosparc server** : In a new cluster terminal window (login node is fine), enter the following command:
    ```
    ycrc_launch_cryosparc.sh
    ```

2. **Connect to the cryoSPARC GUI with your web browser** : `ycrc_launch_cryosparc.sh` will print instructions on how to connect to the cryoSPARC GUI. You may choose one of two options:

    A. Connecting from your local laptop web browser

    B. Launching a minimal [OnDemand Remote Desktop session](https://docs.ycrc.yale.edu/clusters-at-yale/access/ood-remote-desktop) and using firefox. We suggest using the following options for your session: `devel` partition with 1 CPU and 32 GB RAM, up to 6 hours runtime.

    - Note, you may re-run `ycrc_launch_cryosparc.sh` after the initial launch to obtain this connection info anytime.

3. **Submit job** : Once you start the job submission process by clicking on `Submit job` in the job builder, the cryosparc GUI will prompt you to choose a compute lane that individual jobs will be submitted to. YCRC has set up the following lanes for your use: `cpu`, `gpu`, `gpu_devel` as well as `priority_cpu` and `priority_gpu` if you have purchased [priority tier access](/clusters-at-yale/job-scheduling/priority-tier/). 

4. **Specify the job runtime** (important): after selecting the compute lane, you must explicitly give a suitable slurm runtime. **Currently this option is hidden at the bottom of the submission pane** (tab on the right-hand side of the window, titled `Queue P*xxx* J*xxx*`). Click on the purple box beneath your selected compute lane, labeled `Cluster submission script variables`. The box will expand to reveal two additional options. Click on `Maximum runtime` and give your value in hours:minutes:seconds format (i.e. 1:00:00).

    !!! Note
        The runtime should be generous, otherwise your job may be terminated prematurely; on the other hand, if you significantly overestimate the runtime, this may cause delays in when your job actually starts running. You may need to experiment to get a sense of what works best for your particular use cases. Please share any info you learn on this, so we can help make cryosparc easier for users to manage.

5. **Optionally specify a 'memory multiplier'** : When cryosparc submits your job to slurm, it will try to guess the amount of memory required; however, for certain job types we have found that this guess can underestimate the memory requirements, **leading to memory-related job failures**. If a job crashes unexpectedly, find the job ID in the cryosparc log and run `jobstats` to confirm whether this is a memory issue ('State: OUT_OF_MEMORY'; see [CryoSPARC job issues](#cryosparc_job_issues) in our Troubleshooting section).

    - To fix this type of memory issue, set the `RAM multiplier` to a value larger than one; a value of 4 is quite conservative and should almost always work, while 2 may suffice for many cases. `RAM multiplier` is found in the `Cluster submission script variables` along with `Maximum runtime` (described above).

    - Job types where we have seen this problem include:  'Local Refinement', '2D Classification' and '2D Template Matching'

6. **Click 'Submit to lane'** : the YCRC slurm scheduler will assign your task to an available compute node. It will be helpful to monitor your job not only in the cryosparc GUI, but also using the YCRC slurm tools (i.e. 'User Portal' from the OOD Utilities menu, or the terminal command `squeue --me`).

    - Note, if you change your mind about job runtime after you submit to a lane, but before it starts running, you may use the following bash terminal command to adjust it, for example:

    ``` bash
    scontrol update JobId=1234567 TimeLimit=6:00:00
    ```

    You may also use slurm to change the partition a job runs in (again, you need to do this before the job starts running):
    
    ``` bash
    scontrol update JobId=1234567 Partition=priority_gpu
    ```
         
## Add Topaz

[Topaz](https://cb.csail.mit.edu/cb/topaz/) is a pipeline for particle picking in cryo-electron microscopy images using
convolutional neural networks. It can optionally be used from inside CryoSPARC using our cluster module.

1. **In a running CryoSPARC instance, add the executable '/apps/services/cryosparc/topaz.sh' to the General settings** :
    ![](/img/TopazCryosparc.png)

2. **Consult the [cryoSPARC guide](https://guide.cryosparc.com/processing-data/all-job-types-in-cryosparc/deep-picking/topaz)** for details on using Topaz with CryoSPARC.

## Troubleshooting

Unfortunately, information needed to diagnose cryoSPARC job failures in cluster lanes can be a bit tedious to track down. Luckily, we have found that most job failures have simple explanations and solutions. Listed below are notes on how to solve some of the more common problems.

### CryoSPARC job issues

1. **Insufficient memory** : this is probably most common source of cryoSPARC job failures, other than not **specifying enough runtime**. Unfortunately, cryoSPARC itself provides little or no diagnostic information on this type of problem. If you do not see an obvious source for the job failure within cryoSPARC, check for a memory failure using our [jobstats tools](/clusters-at-yale/job-scheduling/jobstats/):

    - Go to the OnDemand [User Portal](/clusters-at-yale/access/ood/#user-portal), click on 'Job Overview' on the left and then select an appropriate time period from the blue drop-down menu box at the top. Locate your job 'cryosparc_Pxx_Jxxx' from the list of jobs, and check for 'OUT_OF_MEMORY' under the 'State' column.

    - If this was the problem, increase the job memory by changing the `mem_multiplier` parameter- see 'Optionally specify a memory multiplier' under [Run the YCRC cryosparc workflow](#run-the-ycrc-cryosparc-workflow) for details on how to do this.

2. **Resource requests do not match the requested partition** : if you see a `Job violates accounting/QOS policy` error message and/or a job submission fails immediately (before the process even starts running) this indicates the requested job runtime (or, possibly, memory) may exceed the allowed user limit in a given partition. To fix, switch partitions or change the `Maximum runtime` parameter (see above sections under [Running](#run-the-ycrc-cryosparc-workflow)).

3. **Drilling down further** : Within the cryoSPARC interface, find the job location (located in a text box) and copy it by clicking on it. Then, in a terminal, navigate to this folder where you will find a number of useful files, including log files (i.e., `P1_J2_slurm.log`, `P1_J2_slurm.err`, `job.log`) and also a copy of the slurm submission script (`queue_sub_script.sh`). A useful debugging technique is to create a copy of queue_sub_script.sh outside the job folder, edit and manually submit it. If the target YCRC partition is busy, you can accelerate your diagnosis by giving the script 'lightweight' slurm parameters and specifying the gpu_devel partition. In this way you can quickly get the job started on slurm, allowing trivial errors to be quickly spotted.

4. **Mismatch between cryoSPARC and GPU/CUDA** Newer graphics cards being installed on the Bouchet cluster are incompatible with cryoSPARC versions prior to 5.0.0. This can cause certain jobs (but not all) GPU-dependent jobs to crash. The solution is to upgrade your cryoSPARC to version >= 5.0.0

5. **CryoSPARC installation bug**: One of our users experienced a issue where cryoSPARC GPU jobs uniformly crashed on startup, failing with a cryptic Python error. We have found a way fix this problem by patching the cryoSPARC python libraries (a buggy CUDA version compatibility check).

### General cryoSPARC issues

1. **Database corruption** : Occasionally a crash or other interrupted task may damage cryoSPARC's 'mongo' database. If it cannot be repaired, you can make use of our [daily project folder snapshots](/data/backups/#retrieve-data-from-snapshots) to restore a previous version of the `cryosparc_database` folder from the past several days. This can avoid a long and painful troubleshooting process with minimal loss of work.

    ``` bash
    cd $(dirname "$(dirname "$(dirname "$(which cryosparcm)")")")
    mv cryosparc_database cryosparc_database_corrupt

    # Now substitute, i.e., snapshot_2026-06-02_17_00_00_UTC for <good_backup_date> in the command below:
    cp -a "../.snapshot/<good_backup_date>/cryosparc/cryosparc_database" .
    ```

2. **Browser issues** : Firefox's cache files can become corrupted under certain circumstances (i.e. browser crash) leading to a blank screen when visiting the cryoSPARC GUI page. This can be fixed by resetting Firefox's history and cache data for the page. To do this, open firefox and then:

    - Select `Manage history` (click on the Firefox hamburger menu at the window upper right, then click `History` -> `Manage History`)
    - Click on the search box and type `ycrc.yale.edu`
    - Right click on any cryoSPARC history entries, select `Forget About This Site...`, then click `Forget`
    - Repeat until there are no more cryoSPARC entries left
    - Close the history window and select `Settings` from the Firefox hamburger menu
    - Click `Privacy & Security`, scroll down to `Cookies and Site Data`, and click `Manage Data...`
    - If you see any remaining cryoSPARC entries, click on them and select `Remove Selected`, then `Save Changes`
    - Quit and restart firefox ; hopefully you can now successfully load the cryoSPARC page
    - If this doesn't work the first time, repeating the above steps one or two times more may still resolve the issue

3. **Leftover lock files** : If your submitted cryoSPARC master job is running but unable to start a new CryoSPARC instance, the likeliest reason is leftover files from a previous run that was not shut down properly. Login to the compute node of your cryoSPARC master job and check if cryoSPARC is running with `cryosparcm status`, and check your cryoSPARC master cluster logfile for errors related to the cryoSPARC data base and/or 'mongo'. If a cryosparcm has failed to run and/or you see signs of a database problem, check /tmp and /tmp/${USER} on the compute node for the existence of a `cryosparc*.sock` file or a `mongo*.sock` file.  If they are owned by you, you can just remove them and restart the cryoSPARC master process with `cryosparcm start`. If these files are present but are not owned by you, then it is likely due to another user's interrupted job.  Contact YCRC staff for assistance.

    If your database won't start and *_you're sure_* there isn't another server running, you can remove lock files and try again.

    ``` bash
    # source $(dirname "$(dirname "$(which cryosparcm)")")/config.sh
    # rm -f $CRYOSPARC_DB_PATH/WiredTiger.lock $CRYOSPARC_DB_PATH/mongod.lock
    ```

