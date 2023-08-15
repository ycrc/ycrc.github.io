# HPC Resources

The YCRC maintains and supports a number of high performance computing systems for the Yale research community. Our high performance computing systems are named after [notable members of the Yale community](https://research.computing.yale.edu/about/hpc-resources).

For proposals, we provide [a description of our facilities, equipment, and other resources for HPC and research computing](https://docs.google.com/document/d/1TRoXlMd8muiFP8NUp6g00tl0QAV5P8KScnC0vBv6oBA).

## Compute

We maintain and support three Red Hat Linux compute clusters, listed below. Please click on cluster names for more information. 

!!! info
    The Farnam and Ruddle clusters were both retired in 2023 and their users are now supported on the McCleary cluster.

| Cluster Name        | Approx. Core Count | Approx. Node Count | Login Address<img width=200/> | Purpose                                                            |
|---------------------|--------------------|---------------------|-------------------------------|-------------------------------------------------------------------|
| [Grace](grace)      | 29,000             | 900                 | `grace.hpc.yale.edu`          | general and highly parallel, tightly coupled (InfiniBand)         |
| [McCleary](mccleary)| 12,000               | 312                  | `mccleary.ycrc.yale.edu`      | medical and life science, [YCGA](http://ycga.yale.edu/)           |
| [Milgram](milgram)  | 2,400              | 80                  | `milgram.hpc.yale.edu`        | HIPAA and other sensitive data                                    |

## Storage

We maintain several high performance storage systems. Listed below are these shared filesystems and the clusters where they are available. We distinguish where clusters store their home directories with an asterisk. The directory `/home` will always point to your home directory on the cluster you logged into. For more information about storage quotas and purchasing storage see the [Cluster Storage](/data/hpc-storage) page.

| Name     | Path          | Size     | Mounting Clusters       | File System Software      | Purpose                                  |
|----------|---------------|----------|-------------------------|---------------------------|------------------------------------------|
| Palmer   | /vast/palmer  | 700 TiB  | Grace\*, McCleary\*     | Vast                      | home, scratch storage              |
| Gibbs    | /gpfs/gibbs   | 14.0 PiB | Grace, McCleary | IBM Spectrum Scale (GPFS) | project, purchased project-style storage |
| Slayman  | /gpfs/slayman | 1.0 PiB  | Grace, McCleary | IBM Spectrum Scale (GPFS) | purchased project-style storage          |
| Milgram  | /gpfs/milgram | 3.0 PiB  | Milgram\*      | IBM Spectrum Scale (GPFS) | Milgram primary storage                  |
| YCGA     | /gpfs/ycga    | 3.0 PiB  | McCleary      | IBM Spectrum Scale (GPFS) | YCGA storage     |
