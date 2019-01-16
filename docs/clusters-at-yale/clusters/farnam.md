# Farnam

![Louise](/img/Louise_Whitman_Farnam.jpg){: .cluster-portrait}

The Farnam Cluster is named for [Louise Whitman Farnam](http://archives.yalealumnimagazine.com/issues/2006_09/old_yale.html), the first woman to graduate from the Yale School of Medicine, class of 1916. It consists of a variety of compute nodes networked over ethernet and mounts several shared filesystems.

- - -

## Available Hardware

Farnam is made up of several kinds of compute nodes. We have specified Slurm features for each node type. You can specify features as constraints when submitting jobs to run on the desired node(s). The RAM listed below is the amount available for jobs. The node types from the configurations table below are used as columns for the [partitions](#partitions) tables.

!!! Warning
    Care should be taken if when scheduling your job if you are running programs/libraries optimized for specific hardware.
    See the [guide on how to compile software](/clusters-at-yale/applications/compile) for specific guidance.

### Compute Node Configurations

| Node Type                           | Processors                        | Features                                     | Cores | RAM     |
|-------------------------------------|-----------------------------------|----------------------------------------------|-------|---------|
| Dell PowerEdge M620                 | (2) E5-2670                       | sandybridge, sse4_2, avx, E5-2670            | 16    | 121GiB  |
| Dell PowerEdge M915                 | (4) AMD Opteron 6276              | bulldozer, sse4_2, avx, opteron-6276         | 32    | 507GiB  |
| Lenovo nx360h                       | (2) E5-2660 v3                    | haswell, v3, sse4_2, avx, avx2, E5-2660_v3   | 20    | 121GiB  |
| Lenovo nx360h w/GPUs                | (2) E5-2660 v3,(2) Nvidia K80     | haswell, v3, sse4_2, avx, avx2, E5-2660_v3   | 20    | 121GiB  |
| Lenovo nx360b                       | (2) E5-2680 v4                    | broadwell, v4, sse4_2, avx, avx2, E5-2680_v4 | 28    | 246GiB  |
| Lenovo nx360b w/GPUs                | (2) E5-2660 v4,(2) Nvidia P100    | broadwell, v4, sse4_2, avx, avx2, E5-2660_v4 | 28    | 246GiB  |
| Thinkmate GPX XT4 (gputest)         | (2) E5-2623 v4,(4) Nvidia 1080Ti  | broadwell, v4, sse4_2, avx, avx2, E5-2623_v4 | 8     | 58GiB   |
| Thinkmate GPX XT4                   | (2) E5-2637 v4,(4) Nvidia 1080Ti  | broadwell, v4, sse4_2, avx, avx2, E5-2637_v4 | 8     | 121GiB  |
| Thinkmate GPX XT4 (pi_gerstein_gpu) | (2) E5-2637 v4,(4) Nvidia TITAN V | broadwell, v4, sse4_2, avx, avx2, E5-2637_v4 | 8     | 121GiB  |
| Lenovo 3850X6                       | (4) E7-4809 v3                    | haswell, v3, sse4_2, avx, avx2, E7-4809_v3   | 32    | 1507GiB |
| Lenovo 3850X6 (pi_gerstein)         | (4) E7-4820 v4                    | broadwell, v3, sse4_2, avx, avx2, E7-4820_v4 | 40    | 1507GiB |

## Partitions

Nodes on the clusters are grouped into partitions, to which you submit jobs. The partitions available for general use are `general` (the default), `interactive` (for interactive jobs), `bigmem` (for single-node large memory jobs), `gpu` & `gpu_devel` (for GPU work), and `scavenge`. PI purchased hardware are separated into partitions prefixed with `pi_`. Full access to these partitions is granted at the discretion of the owner.

### Public Partitions

| Partition       | m620    | m915    | nx360h  | nx360b  | GPX XT4 | 3850X6 | Limits                      | Walltime default/max |
|-----------------|---------|---------|---------|---------|---------|--------|-----------------------------|----------------------|
| interactive     | 34      |         | 94      |         |         |        | 20 CPUs,256 GB RAM          | 1d/2d                |
| general         | 34      |         | 94      |         |         |        | 100 CPUs,640 GB RAM         | 1d/30d               |
| scavenge*       | all     | all     | all     | all     | all     | all    | 400 CPUs,2560 GB RAM        | 1d/7d                |
| gpu_devel       |         |         |         |         | 1       |        | 1 job                       | 10min/2hr            |
| gpu             |         |         | 2       |         | 10      |        |                             | 1d/2d                |
| bigmem          |         | 9       |         |         |         | 2      | 2 jobs, 32 CPUs,1532 GB RAM | 1d/7d                |

### PI Partitions

| Partition       | m620    | m915    | nx360h  | nx360b  | GPX XT4 | 3850X6 | Walltime default/max |
|-----------------|---------|---------|---------|---------|---------|--------|----------------------|
| pi_breaker      |         |         |         | 24      |         |        | 1d/14d               |
| pi_cryoem       |         |         |         |         | 10      |        | 1d/∞                 |
| pi_deng         |         |         |         | 1       |         |        | 1d/14d               |
| pi_gerstein     |         | 2       |         | 11      |         | 1      | 1d/14d               |
| pi_gerstein_gpu |         |         | 3       | 2       | 1       |        | 1d/14d               |
| pi_gruen        |         |         |         | 1       |         |        | 1d/14d               |
| pi_jadi         |         |         |         | 2       |         |        | 1d/14d               |
| pi_kleinstein   |         | 1       | 3       |         |         |        | 1d/14d               |
| pi_krauthammer  |         |         | 1       |         |         |        | 1d/14d               |
| pi_ma           |         |         | 2       |         |         |        | 1d/14d               |
| pi_ohern        | 6       |         | 3       |         |         |        | 1d/14d               |
| pi_sigworth     |         |         | 1       |         |         |        | 1d/14d               |
| pi_sindelar     | 4       | 1       | 1       |         |         |        | 1d/14d               |
| pi_strobel      |         | 1       |         |         |         |        | 1d/14d               |
| pi_townsend     |         |         | 5       |         |         |        | 1d/14d               |
| pi_zhao         | 17      | 1       |         |         |         |        | 1d/14d               |

## Public datasets

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

Farnam has 2.5 Petabytes of GPFS parallel file storage, split across the mounts `/gpfs/ysm` (where most data are) and `/gpfs/slayman` (PI storage). Farnam also mounts Grace storage at `/gpfs/loomis`. On all the YCRC clusters, we create symlinks that point to your personal project and scratch60 directories for your convenience. To get the true absolute path to a directory use `pwd -P`.

Running the `groupquota` command will give your current storage usage & limits. Note that the per-user usage details only update once daily.

### Default Quotas

| Partition             | Storage     | File Count |
|-----------------------|-------------|------------|
| `/gpfs/ysm/home`      | 125GiB/user | 500,000    |
| `/gpfs/ysm/project`   | 4TiB/group  | 5,000,000  |
| `/gpfs/ysm/scratch60` | 10TiB/group | 5,000,000  |

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.