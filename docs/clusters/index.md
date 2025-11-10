# Computing Resources

The YCRC maintains and supports a number of high performance computing systems for the Yale research community. Our high performance computing systems are named after [notable members of the Yale community](https://research.computing.yale.edu/about/hpc-resources).

Each YCRC cluster undergoes regular scheduled maintenance twice a year, see [our maintenance schedule](/clusters/maintenance) for more details.

For proposals, we provide [a description of our facilities, equipment, and other resources for HPC and research computing](https://docs.google.com/document/d/1TRoXlMd8muiFP8NUp6g00tl0QAV5P8KScnC0vBv6oBA).

## Compute

We maintain and support three Red Hat Linux compute clusters, listed below. Please click on cluster names for more information. 


| Cluster Name        | Approx. Core Count | Approx. Node Count | Login Address<img width=200/> | Purpose                                                            |
|---------------------|--------------------|---------------------|-------------------------------|-------------------------------------------------------------------|
| [Bouchet](bouchet)  | 11,000             | 180                 | `bouchet.ycrc.yale.edu`       | all research with low-risk data, including tightly coupled (InfiniBand)   |
| [Hopper](hopper)    | 6,000              | 100                 | ---                           | NIST 800-171, HIPAA and other sensitive data |
| [Grace](grace)      | 26,000             | 670                 | `grace.ycrc.yale.edu`         | general and highly parallel, tightly coupled (InfiniBand)         |
| [McCleary](mccleary)| 13,000             | 340                 | `mccleary.ycrc.yale.edu`      | medical and life science, [YCGA](http://ycga.yale.edu/)           |
| [Milgram](milgram)  | 2,000              | 50                  | `milgram.ycrc.yale.edu`       | sensitive data                                    |
| [Misha](misha)      | 2,000              | 40                  | `misha.ycrc.yale.edu`         | [Wu Tsai Institute](http://wti.yale.edu)                          |


## Storage

We maintain several high performance storage systems. Listed below are these shared filesystems and the clusters where they are available. We distinguish where clusters store their home directories with an asterisk. The directory `/home` will always point to your home directory on the cluster you logged into. For more information about storage quotas and purchasing storage see the [Cluster Storage](/data/hpc-storage) page.

| Name     | Path          | Size     | Mounting Clusters       | File System Software      | Purpose                                  |
|----------|---------------|----------|-------------------------|---------------------------|------------------------------------------|
| Roberts  | /nfs/roberts  | 3.6 PiB  | Bouchet\*               | VAST                      | Bouchet primary storage                  |
| Weston        | /nfs/weston  | 2.4 PiB  | Hopper\*     | VAST                      | home, work, scratch storage, purchased work-style storage |
| Palmer   | /vast/palmer  | 700 TiB  | Grace\*, McCleary\*     | VAST                      | home, scratch storage, purchased project-style storage |
| Gibbs    | /gpfs/gibbs   | 14.0 PiB | Grace, McCleary         | IBM Spectrum Scale (GPFS) | project, purchased project-style storage |
| YCGA           | /gpfs/ycga    | 3.0 PiB  | McCleary                | IBM Spectrum Scale (GPFS) | YCGA storage                             |
| Milgram       | /gpfs/milgram | 3.0 PiB  | Milgram\*               | IBM Spectrum Scale (GPFS) | Milgram primary storage                  |
| Radev | /gpfs/radev   | 2.0 PiB  | Misha\*                 | IBM Spectrum Scale (GPFS) | Misha primary storage                    |
