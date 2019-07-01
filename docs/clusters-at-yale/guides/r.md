# R

## Load R

### Your Own R Environment

We recommend setting up your own R installation using Conda so you can manage your own packages and dependencies. You can find detailed instructions on our [Conda page](/cluster-at-yale/guides/conda).

### Installing Non-Conda Packages

If there are packages that you need that are not available via Conda, you can 
install them into your local space. We recommend using the `project` 
directory, since these files can get large. 

First, you will need to change the default install path:

```sh
export R_LIBS=$HOME/project/r_libs
mkdir $R_LIBS
```

Then you can launch your R installation and install packages 
(`lattice` for example) directly:

```sh
$ R

> install.packages("lattice", repos="http://cran.r-project.org")

```

Finally, make sure to add `export R_LIBS=$HOME/project/r_libs` to your .bashrc 
file to automatically load that variable every time you log in.

### System Environment

We also provide a basic R installing on some of the clusters which you can use. However, if you find it is missing packages you need, we recommend setting up your own environment as described above.

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

See our [Slurm documentation](/clusters-at-yale/job-scheduling) for more detailed information on requesting resources for interactive jobs.

### Batch Mode

To run R in batch mode, you create a [batch script](/clusters-at-yale/job-scheduling). In that script, you would invoke your R script in batch mode.

```
#!/bin/bash
#SBATCH -J my_r_program

R --slave -f myscript.R
```

