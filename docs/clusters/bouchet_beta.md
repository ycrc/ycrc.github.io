# Bouchet Beta Testing

Bouchet HPC cluster is YCRC's first installation at [Massachusetts High Performance Computing Center (MGHPCC)](https://research.computing.yale.edu/about/yale-joins-mghpcc). The first installations of nodes, approximately 4,000 direct-liquid-cooled cores, will be dedicated to tightly coupled parallel workflows, such as those run in the "mpi" partition on the Grace cluster. 

During the beta testing, we are explicitly and exclusively seeking tighly coupled, MPI-enabled workloads. We encourage researchers to participate in the beta as it will help ensure that the production cluster will run your work without issue and provide optimal performance. There will be no compute charges on Bouchet during testing.  

Bouchet MPI parition provides a number of benefits compared to Grace MPI partition:

1. Bouchet MPI nodes are Emerald Rapids Platinum 8562Y+ nodes, which are a newer generation compared to Skylake 6136 nodes in the Grace MPI partition 
2. Each compute node in Bouchet has 487GiB of usable RAM, significantly more than the 88GiB/node in Grace MPI parition
3. The installed software packages in Bouchet are compiled specifically for the Emeral Rapids architecture to provide optimal performance 

## Access the cluster

Once you have an account, the cluster can be accessed [via ssh](/clusters-at-yale/access). You can log in with the command:

```
ssh netid@bouchet.ycrc.yale.edu
```

## Key Differences from Other Clusters 

### Primary Group is your NetID

On other clusters, your PI name is the primary group of your account. On Bouchet, your primary group is your NetID, and your PI name is your secondary group. This setup makes the process of group change easier and can also accomodate "project"-based secondary groups.   

### Partition 

### Storage

Bouchet filesystem is an all-flash storage system from VAST data and does not have any GPFS filesystem. `/nfs/roberts/` hosts Bouchet's home, project and scratch directories.

|Storage         | Root Directory            | Quota                                   | File Count | 
|----------------|---------------------------|-----------------------------------------|------------|
| home           | `/nfs/roberts/home`       | 125GiB/user                             | 500,000    | 
| project        | `/nfs/roberts/project`    | 1TiB/group, increase to 4TiB on request | 5,000,000  | 
| scratch        | `/nfs/roberts/scratch`    | 10TiB/group                             | 15,000,000 |

### Transfer data from other clusters

### Applications and software

Commonly used software is available as modules, similar to other clusters. The software module tree is lcoated at `/apps/software`. Currently, all software is compiled and installed with the 2022b version of the toolchain on Bouchet, even if the same software version is installed with an older toolchain (e.g. 2020b) on other clusters.   

If you would like to compile your own code specifically to the Bouchet MPI compute node architecture, you can request an interactive compute session in the devel partition of Bouchet. Because Bouchet does not have any GPFS filesystem, please turn off any GPFS related optimization configuration. 


## Report Issues

If you discover issues when running your workflow or experience performance issues, feel free to [contact](/) us for assistance. Please include the working directory, the commands that were run, the software modules used, and any more information needed to reproduce the issue.






  
