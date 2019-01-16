# Farnam

![Louise](/img/Louise_Whitman_Farnam.jpg){: .cluster-portrait}

The Farnam Cluster is named for [Louise Whitman Farnam](http://archives.yalealumnimagazine.com/issues/2006_09/old_yale.html), the first woman to graduate from the Yale School of Medicine, class of 1916. It consists of a variety of compute nodes networked over ethernet and mounts several shared filesystems.

- - -

## Hardware

Farnam is made up of several kinds of compute nodes. The "Features" column lists the features that can be used to specifically request node types using the `--constraints` flag (see our [Slurm documentation](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) for more details). The RAM listed below is the maximum amount of memory available for jobs.

!!! Warning
    Care should be taken if when scheduling your job if you are running programs/libraries optimized for specific hardware.
    See the [guide on how to compile software](/clusters-at-yale/applications/compile) for specific guidance.

### Compute Node Configurations

| Node Type                           | Processors                        | Features                                     | Cores | RAM     |
|-------------------------------------|-----------------------------------|----------------------------------------------|-------|---------|
| Dell PowerEdge M620                 | (2) E5-2670                       | sandybridge, sse4_2, avx, E5-2670            | 16    | 121G  |
| Dell PowerEdge M915                 | (4) AMD Opteron 6276              | bulldozer, sse4_2, avx, opteron-6276         | 32    | 507G  |
| Lenovo nx360h                       | (2) E5-2660 v3                    | haswell, v3, sse4_2, avx, avx2, E5-2660_v3   | 20    | 121G  |
| Lenovo nx360h w/GPUs                | (2) E5-2660 v3,(2) Nvidia K80     | haswell, v3, sse4_2, avx, avx2, E5-2660_v3   | 20    | 121G  |
| Lenovo nx360b                       | (2) E5-2680 v4                    | broadwell, v4, sse4_2, avx, avx2, E5-2680_v4 | 28    | 246G  |
| Lenovo nx360b w/GPUs                | (2) E5-2660 v4,(2) Nvidia P100    | broadwell, v4, sse4_2, avx, avx2, E5-2660_v4 | 28    | 246G  |
| Thinkmate GPX XT4 (gputest)         | (2) E5-2623 v4,(4) Nvidia 1080Ti  | broadwell, v4, sse4_2, avx, avx2, E5-2623_v4 | 8     | 58G   |
| Thinkmate GPX XT4                   | (2) E5-2637 v4,(4) Nvidia 1080Ti  | broadwell, v4, sse4_2, avx, avx2, E5-2637_v4 | 8     | 121G  |
| Thinkmate GPX XT4 (pi_gerstein_gpu) | (2) E5-2637 v4,(4) Nvidia TITAN V | broadwell, v4, sse4_2, avx, avx2, E5-2637_v4 | 8     | 121G  |
| Lenovo 3850X6                       | (4) E7-4809 v3                    | haswell, v3, sse4_2, avx, avx2, E7-4809_v3   | 32    | 1507G |
| Lenovo 3850X6 (pi_gerstein)         | (4) E7-4820 v4                    | broadwell, v3, sse4_2, avx, avx2, E7-4820_v4 | 40    | 1507G |

## Partitions

Nodes on the clusters are organized into partitions. The column names in the partitions tables refer to the node types in the nodes table above.

### Public Partitions
The partitions available for general use are `general` (the default), `interactive` (for interactive jobs), `bigmem` (for single-node large memory jobs), `gpu` & `gpu_devel` (for GPU work), and `scavenge`.


| Partition       | m620    | m915    | nx360h  | nx360b  | GPX XT4 | 3850X6 | Limits                      | Walltime default/max |
|-----------------|---------|---------|---------|---------|---------|--------|-----------------------------|----------------------|
| interactive     | 34      |         | 94      |         |         |        | 20 CPUs, 256 G RAM          | 1d/2d                |
| general         | 34      |         | 94      |         |         |        | 100 CPUs, 640 G RAM         | 1d/30d               |
| scavenge*       | all     | all     | all     | all     | all     | all    | 400 CPUs, 2560 G RAM        | 1d/7d                |
| gpu_devel       |         |         |         |         | 1       |        | 1 job                       | 10min/2hr            |
| gpu             |         |         | 2       |         | 10      |        |                             | 1d/2d                |
| bigmem          |         | 9       |         |         |         | 2      | 2 jobs, 32 CPUs, 1532 G RAM | 1d/7d                |

### PI Partitions

PI purchased hardware are separated into partitions prefixed with `pi_`. Full access to these partitions is granted at the discretion of the owner.

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

Farnam has access to a number of GPFS filesystems. `/gpfs/ysm` is Farnam's primary filesystem where home, project and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/cluster-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage details only update once daily.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition | Root Directory        | Storage     | File Count | Backups |
|----------|-----------------------|-------------|------------|---------|
|home      | `/gpfs/ysm/home`      | 125G/user | 500,000    | Yes     |
|project   | `/gpfs/ysm/project`   | 4T/group  | 5,000,000  | No      |
|scratch60 | `/gpfs/ysm/scratch60` | 10T/group | 5,000,000  | No      |
