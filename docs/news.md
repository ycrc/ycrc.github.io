# News

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