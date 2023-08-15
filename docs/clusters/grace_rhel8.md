# Grace Operating System Upgrade

Grace's current operating system, Red Hat (RHEL) 7, will be offically end-of-life in 2024 and will no longer be supported with security patches by the developer.
Therefore Grace has been upgraded to RHEL 8 during the August maintenance window, August 15-17, 2023.
This provides a number of key benefits to Grace:

1. consistency with the McCleary cluster
1. continued security patches and support beyond 2023
1. updated system libraries to better support modern software
1. improved node management system to facilitate the growing number of nodes on Grace
1. shared application tree between McCleary and Grace, which brings software parity between the clusters\*

\* some software and workflows will only be supported by YCRC staff on one of the cluster, e.g. tightly couple MPI codes (Grace) or RELION (McCleary).

While we have done extensive testing both internally and with the new McCleary cluster, we recognize that there are a large number custom workflows on Grace that may need to be modified to work with the new operating system. To this end, we provided test partition ahead of the upgrade. Now that the upgrade has been rolled out cluster-wide, the test partitions (e.g. `rhel8_day`) have been removed. All jobs should be submitted to the normal partitions, which now contain exclusively RHEL 8 nodes.

## New Software Tree

Grace now shares a software module tree with the McCleary cluster, providing a more consistent experience for all our users.
Some software may only be initially available in a newer version than was installed on Grace. 

If you cannot find a software package on Grace that you need, please let us know at [hpc@yale.edu](mailto:hpc@yale.edu) and we can look into installing it for you.

## Common Errors

### Python not found

Under RHEL8, we have only installed Python 3, which must be executed using `python3` (not `python`). As always, if you need additional packages, we strongly recommend setting up your own [conda environment](/clusters-at-yale/guides/conda/).

In addition, Python 2.7 is no longer support and therefore not installed by default. To use Python 2.7, we request you setup a [conda environment](/clusters-at-yale/guides/conda/).

## Report Issues

If you continue to have or discover new issues with your workflow, feel free to [contact us](/) for assistance. Please include the working directory, the commands that were run, the software modules used, and any more information needed to reproduce the issue.

