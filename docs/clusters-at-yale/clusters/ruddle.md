# Ruddle

![Frank](/img/Frank-Ruddle.jpg){: .cluster-portrait}

Ruddle is named for [Frank Ruddle](http://www.nytimes.com/2013/03/20/science/francis-ruddle-who-led-transgenic-research-dies-at-83.html), a Yale geneticist who was a pioneer in genetic engineering and the study of developmental genetics.

Ruddle is intended for use only on projects related to the [Yale Center for Genome Analysis](http://ycga.yale.edu/); Please do not use this cluster for other projects. If you have any questions about this policy, please [contact us](mailto:hpc@yale.edu).

- - -

## Hardware

Ruddle is made up of several kinds of compute nodes. The Features column below lists the features that can be used to request different node types using the `--constraints` flag (see our [Slurm documentation](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) for more details). The RAM listed below is the amount of memory available for jobs.

!!! Warning
    Care should be taken if when scheduling your job if you are running programs/libraries optimized for specific hardware.
    See the [guide on how to compile software](/clusters-at-yale/applications/compile) for specific guidance.

### Compute Node Configurations

| Count | Node Type                     | CPU                 | CPU Cores | RAM   | Features                                   |
|-------|-------------------------------|---------------------|-----------|-------|--------------------------------------------|
| 12    | Dell PowerEdge M915           | 4x AMD Opteron 6276 | 32        | 507G  | bulldozer, sse4_2, avx, opteron-6276       |
| 155   | Lenovo nx360h                 | 2x E5-2660 v3       | 20        | 121G  | haswell, v3, sse4_2, avx, avx2, E5-2660_v3 |
| 2     | Lenovo 3850X6                 | 4x E7-4809 v3       | 32        | 1507G | haswell, v3, sse4_2, avx, avx2, E7-4809_v3 |

## Slurm Partitions

Nodes on the clusters are organized into partitions, to which you submit your jobs with [Slurm](/clusters-at-yale/job-scheduling). The general partition is where most batch jobs should run, and is the default if you don't specify a partition. The interactive partition is dedicated to jobs with which you need ongoing interaction. The bigmem partition contains our largest memory nodes; only jobs that cannot be satisfied by general should run here. The scavenge partition allows you to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

All the node types listed are described in more detail in the [hardware](#hardware) table.

| Partition   | User Limits          | Walltime default/max | Node type (number)    |
|-------------|----------------------|----------------------|-----------------------|
| general*    | 300 CPUs, 1800 G RAM | 7d/30d               | nx360h (155)          |
| interactive | 20 CPUs, 256 G RAM   | 1d/2d                | nx360h (155)          |
| bigmem      | 32 CPUs, 1507 G RAM  | 1d/7d                | m915 (12), 3850X6 (2) |
| scavenge    | 800 CPUs, 5120 G RAM | 1d/7d                | all                   |

\* default

## Access Sequencing Data

To avoid duplication of data and to save space that counts against your quotas, we suggest that you make soft links to your sequencing data rather than copying them:

``` bash
ln -s /path/to/sequece_data /path/to/your_link
```

!!! tip
    Original sequence data are archived pursuant to the YCGA retention policy. For long-running projects we recommend you keep a personal backup of your sequence files. If you need to retrieve archived sequencing data, please see our [guide on how to do so](/clusters-at-yale/data/archived-sequencing).

To find the location of the sequence files on the storage, look at the URL that you were sent from YCGA.

| `fullPath` Starts With    | Root Path on Ruddle                      |
|---------------------------|------------------------------------------|
| `gpfs_illumina/sequencer` | `/gpfs/ycga/illumina/sequencer`          |
| `ba_sequencers`           | `/ycga-ba/ba_sequencers`                 |
| `sequencers`              | `/gpfs/ycga/sequencers/panfs/sequencers` |

For example, if the sample link you received is:

```
http://sysg1.cs.yale.edu:2011/gen?fullPath=sequencers2/sequencerV/runs/131107_D00306_0096... etc
```

The path on the cluster to the data is:
```
/gpfs/ycga/sequencers/panfs/sequencers2/sequencerV/runs/131107_D00306_0096... etc
```

## Public Datasets

We host datasets of general interest in a loosely organized directory tree in `/gpfs/ycga/datasets`:

```
├── annovar
│   └── humandb
├── db
│   └── blast
├── genomes
│   ├── Aedes_aegypti
│   ├── Bos_taurus
│   ├── Chelonoidis_nigra
│   ├── Danio_rerio
│   ├── Gallus_gallus
│   ├── hisat2
│   ├── Homo_sapiens
│   ├── Macaca_mulatta
│   ├── Monodelphis_domestica
│   ├── Mus_musculus
│   ├── PhiX
│   └── tmp
└── hisat2
    └── mouse
```

If you would like us to host a dataset or questions about what is currently available, please email hpc@yale.edu.

## Storage

Ruddle has access to two filesystems. `/gpfs/ycga` is Ruddle's filesystem where home, project, and scratch60 directories are located. `/ycga-ba` stores legacy data. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/cluster-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage breakdown only update once daily..

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition  | Root Directory         | Storage     | File Count | Backups |
|-----------|------------------------|-------------|------------|---------|
| home      | `/gpfs/ycga/home`      | 125G/user   | 500,000    | Yes     |
| project   | `/gpfs/ycga/project`   | 4T/group    | 5,000,000  | No      |
| scratch60 | `/gpfs/ycga/scratch60` | 10T/group   | 5,000,000  | No      |
