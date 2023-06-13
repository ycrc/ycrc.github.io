# HPC Resources

The YCRC maintains and supports a number of high performance computing systems for the Yale research community. Our high performance computing systems are named after [notable members of the Yale community](https://research.computing.yale.edu/about/hpc-resources).

For proposals, we provide [a description of our facilities, equipment, and other resources for HPC and research computing](https://docs.google.com/document/d/1TRoXlMd8muiFP8NUp6g00tl0QAV5P8KScnC0vBv6oBA).

## Compute

We maintain and support four Red Hat Linux compute clusters, listed below. Please click on cluster names for more information. 

| Cluster Name        | Approx. Core Count | Approx. Node Count | Login Address<img width=200/> | Purpose                                                            |
|---------------------|--------------------|---------------------|-------------------------------|-------------------------------------------------------------------|
| [Grace](grace)      | 29,000             | 900                 | `grace.hpc.yale.edu`          | general and highly parallel, tightly coupled (InfiniBand)         |
| [Farnam](farnam)    | N/A                | N/A                 | N/A                           | medical and life science [RETIRED]                                |
| [McCleary](mccleary)| 12,000               | 312                  | `mccleary.ycrc.yale.edu`      | medical and life science, [YCGA](http://ycga.yale.edu/)           |
| [Milgram](milgram)  | 2,400              | 80                  | `milgram.hpc.yale.edu`        | HIPAA and other sensitive data                                    |
| [Ruddle](ruddle)    | 4,500              | 200                 | `ruddle.hpc.yale.edu`         | [Yale Center for Genome Analysis](http://ycga.yale.edu/)          |

## Storage

We maintain several high performance storage systems. Listed below are these shared filesystems and the clusters where they are available. We distinguish where clusters store their home directories with an asterisk. The directory `/home` will always point to your home directory on the cluster you logged into. For more information about storage quotas and purchasing storage see the [Cluster Storage](/data/hpc-storage) page.

| Name     | Path          | Size     | Mounting Clusters       | File System Software      | Purpose                                  |
|----------|---------------|----------|-------------------------|---------------------------|------------------------------------------|
| Palmer   | /vast/palmer  | 700 TiB  | Grace\*, McCleary\*     | Vast                      | Grace home, scratch storage              |
| Gibbs    | /gpfs/gibbs   | 14.0 PiB | Grace, Ruddle, McCleary | IBM Spectrum Scale (GPFS) | project, purchased project-style storage |
| YSM      | /gpfs/ysm     | 1.5 PiB  | Grace, McCleary (read-only) | IBM Spectrum Scale (GPFS) | Farnam primary storage [Retiring July 13, 2023]                   |
| Slayman  | /gpfs/slayman | 1.0 PiB  | Grace, McCleary | IBM Spectrum Scale (GPFS) | purchased project-style storage          |
| Milgram  | /gpfs/milgram | 3.0 PiB  | Milgram\*               | IBM Spectrum Scale (GPFS) | Milgram primary storage                  |
| YCGA     | /gpfs/ycga    | 2.0 PiB  | Ruddle\*, McCleary      | IBM Spectrum Scale (GPFS) | Ruddle primary storage, YCGA storage     |
