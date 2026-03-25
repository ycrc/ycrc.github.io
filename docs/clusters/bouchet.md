# Bouchet

![Edward Bouchet](/img/edward-bouchet.jpg){: .cluster-portrait}

The Bouchet HPC cluster is shared-use resource for researchers at Yale. Bouchet is named for [Dr. Edward Bouchet](https://en.wikipedia.org/wiki/Edward_Bouchet) (1852-1918), the first self-identified African American to earn a doctorate from an American university, a PhD in physics at Yale University in 1876.

Bouchet is the successor to both Grace and McCleary, with the majority of HPC infrastructure refreshes and growth deployed at MGHPCC going forward. More information about the decommission of Grace and McCleary is available on the [Decommission Page](/clusters/grace-mccleary-decommission). We welcome any researchers to move their workloads to Bouchet at their convenience between now and then to take advantage of Bouchet’s newer, faster and more powerful computing resources. YCRC staff is available to assist (you can contact us at [research.computing@yale.edu](mailto:research.computing@yale.edu). 

---

## Access the Cluster

!!! info "Get Started on Bouchet"
    Please see the [Bouchet Getting Started](/clusters/bouchet_getting_started/) for more information on key differences about Bouchet compared to older YCRC clusters.

Once you have [an account](https://research.computing.yale.edu/support/hpc/account-request), the cluster can be accessed [via ssh](/clusters-at-yale/access) or [Open OnDemand](/clusters-at-yale/access/ood) at [https://ood-bouchet.ycrc.yale.edu](https://ood-bouchet.ycrc.yale.edu).

## System Status and Monitoring

For system status messages and the schedule for upcoming maintenance, please see the [system status page](https://research.computing.yale.edu/system-status). 
For a current node-level view of job activity, see the [cluster monitor page (VPN only)](http://cluster.ycrc.yale.edu/bouchet/).

## Installed Applications

A large number of software and applications are installed on our clusters.
These are made available to researchers via [software modules](/applications/modules/).

??? summary "Available Software Modules (click to expand)"
    ---8<-- "snippets/bouchet_modules.md"

## Partitions and Hardware

### Public Partitions

See each tab below for more information about the available common use partitions.

--8<-- "snippets/bouchet_partitions.md"

## Storage

Bouchet has access to one filesystem called Roberts. 
Roberts is an all-flash, NFS filesystem similar to the Palmer filesystem on Grace and McCleary.
For more details on the different storage spaces, see our [Cluster Storage](/data/hpc-storage) documentation.

Your `~/project_pi_<netid of the pi>` and `~/scratch_pi_<netid of the pi>` directories are shortcuts. 
Get a list of the absolute paths to your directories with the `mydirectories` command. 
If you want to share data in your Project or Scratch directory, see the [permissions](/data/permissions/) page.

For information on data recovery, see the [Backups and Snapshots](/data/backups) documentation.

!!! Warning
    Files stored in `scratch` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted. Artificial extension of scratch file expiration is forbidden without explicit approval from the YCRC. Please [purchase storage](/data/#purchase-additional-storage) if you need additional longer term storage.

|Partition       | Root Directory            | Storage                                 | File Count | Backups | Snapshots | Notes |
|----------------|---------------------------|-----------------------------------------|------------|---------|-----------|-------|
| home           | `/home`                   | 125GiB/user                             | 500,000    | Yes     | >=2 days  |       |
| project        | `/nfs/roberts/project`    | 4TiB/group                              | 5,000,000  | Yes     | >=2 days  |       |
| scratch        | `/nfs/roberts/scratch`    | 10TiB/group                             | 15,000,000 | No      | No        |       |
| pi             | `/nfs/roberts/pi`         | varies                                  | vareis     | No      | >=2 days  |       |
