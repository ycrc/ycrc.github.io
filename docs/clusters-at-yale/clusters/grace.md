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

| Count | Node Type              | CPU                 | CPU Cores | RAM   |         GPU        | Features                                     |
|-------|------------------------|---------------------|-----------|-------|--------------------|----------------------------------------------|
| 80    | IBM nx360i             | 2x E5-2660 v2       | 20        | 121G  |                    | ivybridge, v2, sse4_2, avx, E5-2660_v2       |
| 136   | Lenovo nx360h          | 2x E5-2660 v3       | 20        | 121G  |                    | haswell, v3, sse4_2, avx, avx2, E5-2660_v3   |
| 20    | Lenovo nx360h          | 2x E5-2660 v3       | 20        | 247G  |                    | haswell, v3, sse4_2, avx, avx2, E5-2660_v3   |
| 6     | Lenovo nx360h w/ GPUs  | 2x E5-2660 v3       | 20        | 121G  | 2x k80 (2GPUs/k80) | haswell, v3, sse4_2, avx, avx2, E5-2660_v3   |
| 8     | Lenovo nx360h w/ GPUs  | 2x E5-2660 v3       | 20        | 247G  | 1x k80 (2GPUs/k80) | haswell, v3, sse4_2, avx, avx2, E5-2660_v3   |
| 161   | Lenovo nx360b          | 2x E5-2660 v4       | 28        | 247G  |                    | broadwell, v4, sse4_2, avx, avx2, E5-2660_v4 |
| 7     | Lenovo nx360b          | 2x E5-2660 v4       | 28        | 247   | 1x p100            | broadwell, v4, sse4_2, avx, avx2, E5-2660_v4 |
| 53    | Lenovo sd530           | 2x Gold 6136        | 24        | 90G   |                    | skylake, sse4_2, avx, avx2, avx512, 6136     |
| 1     | Lenovo sd530           | 2x Gold 6136        | 24        | 176G  |                    | skylake, sse4_2, avx, avx2, avx512, 6126     |
| 1     | Lenovo sd530 w/ GPUs   | 2x Gold 6136        | 24        | 90G   | 2x v100            | skylake, sse4_2, avx, avx2, avx512, 6136     |
| 1     | Lenovo sd530           | 2x Gold 6136        | 24        | 751G  |                    | skylake, sse4_2, avx, avx2, avx512, 6136     |
| 1     | IBM x3850i             | 4x E7-4820 v2       | 32        | 1003G |                    | ivybridge, v2, sse4_2, avx, E7-4820_v2       |
| 1     | Lenovo x3850h          | 4x E7-4809 v2       | 32        | 2011G |                    | haswell, v3, sse4_2, avx, avx2, E7-4809_v3   |
| 4     | Lenovo x3850b          | 4x E7-4820 v4       | 40        | 1507G |                    | broadwell, v4, sse4_2, avx, avx2, E7-4820_v4 |
| 1     | Thinkmate GPX XT4      | 2x E5-2637 v4       | 8         | 121G  | 4x 1080ti          | broadwell, v4, sse4_2, avx, avx2, E5-2637_v4 |
| 9     | Penguin XE2118GT       | 2x Gold 6136        | 24        | 183G  | 4x p100            | skylake, sse4_2, avx, avx2, avx512, 6136     |

## Slurm Partitions

Nodes on the clusters are organized into partitions, to which you submit your jobs with [Slurm](/clusters-at-yale/job-scheduling/slurm).

### Public Partitions

The day partition is where most batch jobs should run, and is the default if you don't specify a partition. The week partition is smaller, but allows for longer jobs. The interactive partition should only be used for testing or compiling software. The bigmem partition contains our largest memory node; only jobs that cannot be satisfied by general should run here. The gpu_devel partition is a single node meant for testing or compiling GPU accelerated code, and the gpu partition is where normal GPU jobs should run. The mpi partition is a permission-only place to run large parallel jobs. The scavenge partition allows you to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Slurm documentation](/clusters-at-yale/job-scheduling/scavenge).

All the node types listed are described in more detail in the [hardware](#hardware) table.

| Partition   | Group Limits                | User Limits                 | Walltime default/max | Node type (number)                              |
|-------------|-----------------------------|-----------------------------|----------------------|-------------------------------------------------|
| day*        | 900 CPUs                    | 640 CPUs                    | 1h/1d                | nx360i (49), nx360h (32), nx360b (72)           |
| week        | 250 CPUs                    | 100 CPUs                    | 1h/7d                | nx360h (48), nx360b (7)                         |
| interactive |                             | 1 job, 4 CPUs, 32 G RAM     | 1h/6h                | nx360i (2)                                      |
| bigmem      |                             | 40 CPUs, 1500 G RAM         | 1h/1d                | x3850b (1)                                      |
| gpu_devel   |                             | 1 job, 10 CPUs, 60 G RAM    | 10min/4hr            | nx360h k80 (1)                                  |
| gpu         | 32 CPUs, 256 G RAM          | 6 nodes                     | 1h/1d                | nx360b p100 (6), nx360h k80 (3), sd530 v100 (1) |
| mpi         | 900 CPUs                    | 640 CPUs                    | 1h/7d                | sd530 (35)                                      |
| scavenge    |                             | 6400 CPUs                   | 1h/1d                | all                                             |

*default

### Private Partitions

Private partitions contain nodes acquired by specific research groups. Full access to these partitions is granted at the discretion of the owner. Contact us if your group would like to purchase nodes.

| Partition           | Walltime default/max | Node type (number)                         |
|---------------------|----------------------|--------------------------------------------|
| pi_altonji          | 1d/28d               | nx360h (2)                                 |
| pi_anticevic        | 1d/100d              | nx360h (16), nx360b (20)                   |
| pi_anticevic_bigmem | 1d/100d              | x3850h (1)                                 |
| pi_anticevic_fs     | 1d/100d              | nx360h (3)                                 |
| pi_anticevic_gpu    | 1d/100d              | nx360h k80 (8)                             |
| pi_balou            | 1d/28d               | nx360b (30)                                |
| pi_berry            | 1d/28d               | nx360h (1)                                 |
| pi_cowles           | 1d/28d               | nx360h (14)                                |
| pi_cowles_nopreempt | 1d/28d               | nx360h (10)                                |
| pi_gelernter        | 1d/28d               | nx360b (1)                                 |
| pi_gerstein         | 1d/28d               | x3850i (1), nx360h (32)                    |
| pi_glahn            | 1d/100d              | nx360h (1)                                 |
| pi_hammes_schiffer  | 1d/28d               | sd530 (17), GPX XT4 1080ti (1)             |
| pi_holland          | 1d/28d               | nx360h (2)                                 |
| pi_jetz             | 1d/28d               | nx360b (2)                                 |
| pi_kaminski         | 1d/28d               | nx360h (8)                                 |
| pi_mak              | 1d/28d               | nx360h (8)                                 |
| pi_manohar          | 1d/180d              | nx360b (8), x3850b (2),  nx360b p100 (1)   |
| pi_ohern            | 1d/28d               | nx360i (16), nx360b (3), XE2118GT p100 (9) |
| pi_owen_miller      | 1d/28d               | nx360b (5)                                 |
| pi_poland           | 1d/28d               | nx360b (10)                                |
| pi_seto             | 1d/28d               | nx360b (1), sd530(3)                       |
| pi_som              | 1d/28d               | nx360i (4)                                 |
| pi_tsmith           | 1d/28d               | nx360h (1)                                 |

## Storage

Grace has access to a number of GPFS filesystems. `/gpfs/loomis` is Grace's primary filesystem where home, project, and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/cluster-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage details only update once daily.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition  | Root Directory            | Storage     | File Count | Backups |
|-----------|---------------------------|-------------|------------|---------|
| home      | `/gpfs/loomis/home.grace` | 100G/user   | 500,000    | Yes     |
| project   | `/gpfs/loomis/project`    | 1T/group    | 5,000,000  | No      |
| scratch60 | `/gpfs/loomis/scratch60`  | 10T/group   | 5,000,000  | No      |
