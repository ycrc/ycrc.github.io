# R

[R](https://www.r-project.org/about.html) is a free software environment for statistical computing and graphics. On the Yale Clusters there are a couple ways in which you can set up your R environment. There is no R executable provided by default; you have to choose one of the following methods to be able to run R.

## The R Module

We provide a R as a [software module](/clusters-at-yale/applications/modules). The R modules are the only way we currently support the RStudio app via [Open Ondemand](/clusters-at-yale/access/ood/#interactive-apps).

### Find and Load R

Find the available versions of R version 3 with:

``` bash
module avail R/3
```

To load version 3.6.1:

``` bash
module load R/3.6.1-foss-2018b
```

To show installed R packages and their versions for the `R/3.6.1-foss-2018b` module:

``` bash
module help R/3.6.1-foss-2018b
```

### Install Packages

The software modules include many commonly used packages, but you can install additional packages locally, _i.e._ to your home directory. We recommend you install packages in an [interactive job](/clusters-at-yale/job-scheduling/#interactive-jobs) with the slurm option `-C oldest`. This will ensure the compiled portions of your R library are compatible with all compute nodes on the cluster. If there is a missing library your package of interest needs you should be able to load its module. If you cannot find a dependency or have trouble installing an R package, [please get in touch with us](/#web-and-email-support).

To get started load the R module and start R:

```bash
srun --pty -C oldest -p interactive bash
module load R/3.6.1-foss-2018b
R
# in R
> install.packages("lattice", repos="http://cran.r-project.org")
```

This will throw a warning like:

```bash
Warning in install.packages("lattice") :
'lib = "/ysm-gpfs/apps/software/R/3.4.1-foss-2016b/lib64/R/library"' is not writable
Would you like to create a personal library
~/R/x86_64-unknown-linux-gnu-library/3.6
to install packages into?  (y/n)
```

This will install the `lattice` package to your `~/R/x86_64-unknown-linux-gnu-library/3.6` directory. There is a separate directory for R packages for each minor version of R, so packages installed with v 3.4 will not be visible from v 3.6.


## Conda-based R Environments

If there isn't a module available for the version of R you want, you can set up your own R installation using [Conda](/clusters-at-yale/guides/conda). With Conda you can manage your own packages and dependencies, for R, Python, etc.

### Install Conda Packages

Most of the time the best way to install R packages for your Conda R environment is via `conda`.

``` bash
# Source the conda environment
conda activate my_r_env

# Install the lattice package (r-lattice) from the r channel (-c r)
conda install r-lattice

```

If there are packages that conda does not provide, you can install using the `install.packages` function, but this may occasionally not work as well. When you install packages with `install.packages` Make sure to load your Conda environment first.

``` bash
srun --pty -C oldest -p interactive bash
module load miniconda
source activate my_r_env
R
# in R
> install.packages("lattice", repos="http://cran.r-project.org")
```

## Run R

We will kill R jobs on the login nodes that are using excessive resources. To be a good cluster citizen, launch your R computation in jobs. See our [Slurm documentation](/clusters-at-yale/job-scheduling) for more detailed information on submitting jobs.

### Interactive Job

To run R interactively, first launch an interactive job on a compute node. If your R sessions will need up to 10 GiB of RAM and up to 4 hours, you would submit you job with:

``` bash
srun --pty -p interactive --mem=10G -t 4:00:00 bash
```

Once your interactive session starts, you can load the appropriate module or Conda environment (see above) and start R by entering `R` on your command prompt. If you are happy with your R commands, save them to a file which can then be submitted and run as a batch job.

### Batch Mode

To run R in batch mode, create a plain-text batch script to submit. In that script, you can run your R script. In this case `myscript.R` is in the same directory as the batch script, batch script contents shown below.

``` bash
#!/bin/bash
#SBATCH -J my_r_program
#SBATCH --mem=10G
#SBATCH -t 4:00:00

module load R/3.6.1-foss-2018b
R --slave -f myscript.R
```

To actually submit the job, run `sbatch my_r_job.sh` where the batch script above was saved as `my_r_job.sh`.

### RStudio

You can run RStudio via X11 forwarding in an interactive job, but we recommend using the RStudio app via [Open Ondemand](/clusters-at-yale/access/ood/#interactive-apps) instead.

## Parallel R with Conda

On a cluster you may want to use R in parallel across multiple nodes. While there are a few different ways this can be achieved, we recommend using `conda` to set up a specific R environment with the required packages and libraries.

In particular, you will need `Rmpi`, `doMC`, and `doMPI`. The first two can be installed via conda, while the last one must be installed manually.

```bash
# load the miniconda module
module load miniconda

# create the environment with the required packages
conda create --name parallel_r r-base r-essentials r-doMC r-Rmpi

# activate the environment
conda activate parallel_r
```

This will produce an environment that is nearly ready to-go. 
The last step is to install `doMPI`, which at the moment is not available via `conda`.
We can use the `install.packages` method from within R to get this final piece:
```bash
(parallel_r) $ R
> install.packages('doMPI')
```
It's important that this last step is performed on a login node so that it doesn't interfere with 
the SLURM scheduler. 
Once this is complete, you should have a fully functional parallel-enabled R environment.

To test it, we can create a simple R script named `ex1.R`

```R
library("Rmpi")

n<-mpi.comm.size(0)
me<-mpi.comm.rank(0)

mpi.barrier(0)
val<-777
mpi.bcast(val, 1, 0, 0)
print(paste("me", me, "val", val))
mpi.barrier(0)

mpi.quit()

```

Then we can launch it with an sbatch script (`ex1.sh`):

```sh
#!/bin/bash

#SBATCH -n 4 -N 4 -t 5:00
#SBATCH --mail-type=none

module purge
module load miniconda

source activate parallel_r

mpirun R --slave -f ex1.R
```

This script should execute a simple broadcast and complete in a few seconds. 


