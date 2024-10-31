# Bouchet Beta Testing

Bouchet HPC cluster is YCRC's first installation at [Massachusetts High Performance Computing Center (MGHPCC)](https://research.computing.yale.edu/about/yale-joins-mghpcc). The first installations of nodes, approximately 4,000 direct-liquid-cooled cores, will be dedicated to tightly coupled parallel workflows, such as those run in the "mpi" partition on the Grace cluster. During the beta testing, we are explicitly and exclusively seeking tighly coupled, MPI-enabled workloads. We encourage researchers to participate in the beta as it will help ensure that the production cluster will run your work without issue and provide optimal performance. There will be no compute charges on Bouchet during beta testing.  

Bouchet MPI parition provides a number of benefits compared to Grace MPI partition:

1. Bouchet MPI nodes are 64-core Emerald Rapids Platinum 8562Y+ nodes, which are a newer generation compared to Skylake 6136 nodes in the Grace MPI partition 
2. Each compute node in Bouchet has 487GiB of usable RAM, significantly more than the 88GiB/node in Grace MPI parition
3. The installed software packages in Bouchet are compiled specifically for the Emeral Rapids architecture to provide optimal performance 

## Access the cluster

Once you have an account, the cluster can be accessed [via ssh](/clusters-at-yale/access). Open OnDemand for Bouchet will be available in the future. You can log in with the command:

```
ssh NETID@bouchet.ycrc.yale.edu
```

## Key Differences from Other Clusters 

### Primary Group

On non-Bouchet clusters, your PI name is the primary group of your account. On Bouchet, your primary group is your NetID, and your PI name is your secondary group. This setup makes the process of group change easier and can also accomodate "project"-based secondary groups rather than PI-based secondary groups.    

### Partition 

Currently, `devel` and `mpi` nodes are available. Both partitions have identical 64 core, 2x Emerald Rapids Platinum 8562Y+, 500GiB RAM (487GiB usable) nodes. For more detailed information about job limits and avalable compute nodes in each partition, please refer to [our Bouchet partition documentation](https://docs.ycrc.yale.edu/clusters/bouchet/#partitions-and-hardware). Please use `devel` partition for code development, debugging, and compilation. Jobs submitted to [`mpi` partitions](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/mpi/) need to request at least two nodes and are allocated full nodes.      

### Storage

Bouchet filesystem is an all-flash storage system from VAST data and does not have any GPFS filesystem. `/nfs/roberts/` hosts Bouchet's home, project, and scratch directories. Your project and scratch storage usage and quota are shared with the members of your secondary group. 

|Storage         | Root Directory            | Quota                                   | File Count | 
|----------------|---------------------------|-----------------------------------------|------------|
| home           | `/nfs/roberts/home`       | 125GiB/user                             | 500,000    | 
| project        | `/nfs/roberts/project`    | 1TiB/group, increase to 4TiB on request | 5,000,000  | 
| scratch        | `/nfs/roberts/scratch`    | 10TiB/group                             | 15,000,000 |

### Transfer data from other clusters

To transfer data from other clusters to Bouchet, we encourage using `rsync`. `rsync` is a commonly used command-line tool for remote transfers between two systems. 

Before getting started with the transfer with `rsync`, we first need to enable access to Bouchet from other clusters. Please run the following command on Bouchet:

```
cat ~/.ssh/id_rsa.pub
```

and copy and paste the output to our [SSH key uploader](https://sshkeys.ycrc.yale.edu/). The propagation of this public key to other clusters can take a few minutes. 

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

Commonly used software is available as modules, similar to other clusters. The software module tree is lcoated at `/apps/software`. Currently, all software is compiled and installed with the 2022b version of the toolchain on Bouchet, even if the same software version is installed with an older toolchain (e.g. 2020b) on other clusters.If you would like to compile your own code specifically to the Bouchet MPI compute node architecture, you can request an interactive compute session in the devel partition of Bouchet. Because Bouchet does not have any GPFS filesystem, please turn off any GPFS related optimization configuration. 


## Report Issues

If you discover issues when running your workflow or experience performance issues, feel free to [contact](/) us for assistance. Please include the working directory, the commands that were run, the software modules used, and any more information needed to reproduce the issue.






  
