# Bouchet Beta Testing

The Bouchet HPC cluster is YCRC's first installation at [Massachusetts High Performance Computing Center (MGHPCC)](https://research.computing.yale.edu/about/yale-joins-mghpcc). 
Bouchet is the planned successor to both Grace and McCleary, with the majority of HPC infrastructure refreshes and growth deployed at MGHPCC going forward.
The first installations of nodes, approximately 4,000 direct-liquid-cooled cores, will be dedicated to tightly coupled parallel workflows using `mpi`. 
A second set of nodes will be installed in early 2025 aimed at general purpose workflows, including GPU-accelerated work.
We encourage researchers to participate in the beta as it will help ensure that the production cluster will run your work without issue and provide optimal performance. 

Compared to the existing `mpi` partition Bouchet provides several key improvements:

1. Bouchet MPI nodes are 64-core Emerald Rapids Platinum 8562Y+ nodes, which are several generations newer compared to current Skylake 6136 nodes 
2. Each compute node in Bouchet has 487GiB of usable RAM, significantly more than the 88GiB/node currently available
3. The installed software packages in Bouchet are compiled specifically for the Emerald Rapids architecture to provide optimal performance

!!! warning
    While in beta, Bouchet may become unavailable with little or no notice as the YCRC configures and troubleshoots the system for production deployment. No data on Bouchet is currently backed up. Bouchet is expected to stay in beta until at least mid-January.

## Access the Cluster

Once you have an account, the cluster can be accessed [via ssh](/clusters-at-yale/access). 
You can log in with the command:

```
ssh NETID@bouchet.ycrc.yale.edu
```

Open OnDemand for Bouchet will be available in the future. Additionally, the implementation of certain utility commands that are available on other clusters is still in progress.  

## Key Differences from Other Clusters

### Primary Group

On non-Bouchet clusters, your PI name is the primary group of your account. 
On Bouchet, your primary group is your NetID, and secondary groups are assigned for any PI group you belong to. 
This setup makes the process of group change easier and can also accomodate "project"-based secondary groups rather than PI-based secondary groups.    
Files created in PI-owned project and scratch directories will inherit the correct PI group-ownership.
However, be careful about copying existing files from `$HOME` to project spaces, as those files may need to have their group ownership updated. 

### Partition

Currently, `devel` and `mpi` partitions are available. 
For detailed information about job limits and avalable compute nodes in each partition, please refer to [our Bouchet partition documentation](/clusters/bouchet/#partitions-and-hardware). 
Please use `devel` partition for code development, debugging, and compilation. 
Jobs submitted to [`mpi` partitions](/clusters-at-yale/job-scheduling/mpi/) need to request at least two nodes and are allocated full nodes.      

### Storage

Bouchet's filesystem, Roberts, is an all-flash storage system from VAST data and does not have a GPFS filesystem. 
`/nfs/roberts/` hosts Bouchet's home, project, and scratch directories. 
Your project and scratch storage usage and quota are shared with the members of the associated secondary group. 

|Storage         | Root Directory            | Quota                                   | File Count | 
|----------------|---------------------------|-----------------------------------------|------------|
| home           | `/nfs/roberts/home`       | 125GiB/user                             | 500,000    | 
| project        | `/nfs/roberts/project`    | 1TiB/group, increase to 4TiB on request | 5,000,000  | 
| scratch        | `/nfs/roberts/scratch`    | 10TiB/group                             | 15,000,000 |

### Transfer data from other clusters

To transfer data from other clusters to Bouchet, we encourage using [`rsync`](/data/transfer/#rsync). 
`rsync` is a commonly used command-line tool for remote transfers between two systems. 
Globus is not yet available on Bouchet.

Before getting started with the transfer with `rsync`, we first need to enable access to Bouchet from other clusters. 
Please run the following command on Bouchet:

```
cat ~/.ssh/id_rsa.pub
```

and copy and paste the output to our [SSH key uploader](https://sshkeys.ycrc.yale.edu/). 
The propagation of this public key to other clusters can take a few minutes. 

To initiate the transfer from Bouchet cluster, log into the `transfer` node via ssh:

```
[an492@login1.bouchet ~]$ ssh transfer1
[an492@transfer1.bouchet ~]$
```
and run the `rsync` commands on the `transfer` node. 

We recommend using the following flags with the `rsync` command:
```
rsync -avP NETID@transfer-CLUSTER.ycrc.yale.edu:/path/to/existing/data /path/to/new/home/for/data
```
Here the `-a` will run transfer in `archive` mode, which preserves ownership, permissions, and creation/modification times. Additionally, the `-v` will run in `verbose` mode where the name of every file is printed out, and `-P` displays a progress bar. 

As an example, to transfer a directory (named `mydata`) from Grace project directory to Bouchet project directory:
```
rsync -avP NETID@transfer-grace.ycrc.yale.edu:/gpfs/gibbs/project/GROUP/NETID/mydata /nfs/roberts/project/GROUP/NETID 
```

For `rsync` transfers that may take a while, it is best to run the transfer inside a [tmux](https://docs.ycrc.yale.edu/clusters-at-yale/guides/tmux/) sesseion. 


### Applications and software

Commonly used software is available as [modules](/applications/modules/), similar to other clusters. 
Currently, all software is compiled and installed with the 2022b version of the toolchain on Bouchet, even if the same software version is installed with an older toolchain (e.g. 2020b) on other clusters.
If you would like to compile your own code specifically to the Bouchet MPI compute node architecture, you can request an interactive compute session in the `devel` partition of Bouchet. 
Because Bouchet does not have a GPFS filesystem, be sure to turn off any GPFS related optimization configuration. 


## Report Issues

If you discover issues when running your workflow or experience performance issues, feel free to [contact](/) us for assistance. 
Please include the working directory, the commands that were run, the software modules used, and any more information needed to reproduce the issue.






  
