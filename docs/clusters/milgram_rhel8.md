# Milgram Operating System Upgrade

Milgram's previous operating system, Red Hat (RHEL) 7, will be officially end-of-life in 2024 and will no longer be supported with security patches by the developer.
Therefore Milgram has been upgraded to RHEL 8 during the February maintenance window, February 6-8, 2024.
This provides a number of key benefits to Milgram:

1. continued security patches and support beyond 2024
1. updated system libraries to better support modern software
1. improved node management system to facilitate the growing number of nodes on Milgram

## Common Errors

Below are common errors encountered when moving workflows to 

### Python not found

Under RHEL8, we have only installed Python 3, which must be executed using `python3` (not `python`). 
As always, if you need additional packages, we strongly recommend setting up your own [conda environment](/clusters-at-yale/guides/conda/).

In addition, Python 2.7 is no longer support and therefore not installed by default. 
To use Python 2.7, we request you setup a [conda environment](/clusters-at-yale/guides/conda/).
  
### Missing System Libraries

Some of the existing applications may depend on libraries that are no longer installed in the operating system.
If you run into these errors please email [hpc@yale.edu](mailto:hpc@yale.edu) and include which application/version you are using along with the full error message.
We will investigate these on a case-by-case basis and work to get the issue resolved.

## Report Issues

If you continue to have or discover new issues with your workflow, feel free to [contact us](/) for assistance. Please include the working directory, the commands that were run, the software modules used, and any more information needed to reproduce the issue.

