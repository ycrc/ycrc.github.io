# Common Job Failures

Your jobs haven't failed, you have just found ways to run them that won't work. Here are some common error messages and steps to correct them.

## Memory Limits

Jobs can fail due to an insufficient memory being requested. Depending on the job, this failure might present as a Slurm error:

```
slurmstepd: error: Detected 1 oom-kill event(s).
Some of your processes may have been killed by the cgroup out-of-memory handler.
```

This means Slurm detected the job hitting the maximum requested memory and then the job was killed.

When process inside a job tries to access memory outside what was allocated to that job (more than what you requested) the operating system tells your program that address is invalid with the fault `Bus Error`. A similar fault you might be more familiar with is a `Segmentation Fault`, which usually results from a program incorrectly trying to access a valid memory address.

These errors can be fixed in two ways.

### Request More Memory

The default is almost always `--mem-per-cpu=5G`

In a batch script:

``` bash
#SBATCH --mem-per-cpu=8G
```

In an interactive job:

``` bash
srun --pty -p interactive --mem-per-cpu=8G
```

### Use Less Memory

This method is usually a little more involved, and is easier if you can inspect the code you are using. Watching your [job's resource usage](/clusters-at-yale/job-scheduling/resource-usage), attending [a workshop](https://research.computing.yale.edu/training/writing-efficient-r-code), or [getting in touch](/#get-help) with us are good places to start.

## Disk Quotas

Since the clusters are shared resources, we have quotas in place to enforce fair use of storage. More details about quotas can be found [here](/clusters-at-yale/data/cluster-storage/). When you or your group reach a quota, you can't write to existing files or create new ones. Any jobs that depend on creating or writing files that count toward the affected quota will fail. To inspect your current usage, run the command `getquota`. Remember, your home quota is yours but your project, scratch60, and any purchased storage quotas are shared across your group.

### Archive Files

You may find that some files or direcories for previous projects are no longer needed on the cluster. We recommend you [archive these](/data/archive/) to recover space.

### Delete Files

If you are *_sure_* you no longer need some files or direcories, you can delete them. Unless files are in your home directory (not `project` or `scratch60`) they are not backed up and may be unrecoverable. Use the [`rm -rf`](https://thenextweb.com/media/2012/05/21/how-pixars-toy-story-2-was-deleted-twice-once-by-technology-and-again-for-its-own-good) command very carefully.

### Buy More Space

If you would like to purchase more than the default quotas, we can help you [buy space on the clusters](/clusters-at-yale/data/cluster-storage/#get-more-storage).

## Software Modules

We build and organize [software modules](/clusters-at-yale/applications/modules) on the cluster using [toolchains](/clusters-at-yale/applications/easybuild/#toolchains). The major toolchains we use produce modules that end in foss-yearletter or intel-yearletter, *e.g.* `foss-2018b` or `intel-2018a`. If modules from different toolchains are loaded at the same time, the conflicts that arise often lead to errors or strange application behavior. Seeing either of the following messages is a sign that you are loading incompatible modules. 

```
The following have been reloaded with a version change:
  1) FFTW/3.3.7-gompi-2018a => FFTW/3.3.4-gompi-2016b
  2) GCC/6.4.0-2.28 => GCC/5.4.0-2.26
  3) GCCcore/6.4.0 => GCCcore/5.4.0
...
```

or

```
GCCcore/5.4.0 exists but could not be loaded as requested.
```

### Match or Purge Your Toolchains

Where possible, only use one toolchain at a time. When you want to use software from muliple toolchains run `module purge` between running new `module load` commands. If your work requires a version of software that is not installed, [contact us](/#get-help).

## Conda Environments

[Conda environments](/clusters-at-yale/guides/conda/) provide a nice way to manage `python` and `R` packages and modules. Conda acieves this by setting functions and environment variables that point to your environment files when you run `conda activate`. Unlike [modules](/clusters-at-yale/applications/modules/), conda environments are not completely forwarded into a job; having a conda environment loaded when you submit a job doesn't forward it well into your job. You will likely see messages about missing packages and libraries you definitely installed into the environment you want to use in your job.

### Load Conda Environments Right Before Use

To make sure that your environment is set up properly for interactive use, wait until you are on the host you plan to use your environment on. Then run `conda activate my_env`.

To make sure batch jobs function properly, only submit jobs without an environment loaded (`conda deactivate` before `sbatch`). Make sure you load miniconda and your environment in the body of your batch submission script.
