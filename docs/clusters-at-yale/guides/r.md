# R

## Load R

### Conda-based R Environments

We recommend setting up your own R installation using Conda so you can manage your own packages and dependencies. 
You can find detailed instructions on our [Conda page](/clusters-at-yale/guides/conda).
The conda package repository has many (though not all) of the common R packages that can be installed with the typical conda syntax:

```sh
# Source the conda environment
$ source activate my_r_env

# Install the lattice package (r-lattice) from the r channel (-c r)
(my_r_env)$ conda install -c r r-lattice 

```
If there are packages that conda does not provide, you can install them locally from within R using the `install.packages` function.
To install a package (`lattice` for example) directly, simply run:

```sh
$ module load Tools/miniconda
$ source activate my_r_env
(my_r_env)$ R

> install.packages("lattice", repos="http://cran.r-project.org")

```

Each conda environment manages a unique `$R_LIBS` directory so that there is no conflict between installations.

### System Environment

We also provide a basic R installing on some of the clusters which you can use. However, if you find it is missing packages you need, we recommend setting up your own environment as described above.

Run one of the commands below, which will list available versions and the corresponding module files:

``` bash
module avail R
```

Load the appropriate module file. For example, to run version 3.4.1:

``` bash
module load  R/3.4.1-foss-2016b
```

The module load command sets up your environment, including the PATH to find the proper version of R.

This installation includes the most commonly used packages, but if something specific is required, packages can be installed into your local space.
To get started load the R module and start R:

```bash
$ module load R/3.4.1-foss-2016b
$ R
> install.packages("lattice", repos="http://cran.r-project.org")

```

This will throw a warning like:

```bash
Warning in install.packages("lattice") :
'lib = "/ysm-gpfs/apps/software/R/3.4.1-foss-2016b/lib64/R/library"' is not writable
Would you like to create a personal library
~/R/x86_64-unknown-linux-gnu-library/3.3
to install packages into?  (y/n) 
```

This will install the `lattice` package locally and will then be available to load into an R session.


## Run R

To run R, launch it using the `R` command.

``` bash
# launch an R session
R
# or to launch a script
R --slave -f myscript.R
```



!!!warning
    The R program is too large to fit on a login node. If you try to run it there, it will crash. Instead, launch it in an interactive or batch job (see below).

### Interactive Job

To run R interactively, you need to launch an interactive session on a compute node. For example

``` bash
srun --pty -p interactive -t 4:00:00 bash
```

Once your interactive session starts, you can load the appropriate module file and start R as described above.

See our [Slurm documentation](/clusters-at-yale/job-scheduling) for more detailed information on requesting resources for interactive jobs.

### Batch Mode

To run R in batch mode, you create a [batch script](/clusters-at-yale/job-scheduling). In that script, you would invoke your R script in batch mode.

``` bash
#!/bin/bash
#SBATCH -J my_r_program

R --slave -f myscript.R
```
