# Misha

![Misha](/img/misha.jpeg){: .cluster-portrait}

Misha is a cluster intended for use on projects associated with the [Wu Tsai Institute](https://wti.yale.edu/), an interdisciplinary research endeavor at Yale University connecting neuroscience and data science to accelerate breakthroughs in understanding cognition. 

Misha is named for [Dr. Misha Mahowald](https://en.wikipedia.org/wiki/Misha_Mahowald), an American computational neuroscientist in the neuromorphic engineering, known for her work on the silicon retina. 

- - -

## Access the Cluster

Once you have [an account](https://research.computing.yale.edu/support/hpc/account-request), the cluster can be accessed [via ssh](/clusters-at-yale/access) or through the [Open OnDemand web portal](/clusters-at-yale/access/ood/).


## System Status and Monitoring

For system status messages and the schedule for upcoming maintenance, please see the [system status page](https://research.computing.yale.edu/system-status).

## Installed Applications

A large number of software and applications are installed on our clusters.
These are made available to researchers via [software modules](/applications/modules/).

??? summary "Available Software Modules (click to expand)"
    ---8<-- "snippets/misha_modules.md"

## Partitions and Hardware

Misha is made up of several kinds of compute nodes. We group them into  (sometimes overlapping) [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes. By combining the `--partition` and [`--constraint`](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) Slurm options you can more finely control what nodes your jobs can run on.

--8<-- "snippets/submission_rate_limit.md"


### Public Partitions

See each tab below for more information about the available common use partitions.

--8<-- "snippets/misha_partitions.md"

## Storage

`/gpfs/radev` is Misha's filesystem where home, project, and scratch directories are located. For more details on the different storage spaces, see our [Cluster Storage](/data/hpc-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage breakdown only update once daily.

For information on data recovery, see the [Backups and Snapshots](/data/backups) documentation.

!!! Warning
    Files stored in `scratch` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted. Artificial extension of scratch file expiration is forbidden without explicit approval from the YCRC. Please [purchase storage](/data/#purchase-additional-storage) if you need additional longer term storage.

|Partition  | Root Directory          | Storage                                 | File Count | Backups | Snapshots |
|-----------|-------------------------|-----------------------------------------|------------|---------|-----------|
| home      | `/gpfs/radev/home`      | 125GiB/user                             | 500,000    | Not yet | >=2 days  |
| project   | `/gpfs/radev/project`   | 1TiB/group, increase to 4TiB on request | 5,000,000  | No      | >=2 days  |
| scratch   | `/gpfs/radev/scratch`   | 10TiB/group                             | 15,000,000 | No      | No        |
