# Submission Script Examples

In addition to those below, we have additional example submission scripts for [Parallel R, Matlab and Python](https://github.com/ycrc/ycrc_example_scripts).

## Single threaded programs (basic)

```
#!/bin/bash

#SBATCH --job-name=my_job
#SBATCH --time=10:00

./hello.omp
```

## Multi-threaded programs

```
#!/bin/bash

#SBATCH --job-name=omp_job
#SBATCH --output=omp_job.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=10:00

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
./hello.omp
```

## Multi-process programs

```
#!/bin/bash

#SBATCH --job-name=mpi
#SBATCH --output=mpi_job.txt
#SBATCH --ntasks=4
#SBATCH --time=10:00

mpirun hello.mpi
```

!!! tip
    On Omega, try to make ntasks equal to a multiple of 8.

## Hybrid (MPI+OpenMP) programs

```
#!/bin/bash

#SBATCH --job-name=hybrid
#SBATCH --output=hydrid_job.txt
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=5
#SBATCH --nodes=2
#SBATCH --time=10:00

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

mpirun hello_hybrid.mpi
```

## GPU job

```
#!/bin/bash

#SBATCH --job-name=deep_learn
#SBATCH --output=gpu_job.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --gres=gpu:k80:2
#SBATCH --partition=gpu
#SBATCH --gres-flags=enforce-binding
#SBATCH --time=10:00

module load CUDA
module load cuDNN
# using your anaconda environment
source activate deep-learn
python my_tensorflow.py
```
