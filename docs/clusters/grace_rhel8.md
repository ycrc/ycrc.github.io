# Grace Operating System Upgrade

Grace's current operating system, Red Hat (RHEL) 7, will be offically end-of-life in 2024 and will no longer be supported with security patches.
Therefore we will be working to upgrade the operating system to RHEL 8 in the summer maintenance window, August 15-17, 2023.
This will bring it in-line with McCleary and provides a number of key benefits to Grace:

1. continued security patches and support beyond 2023
2. updated system libraries to better support modern software
3. improved node management system to facilitate the growing number of nodes on Grace
4. shared application tree between McCleary and Grace, which brings software parity between the clusters

While we have done extensive testing both internally and with the new McCleary cluster, we recognize that there are a large number custom workflows on Grace that may need to be modified to work with the new operating system. 
To this end, we have preemptively set aside `rhel8_day` and `rhel8_mpi` partitions for use in debugging and testing of workflows before the August maintenace.
These partitions are available now and are exempt from billing.


## Testing Red Hat 8
We recommend testing key workflows early so that YCRC can make any changes required before deploying to the full cluster in August.
To try out the new operating system, you will need to log into a separate `rhel8_login` node after logging into grace:

```sh
# after logging into grace:
ssh rhel8_login
```

Then you will be able to submit jobs to the `rhel8_day` and `rhel8_mpi` partitions like this:


### Simple interactive job on the `rhel8_day` partition

Request 4 CPUs, 24G of memory for 4 hours. 

```sh
salloc -p rhel8_day -c 4 --mem-per-cpu=6G --time 4:00:00
```

### Basic MPI job on `rhel8_mpi`:

Here is an example script running QuantumESPRESSO on two nodes of the `rhel8_mpi` partition (assuming the input file is named `qe.in`):

```sh
#!/bin/bash

#SBATCH --partition rhel8_mpi
#SBATCH --nodes 2
#SBATCH --cpus-per-task 1
#SBATCH --ntasks-per-node 24
#SBATCH --mem=0 # request all memory on the node

module purge
module load QuantumESPRESSO/7.1-intel-2020b
module list

srun ${EBROOTQUANTUMESPRESSO}/bin/pw.x -ndiag 100 -i qe.in

```

## Reporting issues

If any issues are encountered while testing, please report them to [hpc@yale.edu](mailto:hpc@yale.edu) so that we can address them in a timely manner.
Kindly include the working directory, the commands that were run, the software modules used, and any more information needed to reproduce the issue.

