# R

## Load R

Run one of the commands below, which will list available versions and the corresponding module files:

```
module avail R
```

Load the appropriate module file. For example, to run version 3.4.1:

```
module load  R/3.4.1-foss-2016b
```

The module load command sets up your environment, including the PATH to find the proper version of R.

## Run R

To run R, launch it using the `R` command.

```
# launch an R session
R
# or to launch a script
R --slave -f myscript.R
```

!!!warning
    The R program is too large to fit on a login node. If you try to run it there, it will crash. Instead, launch it in an interactive or batch job (see below).

### Interactive Job

To run R interactively, you need to launch an interactive session on a compute node. For example

```
srun --pty -p interactive -t 4:00:00 bash
```

Once your interactive session starts, you can load the appropriate module file and start R as described above.

See our [Slurm documentation](/clusters-at-yale/job-scheduling/slurm) for more detailed information on requesting resources for interactive jobs.

### Batch Mode

To run R in batch mode, you create a [batch script](/cluster-at-yale/job-scheduling/slurm). In that script, you would invoke your R script in batch mode.

```
#!/bin/bash
#SBATCH -J my_r_program

R --slave -f myscript.R
```

## Install Additional R Packages

Our R module has some of the most commonly used packages pre-installed, such as Rmpi. If you need additional R packages not already included, we recommend installing them into your own directories using the `install.package()` R function. Contact us at [hpc@yale.edu](mailto:hpc@yale.edu) if you run into issues.
