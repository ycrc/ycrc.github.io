# HPC Resources

The YCRC maintains and supports a number of high performance computing systems for the Yale research community. To download a Word document that describes our facilities, equipment, and other resources for HPC and research computing, click [here](https://research.computing.yale.edu/sites/default/files/files/Facilities%20and%20Equipment%20Document-2020-02-27.docx). 

## Compute

We maintain and support four Red Hat Linux compute clusters, listed below. Please click on cluster names for more information. 

| Cluster Name       | Approx. Core Count | Approx. Node Count | Login Address<img width=200/> | Purpose                                                   |
|--------------------|--------------------|---------------------|-------------------------------|----------------------------------------------------------|
| [Grace](grace)     | 27,000             | 900                 | `grace.hpc.yale.edu`          | general and highly parallel, tightly coupled (InfiniBand)|
| [Farnam](farnam)   | 5,700              | 250                 | `farnam.hpc.yale.edu`         | medical and life science                                 |
| [Milgram](milgram) | 2,400              | 80                  | `milgram.hpc.yale.edu`        | HIPAA and other sensitive data                           |
| [Ruddle](ruddle)   | 3,200              | 200                 | `ruddle.hpc.yale.edu`         | [Yale Center for Genome Analysis](http://ycga.yale.edu/) |

## Storage

We maintain several high performance storage systems. Listed below are these shared filesystems and the clusters where they are available. We distinguish where clusters store their home directories with an asterisk. The directory `/home` will always point to your home directory on the cluster you logged into. For more information about storage quotas and purchasing storage see the [Cluster Storage](/clusters-at-yale/data/index) page.

| Storage  | Path          | Size    | Mounting Clusters     | File System Software      | Purpose                         |
|----------|---------------|---------|-----------------------|---------------------------|---------------------------------|
| Loomis   | /gpfs/loomis  | 2.6 PiB | Grace\*, Farnam       | IBM Spectrum Scale (GPFS) | Grace primary storage           |
| YSM      | /gpfs/ysm     | 1.5 PiB | Grace, Farnam\*       | IBM Spectrum Scale (GPFS) | Farnam primary storage          |
| Gibbs    | /gpfs/gibbs   | 5.4 PiB | Grace, Farnam, Ruddle | IBM Spectrum Scale (GPFS) | purchased project-style storage |
| Slayman  | /gpfs/slayman | 1.0 PiB | Grace, Farnam         | IBM Spectrum Scale (GPFS) | purchased project-style storage |
| Milgram  | /gpfs/milgram | 2.1 PiB | Milgram\*             | IBM Spectrum Scale (GPFS) | Milgram primary storage         |
| YCGA     | /gpfs/ycga    | 2.0 PiB | Ruddle\*              | IBM Spectrum Scale (GPFS) | Ruddle primary storage          |
