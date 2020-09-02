# Staging Data

Large datasets are often stored off-cluster on departmental servers, Storage@Yale, in cloud storage, etc.
If these data are too large to fit in your current quotas and you do not plan on purchasing more storage (see above), you must stage your data.
Since the _permanent_ copy of the data remains on off-cluster storage, you can [transfer](/clusters-at-yale/data/transfer/) a working copy to `scrach60`, for example.
When your computation finishes you can remove the copy and transmit or copy results to a more permanent location.

A sample workflow using `rsync` would be:

``` bash
# copy data to temporary cluster storage
[netID@cluster ~]$ rsync -avP netID@department_server:/path/to/data $HOME/scratch60/
# process data on cluster
[netID@cluster ~]$ sbatch data_processing.sh
# return results to permanent storage for safe-keeping
[netID@cluster ~]$ rsync -avP $HOME/scratch60/output_data netID@department_server:/path/to/outputs/
```

The _working_ copy of the data can then be removed manually or left to be deleted when it reaches the 60-day limit.
See the [Archive Data](/data/archive/) and [Transfer Data](/clusters-at-yale/data/transfer/) pages for more ways to move data efficiently to and from the clusters.

## Transfer Partition
Both `grace` and `farnam` have dedicated data-transfer partitions (named `transfer`) designed for staging data onto the cluster.
All users are able to submit jobs to these partitions.

We recommend using `tmux` to launch interactive transfers so that you are able to log out and leave the job running in the background.

```bash
# enter tmux shell
[netID@grace1 ~]$ tmux
# launch transfer job
[netID@grace1 ~]$ srun --pty --partition transfer --cpus-per-task=1 --time=6:00:00 bash
# start transfer
[netID@c01n03 ~]$ rsync -avP netID@department_server:/path/to/data $HOME/scratch60/
```
You can then type <kbd>Ctrl</kbd>+<kbd>b</kbd> followed by <kbd>d</kbd> to detach from the `tmux` session.
This will leave your transfer running in the background inside the `tmux` session.
For more details about how to use `tmux`, look at our guide [here](/clusters-at-yale/guides/tmux).

Batch transfer jobs are also possible.
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
We can break this into two separate SLURM jobs: a transfer job followed by a processing job.

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

First we would submit the transfer job to SLURM:

```bash
$ sbatch transfer.sbatch
Submitted batch job 12345678
```

Then we can pass this jobID as a dependency for the processing job:

```bash
$ sbatch --dependency=afterok:12345678 process.sbatch
Submitted batch job 12345679
```
SLURM will now hold the processing job until the transfer finishes:

```bash
$ squeue
JOBID    PARTITION  NAME       USER   ST      TIME  NODES NODELIST(REASON)
12345679       day  process    netID  PD      0:00      1 (Dependency)
12345678  transfer  transfer   netID  R       0:15      1 c01n04
```

## Storage@Yale transfers

Storage@Yale shares are only mounted on the transfer partition, enabling you to stage data from these remove servers.
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
