# MATLAB

## MATLAB GUI

If you wish to use the MATLAB GUI, we recommend our web portal, [Open OnDemand](/clusters-at-yale/access/ood). Once logged in, select "MATLAB" from the "Interactive Apps" dropdown.

## Command Line MATLAB

### Find MATLAB

Run one of the commands below, which will list available versions and the corresponding module files:

```
module spider matlab
```

Load the appropriate module file. For example, to run version R2019a:

```
module load MATLAB/2019a
```

The module load command sets up your environment, including the PATH to find the proper version of the MATLAB program.

### Run MATLAB

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

## Using More than 12 Cores with Matlab

In Matlab, 12 workers is a poorly documented default limit (seemingly for historical reasons) when setting up the parallel environment. You can override it by explicitly setting up your parpool before calling parfor or other parallel functions.

```
parpool(feature('NumCores'));
```

