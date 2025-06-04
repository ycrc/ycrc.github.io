# Grace


![Grace](/img/Grace-Hopper.jpg){: .cluster-portrait}

Grace is a shared-use resource for the [Faculty of Arts and Sciences](https://fas.yale.edu) (FAS). It consists of a variety of compute nodes networked over low-latency InfiniBand and mounts several shared filesystems.

The Grace cluster is is named for the computer scientist and United States Navy Rear Admiral [Grace Murray Hopper](https://en.wikipedia.org/wiki/Grace_Hopper), who received her Ph.D. in Mathematics from Yale in 1934.

- - -

!!! warning "NIH Controlled-Access Data and Repositories"
    Effective January 25, 2025, new or renewed Data Use Certifications for NIH Controlled-Access Data and Repositories must adhere to the [NIH Security Best Practices for Users of Controlled-Access Data](https://sharing.nih.gov/sites/default/files/flmngr/NIH-Security-BPs-for-Users-of-Controlled-Access-Data.pdf). While YCRC's new [Hopper cluster](/clusters/hopper) is in development, Yale has completed appropriate documentation for [McCleary](/clusters/mccleary) to be used as an approved location of NIH Controlled-Access Data and Repositories, with the certain conditions. See our [NIH Controlled-Access Data documentation](/data/nih-data) for more information and to request access.

## Access the Cluster

Once you have [an account](https://research.computing.yale.edu/support/hpc/account-request), the cluster can be accessed [via ssh](/clusters-at-yale/access) or through the [Open OnDemand web portal](/clusters-at-yale/access/ood/).

## System Status and Monitoring

For system status messages and the schedule for upcoming maintenance, please see the [system status page](https://research.computing.yale.edu/system-status). For a current node-level view of job activity, see the [cluster monitor page (VPN only)](http://cluster.ycrc.yale.edu/grace/).

## Installed Applications

A large number of software and applications are installed on our clusters.
These are made available to researchers via [software modules](/applications/modules/). 

??? summary "Available Software Modules (click to expand)"
    ---8<-- "snippets/grace_modules.md"

## Partitions and Hardware

Grace is made up of several kinds of compute nodes. We group them into (sometimes overlapping) [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes. By combining the `--partition` and [`--constraint`](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) Slurm options you can more finely control what nodes your jobs can run on.

--8<-- "snippets/submission_rate_limit.md"

### Public Partitions

See each tab below for more information about the available common use partitions.

--8<-- "snippets/grace_partitions.md"

## Storage

Grace has access to a number of filesystems. `/vast/palmer` hosts Grace's home and scratch directories and `/gpfs/gibbs` hosts project directories and most additional purchased storage allocations. For more details on the different storage spaces, see our [Cluster Storage](/data/hpc-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Your `~/project` and `~/palmer_scratch` directories are shortcuts. Get a list of the absolute paths to your directories with the `mydirectories` command. If you want to share data in your Project or Scratch directory, see the [permissions](/data/permissions/) page.

For information on data recovery, see the [Backups and Snapshots](/data/backups) documentation.

!!! Warning
    Files stored in `palmer_scratch` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted. Artificial extension of scratch file expiration is forbidden without explicit approval from the YCRC. Please [purchase storage](/data/#purchase-additional-storage) if you need additional longer term storage.

|Partition       | Root Directory            | Storage                                 | File Count | Backups | Snapshots | Notes |
|----------------|---------------------------|-----------------------------------------|------------|---------|-----------|-------|
| home           | `/vast/palmer/home.grace` | 125GiB/user                             | 500,000    | Yes     | >=2 days  |       |
| project        | `/gpfs/gibbs/project`     | 1TiB/group, increase to 4TiB on request | 5,000,000  | No      | >=2 days  |       |
| scratch        | `/vast/palmer/scratch`    | 10TiB/group                             | 15,000,000 | No      | No        |       |

