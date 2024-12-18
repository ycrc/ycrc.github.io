# Bouchet

![Edward Bouchet](/img/edward-bouchet.jpg){: .cluster-portrait}

Yale [recently joined the Massachusetts Green High Performance Computing Center (MGHPCC)](https://research.computing.yale.edu/about/yale-joins-mghpcc), a not-for-profit, state-of-the-art data center dedicated to computationally-intensive research. We are pleased to announce our first installation at MGHPCC will be a new HPC cluster called Bouchet. Bouchet is named for Edward Bouchet (1852-1918), the first self-identified African American to earn a doctorate from an American university, a PhD in physics at Yale University in 1876.

- - -

## Announcing the Bouchet HPC Cluster

!!! info "Bouchet Beta"
    The Bouchet HPC cluster is now available in beta for tightly coupled, parallel workloads. Please see the [Bouchet Beta Testing documentation](/clusters/bouchet_beta/) for more information.

The first installation of nodes, approximately 4,000 direct-liquid-cooled cores, will be dedicated to tightly coupled parallel workflows, such as those run in the `mpi` partition on the Grace cluster. 
Later on this year we will be acquiring and installing a large number of general purpose compute nodes as well as GPU-enabled compute nodes. 
At that point Bouchet will be available to all Yale researchers for computational work involving low-risk data.

Ultimately, Bouchet is the planned successor to both Grace and McCleary, with the majority of HPC infrastructure refreshes and growth deployed at MGHPCC going forward. 
However, we are still in the early stages of planning that transition and will continue to operate both Grace and McCleary in their current form for a number of years. 
More details will be provided as we consult with faculty and researchers about the transition and how we can minimize disruptions to critical work. 
To this effect, we will be convening a faculty advisory committee this fall to ensure a smooth migration.

If you have any questions about Yale’s partnership at MGHPCC or the Bouchet cluster, please [reach out to us](/).

## Access the Cluster

Once you have [an account](https://research.computing.yale.edu/support/hpc/account-request), the cluster can be accessed [via ssh](/clusters-at-yale/access).

## System Status and Monitoring

For system status messages and the schedule for upcoming maintenance, please see the [system status page](https://research.computing.yale.edu/support/hpc/system-status). 
For a current node-level view of job activity, see the [cluster monitor page (VPN only)](http://cluster.ycrc.yale.edu/bouchet/).

## Partitions and Hardware

### Public Partitions

See each tab below for more information about the available common use partitions.

--8<-- "snippets/bouchet_partitions.md"

## Storage

Bouchet has access to one filesystem called Roberts. 
Roberts is an all-flash, NFS filesystem similar to the Palmer filesystem on Grace and McCleary.
For more details on the different storage spaces, see our [Cluster Storage](/data/hpc-storage) documentation.

Your `~/project` and `~/scratch` directories are shortcuts. 
Get a list of the absolute paths to your directories with the `mydirectories` command. 
If you want to share data in your Project or Scratch directory, see the [permissions](/data/permissions/) page.

For information on data recovery, see the [Backups and Snapshots](/data/backups) documentation.

!!! Warning
    Files stored in `scratch` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted. Artificial extension of scratch file expiration is forbidden without explicit approval from the YCRC. Please [purchase storage](/data/#purchase-additional-storage) if you need additional longer term storage.

|Partition       | Root Directory            | Storage                                 | File Count | Backups | Snapshots | Notes |
|----------------|---------------------------|-----------------------------------------|------------|---------|-----------|-------|
| home           | `/home`                   | 125GiB/user                             | 500,000    | Not yet | >=2 days  |       |
| project        | `/nfs/roberts/project`    | 1TiB/group, increase to 4TiB on request | 5,000,000  | No      | >=2 days  |       |
| scratch        | `/nfs/roberts/scratch`    | 10TiB/group                             | 15,000,000 | No      | No        |       |
