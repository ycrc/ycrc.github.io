# McCleary

![Beatrix McCleary Hamburg](/img/beatrix-mccleary.jpg){: .cluster-portrait}

McCleary is a shared-use resource for the [Yale School of Medicine](https://medicine.yale.edu) (YSM), life science researchers elsewhere on campus and projects related to the [Yale Center for Genome Analysis](http://ycga.yale.edu/). It consists of a variety of compute nodes networked over ethernet and mounts several shared filesystems.

McCleary is named for [Beatrix McCleary Hamburg](https://www.nytimes.com/2018/04/19/obituaries/beatrix-hamburg-barrier-breaking-scholar-is-dead-at-94.html), who received her medical degree in 1948 and was the first female African American graduate of Yale School of Medicine. The McCleary HPC cluster is Yale's first direct-to-chip liquid cooled cluster, moving the YCRC and the Yale research computing community into a more environmentally friendly future.


- - -


!!! warning "NIH Controlled-Access Data and Repositories"
    Effective January 25, 2025, new or renewed Data Use Certifications for NIH Controlled-Access Data and Repositories must adhere to the [NIH Security Best Practices for Users of Controlled-Access Data](https://sharing.nih.gov/sites/default/files/flmngr/NIH-Security-BPs-for-Users-of-Controlled-Access-Data.pdf). While YCRC's new [Hopper cluster](/clusters/hopper) is in development, Yale has completed appropriate documentation for [McCleary](/clusters/mccleary) to be used as an approved location of NIH Controlled-Access Data and Repositories, with the certain conditions. See our [NIH Controlled-Access Data documentation](/data/nih-data) for more information and to request access.

## Access the Cluster

Once you have [an account](https://research.computing.yale.edu/support/hpc/account-request), the cluster can be accessed [via ssh](/clusters-at-yale/access) or through the [Open OnDemand web portal](/clusters-at-yale/access/ood/).

## System Status and Monitoring

For system status messages and the schedule for upcoming maintenance, please see the [system status page](https://research.computing.yale.edu/system-status). For a current node-level view of job activity, see the [cluster monitor page (VPN only)](http://cluster.ycrc.yale.edu/mccleary/).

## Installed Applications

A large number of software and applications are installed on our clusters.
These are made available to researchers via [software modules](/applications/modules/).

??? summary "Available Software Modules (click to expand)"
    ---8<-- "snippets/mccleary_modules.md"

## Partitions and Hardware

McCleary is made up of several kinds of compute nodes. We group them into (sometimes overlapping) [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes. By combining the `--partition` and [`--constraint`](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) Slurm options you can more finely control what nodes your jobs can run on.

!!! info
    YCGA sequence data user?  To avoid being charged for your cpu usage for YCGA-related work, make sure to submit jobs to the ycga partition with -p ycga.

--8<-- "snippets/submission_rate_limit.md"


### Public Partitions

See each tab below for more information about the available common use partitions.

--8<-- "snippets/mccleary_partitions.md"

## Public Datasets

We host datasets of general interest in a loosely organized directory tree in `/gpfs/gibbs/data`:

```
├── alphafold-2.3
├── alphafold-2.2 (deprecated)
├── alphafold-2.0 (deprecated)
├── annovar
│   └── humandb
├── cryoem
├── db
│   ├── annovar
│   ├── blast
│   ├── busco
│   └── Pfam
└── genomes
    ├── 1000Genomes
    ├── 10xgenomics
    ├── Aedes_aegypti
    ├── Bos_taurus
    ├── Chelonoidis_nigra
    ├── Danio_rerio
    ├── Drosophila_melanogaster
    ├── Gallus_gallus
    ├── hisat2
    ├── Homo_sapiens
    ├── Macaca_mulatta
    ├── Mus_musculus
    ├── Monodelphis_domestica
    ├── PhiX
    └── Saccharomyces_cerevisiae
    └── tmp
└── hisat2
    └── mouse
```

If you would like us to host a dataset or questions about what is currently available, please [contact us](/#get-help).

## YCGA Data

Data associated with YCGA projects and sequenceers are located on the YCGA storage system, accessible at `/gpfs/ycga`.

For more information on accessing this data as well as sequencing data retention polices, see the [YCGA Data documentation](/data/ycga-data).

## Storage

McCleary has access to a number of GPFS filesystems. `/vast/palmer` is McCleary's primary filesystem where Home and Scratch60 directories are located. Every group on McCleary also has access to a Project allocation on the Gibbs filesytem on `/gpfs/gibbs`. For more details on the different storage spaces, see our [Cluster Storage](/data/hpc-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Your `~/project` and `~/palmer_scratch` directories are shortcuts. Get a list of the absolute paths to your directories with the `mydirectories` command. If you want to share data in your Project or Scratch directory, see the [permissions](/data/permissions/) page.

For information on data recovery, see the [Backups and Snapshots](/data/backups) documentation.

!!! Warning
    Files stored in `palmer_scratch` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted. Artificial extension of scratch file expiration is forbidden without explicit approval from the YCRC. Please [purchase storage](/data/#purchase-additional-storage) if you need additional longer term storage.

|Partition  | Root Directory                   | Storage                                 | File Count | Backups | Snapshots |
|-----------|----------------------------------|-----------------------------------------|------------|---------|-----------|
| home      | `/vast/palmer/home.mccleary`     | 125GiB/user                             | 500,000    | Yes     | >=2 days  |
| project   | `/gpfs/gibbs/project`            | 1TiB/group, increase to 4TiB on request | 5,000,000  | No      | >=2 days  |
| scratch   | `/vast/palmer/scratch`           | 10TiB/group                             | 15,000,000 | No      | No        |

