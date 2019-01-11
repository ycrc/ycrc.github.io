# Slurm

Slurm is used to submit jobs to a specified set of compute resources, which are variously called queues or partitions. Slurm uses the term partition. Partitions, their defaults, limits and purposes are listed on [each cluster page](/node/4093). To see more details about how jobs are scheduled see our [Job Scheduling documentation](/fairshare).

Please be a good cluster citizen. Do not run jobs on login nodes (e.g. grace1, farnam2), as these can impact the sessions and connectivity of everyone else on the cluster. We also sometimes find jobs on the clusters that allocate resources incorrectly for the job that is running. Please see our [Measuring Memory and CPU Usage](/node/3765) for examples of how to measure the resources your jobs use. If you find yourself wondering how best to schedule a job feel free to [email us](mailto:hpc@yale.edu?Subject=Job%20help) or come to [office hours](/node/4227). Efficient jobs help you get your work done faster and free resources for others as well.

### Common Slurm Commands

Submit a submission script (see below for details)

```
sbatch <script>
```

List queued and running jobs

```
squeue -u$USER
```

Cancel a queued job or kill a running job

```
scancel <job_id>
```

Check status of individual job (including failed or completed)

```
sacct -j <job_id>
```

<a name="interactive-jobs"></a>

### Interactive Jobs

Interactive jobs can be used for testing and troubleshooting code. By requesting an interactive job, you will be allocated resources and logged onto the node in a shell.

```
srun --pty -p interactive bash
```

This will assign a free node to you, allocating the requested number of CPUs, walltime, and memory, and put you within a shell on that node. You can run any number of commands within that shell. To free the allocated node, exit from the shell.

When using an interactive shell under slurm, your job is vulnerable to being killed if you lose your network connection. We recommend using [`tmux`](/node/12826) alleviate this. When using `tmux`, please be sure to keep track of your allocations and free those no longer needed!

To use a GUI application (such as Matlab), when in an interactive job, use the `--x11` flag:

```
srun --pty --x11 -p interactive [additional slurm options] bash
```

Note that for X11 forwarding to work, you need to have your local machine setup properly. Please see our [X11 setup guide](/node/3803) for more info.

<a name="batch-jobs"></a>

### Batch Jobs

To submit a job via Slurm, you first write a simple shell script called a "submission script" that wraps your job. A submission script is comprised of three parts:

1.  The program that should run the script. This is normally `#!/bin/bash`.
2.  The "directives" that tell the scheduler how to setup the computational resources for your job.**These lines must appear before any other commands or definitions, otherwise they will be ignored.**
3.  The actual "script" portion, which are the commands you want executed during your job.

Here is an example script.sh that runs a job on one CPU on single node:

```
#!/bin/bash
#SBATCH --partition=general
#SBATCH --job-name=my_job
#SBATCH --ntasks=1 --nodes=1
#SBATCH --mem-per-cpu=6000 
#SBATCH --time=12:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=_email_

./myprog -p 20 arg1 arg2 arg3 ...
```

### Directives

As shown in the above example, "directives" are comprised of `#SBATCH` followed by Slurm options. Most commonly used options include:

|Full Option|Abbreviated|Description|
|--- |--- |--- |
|`--job-name=name`|`-J name`|Custom job name|
|`--partition=name`|`-p partition`|Partition to run on|
|`--nodes=#`|`-N #`|Total number of nodes|
|`--ntasks=#`|`-n #`|Number of "tasks". For use with distributed parallelism. See below.|
|`--cpus-per-task=#`|`-c #`|# of CPUs allocated to each task. For use with shared memory parallelism.|
|`--ntasks-per-node=#`||Number of "tasks" per node. For use with distributed parallelism. See below.|
|`--time=[[DD-]HH:]MM:SS`|`-t [[DD-]HH:]MM:SS`|Maximum walltime of the job in Days-Hours:Minutes:Sec|
|`--constraint=node_type`|`-C node_type`|specific node architecture (if applicable)|
|`--mem-per-cpu=#`||Memory requested per CPU in MB|
|`--mem=#`||Memory requested per node in MB|
|`--mail-user=_email_`||Mail address (alternatively, put your email address in ~/.forward)|
|`--mail-type=ALL`||Send emails to user on all job events|

Additional options can be found on in the [official Slurm documentation](http://slurm.schedmd.com/documentation.html).

### Resource Limit Enforcement

Slurm uses the linux cgroup feature to enforce limits on CPUs, GPUs, and memory. Jobs are only permitted to run on a node if they have a valid allocation, and only within the limits specified by that limitation. Thus, if you request a single core from slurm (the default) and start a job that runs 20 parallel threads, those threads will be packed into a single CPU, and run very slowly. Similarly, if you do not explicitly request memory, your job will be granted a fairly modest default per CPU, and if your job attempts to exceed that amount, it will be killed.

<a name="requesting-cores-and-nodes"></a>

### Requesting Cores and Nodes

Slurm is very explicit in how one requests cores and nodes. While extremely powerful, the three flags, `--nodes`, `--ntasks`, and `--cpus-per-task` can be a bit confusing at first. We attempt to disambiguate them below.

#### `--ntasks` vs `--cpus-per-task`

The term "task" in this context can be thought of as a "process". Therefore, a multi-process program (e.g. MPI) is comprised of multiple tasks. And a multi-threaded program is comprised of a single task, which can in turn use multiple CPUs. In Slurm, tasks are requested with the `--ntasks` flag. CPUs, for the multithreaded programs, are requested with the `--cpus-per-task` flag.

#### 1\. Multi-threaded & multi-process programs

To request CPUs for your multi-threaded program, use the `--cpus-per-task` flag. Individual tasks cannot be split across multiple compute nodes, so requesting a number of CPUs with `--cpus-per-task` flag will always result in all your CPUs allocated on the same compute node.

#### 2\. MPI programs

In Slurm, the `--ntasks` flag specifies the number of MPI tasks created for your job. Note that, even within the same job, multiple tasks do not necessarily run on a single node. Therefore, requesting the same number of CPUs as above, but with the `--ntasks` flag, could result in those CPUs being allocated on several, distinct compute nodes.

For many users, differentiating between `--ntasks` and `--cpus-per-task` is sufficient. However, for more control over how Slurm lays out your job, you can add the `--nodes` and `--ntasks-per-node` flags. `--nodes` specifies how many nodes to allocate to your job. Slurm will allocate your requested number of cores to a minimal number of nodes on the cluster, so it is extremely likely if you request a small number of tasks that they will all be allocated on the same node. However, to ensure they are on the same node, set `--nodes=1` (obviously this is contingent on the number of CPUs on your cluster's nodes and requesting too many may result in a job that will never run). Conversely, if you would like to ensure a specific layout, such as one task per node for memory, I/O or other reasons, you can also set `--ntasks-per-node=1`. Note that the following must be true:

```
ntasks-per-node * nodes >= ntasks
```

#### 3\. Hybrid (MPI+OpenMP) programs

For the most predictable performance for hybrid codes, you will need to use all three of the `--ntasks`, `--cpus-per-task`, and `--nodes` flags, where `--ntasks` equals the number of MPI tasks, `--cpus-per-task` equals the number of OMP_NUM_THREADS and `--nodes` is the number of nodes required to fit `--ntasks * --cpus-per-task`.


### Requesting GPUs

Some of our clusters have nodes that contain GPU co-processors. Please refer to the cluster-specifc documentation regarding the node configurations that include gpus. In order for your job to be able to access gpus, you must request them as a slurm "Generic Resource" or gres. You spcify the gres configuration per-node for a job with the `--gres` flag, optionally a type of resource, and a number of gpus. For example, to request one nvidia p100 for each node in your job, you would use the flag `--gres=gpu:p100:1`. In cases where there are multiple gpus on a node, it is often a good idea to also specify the `--gres-flags=enforce-binding` flag, which tells slurm to force CPU(s) your job is allocated to share a PCIe Host Bridge with the GPU(s). Depending on your application, this can lead to improved performance, especially in transferring data to and from the GPU.

For more documentation on using GPUs on our clusters, please see [Using GPUs with Python Deep Learning](/node/13261) and [GPUs and CUDA](/node/3771).

### Example submission scripts

#### 1\. Multi-threaded programs

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

#### 2\. Multi-process programs

On Omega, try to make ntasks equal to a multiple of 8.

```
#!/bin/bash

#SBATCH --job-name=mpi
#SBATCH --output=mpi_job.txt
#SBATCH --ntasks=4
#SBATCH --time=10:00

mpirun hello.mpi
```

#### 3\. Hybrid (MPI+OpenMP) programs

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

#### 3\. GPU job

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

<a name="monitoring-job-status"></a>

### Monitoring Job Status

To check on the status of your jobs, do:

```
squeue -l -u <netid>
```

To kill a running job, do:

```
scancel <job_id>
```

To check on the status of a partition(to see how many nodes are free, for example), do:

```
squeue -p partition
```

### Using Private Partitions

If you have special permission to submit to a partition that belongs to another group, you may be asked to assign a special "account" to your jobs in that partition. You will be given the name of this account when you get access the partition and then simple add the `-A <account>` flag to your submission command or as an additional directive in your submission script.

### Features and Constraints

You may want to run programs that require more specific hardware than slurm may be willing to allocate to your job. To ensure your job runs on specific types of nodes, use the `--constraint` flag. You can use the processor type (e.g. `E5-2660_v3`) or processor codename (e.g. `haswell`) to limit your job to specific node types. You can also specify an instruction set (e.g. `avx`) to require that no matter what CPU your job runs on, it must understand at least these instructions. See the individual cluster pages for the exact tags for the different node types.

```
# run on a node with a haswell codenamed CPU (e.g. a E5-2660 v3)
sbatch --constraint=haswell submit.sh

# only run on nodes with E5-2660 v4 CPUs
sbatch --constraint=E5-2660_v4 submit.sh

# run on any node that understands avx instructions
# Your job could also run on an avx2 node
sbatch --constraint=avx submit.sh

```

Use the command `scontrol show node hostname`, replacing hostname with the node's hostname you're insterested in, to see more information about it including its features.

### Migrating from another queuing system to Slurm

Most commands and batch script can be easily converted to slurm. SchedMD created a ["rosetta stone"](http://slurm.schedmd.com/rosetta.pdf) showing equivalent operations in various batch queuing systems. Here are some specific hints:

Migrating from Torque:

*   You do not need to change directory by doing cd $PBS_O_WORKDIR. Slurm runs jobs in the submission directory by default
*   You must have an interpreter command as the first line of your slurm batch script. Usually #!/bin/bash is what you want.