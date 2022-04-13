# MATLAB

## MATLAB GUI

To use the MATLAB GUI, we recommend our web portal, [Open OnDemand](/clusters-at-yale/access/ood). Once logged in, click MATLAB pinned on the dashboard, or select "MATLAB" from the "Interactive Apps" list.

## Command Line MATLAB

### Find MATLAB

Run one of the commands below, which will list available versions and the corresponding module files:

```
module avail matlab
```

Load the appropriate module file. For example, to run version R2021a:

```
module load MATLAB/2021a
```

The module load command sets up your environment, including the PATH to find the proper version of the MATLAB program.

### Run MATLAB

!!!warning
    If you try to run MATLAB on a login node, it will likely crash. Instead, launch it in an interactive or batch job (see below).

### Interactive Job (without a GUI)

To run MATLAB interactively, you need to create an interactive session on a compute node.

You could start an interactive session using 4 cores, 16GiB of RAM for 4 hours with:

``` batch
srun --pty -c 4 --mem 16G -p interactive -t 4:00:00 bash
```

Once your interactive session starts, you can load the appropriate module file and start MATLAB

```
module load MATLAB/2021a

# launch the MATLAB command line prompt
maltab -nodisplay

# launch a script on the command line
matlab -nodisplay < runscript.m

```

See our [Slurm documentation](/clusters-at-yale/job-scheduling) for more detailed information on requesting resources for interactive jobs.

### Batch Mode (without a GUI)

Create a batch script with the [resource requests](/clusters-at-yale/job-scheduling/resource-requests) appropriate to your MATLAB function(s) and script(s). In it load the MATLAB module version you want, then run `matlab` with the `-b` option and your function/script name. Here is an example that requests 4 CPUs and 18GiB of memory for 8 hours: 

```
#!/bin/bash
#SBATCH --job-name myjob
#SBATCH --cpus-per-task 4
#SBATCH --mem 18G
#SBATCH -t 8:00:00

module load MATLAB/2021a
# assuming you have your_script.m in the current directory
matlab -b "your_script"

# if using MATLAB older than R2019a
# matlab -nojvm -nodisplay -nosplash < your_script.m

```

## Using More than 12 Cores with MATLAB

In MATLAB, 12 workers is a poorly documented default limit (seemingly for historical reasons) when setting up the parallel environment. You can override it by explicitly setting up your parpool before calling parfor or other parallel functions.

```
parpool(feature('NumCores'));
```

