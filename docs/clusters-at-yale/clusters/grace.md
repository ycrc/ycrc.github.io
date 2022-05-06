# Grace


![Grace](/img/Grace-Hopper.jpg){: .cluster-portrait}

Grace is a shared-use resource for the [Faculty of Arts and Sciences](https://fas.yale.edu) (FAS). It consists of a variety of compute nodes networked over low-latency InfiniBand and mounts several shared filesystems.

The Grace cluster is is named for the computer scientist and United States Navy Rear Admiral [Grace Murray Hopper](https://en.wikipedia.org/wiki/Grace_Hopper), who received her Ph.D. in Mathematics from Yale in 1934.

- - -

## Access the Cluster

Once you have [an account](https://research.computing.yale.edu/support/hpc/account-request), the cluster can be accessed [via ssh](/clusters-at-yale/access) or through the [Open OnDemand web portal](/clusters-at-yale/access/ood/).

## System Status and Monitoring

For system status messages and the schedule for upcoming maintenance, please see the [system status page](https://research.computing.yale.edu/support/hpc/system-status). For a current node-level view of job activity, see the [cluster monitor page (VPN only)](http://cluster.ycrc.yale.edu/grace/).

## Partitions and Hardware

Grace is made up of several kinds of compute nodes. We group them into (sometimes overlapping) [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes. By combining the `--partition` and [`--constraint`](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) Slurm options you can more finely control what nodes your jobs can run on.

--8<-- "snippets/submission_rate_limit.md"

### Public Partitions

See each tab below for more information about the available common use partitions.

--8<-- "snippets/grace_partitions.md"

## Storage

Grace has access to a number of filesystems. `/vast/palmer` hosts Grace's home and scratch directories. `/gpfs/loomis` is Grace's primary filesystem where project and the older scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/index) documentation.

You can check your current storage usage & limits by running the `getquota` command. Your `~/project`, `~/scratch60`, and `~/palmer_scratch` directories are shortcuts. Get a list of the absolute paths to your directories with the `mydirectories` command. If you want to share data in your Project or Scratch directory, see the [permissions](/clusters-at-yale/data/permissions/) page.

For information on data recovery, see the [Backups and Snapshots](/clusters-at-yale/data/#backups-and-snapshots) documentation.

!!! Warning
    Files stored in `scratch60` and `palmer_scratch` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition       | Root Directory            | Storage                                 | File Count | Backups | Snapshots | Notes |
|----------------|---------------------------|-----------------------------------------|------------|---------|-----------|-------|
| home           | `/vast/palmer/home.grace` | 125GiB/user                             | 500,000    | Yes     | No        | will be enabled late 2022      |
| project        | `/gpfs/loomis/project`    | 1TiB/group, increase to 4TiB on request | 5,000,000  | No      | >=2 days  |       |
| scratch60      | `/gpfs/loomis/scratch60`  | 20TiB/group                             | 15,000,000 | No      | No        | decommissioning in late 2022 |
| palmer_scratch | `/vast/palmer/scratch`    | 20TiB/group                             | 15,000,000 | No      | No        | |
