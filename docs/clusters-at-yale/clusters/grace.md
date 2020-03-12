# Grace

![Grace](/img/Grace-Hopper.jpg){: .cluster-portrait}

The Grace cluster is is named for the computer scientist and United States Navy Rear Admiral [Grace Murray Hopper](https://en.wikipedia.org/wiki/Grace_Hopper), who received her Ph.D. in Mathematics from Yale in 1934.

Grace is a shared-use resource for the [Faculty of Arts and Sciences](https://fas.yale.edu) (FAS). It consists of a variety of compute nodes networked over low-latency InfiniBand and mounts several shared filesystems.

- - -

## Hardware

Grace is made up of several kinds of compute nodes. The Features column below lists the features that can be used to request different node types using the `--constraints` flag (see our [Slurm documentation](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) for more details). The RAM listed below is the amount of memory available for jobs. GPUs listed can be requested with the `--gres` flag, e.g. `--gres=gpu:p100:1` would request one Tesla P100 GPU per node. See the [Request Compute Resources page](clusters-at-yale/job-scheduling/resource-requests/#request-gpus) for more info.

!!! Warning
    Care should be taken when scheduling your job if you are running programs/libraries optimized for specific hardware.
    You can narrow which nodes can run your job by requesting the features from the Node Configurations table as constraints (slurm `--constraint` flag) to your job.
    See the [Request Compute Resources page](/clusters-at-yale/job-scheduling/resource-requests/#features-and-constraints) and the [Build Software page](/clusters-at-yale/applications/compile) for further guidance.

### Compute Node Configurations

|   Count | CPU           |   Cores | RAM   | GPU                           | Features                                     |
|--------:|:--------------|--------:|:------|:------------------------------|:---------------------------------------------|
|      80 | 2x E5-2660_v2 |      20 | 121G  |                               | ivybridge,E5-2660_v2,nogpu,standard,oldest   |
|       1 | 2x E7-4820_v2 |      32 | 1003G |                               | ivybridge,E7-4820_v2,nogpu                   |
|     136 | 2x E5-2660_v3 |      20 | 121G  |                               | haswell,avx2,E5-2660_v3,nogpu,standard       |
|      20 | 2x E5-2660_v3 |      20 | 247G  |                               | haswell,avx2,E5-2660_v3,nogpu,standard       |
|       8 | 2x E5-2660_v3 |      20 | 247G  | 2x k80                        | haswell,avx2,E5-2660_v3,doubleprecision      |
|       6 | 2x E5-2660_v3 |      20 | 121G  | 4x k80                        | haswell,avx2,E5-2660_v3,doubleprecision      |
|       1 | 2x E7-4809_v3 |      32 | 2011G |                               | haswell,avx2,E7-4809_v3,nogpu                |
|     161 | 2x E5-2660_v4 |      28 | 247G  |                               | broadwell,avx2,E5-2660_v4,nogpu,standard     |
|       7 | 2x E5-2660_v4 |      28 | 247G  | 1x p100                       | broadwell,avx2,E5-2660_v4,doubleprecision    |
|       4 | 2x E7-4820_v4 |      40 | 1507G |                               | broadwell,avx2,E7-4820_v4,nogpu              |
|       1 | 2x E5-2637_v4 |       8 | 121G  | 4x gtx1080ti                  | broadwell,avx2,E5-2637_v4,singleprecision    |
|      92 | 2x 6136       |      24 | 90G   |                               | hdr,skylake,avx2,avx512,6136,nogpu,standard  |
|      53 | 2x 6136       |      24 | 90G   |                               | edr,skylake,avx2,avx512,6136,nogpu,standard  |
|       9 | 2x 6136       |      24 | 183G  | 4x p100                       | skylake,avx2,avx512,6136,doubleprecision     |
|       3 | 2x 6142       |      32 | 183G  |                               | skylake,avx2,avx512,6142,nogpu,standard      |
|       2 | 2x 5122       |       8 | 183G  | 4x rtx2080                    | skylake,avx2,avx512,5122,singleprecision     |
|       1 | 2x 6126       |      24 | 176G  |                               | skylake,avx2,avx512,6126,nogpu,standard      |
|       1 | 2x 6136       |      24 | 90G   | 2x v100                       | skylake,avx2,avx512,6136,doubleprecision     |
|       1 | 2x 6136       |      24 | 751G  |                               | skylake,avx2,avx512,6136,nogpu               |
|     131 | 2x 6240       |      36 | 183G  |                               | cascadelake,avx2,avx512,6240,nogpu,standard  |
|      20 | 2x 8260       |      96 | 183G  |                               | cascadelake,avx2,avx512,8260,nogpu           |
|       5 | 2x 6240       |      36 | 372G  | 4x v100                       | cascadelake,avx2,avx512,6240,doubleprecision |
|       5 | 2x 6240       |      36 | 183G  | 4x rtx2080ti                  | cascadelake,avx2,avx512,6240,singleprecision |
|       2 | 2x 6240       |      36 | 1506G |                               | cascadelake,avx2,avx512,6240,nogpu           |
|       1 | 2x 6254       |      36 | 1506G | 4x rtx4000 2x rtx8000 2x v100 | cascadelake,avx2,avx512,6254                 |

## Slurm Partitions

Nodes on the clusters are organized into partitions, to which you submit your jobs with [Slurm](/clusters-at-yale/job-scheduling). The default resource requests for all jobs is 1 core and 5GB of memory, unless otherwise specified.

### Public Partitions

The day partition is where most batch jobs should run, and is the default if you don't specify a partition. The week partition is smaller, but allows for longer jobs. The interactive partition should only be used for testing or compiling software. The bigmem partition contains our largest memory node; only jobs that cannot be satisfied by general should run here. The gpu_devel partition is a single node meant for testing or compiling GPU accelerated code, and the gpu partition is where normal GPU jobs should run. The mpi partition is reserved for tightly-coupled parallel and access is by special request only. The scavenge partition allows you to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

The limits listed below are for all running jobs combined. Per-node limits are bound by the node types, as described in the [hardware](#hardware) table.

| Partition    | Group Limits   | User Limits          | Walltime (Default/Max)   | Node Type (count)                                                                                   |
|:-------------|:---------------|:---------------------|:-------------------------|:----------------------------------------------------------------------------------------------------|
| interactive  |                | CPUs: 4, RAM: 32G    | 1h/6h                    | E5-2660_v2 (2), 6126 (1)                                                                            |
| day*         | CPUs: 900      | CPUs: 640            | 1h/1d                    | E5-2660_v2 (38), E5-2660_v3 (44), E5-2660_v4 (72), 6240 (59)                                        |
| week         | CPUs: 250      | CPUs: 100            | 1h/7d                    | E5-2660_v3 (36), E5-2660_v4 (7)                                                                     |
| bigmem       |                | CPUs: 40, RAM: 1500G | 1h/1d                    | E7-4820_v4 1507G (2), 6240 1506G (2)                                                                |
| gpu          |                | GPUs: 24             | 1h/1d                    | E5-2660_v3 k80:4 (5), E5-2660_v4 p100:1 (6), 6136 v100:2 (1), 6240 v100:4 (5), 6240 rtx2080ti:4 (5) |
| gpu_devel    |                | CPUs: 10             | 1h/4h                    | E5-2660_v3 k80:4 (1)                                                                                |
| mpi**        | Nodes: 48      | Nodes: 32            | 1h/1d                    | 6136 (113)                                                                                          |
| scavenge     |                | CPUs: 10000          | 1h/1d                    | all                                                                                                 |
| scavenge_gpu |                | GPUs: 30             | 1h/1d                    | all with GPUs (see Nodes table)                                                                     |

\* default  
** The mpi partition is reserved for tightly-coupled parallel programs that make efficient use of multiple nodes. See our [MPI documentation](/clusters-at-yale/job-scheduling/mpi) if your workload fits this description. The default memory request on the mpi partition in 3.75GB per core.

### Private Partitions

Private partitions contain nodes acquired by specific research groups. Full access to these partitions is granted at the discretion of the owner. Contact us if your group would like to purchase nodes.

| Partition           | Walltime Default/Max   | Node Type (count)                                                        |
|:--------------------|:-----------------------|:-------------------------------------------------------------------------|
| pi_altonji          | 1h/28d                 | E5-2660_v3 (2)                                                           |
| pi_anticevic        | 1h/100d                | E5-2660_v3 (16), E5-2660_v4 (20)                                         |
| pi_anticevic_bigmem | 1h/100d                | E7-4809_v3 2011G (1)                                                     |
| pi_anticevic_gpu    | 1h/100d                | E5-2660_v3 k80:2 (8)                                                     |
| pi_anticevic_z      | 1h/100d                | E5-2660_v3 (3)                                                           |
| pi_balou            | 1h/28d                 | E5-2660_v4 (30), 6240 (9)                                                |
| pi_berry            | 1h/28d                 | E5-2660_v3 (1), 6240 (1)                                                 |
| pi_cowles           | 1h/28d                 | E5-2660_v3 (14)                                                          |
| pi_cowles_nopreempt | 1h/28d                 | E5-2660_v3 (10)                                                          |
| pi_econ_io          | 1h/28d                 | 6240 (6)                                                                 |
| pi_econ_lp          | 1h/28d                 | 6240 (5)                                                                 |
| pi_esi              | 1h/28d                 | 6240 (36)                                                                |
| pi_fedorov          | 1h/28d                 | 6136 (12)                                                                |
| pi_gelernter        | 1h/28d                 | E5-2660_v4 (1), 6240 (1)                                                 |
| pi_gerstein         | 1h/28d                 | E5-2660_v3 (32), E7-4820_v2 1003G (1)                                    |
| pi_glahn            | 1h/100d                | E5-2660_v3 (1)                                                           |
| pi_hammes_schiffer  | 1h/28d                 | E5-2637_v4 gtx1080ti:4 (1), 6136 751G (1), 6136 (16), 5122 rtx2080:4 (2) |
| pi_hodgson          | 1h/28d                 | 6240 (1)                                                                 |
| pi_holland          | 1h/28d                 | E5-2660_v3 (2)                                                           |
| pi_howard           | 1h/28d                 | 6240 (1)                                                                 |
| pi_jetz             | 1h/28d                 | E5-2660_v4 (2)                                                           |
| pi_kaminski         | 1h/28d                 | E5-2660_v3 (8)                                                           |
| pi_lederman         | 1h/28d                 | 6254 1506G rtx4000:4,rtx8000:2,v100:2 (1)                                |
| pi_levine           | 1h/28d                 | 8260 (20)                                                                |
| pi_lora             | 1h/28d                 | 6136 (4)                                                                 |
| pi_mak              | 1h/28d                 | E5-2660_v4 (3)                                                           |
| pi_manohar          | 1h/180d                | E5-2660_v4 (8), 6240 (4), E7-4820_v4 1507G (2), E5-2660_v4 p100:1 (1)    |
| pi_ohern            | 1h/28d                 | E5-2660_v4 (3), 6136 p100:4 (9), 6240 (2), E5-2660_v2 (16)               |
| pi_owen_miller      | 1h/28d                 | E5-2660_v4 (5)                                                           |
| pi_poland           | 1h/28d                 | E5-2660_v4 (10), 6240 (8)                                                |
| pi_polimanti        | 1h/28d                 | 6240 (1)                                                                 |
| pi_seto             | 1h/28d                 | 6142 (3)                                                                 |
| pi_tsmith           | 1h/28d                 | E5-2660_v3 (1)                                                           |

\* The default memory request on this partition is 3.75GB per core.  

## Storage

Grace has access to a number of GPFS filesystems. `/gpfs/loomis` is Grace's primary filesystem where home, project, and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/cluster-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage breakdown only update once daily.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition  | Root Directory            | Storage     | File Count | Backups |
|-----------|---------------------------|-------------|------------|---------|
| home      | `/gpfs/loomis/home.grace` | 100G/user   | 200,000    | Yes     |
| project   | `/gpfs/loomis/project`    | 1T/group    | 5,000,000  | No      |
| scratch60 | `/gpfs/loomis/scratch60`  | 20T/group   | 5,000,000  | No      |
