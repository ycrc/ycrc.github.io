---
date: '2022-06-08'
---

## Milgram Maintenance
_June 7-8, 2022_

### Software Updates

- Security updates
- Slurm updated to 21.08.8-2
- NVIDIA drivers updated to 515.43.04
- Singularity replaced by Apptainer version 1.0.2 (note: the "singularity" command will still work as expected)
- Lmod updated to 8.7
- Open OnDemand updated to 2.0.23

### Hardware Updates

- The hostnames of the compute nodes on Milgram were changed to bring them in line with YCRC naming conventions.

### Changes to non-interactive sessions

Non-interactive sessions (e.g. file transfers, commands sent over ssh) no longer load the standard cluster environment to alleviate performance issues due to unnecessary module loads.
Please contact us if this change affects your workflow so we can resolve the issue or provide a workaround.
