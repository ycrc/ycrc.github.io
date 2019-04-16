# HPC Resources

## Compute

We maintain and support 5 compute clusters, with roughly 29,000 cores total. Please click on cluster names for more information. To download a Word document that describes our facilities, equipment, and other resources for HPC and research computing, click [here](/files/Facilities_Equipment-YCRC_20180705.docx).

| Cluster Name       | Approx. Core Count | Login Address<img width=150/> | Monitor Dashboard                                                                                        | Purpose                                                  |
|--------------------|--------------------|-------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [Grace](grace)     | 13,500             | `grace.hpc.yale.edu`          | [cluster.ycrc.yale.edu/grace](http://cluster.ycrc.yale.edu/grace/)                                       | general                                                  |
| [Farnam](farnam)   | 5,200              | `farnam.hpc.yale.edu`         | [cluster.ycrc.yale.edu/farnam](http://cluster.ycrc.yale.edu/farnam/)                                     | medical/life science                                     |
| [Omega](omega)     | 6,500              | `omega.hpc.yale.edu`          | [cluster.ycrc.yale.edu/omega](http://cluster.ycrc.yale.edu/omega/)                                       | highly parallel, tightly coupled                         |
| [Ruddle](ruddle)   | 3,800              | `ruddle.hpc.yale.edu`         | [cluster.ycrc.yale.edu/ruddle](http://cluster.ycrc.yale.edu/ruddle/)                                     | [Yale Center for Genome Analysis](http://ycga.yale.edu/) |
| [Milgram](milgram) | 1,600              | `milgram.hpc.yale.edu`        | [monitor1.milgram.hpc.yale.internal:4001](http://monitor1.milgram.hpc.yale.internal:4001) (on HIPAA VPN) | HIPAA                                                    |

## Storage

We maintain several high performance storage systems which amount to about 9 PB total. Listed below are these shared filesystems and the clusters where they are available. We distinguish where clusters store their home directories with an asterisk. The directory `/home` will always contain the home directory of the cluster you are on.

| Filesystem    | Size   | Mounting Clusters        |
|---------------|--------|--------------------------|
| /gpfs/loomis  | 2.6 PB | Grace\*, Omega\*, Farnam |
| /gpfs/ysm     | 1.5 PB | Grace, Omega, Farnam\*   |
| /gpfs/slayman | 1.0 PB | Grace, Omega, Farnam     |
| /gpfs/ycga    | 2.0 PB | Ruddle\*                 |
| /ycga-ba      | 1.1 PB | Ruddle                   |
| /gpfs/milgram | 1.1 PB | Milgram\*                |
