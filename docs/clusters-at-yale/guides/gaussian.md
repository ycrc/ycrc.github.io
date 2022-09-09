# Gaussian

!!! note 
    Access to Gaussian on the Yale clusters is free, but available by request only. To gain access to the installations of Gaussian, please [contact us](/#get-help) to be added to the `gaussian` group.

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
salloc -c 4 -t 4:00:00
```

See our [Slurm documentation](/clusters-at-yale/job-scheduling) for more detailed information on requesting resources for interactive jobs.

## GaussView

In connection with Gaussian 16, we have also installed GaussView 6, Gaussian Inc.'s most advanced and powerful graphical interface for Gaussian. With GaussView, you can import or build the molecular structures that interest you; set up, launch, monitor and control Gaussian calculations; and retrieve and view the results, all without ever leaving the application. GaussView 6 includes many new features designed to make working with large systems of chemical interest convenient and straightforward. It also provides full support for all of the new modeling methods and features in Gaussian 16.

In order to use GaussView, you must run an X Server on your desktop or laptop, and you must enable X forwarding when logging into the cluster. See our [X11 forwarding documentation](/clusters-at-yale/access/x11) for instructions.

Loading the module file for Gaussian sets up your environment for GaussView as well. Then you can start GaussView by typing the command `gv`. GaussView 6 may not be compatible with certain versions of the X servers you may run on your desktop or laptop. If you encounter problems, these can often be overcome by starting GaussView with the command `gv -mesagl` or `gv -soft`.
