# NAMD

[NAMD](https://www.ks.uiuc.edu/Research/namd/) is a parallel molecular dynamics code designed for high-performance simulation of large biomolecular systems. NAMD scales to hundreds of cores for typical simulations. NAMD uses the popular molecular graphics program [VMD](https://www.ks.uiuc.edu/Research/vmd/), for simulation setup and trajectory analysis, but is also file-compatible with AMBER, CHARMM, and X-PLOR.To see a full list of available versions of NAMD on the cluster, run:

``` bash
module avail namd/
```

As of this writing, the latest installed version is 2.13.

## Running NAMD on the Cluster

To set up NAMD on the cluster,

``` bash
module load NAMD/2.13-multicore
```

for the standard multicore version, or

``` bash
module load NAMD/2.13-multicore-CUDA
```

for the GPU-enabled version (about which there is more information below).

NAMD can be run interactively, or as a batch job.

To run NAMD interactively, you need to create an interactive session on a compute node. You could start an interactive session using 4 cores for 4 hours using

``` bash
srun --x11 --pty -c 4  -p interactive -t 4:00:00 bash
```


For longer simulations, you will generally want to run non-interactively via a [batch job](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/#batch-jobs).

### Parallelization

NAMD is most effective when run with parallelization. For running on a single node,

``` bash
namd2 +p${SLURM_CPUS_PER_TASK} YourConfigfile
```

where ${SLURM_CPUS_PER_TASK} is set by your "-c" job resource request.

NAMD uses charm++ parallel objects for multinode parallelization and the program launch uses the charmrun interface. Setting up a multinode run in a way that provides improved performance can be a complicated undertaking.  If you wish to run a multinode NAMD job and are not already familiar with MPI, feel free to contact the YCRC staff for assistance.

### GPUs

To use the GPU-accelerated version, request GPU resources for your SLURM job, and load a CUDA-enabled version of NAMD:

``` bash
module load NAMD/2.13-multicore-CUDA
```


For a single-node run, you will need at least one thread for each GPU you want to use:

``` bash
#SBATCH -c 4 --gpus=4
...

charmrun namd2 ++local +p${SLURM_CPUS_PER_TASK} YourConfigfile
```
