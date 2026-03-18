# AICR

[AICR](https://www.mass.gov/news/governor-healey-advances-states-ai-leadership-with-major-investments-in-massachusetts-ai-hub) is a multi-institution AI-focused computing cluster at MGHPCC that will be available to Yale researchers later this year.
The system is designed to accelerate AI innovation by providing the compute and data capacity essential for cutting-edge development.
This effort is a partnership between the Massachusetts Commonwealth and MGHPCC’s six member universities—Boston University, Harvard University, MIT, Northeastern University, the University of Massachusetts, and Yale University.

The cluster initially contains 248 B200 GPUs and 152 RTX6000 Pro Blackwell GPUs for AI and AI-enabled research. 

## Access the Cluster

AICR will be available in Spring 2026.
AICR availability and information on how to request access will be announced to the YCRC user mailing list and the YCRC Bulldog newsletter.

## Installed Applications

A large number of software and applications are installed on our clusters, including AICR.
AICR software will be made available to researchers via [software modules](/applications/modules/). 


## Partitions and Hardware

AICR initially contains 248 B200 GPUs and 152 RTX6000 Pro Blackwell GPUs, grouped into [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes. More information on the partition layout will be available soon.


## Storage

AICR has access to an all-flash, NFS filesystem similar to the Roberts filesystem on Bouchet and the Palmer filesystem on Grace and McCleary.


|Partition       | Root Directory            | Storage                                 | File Count | Backups | Snapshots | Notes |
|----------------|---------------------------|-----------------------------------------|------------|---------|-----------|-------|
| home           | TBD | 100GiB/user                             | 500,000    | No     | 7 days  |       |
| work        | TBD     | TBD | TBD | No      | 7 days  |       |
| scratch        | TBD    | 10TiB/user                             | 15,000,000 | No      | No        |       |

