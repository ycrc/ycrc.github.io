# MPI Parallelism with Python

!!!note
    Before venturing into MPI-based parallelism, consider whether your work can be resturctured to make use of [dSQ](/clusters-at-yale/job-scheduling/dsq/) or more "embarrassingly parallel" workflows.
    MPI can be thought of as a "last resort" for parallel programming.

There are many computational problems that can be have increased performance by running pieces in parallel. 
These often require communication between the different steps and need a way to send messages between processes.

Examples of this include simulations of galaxy formation and electric field simulations, analysis of a single large dataset, or complex `search` or `sort` algorithms.

## MPI and `mpi4py`

There is a standard protocol, called `MPI`, that defines how messages are passed between processes, including one-to-one and broadcast communications.

The Python module for this is called `mpi4py`:

[mpi4py Read The Docs](https://mpi4py.readthedocs.io/en/stable/)

_Message Passing Interface implemented for Python._

> Supports point-to-point (sends, receives) and collective (broadcasts, scatters, gathers) communications of any picklable Python object, as well as optimized communications of Python object exposing the single-segment buffer interface (NumPy arrays, builtin bytes/string/array objects)

We will go over a few simple examples here.


## Definitions

`COMM`: The communication "world" defined by MPI

`RANK`: an ID number given to each internal process to define communication

`SIZE`: total number of processes allocated



`BROADCAST`: One-to-many communication

`SCATTER`: One-to-many data distribution

`GATHER`: Many-to-one data distribution


## Installing mpi4py


On the clusters, the easiest way to install `mpi4py` is to use the module-based software for OpenMPI and Python:

    module load Python/3.8.6-GCCcore-10.2.0 OpenMPI/4.0.5-GCC-10.2.0

Then `mpi4py` can be installed using `pip`:

    pip install --user mpi4py

 This will ensure that `mpi4py` can properly communicate with Slurm and will know the layout of resources allocated.

For operation on personal machines, `mpi4py` can be installed via `conda` which installs all dependences (including MPI):

    conda create --name mpi python=3.8 mpi4py numpy scipy

!!! warning
    Conda-based MPI does not work on the cluster due to the complexity of MPI interfacing with Slurm. Make sure to use the software modules as discussed above for anything on the cluster.

## Cluster Resource Requests

MPI utilizes Slurm tasks as the individual parallel workers. 
Therefore, when requesting resources (either interactively or in batch-mode) the number of tasks will determine the number of parallel workers (or to use MPI's language, the `SIZE` of the `COMM World`).

To request four tasks (each with a single CPU) interactively run the following:

    srun --pty -p day --cpus-per-task=1 --ntasks=4 bash

This can also be achieved in batch-mode like this:

    #SBATCH --partition Display
    #SBATCH --cpus-per-task=1
    #SBATCH --ntasks=4

A more detailed discussion of resource requests can be found [here](/clusters-at-yale/job-scheduling/resource-requests/) and further examples are available [here](/clusters-at-yale/job-scheduling/slurm-examples/)

## Examples

### Ex 1: Rank

This is a simple example where each worker reports their `RANK` and the process ID running that particular task.

```python
from mpi4py import MPI

# instantize the communication world
comm = MPI.COMM_WORLD

# get the size of the communication world
size = comm.Get_size()

# get this particular processes' `rank` ID
rank = comm.Get_rank()

PID = os.getpid()

print(f'rank: {rank} has PID: {PID}')
```

We then execute this code (named `mpi_simple.py`) by running the following on the command line:

    mpirun -n 4 python mpi_simple.py

The `mpirun` command is a wrapper for the MPI interface.

Then we tell that to set up a `COMM_WORLD` with 4 workers.

Finally we tell `mpirun` to run `python mpi_simple.py` on each of the four workers.

Which outputs the following:

    rank: 0 has PID: 89134
    rank: 1 has PID: 89135
    rank: 2 has PID: 89136
    rank: 3 has PID: 89137


### Ex 2: Point to Point Communicators

The most basic communication operators are "`send`" and "`recv`". These can be a bit tricky since they are "blocking" commands and can cause the program to hang.

    comm.send(obj, dest, tag=0)
    comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=None)
- `tag` can be used as a filter
- `dest` must be a rank in the current communicator
- `source` can be a rank or a wild-card (`MPI.ANY_SOURCE`)
- `status` used to retrieve information about recv'd message

We now we create a file (`mpi_comm.py`) that contains the following:

```python
from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    msg = 'Hello, world'
    comm.send(msg, dest=1)
elif rank == 1:
    s = comm.recv()
    print(f"rank {rank}: {s}")

```

When we run this on the command line (`mpirun -n 4 python mpi_comm.py`) we get the following:

    rank 1: Hello, world


The `RANK=0` process sends the message, and the `RANK=1` process receives it. The other two processes are effectively bystanders in this example.

### Ex 3: Broadcast

Now we will try a slightly more complicated example that involves sending messages and data between processes.
```python
# Import MPI
from mpi4py import MPI

# Define world
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Create some data in the RANK_0 worker
if rank == 0:
    data = {'key1' : [7, 2.72, 2+3j], 'key2' : ( 'abc', 'xyz')}
else:
    data = None

# Broadcast the data from RANK_0 to all workers
data = comm.bcast(data, root=0)

# Append the RANK ID to the data
data['key1'].append(rank)

# Print the resulting data
print(f"Rank: {rank}, data: {data}")
```

We then execute this code (named `mpi_message.py`) by running the following on the command line:

    mpirun -n 4 python mpi_message.py


Which outputs the following:

    Rank: 0, data: {'key1': [7, 2.72, (2+3j), 0], 'key2': ('abc', 'xyz')}
    Rank: 2, data: {'key1': [7, 2.72, (2+3j), 2], 'key2': ('abc', 'xyz')}
    Rank: 3, data: {'key1': [7, 2.72, (2+3j), 3], 'key2': ('abc', 'xyz')}
    Rank: 1, data: {'key1': [7, 2.72, (2+3j), 1], 'key2': ('abc', 'xyz')}

### Ex 4: Scatter and Gather

An effective way of distributing computationally intensive tasks is to `scatter` pieces of a large dataset to each task. The separate tasks perform some analysis on their chunk of data and then the results are `gathered` by `RANK_0`.

This example takes a large array of random numbers and splits it into pieces for each task. These smaller datasets are analyzed (taking an average in this example) and the results are returns to the main task with a `Gather` call.

```python

# import libraries
from mpi4py import MPI
import numpy as np

# set up MPI world
comm = MPI.COMM_WORLD
size = comm.Get_size() # new: gives number of ranks in comm
rank = comm.Get_rank()

# generate a large array of data on RANK_0
numData = 100000000 # 100milion values each
data = None
if rank == 0:
    data = np.random.normal(loc=10, scale=5, size=numData)

# initialize empty arrays to receive the partial data
partial = np.empty(int(numData/size), dtype='d')

# send data to the other workers
comm.Scatter(data, partial, root=0)

# prepare the reduced array to receive the processed data
reduced = None
if rank == 0:
    reduced = np.empty(size, dtype='d')

# Average the partial arrays, and then gather them to RANK_0
comm.Gather(np.average(partial), reduced, root=0)

if rank == 0:
    print('Full Average:',np.average(reduced))
```

This is executed on the command line:

    mpirun -n 4 python mpi/mpi_scatter.py

Which prints:

    Full Average: 10.00002060397186

## Key Take-aways and Further Reading

1. `MPI` is a powerful tool to set up communication worlds and send data and messages between workers
2. The `mpi4py` module provides tools for using MPI within Python.
3. This is just the beginning, `mpi4py` can be used for so much more...

To learn more, take a look at the `mpi4py` tutorial [here](https://mpi4py.readthedocs.io/en/stable/tutorial.html).


