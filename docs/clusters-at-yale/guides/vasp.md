# VASP

NOTE: VASP requires a paid license. If you looking to use VASP, but your research group has not purchased a license, please do not use the cluster installations without first contacting [hpc@yale.edu](mailto:hpc@yale.edu). Thank you for your cooperation.

## VASP and Slurm

In Slurm, there is big difference between `--ntasks` and `--cpus-per-task` which is explained in our [Requesting Resources documentation](/clusters-at-yale/job-scheduling/resource-requests).

For the purposes of VASP, `--cpu-per-tasks` should always equal `NCORE` (in your INCAR file). Then `--ntasks` should be equal to the total number of cores you want, divided by `--cpu-per-tasks`.

VASP has two parameters for controlling processor layouts, `NCORE` and `NPAR`, but you only need to set one of them. If you set `NCORE`, you don’t need to set `NPAR`. Instead VASP will automatically set `NPAR` to `--ntasks`. So the formula should be:

In your mpirun line, you should specify the number of MPI tasks as:

``` bash
mpirun -n $SLURM_NTASKS vasp_std
```

You don’t need to specify `—nodes` unless you are trying to force the tasks on a certain number of nodes (which will likely increase you wait time with minimal speed up). But regardless, `--nodes` shouldn’t be part of the total number of cpu calculation.

### Cores Layout Examples

If you want 40 cores (2 nodes and 20 cpus per node):

in your submission script:

``` bash
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=20
```

``` bash
mpirun -n 2 vasp_std
```

in `INCAR`:

```
NCORE=20
```

You may however find that the wait time to get 20 cores on two nodes can be very long since cores request via `--cpus-per-task` can’t span multiple nodes. Instead you might want to try breaking it up into smaller chunks. Therefore, try:

in your submission script:

``` bash
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=10
```

``` bash
mpirun -n 4 vasp_std
```

in `INCAR`:

```
NCORE=10
```

which would likely spread over 4 nodes using 10 cores each and spend less time in the queue.

## Omega

On Omega, since cores are assigned as whole 8-core nodes, `NCORE` should always be equal to 8 and then you can just request `—ntasks` in multiples of 8.

in your submission script:

``` bash
#SBATCH --ntasks=16 # some multiple of 8
```

``` bash
mpirun -n $SLURM_NTASKS vasp_std
```

in `INCAR`:

```
NCORE=8
```

## Additional Reading

Here is some documentation on how to optimally configure NCORE and NPAR:

* [https://cms.mpi.univie.ac.at/wiki/index.php/NCORE](https://cms.mpi.univie.ac.at/wiki/index.php/NCORE)
* [https://cms.mpi.univie.ac.at/wiki/index.php/NPAR](https://cms.mpi.univie.ac.at/wiki/index.php/NPAR)
* [https://www.nsc.liu.se/~pla/blog/2015/01/12/vasp-how-many-cores/](https://www.nsc.liu.se/~pla/blog/2015/01/12/vasp-how-many-cores/)