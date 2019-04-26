# Scavenge Partition

A scavenge partition is available on all of our clusters. It allows you to (a) run jobs outside of your normal limits (e.g. `QOSMaxCpuPerUserLimit`) and (b) use unutilized cores, if available, in any private partition on the cluster. You can also use the scavenge partition to get access to unused cores in special purpose partitions, such as the "gpu" or "mpi" partitions, and unused GPUs in private partitions.

However, any job running in the scavenge partition is subject to preemption if any node in use by the job is required for a job in the node's normal partition. This means that your job may be killed without advance notice, so you should only run jobs in the scavenge partition that either have checkpoint capabilities or that can otherwise be restarted with minimal loss of progress.

!!!warning
    Not all jobs are a good fit for the scavenge partition, such as jobs with long startup times or jobs that run a long time between checkpoint operations.

## Automatically Requeue Preempted Jobs

If you would like your job to be automatically added back to the queue if preempted, you can add the `--requeue` flag to your submission script.

```bash
#SBATCH --requeue
```

Be aware that your job, when started from a requeue, will still re-run the entire original submission script. It will only resume progress if your program has the its own ability to checkpoint and restart from previous progress.

### Track History of a Requeued Job

When a scavenge job is requeued after preemption, it retains the same job id. However, this can make it difficult to track the history of the job (how many times it was requeued, how long it ran for each time). To view the full history of your job use the `--duplicates` flag for the `sacct` command.

``` bash
sacct -j <jobid> --duplicates
```

## Scavenge GPUs

On Grace and Farnam, we also have a `scavenge_gpu` partition, that contains all scavenge-able GPU enabled nodes and has higher priority for those node than normal scavenge. In all other ways
(e.g. preemption, time limit), `scavenge_gpu` behaves the same as the normal scavenge partition. You can see the full count of GPU nodes in the Compute Node tables on the respective cluster pages.

## Research Available Nodes

If you are interested in specific hardware and its availability, you can use the `sinfo` command to query how many of each type of node is available and what features it lists. For example:

``` bash
sinfo -e -o "%.6D|%c|%G|%b" | column -ts "|"
```

will show you the kinds of nodes available, and

``` bash
sinfo -e -o "%.6D|%T|%c|%G|%b" | column -ts "|"
```

will break out how many nodes in each state (e.g. allocated, mixed, idle) there are. For more options see the official [`sinfo` documentation](https://slurm.schedmd.com/sinfo.html).