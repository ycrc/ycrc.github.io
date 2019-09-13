# MATLAB

## Find MATLAB

Run one of the commands below, which will list available versions and the corresponding module files:

```
module spider matlab
```

Load the appropriate module file. For example, to run version R2014a:

```
module load MATLAB/2014a
```

The module load command sets up your environment, including the PATH to find the proper version of the MATLAB program.

## Run MATLAB

!!!warning
    The MATLAB program is too large to fit on a login node. If you try to run it there, it will crash. Instead, launch it in an interactive or batch job (see below).

To launch MATLAB, using `matlab` command.

```
# launch the MATLAB GUI
matlab
# or launch the MATLAB command line prompt
maltab -nodisplay
# or to launch a script
matlab -nodisplay < runscript.m
```

### Interactive Job

To run Matlab interactively, you need to create an interactive session on a compute node.

You could start an interactive session using 4 cores on 1 node using something like

```
srun --pty --x11 -c 4 -p interactive -t 4:00:00 bash

```

Once your interactive session starts, you can load the appropriate module file and start Matlab as described above.

See our [Slurm documentation](/clusters-at-yale/job-scheduling) for more detailed information on requesting resources for interactive jobs.

### Batch Mode (without a GUI)

Create a batch script containing both instructions to the scheduler and shell instructions to set up directories and start Matlab. At the point you wish to start Matlab, use a command like:

```
matlab -nodisplay -nosplash -r YourFunction < /dev/null

```

This command will run the contents of YourFunction.m. Your batch submission script must either be in or `cd` to the directory containing YourFunction.m for this to work.

Below is a sample batch script to run Matlab in batch mode on Grace. If the name of the script is runit.sh, you would submit it using

```
sbatch  runit.sh
```

Here's a script for Grace:

```
#!/bin/bash
#SBATCH -J myjob
#SBATCH -c 4
#SBATCH -t 24:00:00
#SBATCH -p day

module load MATLAB/2016b
matlab -nodisplay -nosplash -r YourFunction < /dev/null

```

Unless you specify otherwise (using > redirects), both output and error logs will show up in the slurm-jobid.out log file in the same directory as your submission script.

### Using More than 12 Cores with Matlab

In Matlab, 12 workers is a poorly documented default limit (seemingly for historical reasons) when setting up the parallel environment. You can override it by explicitly setting up your parpool before calling parfor or other parallel functions.

```
parpool(feature('NumCores'));
```

## Matlab Distributed Computing Engine (MDCE)

The Matlab Distributed Computing Engine (MDCE) allows users to run parallel Matlab computations over multiple cluster compute nodes. To run parallel Matlab computations on any number of cores of a single compute node, please use ordinary Matlab (not MDCE) as described above to avoid tying up our limited number of licenses for MDCE.

MDCE is installed on all the HPC clusters, and we provide scripts to make it easy to use. Currently, our license for MDCE is restricted to a total of 32 concurrent labs per cluster (aggregated over all jobs using MDCE on the cluster), plus an additional 128 licenses that float and are available on any of the clusters when the cluster-specific licenses are already in use.

### Use (MDCE)

The first step required for use of MDCE is to develop a parallel Matlab program using the Parallel Computing Toolbox (PCT). The PCT allows you to run parallel computations on a single node. When used with MDCE, the PCT can enable you to run your computation across multiple nodes. In most cases, before running on multiple nodes, you should develop and test your algorithm on a single node using multiple cores.

For the single-node case, you simply run ordinary Matlab as described above (either interactively or in batch mode) and make use of the PCT commands using the "local" cluster configuration. This capability is enabled for any Matlab invocation on any of the clusters, and there are no limitations on the number of concurrent PCT users in this case. If you intend to run on a single node, therefore, please do not use MDCE, since that would consume some of our limited quantity of multi-node MDCE licenses.

For the multi-node case, you must run an MDCE server that is private to your job. We provide a script (yale_mdce_start.sh) that starts the server and the Matlab workers (known as "labs") for you. The yale_mdce_start.sh script has parameters that allow you to control the number of labs on each node, subject to license availability. (For details, see the comments in the file runit.sh shown later on this page.) The MDCE server will be terminated automatically when your cluster job ends, though we also provide a script (yale_mdce_stop.sh) to terminate it earlier if you wish. The yale_mdce scripts will be in your PATH once you have loaded a Matlab module file (e.g., MATLAB/2016b). To use the yale_mdce_start.sh script, you need to load module files for both Matlab and OpenMPI (see the runit.sh script below for an example).

We have also developed a template batch script (runit.sh) that you can submit to the job scheduler to run your parallel Matlab program. The script loads module files, invokes yale_mdce_start.sh, and then runs Matlab in batch mode. You can copy the template and and customize it to meet your needs. If you prefer to run interactively, you can start an ordinary multi-node interactive session (similar to what's shown above) and run the setup commands in runit.sh by hand.

### Example Submission Script (for Slurm)

```
#!/bin/bash

#SBATCH -J MDCE_JOB
#SBATCH --ntasks=25
#SBATCH --time=24:00:00
#SBATCH --partition=day

# Load Matlab and MPI module files
module load MATLAB/2016b OpenMPI/2.1.2-GCC-6.4.0-2.28

# Invoke yale_mdce_start.sh to set up a job manager and MDCE server
# Note: yale_mdce_start.sh and runscript.m are in the MDCE_SCRIPTS subdirectory of the root Matlab directory (e.g., /home/apps/fas/Apps/Matlab on Omega).
#       The MDCE_SCRIPTS directory is added to your PATH by the Matlab module file loaded above.

# Options for yale_mdce_start.sh:

# -jmworkers: number of labs to run on same node as the job manager.
# "-jmworkers NN" runs NN labs on job manager node
# "-jmworkers -1" run 1 fewer than labs than the number of cores allocated on the node
# Default: -1

# -nodeworkers: number of labs to run on nodes other than the job manager node.
# "-nodeworkers NN" runs NN labs on each node
# "-nodeworkers -1" run same number of labs as the number of cores allocated on each node
# Default: -1

yale_mdce_start.sh -jmworkers -1 -nodeworkers -1

export MDCE_JM_NAME=`cat MDCE_JM_NAME`

# invoke either runscript.m or your own M-file
# (You need to modify runscript.m first to run your computations!!)

# runscript.m uses the parallel cluster created by yale_mdce_start.sh.

matlab -nodisplay < runscript.m


```

### Example runscript.m

```
clear

% CD TO PROPER DIRECTORY HERE, IF NECESSARY

% FOLLOWING ASSUMES USE OF STANDARD YALE MDCE STARTUP SCRIPT
p=parallel.cluster.MJS('Name',getenv('MDCE_JM_NAME'))
nw = p.NumIdleWorkers
ppool=p.parpool(nw)
ppool.NumWorkers

% INVOKE YOUR OWN SCRIPT HERE

ppool.delete
exit
```