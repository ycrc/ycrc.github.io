# Ruddle

![Frank](/img/Frank-Ruddle.jpg){: .cluster-portrait}

Ruddle is named for [Frank Ruddle](http://www.nytimes.com/2013/03/20/science/francis-ruddle-who-led-transgenic-research-dies-at-83.html), a Yale geneticist who was a pioneer in genetic engineering and the study of developmental genetics.

Ruddle is intended for use only on projects related to the [Yale Center for Genome Analysis](http://ycga.yale.edu/); Please do not use this cluster for other projects. If you have any questions about this policy, please [contact us](mailto:hpc@yale.edu).

- - -

## Hardware

Ruddle is made up of several kinds of compute nodes. The Features column below lists the features that can be used to request different node types using the `--constraints` flag (see our [Slurm documentation](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) for more details). The RAM listed below is the amount of memory available for jobs.

!!! Warning
    Care should be taken when scheduling your job if you are running programs/libraries optimized for specific hardware.
    You can narrow which nodes can run your job by requesting the features from the Node Configurations table as constraints (slurm `--constraint` flag) to your job.
    See the [Request Compute Resources page](/clusters-at-yale/job-scheduling/resource-requests/#features-and-constraints) and the [Build Software page](/clusters-at-yale/applications/compile) for further guidance.

### Compute Node Configurations

| Count | CPU                 | CPU Cores | RAM   | Features                          |
|-------|---------------------|-----------|-------|-----------------------------------|
| 155   | 2x E5-2660 v3       | 20        | 121G  | haswell, avx2, E5-2660_v3, oldest |
| 2     | 4x E7-4809 v3       | 32        | 1507G | haswell, avx2, E7-4809_v3         |

## Slurm Partitions

Nodes on the clusters are organized into partitions, to which you submit your jobs with [Slurm](/clusters-at-yale/job-scheduling). The default resource requests for all jobs is 1 core and 5GiB of memory per core. The general partition is where most batch jobs should run, and is the default if you don't specify a partition. The interactive partition is dedicated to jobs with which you need ongoing interaction. The bigmem partition contains our largest memory nodes; only jobs that cannot be satisfied by general should run here. The scavenge partition allows you to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

The limits listed below are for all running jobs combined. Per-node limits are bound by the node types, as described in the [hardware](#hardware) table.

| Partition   | Group Limits          | User Limits          | Walltime Default/Max | Node Type (count)                       |
|-------------|-----------------------|----------------------|----------------------|-----------------------------------------|
| general*    | 400 CPUs, 2000 G RAM  | 300 CPUs, 1800 G RAM | 7d/30d               | E5-2660_v3 (155)                        |
| interactive |                       | 20 CPUs, 256 G RAM   | 1d/2d                | E5-2660_v3 (155)                        |
| bigmem      |                       | 32 CPUs, 1507 G RAM  | 1d/7d                | E7-4809_v3 1507G (2)                    |
| scavenge    |                       | 800 CPUs, 5120 G RAM | 1d/7d                | all                                     |

\* default

## YCGA Data Retention Policy

Illumina sequence data is initially written to YCGA's main storage system, which is located in the main HPC datacenter at Yale's West Campus.   Data stored there is protected against loss by software RAID.  Raw basecall data (bcl files) is immediately transformed into DNA sequences (fastq files).

- 45 days after sequencing, the raw bcl files are deleted.
- 60 days after sequencing, the fastq files are written to a tape archive.  Two tape libraries store identical copies of the data, located in two datacenters in separate buildings on West Campus.
- 365 days after sequencing, all data is deleted from main storage.  Users continue to have access to the data via the tape archive.  Data is retained on the tape archive indefinitely.  [Instructions for retrieving archived data](/clusters-at-yale/data/archived-sequencing).

All compression of sequence data is lossless.  Gzip is used for data stored on the main storage, and quip is used for data stored on the tape archive.
Disaster recovery is provided by the data stored on the tape library.

## Access Sequencing Data

To avoid duplication of data and to save space that counts against your quotas, we suggest that you make soft links to your sequencing data rather than copying them.

Normally, YCGA will send you an email informing you that your data is ready, and will include a url that looks like:
http://fcb.ycga.yale.edu:3010/_randomstring_/sample_dir_001

You can use that link to download your data in a browser, but if you plan to process the data on Ruddle, it is better to make a soft link to the data, rather than copying it.  You can use the ycgaFastq tool to do that:

```bash
$ /home/bioinfo/software/knightlab/bin_Mar2018/ycgaFastq  fcb.ycga.yale.edu:3010/randomstring/sample_dir_001
```

If you would like to know the true location of the data on Ruddle, do this:
``` bash
$ cd /ycga-gpfs/project/fas/lsprog/tools/external/data/randomstring/sample_dir_001
$ ls -l
```

!!! tip
    Original sequence data are archived pursuant to the YCGA retention policy. For long-running projects we recommend you keep a personal backup of your sequence files. If you need to retrieve archived sequencing data, please see our [guide on how to do so](/clusters-at-yale/data/archived-sequencing).

If you have a very old link from YCGA that doesn't use the random string, you can find the location by decoding the url as shown below:

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

Ruddle's filesystem, `/gpfs/ycga`, is  where home, project, and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/cluster-storage) documentation. Ruddle's legacy filesystem, `/ycga-ba`, was retired. See [here](/clusters-at-yale/clusters/ycga-ba) for details.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage breakdown only update once daily..

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition  | Root Directory         | Storage     | File Count | Backups |
|-----------|------------------------|-------------|------------|---------|
| home      | `/gpfs/ycga/home`      | 125G/user   | 500,000    | Yes     |
| project   | `/gpfs/ycga/project`   | 4T/group    | 5,000,000  | No      |
| scratch60 | `/gpfs/ycga/scratch60` | 10T/group   | 5,000,000  | No      |
