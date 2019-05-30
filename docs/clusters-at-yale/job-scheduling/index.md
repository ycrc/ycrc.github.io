# Run Jobs with Slurm

Slurm is used to submit jobs to a specified set of compute resources, which are variously called queues or partitions. Slurm uses the term partition. Partitions, their defaults, limits and purposes are listed on [each cluster page](/clusters-at-yale/clusters). To see more details about how jobs are scheduled see our information on [factors affecting scheduling priority](/clusters-at-yale/job-scheduling/fairshare).

Please be a good cluster citizen. Do not run jobs on login nodes (e.g. grace1, farnam2), as these can impact the sessions and connectivity of everyone else on the cluster. We also sometimes find jobs on the clusters that allocate resources incorrectly for the job that is running. Please see our documentation on [Monitoring CPU and Memory Usage](/clusters-at-yale/job-scheduling/resource-usage) for examples of how to measure the resources your jobs use. If you find yourself wondering how best to schedule a job feel free to [email us](mailto:hpc@yale.edu?Subject=Job%20help) or come to [office hours](/). Efficient jobs help you get your work done faster and free resources for others as well.

## Common Slurm Commands

Submit a submission script (see below for details)

``` bash
sbatch <script>
```

List queued and running jobs

``` bash
squeue -u$USER
```

Cancel a queued job or kill a running job

``` bash
scancel <job_id>
```

Check status of individual job (including failed or completed)

``` bash
sacct -j <job_id>
```

## Interactive Jobs

Interactive jobs can be used for testing and troubleshooting code. By requesting an interactive job, you will be allocated resources and logged onto the node in a shell.

``` bash
srun --pty -p interactive bash
```

This will assign a free node to you, allocating the requested number of CPUs, walltime, and memory, and put you within a shell on that node. You can run any number of commands within that shell. To free the allocated node, exit from the shell.

!!!tip
    When using an interactive shell under slurm, your job is vulnerable to being killed if you lose your network connection. We recommend using [`tmux`](/clusters-at-yale/guides/tmux) alleviate this. When using `tmux`, please be sure to keep track of your allocations and free those no longer needed!

To use a GUI application (such as Matlab), when in an interactive job, use the `--x11` flag:

``` bash
srun --pty --x11 -p interactive [additional slurm options] bash
```

!!!warning
    For X11 forwarding to work, you need to have your local machine setup properly. Please see our [X11 setup guide](/clusters-at-yale/access/x11) for more info.

## Batch Jobs

To submit a job via Slurm, you first write a simple shell script called a "submission script" that wraps your job. A submission script is comprised of three parts:

1. The program that should run the script. This is normally `#!/bin/bash`.
1. The "directives" that tell the scheduler how to setup the computational resources for your job.**These lines must appear before any other commands or definitions, otherwise they will be ignored.**
1. The actual "script" portion, which are the commands you want executed during your job.

Here is an example script.sh that runs a job on one CPU on single node:

``` bash
#!/bin/bash
#SBATCH --partition=general
#SBATCH --job-name=my_job
#SBATCH --ntasks=1 --nodes=1
#SBATCH --mem-per-cpu=6000
#SBATCH --time=12:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<email>

./myprog -p 20 arg1 arg2 arg3 ...
```

## Directives

As shown in the above example, "directives" are comprised of `#SBATCH` followed by Slurm options. Most commonly used options include:

|Full Option<img width=100/>|Abbreviated|Description|
|--- |--- |--- |
|`--job-name`|`-J`|Custom job name|
|`--partition`|`-p`|Partition to run on|
|`--nodes`|`-N`|Total number of nodes|
|`--ntasks`|`-n`|Number of "tasks". For use with distributed parallelism. See below.|
|`--cpus-per-task`|`-c`|# of CPUs allocated to each task. For use with shared memory parallelism.|
|`--ntasks-per-node`||Number of "tasks" per node. For use with distributed parallelism. See below.|
|`--time`|`-t `|Maximum walltime of the job in the format D-HH:MM:SS (e.g. `--time=1-` for one day or `--time=4:00:00` for 4 hours)|
|`--constraint`|`-C`|specific node architecture (if applicable)|
|`--mem-per-cpu`||Memory requested per CPU in MB|
|`--mem`||Memory requested per node in MB|
|`--mail-user`||Mail address (alternatively, put your email address in ~/.forward)|
|`--mail-type`||Control emails to user on job events. Use `ALL` to receive email notications at the beginning and end of the job.|

Additional options can be found on in the [official Slurm documentation](http://slurm.schedmd.com/documentation.html).

## Resource Limit Enforcement

Slurm uses the linux cgroup feature to enforce limits on CPUs, GPUs, and memory. Jobs are only permitted to run on a node if they have a valid allocation, and only within the limits specified by that limitation. Thus, if you request a single core from slurm (the default) and start a job that runs 20 parallel threads, those threads will be packed into a single CPU, and run very slowly. Similarly, if you do not explicitly request memory, your job will be granted 5G of RAM per CPU, and if your job attempts to exceed that amount, it will be killed.

## Using Private Partitions

If you have special permission to submit to a partition that belongs to another group, you may be asked to assign a special "account" to your jobs in that partition. You will be given the name of this account when you get access the partition and then simple add the `-A <account>` flag to your submission command or as an additional directive in your submission script.
