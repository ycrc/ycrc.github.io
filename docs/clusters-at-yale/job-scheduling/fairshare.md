# Factors Affecting Job Scheduling

## Job Priority Score

### Fairshare

We have "fairshare" systems on our clusters, which means that jobs have a "priority" score that is affected by the amount of CPU hours used in the past few weeks. If a group has used a large amount of CPU hours, their jobs are given a lower priority score and therefore will take longer to start if the cluster is busy. Regardless of a job's prority, the scheduler still considers all jobs for backfill (see below).

To see all pending jobs sorted by priority (jobs with higher priority at the top), use the following `squeue` command:

```
squeue --sort=-p -t PD -p <partition_name>
```

To monitor usage of members of your group, run the `sshare` command:

```
sshare -a -A <group>
```

Note: Resources used on private partitions do not count affect fairshare.

Similarly, resources used in the scavenge partition cost 10% of comparable resources in the other partitions.

### Length of Time in Queue

In addition to fairshare, any pending job will accrue priority over time, which can help overcome small fairshare penalties. To see the factors affecting your job's priority, run the following `sprio` command:

```
sprio -j <job_id>
```

## Backfill

In addition to the main scheduling cycle, where jobs are run in the order of priority and availability of resources, all jobs are also considered for "backfill". Backfill is a mechanism which will let jobs with lower priority score start before high priority jobs if they can fit in around them. For example, if a higher priority job needs 4 nodes with 20 cores on each node and it will have to wait 30 hours for those resources to be available, if a lower priority job only needs a couple cores for an hour, Slurm will run that job in the meantime.

For this reason, it is important to request accurate walltime limits for your jobs. If your job only requires 2 hours to run, but you request 24 hours, the likelihood that your job will be backfilled is greatly lowered. Moreover, for performance reasons, the backfill scheduler on Grace only looks at the top 10 jobs by each user. Therefore, if you bundle similar jobs into job arrays (see [dSQ](dsq)), the backfill cycle will consider more of your jobs since entire job arrays only count as one job for the limit accounting.