# Grace

![Grace](/img/Grace-Hopper.jpg){: .cluster-portrait}

The Grace cluster is is named for the computer scientist and United States Navy Rear Admiral [Grace Murray Hopper](https://en.wikipedia.org/wiki/Grace_Hopper), who received her Ph.D. in Mathematics from Yale in 1934.

Grace is a shared-use resource for the [Faculty of Arts and Sciences](https://fas.yale.edu) (FAS). It consists of a variety of compute nodes networked over low-latency InfiniBand and mounts several shared filesystems.

- - -

## Hardware

Grace is made up of several kinds of compute nodes. The Features column below lists the features that can be used to request different node types using the `--constraints` flag (see our [Slurm documentation](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) for more details). The RAM listed below is the amount of memory available for jobs.

!!! Warning
    Care should be taken if when scheduling your job if you are running programs/libraries optimized for specific hardware.
    See the [guide on how to compile software](/clusters-at-yale/applications/compile) for specific guidance.

### Compute Node Configurations

| Count | Node Type              | CPU                 | CPU Cores | RAM   |         GPU        | Features                                |
|-------|------------------------|---------------------|-----------|-------|--------------------|-----------------------------------------|
| 80    | IBM nx360i             | 2x E5-2660 v2       | 20        | 121G  |                    | ivybridge,v2,sse4_2,avx,E5-2660_v2      |
| 136   | Lenovo nx360h          | 2x E5-2660 v3       | 20        | 121G  |                    | haswell,v3,sse4_2,avx,avx2,E5-2660_v3   |
| 20    | Lenovo nx360h          | 2x E5-2660 v3       | 20        | 247G  |                    | haswell,v3,sse4_2,avx,avx2,E5-2660_v3   |
| 6     | Lenovo nx360h w/ GPUs  | 2x E5-2660 v3       | 20        | 121G  | 2x K80 (2GPUs/K80) | haswell,v3,sse4_2,avx,avx2,E5-2660_v3   |
| 8     | Lenovo nx360h w/ GPUs  | 2x E5-2660 v3       | 20        | 247G  | 1x K80 (2GPUs/K80) | haswell,v3,sse4_2,avx,avx2,E5-2660_v3   |
| 161   | Lenovo nx360b          | 2x E5-2660 v4       | 28        | 247G  |                    | broadwell,v4,sse4_2,avx,avx2,E5-2660_v4 |
| 7     | Lenovo nx360b          | 2x E5-2660 v4       | 28        | 247   | 1x P100            | broadwell,v4,sse4_2,avx,avx2,E5-2660_v4 |
| 53    | Lenovo sd530           | 2x Gold 6136        | 24        | 90G   |                    | skylake,sse4_2,avx,avx2,avx512,6136     |
| 1     | Lenovo sd530           | 2x Gold 6136        | 24        | 176G  |                    | skylake,sse4_2,avx,avx2,avx512,6126     |
| 1     | Lenovo sd530 w/ GPUs   | 2x Gold 6136        | 24        | 90G   | 2x v100            | skylake,sse4_2,avx,avx2,avx512,6136     |
| 1     | Lenovo sd530           | 2x Gold 6136        | 24        | 751G  |                    | skylake,sse4_2,avx,avx2,avx512,6136     |
| 1     | Lenovo x3850i          | 4x E7-4820 v2       | 32        | 1003G |                    | ivybridge,v2,sse4_2,avx,E7-4820_v2      |
| 1     | Lenovo x3850h          | 4x E7-4809 v2       | 32        | 2011G |                    | haswell,v3,sse4_2,avx,avx2,E7-4809_v3   |
| 4     | Lenovo x3850b          | 4x E7-4820 v4       | 40        | 1507G |                    | broadwell,v4,sse4_2,avx,avx2,E7-4820_v4 |
| 1     | Thinkmate GPX XT4      | 2x E5-2637 v4       | 8         | 121G  | 4x 1080Ti          | broadwell,v4,sse4_2,avx,avx2,E5-2637_v4 |
| 9     | Penguin XE2118GT       | 2x Gold 6136        | 24        | 183G  | 4x p100            | skylake,sse4_2,avx,avx2,avx512,6136     |

## Slurm Partitions

Nodes on the clusters are organized into partitions, to which you submit your jobs with [Slurm](/clusters-at-yale/job-scheduling/slurm).

### Public Partitions TODO

The general partition is where most batch jobs should run, and is the default if you don't specify a partition. The interactive partition is dedicated to jobs with which you need ongoing interaction. The bigmem partition contains our largest memory nodes; only jobs that cannot be satisfied by general should run here. The gpu_devel partition is a single node meant for testing or compiling GPU accelerated code, and the gpu partition is where normal GPU jobs should run. The scavenge partition allows you to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Slurm documentation](/clusters-at-yale/job-scheduling/scavenge).

All the node types listed are described in more detail in the [hardware](#hardware) table.

| Partition   | User Limits                 | Walltime default/max | Node type (number)                  |
|-------------|-----------------------------|----------------------|-------------------------------------|
| interactive | 20 CPUs, 256 G RAM          | 1d/2d                | m620 (34), nx360h (94)              |
| general*    | 200 CPUs, 1280 G RAM        | 1d/30d               | m620 (34), nx360h (94)              |
| scavenge    | 800 CPUs, 5120 G RAM        | 1d/7d                | all                                 |
| gpu_devel   | 1 job                       | 10min/2hr            | GPX XT4 1080Ti (1)                  |
| gpu         | 32 CPUs, 256 G RAM          | 1d/2d                | nx360h K80 (2), GPX XT4 1080Ti (10) |
| bigmem      | 2 jobs, 32 CPUs, 1532 G RAM | 1d/7d                | m915 (9), 3850X6 (2)                |

*default

### Private Partitions

Private partitions contain nodes acquired by specific research groups. Full access to these partitions is granted at the discretion of the owner. Contact us if your group would like to purchase nodes.

| Partition       | Walltime default/max | Node type (number)                                   |
|-----------------|----------------------|------------------------------------------------------|
| pi_breaker      | 1d/14d               | nx360b (24)                                          |

## Storage

Grace has access to a number of GPFS filesystems. `/gpfs/loomis` is Grace's primary filesystem where home, project, and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/cluster-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage details only update once daily.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition  | Root Directory            | Storage     | File Count | Backups |
|-----------|---------------------------|-------------|------------|---------|
| home      | `/gpfs/loomis/home.grace` | 125G/user   | 500,000    | Yes     |
| project   | `/gpfs/loomis/project`    | 4T/group    | 5,000,000  | No      |
| scratch60 | `/gpfs/loomis/scratch60`  | 10T/group   | 5,000,000  | No      |
