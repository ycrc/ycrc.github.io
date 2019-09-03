# Farnam

![Louise](/img/Louise-Whitman-Farnam.jpg){: .cluster-portrait}

The Farnam Cluster is named for [Louise Whitman Farnam](http://archives.yalealumnimagazine.com/issues/2006_09/old_yale.html), the first woman to graduate from the Yale School of Medicine, class of 1916.

Farnam is a shared-use resource for the [Yale School of Medicine](https://medicine.yale.edu) (YSM). It consists of a variety of compute nodes networked over ethernet and mounts several shared filesystems.

- - -

## Hardware

Farnam is made up of several kinds of compute nodes. The Features column below lists the features that can be used to request different node types using the `--constraints` flag (see our [Slurm documentation](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) for more details). The RAM listed below is the amount of memory available for jobs. GPUs listed can be requested with the `--gres` flag, e.g. `--gres=gpu:gtx1080ti:2` would request 2 GeForce GTX 1080Ti GPUs per node. See the [Request Compute Resources page](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) for more info.

!!! Warning
    Care should be taken if when scheduling your job if you are running programs/libraries optimized for specific hardware.
    See the [guide on how to compile software](/clusters-at-yale/applications/compile) for specific guidance.

### Compute Node Configurations

| Count | CPU           | CPU Cores | RAM   |         GPU        | vRAM/GPU | Features                                         |
|-------|---------------|-----------|-------|--------------------|----------|--------------------------------------------------|
|   117 | 2x E5-2660_v3 |        20 |  121G |                    |          | haswell,avx2,E5-2660_v3,nogpu,standard           |
|     5 | 2x E5-2660 v3 |        20 |  121G | 2x k80 (2GPUs/k80) |      12G | haswell, avx2, E5-2660_v3, doubleprecision       |
|     2 | 4x E7-4809_v3 |        32 | 1507G |                    |          | haswell, avx2, E7-4809_v3, nogpu                 |
|     1 | 2x E5-2623 v4 |         8 |   59G | 4x gtx1080ti       |      11G | broadwell, avx2, E5-2623_v4, singleprecision     |
|     1 | 2x E5-2637 v4 |         8 |  121G | 4x titanv          |      12G | broadwell, avx2, E5-2637_v4, doubleprecision     |
|    21 | 2x E5-2637 v4 |         8 |  121G | 4x gtx1080ti       |      11G | broadwell, avx2, E5-2637_v4, singleprecision     |
|     3 | 2x E5-2660 v4 |        28 |  247G | 2x p100            |      16G | broadwell, avx2, E5-2660_v4, doubleprecision     |
|    38 | 2x E5-2680_v4 |        28 |  247G |                    |          | broadwell, avx2, E5-2680_v4, nogpu, standard     |
|     1 | 4x E7-4820_v4 |        40 | 1507G |                    |          | broadwell, avx2, E7-4820_v4, nogpu               |
|     2 | 2x 5122       |         8 |  183G | 4x rtx2080         |       8G | skylake, avx2, avx512, 5122, singleprecision     |
|     1 | 2x 6132       |        28 |  751G |                    |          | skylake, avx2, avx512, 6132, nogpu               |
|     2 | 2x 6132       |        28 |  183G |                    |          | skylake, avx2, avx512, 6132, nogpu, standard     |
|     4 | 2x 6240       |        36 |  750G |                    |          | cascadelake, avx2, avx512, 6240, nogpu           |
|     4 | 2x 6240       |        36 |  372G |                    |          | cascadelake, avx2, avx512, 6240, nogpu           |
|    24 | 2x 6240       |        36 |  183G |                    |          | cascadelake, avx2, avx512, 6240, nogpu, standard |

## Slurm Partitions

Nodes on the clusters are organized into partitions, to which you submit your jobs with [Slurm](/clusters-at-yale/job-scheduling). The default resource requests for all jobs is 1 core and 5G of memory per core.

### Public Partitions

The general partition is where most batch jobs should run, and is the default if you don't specify a partition. The interactive partition is dedicated to jobs with which you need ongoing interaction. The bigmem partition contains our largest memory nodes--only jobs that cannot be satisfied by general should run here. The gpu_devel partition is a single node meant for testing or compiling GPU accelerated code, and the gpu partition is where normal GPU jobs should run. The scavenge partition allows you to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

The limits listed below are for all running jobs combined. Per-node limits are bound by the node types, as described in the [hardware](#hardware) table.

| Partition    | Group Limits         | User Limits                 | Walltime Default/Max | Node Type (count)                             |
|--------------|----------------------|-----------------------------|----------------------|-----------------------------------------------|
| general*     | 400 CPUs, 2560 G RAM | 200 CPUs, 1280 G RAM        | 1d/30d               | E5-2660_v3 (93), 6240 (19)                    |
| interactive  |                      | 20 CPUs, 256 G RAM          | 1d/2d                | E5-2660_v3 (93)                               |
| bigmem       |                      | 2 jobs, 32 CPUs, 1532 G RAM | 1d/7d                | E7-4809_v3 (2)                                |
| gpu_devel    |                      | 1 job                       | 10min/2hr            | E5-2623_v4 gtx1080ti (1)                      |
| gpu          |                      | 32 CPUs, 256 G RAM          | 1d/2d                | E5-2660_v3 k80 (2), E5-2637_v4 gtx1080ti (10) |
| scavenge     |                      | 800 CPUs, 5120 G RAM        | 1d/7d                | all                                           |
| scavenge_gpu |                      | 32 CPUs, 256 G RAM          | 1d/2d                | all nodes with GPUs (see Compute Node table)  |

\* default

### Private Partitions

Private partitions contain nodes acquired by specific research groups. Full access to these partitions is granted at the discretion of the owner. Contact us if your group would like to purchase nodes.

| Partition       | Walltime Default/Max   | Node Type (count)                                              |
|:----------------|:-----------------------|:---------------------------------------------------------------|
| pi_breaker      | 1d / 14d               | E5-2680_v4 (24)                                                |
| pi_cryoem       | 1d / 365d              | E5-2637_v4 gtx1080ti (10)                                      |
| pi_deng         | 1d / 14d               | E5-2680_v4 p100 (1)                                            |
| pi_dunn         | 1d / 14d               | 6240 (1)                                                       |
| pi_edwards      | 1d / 14d               | 6240 (1)                                                       |
| pi_gerstein     | 1d / 14d               | E7-4820_v4 (1), E5-2680_v4 (11), 6132 751G (1), 6132 (2)       |
| pi_gerstein_gpu | 1d / 14d               | E5-2660_v3 k80 (3), E5-2680_v4 p100 (2), E5-2637_v4 titanv (1) |
| pi_gruen        | 1d / 14d               | E5-2680_v4 (1)                                                 |
| pi_jadi         | 1d / 365d              | E5-2680_v4 (2)                                                 |
| pi_jetz         | 1d / 14d               | 6240 372G (4), 6240 750G (4)                                   |
| pi_kleinstein   | 1d / 14d               | 6240 (1), E5-2660_v3 (3)                                       |
| pi_krauthammer  | 1d / 14d               | E5-2660_v3 (1)                                                 |
| pi_ma           | 1d / 14d               | E5-2660_v3 (2)                                                 |
| pi_ohern        | 1d / 14d               | E5-2660_v3 (5)                                                 |
| pi_reinisch     | 1d / 14d               | 5122 gpu:4 (2)                                                 |
| pi_sigworth     | 1d / 14d               | E5-2660_v3 (1)                                                 |
| pi_sindelar     | 1d / 14d               | E5-2637_v4 gtx1080ti (1), E5-2660_v3 (1)                       |
| pi_townsend     | 1d / 14d               | E5-2660_v3 (5)                                                 |
| pi_zhao         | 1d / 14d               | 6240 (2)                                                       |

## Public Datasets

We host datasets of general interest in a loosely organized directory tree in `/gpfs/ysm/datasets`:

```
├── cryoem
├── db
│   ├── annovar
│   └── blast
└── genomes
    ├── 1000Genomes
    ├── 10xgenomics
    ├── Aedes_aegypti
    ├── Chelonoidis_nigra
    ├── Danio_rerio
    ├── hisat2
    ├── Homo_sapiens
    ├── Mus_musculus
    ├── PhiX
    └── Saccharomyces_cerevisiae
```

If you would like us to host a dataset or questions about what is currently available, please email hpc@yale.edu.

## Storage

Farnam has access to a number of GPFS filesystems. `/gpfs/ysm` is Farnam's primary filesystem where home, project, and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/cluster-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage breakdown only update once daily.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition  | Root Directory        | Storage     | File Count | Backups |
|-----------|-----------------------|-------------|------------|---------|
| home      | `/gpfs/ysm/home`      | 125G/user   | 500,000    | Yes     |
| project   | `/gpfs/ysm/project`   | 4T/group    | 5,000,000  | No      |
| scratch60 | `/gpfs/ysm/scratch60` | 10T/group   | 5,000,000  | No      |
