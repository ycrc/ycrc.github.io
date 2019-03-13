# Omega

!!!warning
    All of Omega's scratch space is read-and-delete-only as of Dec 3, 2018. The scratch space will be purged and all data permanently deleted on Feb 1, 2019.

Omega has now served Yale’s research community well for more than 2 years past the normal end-of-life for similar clusters. Most of its components are no longer under vendor warranty, and parts are sometimes difficult to obtain, so we are forced to support it on a best-effort basis. Last year, we developed a multi-year plan to replace Omega, which began with moving Omega’s shared resources to our Grace cluster, for which we acquired new commons nodes.

We plan to continue to support groups with dedicated node allocations and other users running tightly-coupled parallel jobs on Omega until Mid 2019. The `mpi` partition on Grace contains the replacement nodes the remainder of Omega. Please test your workload on those nodes are your convenience. We will provide ample warning before the final Omega decommission.

## Clean Out Omega Data

All Omega files are now stored solely on the Loomis GPFS system. For groups that have migrated their workloads entirely to Grace or Farnam, their Omega data is now available from Grace and Farnam for copying and clean-up until Feb 2019. See [Cleaning Out Omega Data](/clusters-at-yale/data/omega-data) for instructions on retrieving your data.

## Hardware

The cluster is made up of several kinds of compute nodes. The Features column below lists the features that can be used to request different node types using the `--constraints` flag (see our [Slurm documentation](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) for more details). The RAM listed below is the amount of memory available for jobs.

### Compute Node Configurations

| Count | Node Type              | CPU                 | CPU Cores  | RAM   | Features                          |
|-------|------------------------|---------------------|------------|-------|-----------------------------------|
| 668   | HP ProLiant BL460c     | X5560               | 8          | 32G   | nehalem,sse4_2,X5560              |
| 32    | HP ProLiant BL460c     | X5560               | 8          | 44G   | nehalem,sse4_2,X5560,extramem     |
| 4     | HP ProLiant SL250s     | E5-2650             | 16         | 121G  | sandybridge,sse4_2,avx,E5-2650    |
| 60    | HP ProLiant SL230s     | E5-2620             | 12         | 59G   | sandybridge,sse4_2,avx,E5-2620    |

## Slurm Partitions

Nodes on the clusters are organized into partitions, to which you submit your jobs with [Slurm](/clusters-at-yale/job-scheduling).

### Public Partitions

The day partition is where most batch jobs should run, and is the default if you don't specify a partition. The week partition is smaller, but allows for longer jobs. The interactive partition should only be used for testing or compiling software. The bigmem partition contains our largest memory node; only jobs that cannot be satisfied by day should run here. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

The limits listed below are for all running jobs combined. Per-node limits are bound by the node types, as described in the [hardware](#hardware) table.

| Partition   |  User Limits                 | Walltime default/max | Node type (number)                   |
|-------------|-----------------------------|-----------------------|--------------------------------------|
| day*        | 128 nodes                   | 1h/1d                 | BL460c (218)                         |
| week        | 64 nodes                    | 1h/7d                 | BL460c (46), BL460c-extramem (16)    |
| interactive | 1 job, 8 CPUs, 1 node       | 1h/4h                 | BL460c (2)                           |
| shared**    |                             | 1h/1d                 | BL460c (2)                           |
| bigmem      |                             | 1h/1d                 | SL250s (4)                           |
| scavenge    |                             | 1h/7d                 | all                                  |

\* default partition  
** The shared partition is for jobs that require less than a full node of cores

### Private Partitions

Private partitions contain nodes acquired by specific research groups. Full access to these partitions is granted at the discretion of the owner. Contact us if your group would like to purchase nodes.

| Partition           | Walltime default/max | Node type (number)                   |
|---------------------|----------------------|--------------------------------------|
| astro               | 1h/28d               | BL460c (112), BL460c-extramem (16)   |
| geo                 | 1h/7d                | BL460c (207)                         |
| hep                 | 1h/7d                | BL460c (47)                          |
| esi                 | 1h/28d               | SL230s (60)                          |

## Storage

`/gpfs/loomis` is Omega's primary filesystem where home, and scratch60 directories are located. You can also access Grace's project space (if you have a Grace account) from Omega. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/cluster-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage breakdown only update once daily.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

|Partition  | Root Directory                | Storage     | File Count | Backups |
|-----------|-------------------------------|-------------|------------|---------|
| home      | `/gpfs/loomis/home.omega`     | 300G/group  | 500,000    | Yes     |
| scratch60 | `/gpfs/loomis/scratch60`      | 20T/group   | 5,000,000  | No      |
