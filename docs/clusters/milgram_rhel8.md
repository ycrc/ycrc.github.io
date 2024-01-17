# Milgram Operating System Upgrade

Milgram's current operating system, Red Hat (RHEL) 7, will be offically end-of-life in 2024 and will no longer be supported with security patches by the developer.
Therefore Milgram will be upgraded to RHEL 8 during the February maintenance window, February 6-8, 2024.
This provides a number of key benefits to Milgram:

1. continued security patches and support beyond 2024
1. updated system libraries to better support modern software
1. improved node management system to facilitate the growing number of nodes on Milgram

While we have done extensive testing both internally and with McCleary and Grace clusters, we recognize that there are a large number custom workflows on Milgram that may need to be modified to work with the new operating system. To this end, we are setting aside `rhel8_devel` and `rhel8_day` partitions for use in debugging and testing of workflows before the February maintenance. 

## Test Partitions

To submit jobs to the test partitions, open the shell access on Open OnDemand or log into Milgram via SSH with the command:

```
ssh netid@milgram.ycrc.yale.edu
```

Request an interactive job on `rhel8_devel`:

```
salloc -p rhel8_devel -c 4 -t 2:00:00 
```

Submit a batch job to `rhel8_day`:

```
sbatch -p rhel8_day -c 4 -t 2:00:00 batch.sh
```

Please note that the `rhel8_devel` and `rhel8_day` partitions have the same job limits (e.g.maximum time limit) as the `interactive` and `day` partitions, respectively.   

## Common Errors

### Python not found

Under RHEL8, we have only installed Python 3, which must be executed using `python3` (not `python`). 
As always, if you need additional packages, we strongly recommend setting up your own [conda environment](/clusters-at-yale/guides/conda/).

In addition, Python 2.7 is no longer support and therefore not installed by default. 
To use Python 2.7, we request you setup a [conda environment](/clusters-at-yale/guides/conda/).

### MPI applications fail with `srun` command

If your workflow involves loading the 2020b version of OpenMPI and uses `srun` to run your application, please load the OpenMPI module built with RHEL8 after loading other necessary modules.

For example, load the `OpenMPI/4.0.5-GCC-10.2.0-rhel8` module after loading the `gompi/2020b` module:

```
module load gompi/2020b
module load OpenMPI/4.0.5-GCC-10.2.0-rhel8
```
  
### Missing System Libraries

Some of the existing applications may depend on libraries that are no longer installed in the operating system.
If you run into these errors please email [hpc@yale.edu](mailto:hpc@yale.edu) and include which application/version you are using along with the full error message.
We will investigate these on a case-by-case basis and work to get the issue resolved.

## Report Issues

If you continue to have or discover new issues with your workflow, feel free to [contact us](/) for assistance. Please include the working directory, the commands that were run, the software modules used, and any more information needed to reproduce the issue.

