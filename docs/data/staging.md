# Stage Data for Compute Jobs

Large datasets are often stored off-cluster on departmental servers, Storage@Yale, in cloud storage, etc.
Since the _permanent_ home of the data remains on off-cluster storage, you need to [transfer](/data/transfer/) a working copy to the cluster temporarily. When your computation finishes, you would then remove the copy and transfer the results to a more permanent location.

## Temporary Storage

We recommend staging data into your [scratch](/data/hpc-storage/#60-day-scratch) storage space on the cluster, as the _working_ copy of the data can then be removed manually or left to be deleted (which will happen automatically after 60-days). 

## Interactive Transfers
For interactive transfers, please see our [Transfer Data](/data/transfer/) page for a more complete list of ways to move data efficiently to and from the clusters.  

A sample workflow using `rsync` would be:

``` bash
# connect to the transfer node from the login node
[netID@cluster ~] ssh transfer
# copy data to temporary cluster storage
[netID@transfer ~]$ rsync -avP netID@department_server:/path/to/data $HOME/palmer_scratch/
# process data on cluster
[netID@transfer ~]$ sbatch data_processing.sh
# return results to permanent storage for safe-keeping
[netID@transfer ~]$ rsync -avP $HOME/palmer_scratch/output_data netID@department_server:/path/to/outputs/
```

!!! Tip 
    To protect your transfer from network interruptions between your computer and the transfer node, launch your `rsync` inside a [tmux](/clusters-at-yale/guides/tmux/) session on the transfer node.

## Storage@Yale Transfers

Storage@Yale shares are mounted on the transfer nodes on Grace and McCleary, enabling you to stage data from these remote servers.
The process is somewhat simpler than the above example because we do not need to `rsync` the data, and can instead use `cp` directly.

Here, we have modified the `transfer.sbatch` file from above:

### transfer.sbatch

```bash
#!/bin/bash

#SBATCH --partition=day
#SBATCH --time=6:00:00
#SBATCH --cpus-per-task=1
#SBATCH --job-name=my_transfer

cp /SAY/standard/my_say_share/data $HOME/palmer_scratch/

```

This will transfer `data` from the Storage@Yale share to `palmer_scratch` where it can be processed on any of the compute nodes.
