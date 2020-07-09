# Common Job Failures

Though there are many types of work that happens on the clusters, there are a common set of reasons that many jobs fail to run successfully.
Here we will outline some of these common failure modes and detail steps to correcting them.

## Running out of memory
Jobs can often fail due to an insufficient amount of memory being requested.
Depending on the job, this failure might present in a SLURM error:

```
slurmstepd: error: Detected 1 oom-kill event(s).
Some of your processes may have been killed by the cgroup out-of-memory handler.
```
This is stating that SLRUM detected the job hitting the maximum requested memory and then the job was killed.

A program that runs out of memory can also crash generating a `Bus error (core dumped)`.
This error means that the program is attempting to access memory that it does not have permission to reach.

These errors can be fixed in two ways.
First is to increase the amount of memory that is requested from SLURM.
This can be done in an `sbatch` script:

```
#SBATCH --mem-per-cpu=10G
```
or on the command-line using `srun`:

```
srun --pty -p interactive --mem-per-cpus=10G
```

Alternatively, the code can be inspected to see if the program can reduce the amount of memory that is being used.
Further details about monitoring memory usage can be found [here](/clusters-at-yale/job-scheduling/resource-usage).

## Disk Quota Exceeded

Since the clusters are shared resources, we have quotas in place to prevent any group from using too much disk space.
More details about quotas can be found [here](/clusters-at-yale/data/cluster-storage/).
When a group or user reaches the quota, files cannot be created.
Additionally, existing files will not be able to be written to.
This will frequently kill jobs that need to write output or log files.

To inspect your quota, we have developed a tool called `getquota`:

```
$ getquota
This script shows information about your quotas on the current gpfs filesystem.
If you plan to poll this sort of information extensively, please contact us
for help at hpc@yale.edu

## Usage Details for hpcprog (as of Nov 20 2019 05:00)
Fileset       User  Usage (GiB) File Count
------------- ----- ---------- -------------
project       ahs3          82        33,788
project       cag94          0             1
project       kln26        366       533,998
project       njc2           0             1
project       pl543        115       259,212
project       tl397        370       529,026
----
scratch60     ahs3           0            89
scratch60     cag94          0             1
scratch60     kln26       2510       714,703
scratch60     njc2           0             1
scratch60     pl543          0             6
scratch60     tl397      13056       282,212

## Quota Summary for hpcprog (as of right now)
Fileset       Type    Usage (GiB)   Quota (GiB)  File Count    File Limit    Backup    Purged
------------- ------- ------------ ----------- ------------- ------------- --------- ---------
home.grace    USR               39         100       190,055       200,000 Yes        No
project       GRP              707        6144     1,611,981     5,000,000 No         No
scratch60     GRP             4054       20480       987,336     5,000,000 No         60 days

```
There are different quotas for `$HOME`, `$PROJECT`, and `$SCRATCH60`.
In addition to a disk usage quota (in GiB), there is a File Count quota that limits the number of files that can be created.
If your account is running into any of these quotas, jobs may not run successfully.

As the $HOME space is backed up, there is a much smaller quota for each user.
If your home-space is at max capacity, please investigate whether some files can be moved to `$PROJECT`.

## Loading modules from different toolchains

Software on the cluster is managed using *toolchains*.
These are collections of software tools that are all built using the same compilers to ensure that they work properly together.
If modules from different toolchains are loaded at the same time, conflicts can arise that lead to jobs not running successfully.

A sign that incompatible modules are being loaded is a print-out highlighting modules being 'reloaded':

```
[tl397@grace2 ~]$ module load STAR/2.6.0c-foss-2018a
[tl397@grace2 ~]$ module load TopHat/2.1.1-foss-2016b

The following have been reloaded with a version change:
  1) FFTW/3.3.7-gompi-2018a => FFTW/3.3.4-gompi-2016b
  2) GCC/6.4.0-2.28 => GCC/5.4.0-2.26
  3) GCCcore/6.4.0 => GCCcore/5.4.0
  4) OpenBLAS/0.2.20-GCC-6.4.0-2.28 => OpenBLAS/0.2.18-GCC-5.4.0-2.26-LAPACK-3.6.1
  5) OpenMPI/2.1.2-GCC-6.4.0-2.28 => OpenMPI/1.10.3-GCC-5.4.0-2.26
  6) ScaLAPACK/2.0.2-gompi-2018a-OpenBLAS-0.2.20 => ScaLAPACK/2.0.2-gompi-2016b-OpenBLAS-0.2.18-LAPACK-3.6.1
  7) binutils/2.28-GCCcore-6.4.0 => binutils/2.26-GCCcore-5.4.0
  8) foss/2018a => foss/2016b
  9) gompi/2018a => gompi/2016b
 10) hwloc/1.11.8-GCCcore-6.4.0 => hwloc/1.11.3-GCC-5.4.0-2.26
 11) numactl/2.0.11-GCCcore-6.4.0 => numactl/2.0.11-GCC-5.4.0-2.26
 12) zlib/1.2.11-GCCcore-6.4.0 => zlib/1.2.11-GCCcore-5.4.0
```
Here we first loaded a tool from the `foss-2018a` toolchain, but then loaded a module from the incompatible `foss-2016b` toolchain.

To ensure that your jobs run successfully, only use one toolchain at a time.
If your work requires a version of software that is not installed, email <research.computing@yale.edu> and we will work to help.

## Conda Environment

Conda environments provide a nice way to manage `python` and `R` packages and modules.
This is achieved by setting environmental variables that point to the `conda` environment directory.
However, when moving from the login node to a compute node through SLURM, these paths can get messed up.
This can lead to `python` not locating packages that are installed within an environment.

The `which` command can be used to identify which python executable is being located:
```
$ which python
/gpfs/loomis/apps/avx/software/miniconda/4.7.10/bin/python
```

If this doesn't point to the conda environment,  you may need to source the environment again.

To make sure that the environmental variables are correctly set up, avoid activating the conda environment on the login node.
Instead, wait until on a compute node to activate the environment or include the `source activate my_env` statement in the SBATCH submission script.
