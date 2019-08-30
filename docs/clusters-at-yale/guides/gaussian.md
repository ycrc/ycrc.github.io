# Gaussian

[Gaussian](http://www.gaussian.com/) is an electronic structure modeling program that Yale has licensed for its HPC clusters. The latest version of Gaussian is Gaussian 16, which also includes GaussView 6. Older versions of both applications are also available. To see a full list of available versions of Gaussian on the cluster, run:

``` bash
module avail gaussian
```

## Running Gaussian on the Cluster

The examples here are for Gaussian 16. In most cases, you could run the older version Gaussian 09 by replacing "g16" with "g09" wherever it occurs.

When running Gaussian, it is recommended that users request exclusive access to allocated nodes (e.g., by requesting all the cpus on the node) and that they specify the largest possible memory allocation for the number of nodes requested. In addition, in most cases, the scratch storage location (set by the environment variable `GAUSS_SCRDIR`) should be on the local parallel scratch file system (e.g., scratch60)  of the cluster, rather than in the user’s home directory. (This is the default in the Gaussian module files.)

Before running Gaussian, you must set up a number of environment variables. This is accomplished most easily by loading the Gaussian module file using:

``` bash
module load Gaussian
```

To run Gaussian interactively, you need to create an interactive session on a compute node. You could start an interactive session using 4 cores for 4 hours using

``` bash
srun --pty -c 4  -p interactive -t 4:00:00 bash
```

See our [Slurm documentation](/clusters-at-yale/job-scheduling) for more detailed information on requesting resources for interactive jobs.

## Gaussian in Parallel

To run Gaussian in parallel, you may find it simplest to use the script `par_g16` instead of executing Gaussian directly. `par_g16` takes 1 optional argument and is used as shown here:

``` bash
par_g16 [num_proc_shared] < g16_input > g16_output
```

When included in a submission script, par_g16 will set the following Gaussian input variables:

`%LindaWorkers`: List of nodes that will act as parallel workers during parallel portions of the Gaussian computations. The list is created automatically based on the nodes allocated to the particular job. Workers communicate using the Network Linda system provided with the Gaussian software.

`%NProcShared`: Number of shared-memory processes per Linda worker.

It is highly recommended that users run 1 Linda worker per node with `%NProcShared=NN` where `NN` is the number of cpus requested per node. (The default is `%NProcShared=1`.) Of course, both variables may be overridden by including them in the Gaussian input file.)

On YCRC clusters, there are generally more than 20 processors and 128 GB of memory per node, so it may often work well to use a predetermined number of cores on a single node, in which case you can simply modify the Gaussian input file and skip the use of the `par_g16` script. If you do wish to use multiple nodes on the clusters, please pay careful attention to the [Slurm parameters](/clusters-at-yale/job-scheduling) you use (especially `--mem-per-cpu`) to ensure that each of the nodes you request has sufficient resources available.

## GaussView

In connection with Gaussian 16, we have also installed GaussView 6, Gaussian Inc.'s most advanced and powerful graphical interface for Gaussian. With GaussView, you can import or build the molecular structures that interest you; set up, launch, monitor and control Gaussian calculations; and retrieve and view the results, all without ever leaving the application. GaussView 6 includes many new features designed to make working with large systems of chemical interest convenient and straightforward. It also provides full support for all of the new modeling methods and features in Gaussian 16.

In order to use GaussView, you must run an X Server on your desktop or laptop, and you must enable X forwarding when logging into the cluster. See our [X11 forwarding documentation](/clusters-at-yale/access/x11) for instructions.

Loading the module file for Gaussian sets up your environment for GaussView as well. Then you can start GaussView by typing the command `gv`. GaussView 6 may not be compatible with certain versions of the X servers you may run on your desktop or laptop. If you encounter problems, these can often be overcome by starting GaussView with the command `gv -mesagl` or `gv -soft`.
