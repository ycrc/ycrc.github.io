# R

[R](https://www.r-project.org/about.html) is a free software environment for statistical computing and graphics.
On the Yale Clusters there are a couple ways in which you can set up your R environment.
There is no R executable provided by default; you have to choose one of the following methods to be able to run R.

## The R Module

We provide several versions of R as [software modules](/clusters-at-yale/applications/modules).
These modules provide a broad selection of commonly used packages pre-installed.
Notably, this includes a number of geospatial packages like `sf`, `sp`, `raster`, and `terra`.

In addition, there are software modules containing extra R packages including `Seurat` ([homepage](https://satijalab.org/seurat/)) and the `bioconductor` collection of bioinformatics packages ([homepage](https://www.bioconductor.org)).
These can be loaded in addition to their matching R module to provide simple access to these tools.

### Find and Load R

Find the available versions of R version 4 with:

``` bash
module avail R/4
```

To load version 4.1.0:

``` bash
module load R/4.1.0-foss-2020b
```

To show installed R packages and their versions for the `R/4.1.0` module:

``` bash
module help R/4.1.0-foss-2020b
```

To list the available versions of the `Bioconductor` or `Seurat` modules:

```bash
module avail Bioconductor

module avail Seurat
```

To load the `Seurat` module:

```bash
module load Seurat/4.1.0-foss-2020b-R-4.1.0

```

which will also load the `R/4.1.0-foss-2020b` module as a dependency.

### Install Packages

The software modules include many commonly used packages, but you can install additional packages specifically for your account.
As part of the R software modules we define an environment variable which directs R to install packages to your project space.
This helps prevent issues where R cannot install packages due to home-space quotas.
To change the location of where R installs packages, the `R_LIBS_USER` variable can be set in your `~/.bashrc` file:

```
export R_LIBS_USER=$LOOMIS_PROJECT/R/%v
```

where `%v` is a placeholder for the R major and minor version number (e.g. `4.1`).
R will replace this variable with the correct value automatically to segregate packages installed with different versions of R.

We recommend you install packages in an [interactive job](/clusters-at-yale/job-scheduling/#interactive-jobs) with the slurm option `-C oldest`.
This will ensure the compiled portions of your R library are compatible with all compute nodes on the cluster.
If there is a missing library your package of interest needs you should be able to load its module.
If you cannot find a dependency or have trouble installing an R package, [please get in touch with us](/#web-and-email-support).

!!! warning
    Grace's login nodes have newer architecture than the oldest nodes on the cluster. Always install packages in an interactive job submitted with the `-C oldest` Slurm flag if you want to ensure your code will work on all generations of the compute nodes.

To get started load the R module and start R:

```bash
srun --pty -C oldest -p interactive bash
module load R/4.1.0-foss-2020b
R
# in R
> install.packages("lattice", repos="http://cran.r-project.org")
```

This will throw a warning like:

```bash
Warning in install.packages("lattice") :
'lib = "/ysm-gpfs/apps/software/R/4.1.0-foss-2020b/lib64/R/library"' is not writable
Would you like to create a personal library
/gpfs/loomis/project/support/tl397/R/4.1
to install packages into?  (y/n)
```


!!!note
    If you encounter a permission error because the installation does not prompt you to create a personal library, create the directory in the default location in your home directory for the version of R you are using; e.g.,
    ```
    mkdir /path/to/your/project/space/R/4.1
    ```
    You only need the general minor version such as 4.0 instead of 4.0.3.

You can customize where packages are installed and accessed for a particular R session using the .libPaths function in R:
```
# List current package locations
> .libPaths()

# Add new default location to the standard defaults, e.g. project/my_R_libs
> .libPaths(c("/home/netID/project/my_R_libs/", .libPaths()))
```


## Run R

We will kill R jobs on the login nodes that are using excessive resources.
To be a good cluster citizen, launch your R computation in jobs.
See our [Slurm documentation](/clusters-at-yale/job-scheduling) for more detailed information on submitting jobs.

### Interactive Job

To run R interactively, first launch an interactive job on a compute node.
If your R sessions will need up to 10 GiB of RAM and up to 4 hours, you would submit you job with:

``` bash
srun --pty -p interactive --mem=10G -t 4:00:00 bash
```

Once your interactive session starts, you can load the appropriate module or Conda environment (see above) and start R by entering `R` on your command prompt. If you are happy with your R commands, save them to a file which can then be submitted and run as a batch job.

### Batch Mode

To run R in batch mode, create a plain-text batch script to submit.
In that script, you can run your R script. In this case `myscript.R` is in the same directory as the batch script, batch script contents shown below.

``` bash
#!/bin/bash
#SBATCH -J my_r_program
#SBATCH --mem=10G
#SBATCH -t 4:00:00

module load R/4.1.0-foss-2020b
R --slave -f myscript.R
```

To actually submit the job, run `sbatch my_r_job.sh` where the batch script above was saved as `my_r_job.sh`.

### RStudio

You can run RStudio app via [Open Ondemand](/clusters-at-yale/access/ood/#interactive-apps).
Here you can select the desired version of R and RStudio and launch an interactive compute session.

### Parallel R

On a cluster you may want to use R in parallel across multiple nodes.
While there are a few different ways this can be achieved, we recommend using the R software module which already includes `Rmpi`, `parallel`, and `doMC`.


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
module load R/4.1.0-foss-2020b

srun R --slave -f ex1.R
```

This script should execute a simple broadcast and complete in a few seconds.


## Virtual Display Session

It is common for R to require a display session to save certain types of figures.
You may see a warning like "unable to start device PNG" or "unable to open connection to X11 display".
There is a tool, `xvfb`, which can help avoid these issues.

The wrapper `xvfb-run` creates a virtual display session which allows R to create these figures without an X11 session.
See the guide for [xvfb](/clusters-at-yale/guides/xvfb) for more details.


## Conda-based R Environments

If there isn't a module available for the version of R you want, you can set up your own R installation using [Conda](/clusters-at-yale/guides/conda).
With Conda you can manage your own packages and dependencies, for R, Python, etc.

Most of the time the best way to install R packages for your Conda R environment is via `conda`.

``` bash
# load miniconda
module load miniconda
# create the conda environment including r-base and r-essentials package collections
conda create --name my_r_env r-base r-essentials
# activate the environment
conda activate my_r_env

# Install the lattice package (r-lattice)
conda install r-lattice

```

If there are packages that conda does not provide, you can install using the `install.packages` function, but this may occasionally not work as well.
When you install packages with `install.packages` make sure to activate your Conda environment first.

``` bash
srun --pty -C oldest -p interactive bash
module load miniconda
source activate my_r_env
R
# in R
> install.packages("lattice", repos="http://cran.r-project.org")
```

!!!warning
    Conda-based R may not work properly with parallel packages like `Rmpi` when running across multiple compute nodes.
    In general, it's best to use the module installation of R for anything which requires MPI.
