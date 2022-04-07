# News

## March 2022

### Announcements

#### Snapshots

Snapshots are now available on all clusters for home and project spaces. Snapshots enable self-service restoration of modified or deleted files for at least 2 days in the past. [See our User Documentation for more details on availability and instructions.](https://docs.ycrc.yale.edu/clusters-at-yale/data/#backups-and-snapshots)

#### OOD File Browser Tip: Shortcuts

You can add shortcuts to your favorite paths in the OOD File Browser. [See our OOD documentation for instructions on setting up shortcuts.](https://docs.ycrc.yale.edu/clusters-at-yale/access/ood/#customize-favorite-paths)

### Software Highlights

- **R/4.1.0-foss-2020b** is now on Grace.
- **GCC/11.2.0** is now on Grace.

## Grace Maintenance
_February 3-6, 2022_

### Software Updates

* Latest security patches applied
* Slurm updated to version 21.08.5
* NVIDIA driver updated to version 510.39.01 (except for nodes with K80 GPUs which are stranded at 470.82.01)
* Singularity updated to version 3.8.5
* Open OnDemand updated to version 2.0.20

### Hardware Updates

* Changes have been made to networking to improve performance of certain older compute nodes
 
### Changes to Grace Home Directories

During the maintenance, all home directories on Grace have been moved to our new all-flash storage filesystem, Palmer. The move is in anticipation of the decommissioning of Loomis at the end of the year and will provide a robust login experience by protecting home directory interactions from data intensive compute jobs.

Due to this migration, your home directory path has changed from `/gpfs/loomis/home.grace/<netid>` to `/vast/palmer/home.grace/<netid>`.
Your home directory can always be referenced in bash and submission scripts and from the command line with the `$HOME` variable. Please update any scripts and workflows accordingly.
 
### Interactive Jobs

We have added an additional way to request an interactive job. The Slurm command `salloc` can be used to start an interactive job similar to `srun --pty bash`. In addition to being a simpler command (no `--pty bash` is needed), `salloc` jobs can be used to interactively test `mpirun` executables.
 
### Palmer scratch

Palmer is out of beta! We have fixed the issue with Plink on Palmer, so now you can use Palmer scratch for any workloads. See [https://docs.ycrc.yale.edu/clusters-at-yale/data/index#60-day-scratch](https://docs.ycrc.yale.edu/clusters-at-yale/data/index#60-day-scratch) for more information on Palmer scratch. 

## February 2022

### Announcements

#### Grace Maintenance

The biannual scheduled maintenance for the Grace cluster will be occurring February 1-3. During this time, the cluster will be unavailable. See the Grace maintenance email announcement for more details.

#### Data Transfers

For non-Milgram users doing data transfers, transfers should not be performed on the login nodes. We have a few alternative ways to get better networking and reduce the impact on the clusters’ login nodes:

1. **Dedicated transfer node**. Each cluster has a dedicated transfer node, `transfer-<cluster>.hpc.yale.edu`. You can ssh directly to this node and run commands. 
1. **“transfer” Slurm partition**. This is a small partition managed by the scheduler for doing data transfer. You can submit jobs to it using `srun/sbatch -p transfer …` 
*For recurring or periodic data transfers (such as using cron), please use Slurm’s [scrontab](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/scrontab/) to schedule jobs that run on the transfer partition instead.
2. **Globus**. For robust transfers of larger amount of data, see our [Globus](https://docs.ycrc.yale.edu/clusters-at-yale/data/globus/) documentation.

More info about data transfers can be found in our [Data Transfer](https://docs.ycrc.yale.edu/clusters-at-yale/data/transfer/) documentation.

### Software Highlights

- **Rclone** is now installed on all nodes and loading the module is no longer necessary.
- **MATLAB/2021b** is now on all clusters.
- **Julia/1.7.1-linux-x86_64** is now on all clusters.
- **Mathematica/13.0.0** is now on Grace.
- **QuantumESPRESSO/6.8-intel-2020b** and **QuantumESPRESSO/7.0-intel-2020b** are now on Grace.
- **Mathematica** [documentation](https://docs.ycrc.yale.edu/clusters-at-yale/guides/mathematica/#configure-environment-for-parallel-jobs) has been updated with regards to configuring parallel jobs.