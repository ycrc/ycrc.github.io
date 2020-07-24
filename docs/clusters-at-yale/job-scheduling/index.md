# Run Jobs with Slurm

Performing computational work at scale in a shared environment involves organizing everyone's work into jobs and scheduling them. We use [Slurm](https://slurm.schedmd.com/overview.html) to schedule and manage jobs on the [YCRC clusters](/clusters-at-yale/clusters). 

Submitting a job involves specifying a resource request then running one or more commands or applications. These requests take the form of options to the command-line programs `srun` and `sbatch` or those same options as directives inside submission scripts. Requests are made of groups of compute nodes (servers) called partitions. Partitions, their defaults, limits, and purposes are listed on [each cluster page](/clusters-at-yale/clusters). Once submitted, jobs wait in a queue and are subject to several [factors affecting scheduling priority](/clusters-at-yale/job-scheduling/fairshare). When your scheduled job begins, the commands or applications you specify are run on compute nodes the scheduler found to satisfy your resource request. If the job was submitted as a batch job, output normally printed to the screen will be saved to file.

!!! info "Please be a good cluster citizen."

    - Do not run heavy computation on on login nodes (e.g. `grace1`, `farnam2`). Doing so negatively impacts everyone's ability to interact with the cluster.
    - Make resource requests for your jobs that reflect what they will use. Wasteful job allocations slow down everyone's work on the clusters. See our documentation on [Monitoring CPU and Memory Usage](/clusters-at-yale/job-scheduling/resource-usage) for how to measure job resource usage.
    - If you plan to run many similar jobs, use our [Dead Simple Queue](/clusters-at-yale/job-scheduling/dsq) tool or [job arrays](https://slurm.schedmd.com/job_array.html)

If you find yourself wondering how best to schedule a job, please [contact us](/#get-help) for some help.

## Common Slurm Commands

For an exhaustive list of commands and their official manuals, see the [SchedMD Man Pages](https://slurm.schedmd.com/man_index.html). Below are some of the most common commands used to interact with the scheduler.

Submit a script called `my_job.sh` as a job ([see below](#batch-jobs) for details):

``` bash
sbatch my_job.sh
```

List your queued and running jobs:

``` bash
squeue -u$USER
```

Cancel a queued job or kill a running job, *e.g.* a job with ID 12345:

<!--- if this is bash the numbers turn red -->
``` text
scancel 12345
```

Check status of a job, *e.g.* a job with ID 12345:

``` text
sacct -j 12345
```

Check how efficiently a job ran, *e.g.* a job with ID 12345:

``` text
seff 12345
```
See our [Monitor CPU and Memory page](/clusters-at-yale/job-scheduling/resource-usage) for more on tracking the resources your job actually uses.

<a id="directives"></a>
## Common Job Request Options

These options modify the size, length and behavior of jobs you submit. They can be specified when calling `srun` or `sbatch`, or saved to a [batch script](#batch-jobs). Options specified on the command line to `sbatch` will override those in a batch script. See our [Request Compute Resources page](/clusters-at-yale/job-scheduling/resource-requests) for discussion on the differences between `--ntasks` and `--cpus-per-task`, constraints, GPUs, etc. If options are left unspecified defaults are used.

|Long Option<img width=130/>|Short Option|Default            |Description|
|---------------------------|------------|-------------------|-----------|
|`--job-name`               |`-J`        |Name of script     |Custom job name.|
|`--output`                 |`-o`        |`"slurm-%j.out"`   |Where to save `stdout` and `stderr` from the job. See [filename patterns](https://slurm.schedmd.com/sbatch.html#SECTION_%3CB%3Efilename-pattern%3C/B%3E) for more formatting options.|
|`--partition`              |`-p`        |Varies by cluster  |Partition to run on. See individual [cluster pages](/clusters-at-yale/clusters/) for details.|
|`--account`                |`-A`        |Your group name    |Specify if you have access to multiple private partitions.|
|`--time`                   |`-t`        |Varies by partition|Time limit for the job in D-HH:MM:SS, e.g. `-t 1-` is one day, `-t 4:00:00` is 4 hours.|
|`--nodes`                  |`-N`        |`1`                |Total number of nodes.|
|`--ntasks`                 |`-n`        |`1`                |Number of tasks (MPI workers).|
|`--ntasks-per-node`        |            |Scheduler decides  |Number of tasks per node.|
|`--cpus-per-task`          |`-c`        |`1`                |Number of CPUs for each task. Use this for threads/cores in single-node jobs.|
|`--mem-per-cpu`            |            |`5G`               |Memory requested per CPU in MiB. Add `G` to specify GiB (e.g. `10G`).|
|`--mem`                    |            |                   |Memory requested per node in MiB. Add `G` to specify GiB (e.g. `10G`).|
|`--gres`                   |            |                   |Used to [request GPUs](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus)|
|`--constraint`             |`-C`        |                   |[Constraints](/clusters-at-yale/job-scheduling/resource-requests/#features-and-constraints) on node features. To limit kinds of nodes to run on.|
|`--mail-user`              |            |Your Yale email    |Mail address (alternatively, put your email address in ~/.forward).|
|`--mail-type`              |            |None               |Send email when jobs change state. Use `ALL` to receive email notifications at the beginning and end of the job.|

## Interactive Jobs

Interactive jobs can be used for testing and troubleshooting code. Requesting an interactive job will allocate resources and log you into a shell on a compute node. For example:

``` bash
srun --pty -t 2:00:00 --mem=8G -p interactive bash
```

This will assign one CPU and 8GiB of RAM to you for two hours. You can run commands in this shell as needed. To exit, you can type `exit` or <kbd>Ctrl</kbd>+<kbd>d</kbd> 

!!! tip "Use `tmux` with Interactive Sessions"
    Remote sessions are vulnerable to being killed if you lose your network connection. We recommend using [`tmux`](/clusters-at-yale/guides/tmux) alleviate this. When using `tmux` with interactive jobs, please take extra care to stop jobs that are no longer needed.

### Graphical applications

Many graphical applications are well served with the [Open OnDemand Remote Desktop app](/clusters-at-yale/access/ood/#remote-desktop). If you would like to use X11 forwarding, first make sure it is [installed and configured](/clusters-at-yale/access/x11). Then, add the `--x11` flag to an interactive job request:

``` bash
srun --pty --x11 -p interactive bash
```

## Batch Jobs

You can submit a script as a batch job, *i.e.* one that can be run non-interactively in batches. These submission scripts are comprised of three parts:

1. A [hashbang](https://en.wikipedia.org/wiki/Shebang_(Unix)) line specifying the program that runs the script. This is normally `#!/bin/bash`.
1. Directives that list job request options. These lines must appear before any other commands or definitions, otherwise they will be ignored.
1. The commands or applications you want executed during your job.

See our page of [Submission Script Examples](/clusters-at-yale/job-scheduling/slurm-examples/) for a few more, or the [example scripts repo](https://github.com/ycrc/ycrc_example_scripts) for more in-depth examples. Here is an example submission script that prints some job information and exits:

``` bash
--8<-- "docs/files/example_job.sh"
```
    
Save [this file](/files/example_job.sh) as `example_job.sh`, then submit it with:

``` bash
sbatch example_job.sh
```

When the job finishes the output should be stored in a file called `slurm-jobid.out`, where `jobid` is the submitted job's ID. If you find yourself writing loops to submit jobs, instead use our [Dead Simple Queue](/clusters-at-yale/job-scheduling/dsq) tool or [job arrays](https://slurm.schedmd.com/job_array.html).

