# Milgram

![Stanley](/img/Stanley-Milgram.jpg){: .cluster-portrait}

Milgram is named for Dr. Stanley Milgram, a psychologist who researched the behavioral motivations behind social awareness in individuals and obedience to authority figures. He conducted several famous experiments during his professorship at Yale University including the lost-letter experiment, the small-world experiment, and the Milgram experiment on obedience to authority figures.

Milgram is a HIPAA aligned Department of Psychology cluster intended for use on projects that may involve sensitive data. This applies to both storage and computation. If you have any questions about this policy, please [contact us](mailto:hpc@yale.edu).

!!! note
    Connections to Milgram can only be made from the HIPAA VPN (`access.yale.edu/hipaa`). See our [VPN page](/clusters-at-yale/access/vpn) for setup instructions.

- - -

## Hardware

Milgram is made up of a couple kinds of compute nodes. The Features column below lists the features that can be used to request different node types using the `--constraints` flag (see our [Slurm documentation](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) for more details). The RAM listed below is the amount of memory available for jobs.

!!! Warning
    Care should be taken if when scheduling your job if you are running programs/libraries optimized for specific hardware.
    See the [guide on how to compile software](/clusters-at-yale/applications/compile) for specific guidance.

### Compute Node Configurations

| Count | Node Type     | CPU           | CPU Cores | RAM   | Features                                     |
|-------|---------------|---------------|-----------|-------|----------------------------------------------|
| 12    | Dell R730     | 2x E5-2660 v3 | 20        | 121G  | haswell, v3, sse4_2, avx, avx2, E5-2660_v3   |
| 48    | Lenovo nx360b | 2x E5-2660 v4 | 28        | 250G  | broadwell, v4, sse4_2, avx, avx2, E5-2660_v4 |

## Slurm Partitions

Nodes on the clusters are organized into partitions, to which you submit your jobs with [Slurm](/clusters-at-yale/job-scheduling). The short partition is where most batch jobs should run, and is the default if you don't specify a partition. The interactive partition is dedicated to jobs with which you need ongoing interaction. The long and verylong partitions are meant for jobs with projected walltimes that are too long to run in short. For courses using the cluster we set aside the education partition. The scavenge partition allows you to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

All the node types listed are described in more detail in the [hardware](#hardware) table.

| Partition    | Group Limits           | User Limits             | Walltime default/max | Node type (number)    |
|--------------|------------------------|-------------------------|----------------------|-----------------------|
| short*       | 1158 CPUs, 10176 G RAM | 772 CPUs, 6784 G RAM    | 1h/6h                | nx360b (48), R730 (9) |
| interactive  |                        | 1 job, 4 CPUs, 20 G RAM | 1h/6h                | R730 (1)              |
| long         |                        | 1188 CPUs, 5940 G RAM   | 1h/2d                | nx360b (48), R730 (9) |
| verylong     |                        | 792 CPUs, 3960 G RAM    | 1h/7d                | nx360b (48), R730 (9) |
| education    |                        |                         | 1h/6h                | R730 (2)              |
| scavenge     |                        |                         | none                 | nx360b (48), R730 (9) |

\* default

## Storage

`/gpfs/milgram` is Milgram's primary filesystem where home, project, and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/cluster-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage breakdown only update once daily.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition  | Root Directory        | Storage     | File Count | Backups |
|-----------|-----------------------|-------------|------------|---------|
| home      | `/gpfs/milgram/home`  | 100G/user   | 500,000    | Yes     |