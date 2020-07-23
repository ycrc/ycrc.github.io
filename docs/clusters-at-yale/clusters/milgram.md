# Milgram

![Stanley](/img/Stanley-Milgram.jpg){: .cluster-portrait}

Milgram is named for Dr. Stanley Milgram, a psychologist who researched the behavioral motivations behind social awareness in individuals and obedience to authority figures. He conducted several famous experiments during his professorship at Yale University including the lost-letter experiment, the small-world experiment, and the Milgram experiment on obedience to authority figures.

Milgram is a HIPAA aligned Department of Psychology cluster intended for use on projects that may involve sensitive data. This applies to both storage and computation. If you have any questions about this policy, please [contact us](/#get-help).

!!! note
    Connections to Milgram can only be made from the Yale VPN (`access.yale.edu`)--even if you are already on campus (YaleSecure or ethernet). See our [VPN page](/clusters-at-yale/access/vpn) for setup instructions. If your group has a workstation (see [list](/clusters-at-yale/clusters/milgram-workstations)), you can connect using one of those.

- - -

## Hardware

Milgram is made up of a couple kinds of compute nodes. The Features column below lists the features that can be used to request different node types using the `--constraints` flag (see our [Slurm documentation](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) for more details). The RAM listed below is the amount of memory available for jobs.

!!! Warning
    Care should be taken when scheduling your job if you are running programs/libraries optimized for specific hardware.
    You can narrow which nodes can run your job by requesting the features from the Node Configurations table as constraints (slurm `--constraint` flag) to your job.
    See the [Request Compute Resources page](/clusters-at-yale/job-scheduling/resource-requests/#features-and-constraints) and the [Build Software page](/clusters-at-yale/applications/compile) for further guidance.

### Compute Node Configurations

| Count | CPU           | CPU Cores | RAM   |         GPU        | vRAM/GPU | Features                                   |
|-------|---------------|-----------|-------|--------------------|----------|--------------------------------------------|
| 12    | 2x E5-2660 v3 | 20        | 121G  |                    |          | haswell, E5-2660_v3, nogpu, oldest         |
| 48    | 2x E5-2660 v4 | 28        | 250G  |                    |          | broadwell, E5-2660_v4, nogpu               |
| 5     | 2x 6240       | 36        | 372G  | 4x rtx2080ti       |       8G | cascadelake, avx512, 6240, nogpu, standard |

## Slurm Partitions

Nodes on the clusters are organized into partitions, to which you submit your jobs with [Slurm](/clusters-at-yale/job-scheduling). The default resource requests for all jobs is 1 core and 5GiB of memory per core. The short partition is where most batch jobs should run, and is the default if you don't specify a partition. The interactive partition is dedicated to jobs with which you need ongoing interaction. The long and verylong partitions are meant for jobs with projected walltimes that are too long to run in short. For courses using the cluster we set aside the education partition. The scavenge partition allows you to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

The limits listed below are for all running jobs combined. Per-node limits are bound by the node types, as described in the [hardware](#hardware) table.

| Partition    | Group Limits           | User Limits             | Walltime Default/Max | Node Type (count)                         |
|--------------|------------------------|-------------------------|----------------------|-------------------------------------------|
| interactive  |                        | 1 job, 4 CPUs, 20 G RAM | 1h/6h                | E5-2660_v3 (2)                            |
| short*       | 1158 CPUs, 10176 G RAM | 772 CPUs, 6784 G RAM    | 1h/6h                | E5-2660_v3 (9), E5-2660_v4 (48)           |
| long         |                        | 1188 CPUs, 5940 G RAM   | 1h/2d                | E5-2660_v3 (9), E5-2660_v4 (48)           |
| verylong     |                        | 792 CPUs, 3960 G RAM    | 1h/7d                | E5-2660_v3 (9), E5-2660_v4 (48)           |
| gpu          |                        |                         | 1h/7d                | 6240 w/ rtx2080ti (5)                     |
| education    |                        |                         | 1h/6h                | E5-2660_v3 (2)                            |
| scavenge     |                        |                         | none                 | E5-2660_v3 (9), E5-2660_v4 (48), 6240 (5) |

\* default

## Storage

`/gpfs/milgram` is Milgram's primary filesystem where home, project, and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/cluster-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage breakdown only update once daily.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

| Partition      | Root Directory             | Storage     | File Count   | Backups |
|----------------|----------------------------|-------------|--------------|---------|
| home           | `/gpfs/milgram/home`       | 20G/user    | 500,000      | Yes     |
| project        | `/gpfs/milgram/project`    | varies      | varies       | No      |
| scratch60      | `/gpfs/milgram/scratch60`  | varies      | 5,000,000    | No      |
