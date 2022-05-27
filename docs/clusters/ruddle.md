# Ruddle

![Frank](/img/Frank-Ruddle.jpg){: .cluster-portrait}

Ruddle is intended for use only on projects related to the [Yale Center for Genome Analysis](http://ycga.yale.edu/); Please do not use this cluster for other projects. If you have any questions about this policy, please [contact us](/#get-help).

Ruddle is named for [Frank Ruddle](http://www.nytimes.com/2013/03/20/science/francis-ruddle-who-led-transgenic-research-dies-at-83.html), a Yale geneticist who was a pioneer in genetic engineering and the study of developmental genetics.


- - -
## Access the Cluster

Once you have [an account](https://research.computing.yale.edu/support/hpc/account-request), the cluster can be accessed [via ssh](/clusters-at-yale/access) or through the [Open OnDemand web portal](/clusters-at-yale/access/ood/).


## System Status and Monitoring

For system status messages and the schedule for upcoming maintenance, please see the [system status page](https://research.computing.yale.edu/support/hpc/system-status). For a current node-level view of job activity, see the [cluster monitor page (VPN only)](http://cluster.ycrc.yale.edu/ruddle/).

## Partitions and Hardware

Ruddle is made up of several kinds of compute nodes. We group them into (sometimes overlapping) [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes. By combining the `--partition` and [`--constraint`](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) Slurm options you can more finely control what nodes your jobs can run on.

--8<-- "snippets/submission_rate_limit.md"

### Public Partitions

See each tab below for more information about the available common use partitions.

--8<-- "snippets/ruddle_partitions.md"

## YCGA Data Retention Policy

Illumina sequence data is initially written to YCGA's main storage system, which is located in the main HPC datacenter at Yale's West Campus. Data stored there is protected against loss by software RAID.  Raw basecall data (bcl files) is immediately transformed into DNA sequences (fastq files).

- 45 days after sequencing, the raw bcl files are deleted.
- 60 days after sequencing, the fastq files are written to a tape archive.  Two tape libraries store identical copies of the data, located in two datacenters in separate buildings on West Campus.
- 365 days after sequencing, all data is deleted from main storage.  Users continue to have access to the data via the tape archive.  Data is retained on the tape archive indefinitely.  [Instructions for retrieving archived data](/data/archived-sequencing).

All compression of sequence data is lossless.  Gzip is used for data stored on the main storage, and quip is used for data stored on the tape archive.
Disaster recovery is provided by the data stored on the tape library.

## Access Sequencing Data

To avoid duplication of data and to save space that counts against your quotas, we suggest that you make soft links to your sequencing data rather than copying them.

Normally, YCGA will send you an email informing you that your data is ready, and will include a url that looks like:
http://fcb.ycga.yale.edu:3010/_randomstring_/sample_dir_001

You can use that link to download your data in a browser, but if you plan to process the data on Ruddle, it is better to make a soft link to the data, rather than copying it.  You can use the ycgaFastq tool to do that:

```bash
$ /home/bioinfo/software/knightlab/bin/ycgaFastq  fcb.ycga.yale.edu:3010/randomstring/sample_dir_001
```

ycgaFastq can also be used to retrieve data that has been archived to tape.  The simplest way to do that is to provide
the sample submitter's netid and the flowcell (run) name:

```bash
$ ycgaFastq rdb9 AHFH66DSXX
```

If you have a path to the original location of the sequencing data, ycgaFastq can retrieve the data using that, even if the run as been archived and deleted:
```bash
$ ycgaFastq /ycga-gpfs/sequencers/illumina/sequencerD/runs/190607_A00124_0104_AHLF3MMSXX/Data/Intensities/BaseCalls/Unaligned-2/Project_Lz438
```

ycgaFastq can be used in a variety of other ways to retrieve data.  For more information, see the [documentation](http://campuspress.yale.edu/knightlab/ruddle/ycgafastq) or contact us.

If you would like to know the true location of the data on Ruddle, do this:
``` bash
$ readlink -f /ycga-gpfs/project/fas/lsprog/tools/external/data/randomstring/sample_dir_001
```

!!! tip
    Original sequence data are archived pursuant to the YCGA retention policy. For long-running projects we recommend you keep a personal backup of your sequence files. If you need to retrieve archived sequencing data, please see our [guide on how to do so](/data/archived-sequencing).

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

If you would like us to host a dataset or questions about what is currently available, please [contact us](/#get-help).

## Storage

Ruddle's filesystem, `/gpfs/ycga`, is  where home, project, and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/data/hpc-storage) documentation. Ruddle's old `ycga-ba` filesystem has been retired.

You can check your current storage usage & limits by running the `getquota` command. Your `~/project` and `~/scratch60` directories are shortcuts. Get a list of the absolute paths to your directories with the `mydirectories` command. If you want to share data in your Project or Scratch directory, see the [permissions](/data/permissions/) page.

For information on data recovery, see the [Backups and Snapshots](/data/backups) documentation.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition  | Root Directory        | Quota                                   | File Count | Backups | Snapshots |
|-----------|-----------------------|-----------------------------------------|------------|---------|-----------|
| home      | `/gpfs/ycga/home`     | 125GiB/user                             | 500,000    | Yes     | >=2 days  |
| project   | `/gpfs/ycga/project`  | 1TiB/group, increase to 4TiB on request | 5,000,000  | No      | >=2 days  |
| scratch60 | `/gpfs/ycga/scratch60`| 20TiB/group                             | 15,000,000 | No      | >=2 days  |


