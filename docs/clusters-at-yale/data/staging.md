# Stage Data for Compute Jobs

Large datasets are often stored off-cluster on departmental servers, Storage@Yale, in cloud storage, etc.
Since the _permanent_ home of the data remains on off-cluster storage, you need to [transfer](/clusters-at-yale/data/transfer/) a working copy to the cluster temporarily. When your computation finishes, you would then remove the copy and transfer the results to a more permanent location.

## Temporary Storage

We recommend staging data into your [Scratch60](/clusters-at-yale/data) storage space on the cluster, as the _working_ copy of the data can then be removed manually or left to be deleted (which will happen automatically after 60-days). 

## Interactive Transfers
For interactive transfers, please see our [Transfer Data](/clusters-at-yale/data/transfer/) page for a more complete list of ways to move data efficiently to and from the clusters.  

A sample workflow using `rsync` would be:

``` bash
# connect to the transfer node from the login node
[netID@cluster ~] ssh transfer
# setup a tmux to protect your transfer from lost local connections
[netID@transfer ~] tmux
# copy data to temporary cluster storage
[netID@transfer ~]$ rsync -avP netID@department_server:/path/to/data $HOME/scratch60/
# process data on cluster
[netID@transfer ~]$ sbatch data_processing.sh
# return results to permanent storage for safe-keeping
[netID@transfer ~]$ rsync -avP $HOME/scratch60/output_data netID@department_server:/path/to/outputs/
```

!!! note 
    When an `rsync` is running, you can type <kbd>Ctrl</kbd>+<kbd>b</kbd> followed by <kbd>d</kbd> to detach from the `tmux` session. This will leave your transfer running in the background inside the `tmux` session. You can reattached to the session with `tmux attach` to check on the progress or move on to the next step.
    For more details about how to use `tmux`, look at our guide [here](/clusters-at-yale/guides/tmux).

## Transfer Partition
Both Grace and Farnam have dedicated data transfer partitions (named `transfer`) designed for staging data onto the cluster.
All users are able to submit jobs to these partitions. Note each users is limited to running two transfer jobs at one time.
If your workflow requires more simultaneuous transfers, contact us for assistance.

### Transfers as Batch Jobs

A sample `sbatch` script for an `rsync` transfer is show here:

```sh
#!/bin/bash

#SBATCH --partition=transfer
#SBATCH --time=6:00:00
#SBATCH --cpus-per-task=1
#SBATCH --job-name=my_transfer
#SBATCH --output=transfer.txt

rsync -av netID@department_server:/path/to/data $HOME/scratch60/

```
This will launch a batch job that will transfer data from `remote.host.yale.edu` to your scratch60 directory.
Note, this will only work if you have set up password-less logins on the remote host.

## Transfer Job Dependencies

There are `sbatch` options that allow you to hold a job from running until a previous job finishes.
These are called Job Dependencies, and they allow you to include a data-staging step as part of your data processing pipe-line.

Consider a workflow where we would like to process data located on a remote server.
We can break this into two separate Slurm jobs: a transfer job followed by a processing job.

### transfer.sbatch

```bash
#!/bin/bash

#SBATCH --partition=transfer
#SBATCH --time=6:00:00
#SBATCH --cpus-per-task=1
#SBATCH --job-name=my_transfer

rsync -av netID@department_server:/path/to/data $HOME/scratch60/

```

### process.sbatch

```bash
#!/bin/bash

#SBATCH --partition=day
#SBATCH --time=6:00:00
#SBATCH --cpus-per-task=1
#SBATCH --job-name=my_process

module purge
module load miniconda

conda activate my_env

python $HOME/process_script.py $HOME/scratch60/data

```

First we would submit the transfer job to Slurm:

```bash
$ sbatch transfer.sbatch
Submitted batch job 12345678
```

Then we can pass this jobID as a dependency for the processing job:

```bash
$ sbatch --dependency=afterok:12345678 process.sbatch
Submitted batch job 12345679
```
Slurm will now hold the processing job until the transfer finishes:

```bash
$ squeue
JOBID    PARTITION  NAME       USER   ST      TIME  NODES NODELIST(REASON)
12345679       day  process    netID  PD      0:00      1 (Dependency)
12345678  transfer  transfer   netID  R       0:15      1 c01n04
```

## Storage@Yale Transfers

Storage@Yale shares are mounted on the transfer partition, enabling you to stage data from these remote servers.
The process is somewhat simpler than the above example because we do not need to `rsync` the data, and can instead use `cp` directly.

Here, we have modified the `transfer.sbatch` file from above:

### transfer.sbatch

```bash
#!/bin/bash

#SBATCH --partition=transfer
#SBATCH --time=6:00:00
#SBATCH --cpus-per-task=1
#SBATCH --job-name=my_transfer

cp /SAY/standard/my_say_share/data $HOME/scratch60/

```

This will transfer `data` from the Storage@Yale share to `scratch60` where it can be processed on any of the compute nodes.
