# Cryogenic Electron Microscopy (Cryo-EM) Data Processing on Farnam

Below is a work in progress collection of general hints, tips and tricks for running your work on [Farnam](/clusters-at-yale/clusters/farnam). As always, if anything below is unclear or could use updating, please let us know [during office hours, via email or through our web ticketing system](/#get-help).

## Storage

Be wary of you and your group's storage quotas. Run `getquota` from time to time to make sure there isn't usage you aren't expecting. We strongly recommend that you archive raw data off-cluster, as **only home directories are backed up**. Let us know if you need extra space and we can work with you to find a solution that is right for your project and your group.

On most GPU nodes there is a fast SSD mounted at `/tmp`. You can use this as a fast local cache if your program can take advantage of it.

## Schedule Jobs

Many Cryo-EM applications can make use of GPUs as co-processors. In order to use a GPU on Farnam you must allocate a job on a partition with GPUs available and explicitly request GPU(s). Make sure to familiarize yourself with our documentation on [scheduling jobs](/clusters-at-yale/job-scheduling/) and [requesting specific resources](/clusters-at-yale/job-scheduling/resource-requests/).

There are four [partitions](/clusters-at-yale/clusters/farnam/#public-partitions) that give you access to GPUs. The gpu, gpu_devel and savenge_gpu partitions are all for general use. The use of the `pi_cryoem` and `pi_tomo` partitions are limited to users of the Cryo-EM resources on campus. Please coordinate with the staff from West Campus and CCMI ([See here for contact info](https://cryoem.yale.edu/contact)) for access.

## Software

Many Cryo-EM applications are meant to be viewed and interacted with in real-time. This mode of working is not ideal for the way most HPC clusters are set up, so where possible try to prototype a job you would like to run with a smaller dataset or subset of your data. Then develop a script to submit with `sbatch`.

### RELION

The [RELION](https://www3.mrc-lmb.cam.ac.uk/relion//index.php/Main_Page) pipeline operates in two modes. You can use it as a more familiar and beginner-friendly graphical interface, or call the programs involved directly. Once you are comfortable, using the commands directly in scripts submitted with `sbatch` will allow you to get the most work done the fastest.

The authors provide up-to-date hints about performance on their [Benchmarks](https://www3.mrc-lmb.cam.ac.uk/relion/index.php/Benchmarks_&_computer_hardware) page. If you need technical help (jobs submit fine but having other issues) you should search and submit to their [mailing list](http://www.jiscmail.ac.uk/CCPEM).

#### Module

We have GPU-enabled versions of RELION available on Farnam as [software modules](/clusters-at-yale/applications/modules/). To check witch versions are available, run `module avail relion`. To see specific notes about a particular install, you can use `module help`, e.g. `module help RELION/3.0.5-fosscuda-2018b` . 

#### Example Job Parameters

RELION reserves one worker (slurm task) for orchestrating an MPI-based job, which they call the "master". This can lead to inefficient jobs where there are tasks that could be using a GPU but are stuck being the master process. You can request a better layout for your job with a [heterogenous job](https://slurm.schedmd.com/heterogeneous_jobs.html), allocating CPUs on a cpu-only compute node for the task that will not use GPUs. Here is an example 3D refinement job submission script (replace `choose_a_version` with the version you want to use):

``` bash
#!/bin/bash
#SBATCH --partition=general --ntasks 1 -c2 --job-name=class3D_hetero_01 --mem=10G --output="class3D_hetero_01-%j.out"
#SBATCH hetjob
#SBATCH --partition=gpu --ntasks 4 -c2 -N1 --mem-per-cpu=16G --gpus-per-task=1 

module load RELION/choose_a_version

srun --pack-group=0,1 relion_refine_mpi --o hetero/refine3D/job0001 ... --dont_combine_weights_via_disc --j ${SLURM_CPUS_PER_TASK} --gpu
```

This job submission request will result in RELION using a single task/worker on a general purpose CPU node, and efficiently find four GPUs even if they aren't all available on the same compute node. Each GPU node task/worker will have a dedicated GPU, two CPU cores, and 30GiB total memory. 

### EMAN2

EMAN2 has always been a bit of a struggle for us to install properly on the clusters. Below are a few options

#### Conda Install

The EMAN2 authors offer some instructions on how to get EMAN2 running in a cluster environment on [their install page](https://blake.bcm.edu/emanwiki/EMAN2/Install/BinaryInstallAnaconda/2.3#Linux_Clusters). The default install may work as well if you avoid using MPI.

#### Container

 At present, we have a mostly working [apptainer container](/clusters-at-yale/guides/containers/) for EMAN2.3 available here: 

`/gpfs/ysm/datasets/cryoem/eman2.3_ubuntu18.04.sif`

To run a program from EMAN2 using this container you would use a command like:

``` bash
singularity exec /gpfs/ysm/datasets/cryoem/eman2.3_ubuntu18.04.sif e2projectmanager.py
```
### Cryosparc

We have a [whole separate page](/clusters-at-yale/guides/cryosparc/) about this one, it is a bit involved.

### Other Software

We have CCP4, Phenix and some other [software modules](/clusters-at-yale/applications/modules.md) of interest installed. Run `module avail` and the software name to search for them. If you can't find one you need, please [contact us](/#get-help).
