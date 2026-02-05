# SimpleQueue

!!! Warning
    As of 2020, SimpleQueue was deprecated. Please use our new updated and renamed tool, [dSQ](/clusters-at-yale/job-scheduling/dsq/#submit-job-arrays-with-dsq), instead.
    
SimpleQueue is a tool written here to streamline submission of a large number of jobs using a task file. It has a number of advantages:

* You can run more of your sequential jobs concurrently, since there is a limit on the number of individual qsubs you can run simultaneously.
* You only have one job to keep track of.
* If you need to shut everything down, you only need to kill one job.
* SimpleQueue keeps track of the status of individual jobs.

_Note that version 3.0+ of SimpleQueue differs from earlier versions in important ways, in particular the meaning of -n. If you have been using an earlier version, please read the following carefully!_

SimpleQueue is available as [a module](/cluster-at-yale/applications/modules) on our clusters. Run:

``` bash
module avail simplequeue
```

to locate the simplequeue module on your cluster of choice.

## Example SimpleQueue Job

For example, imagine that you have 1000 fastq files that correspond to individual samples you want to map to a genome with `bowtie2` and convert to bam files with `samtools`. Given some initial testing, you think that 80 cpus working together will be enough to finish the job in a reasonable time.

### Step 1: Create Task List

The first step is to create a file with a list of the "tasks" you want to run. Each task corresponds to what you might otherwise have run as a single job. A task can be a simple command invocation, or a sequence of commands. You can call the task file anything, but for this example assume it's called "tasklist.txt" and contains:

``` bash
module load bowtie2 samtools; bowtie2 -p 8 --local --rg-id sample1 --rg SM:sample1 --rg LB:sci_seq --rg PL:ILLUMINA -x my_genome -U sample1.fastq - | samtools view -Shu - | samtools sort  - sample1
module load bowtie2 samtools; bowtie2 -p 8 --local --rg-id sample2 --rg SM:sample2 --rg LB:sci_seq --rg PL:ILLUMINA -x my_genome -U sample2.fastq - | samtools view -Shu - | samtools sort  - sample2
...
module load bowtie2 samtools; bowtie2 -p 8 --local --rg-id sample1000 --rg SM:sample1000 --rg LB:sci_seq --rg PL:ILLUMINA -x my_genome -U sample1000.fastq - | samtools view -Shu - | samtools sort  - sample1000

```

For simplicity, we'll assume that tasklist, input fastq files, and indexed genome are in a directory called `~/genome_proj/mapping`.

### Step 2: Create Submission Script

Load the SimpleQueue module, then create the launch script using:

``` bash
sqCreateScript -q general -N genome_map -n 80 tasklist.txt > run.sh
```

These parameters specify that the job, named genome_map, will be submitted to the general queue/partition. This job will find 80 free cores, start 80 workers on them, and begin processing tasks from the taskfile `tasklist.txt`.

sqCreateScript takes a number of options. They differ somewhat from cluster to cluster, particularly the default values for queue, walltime, and memory. You can run sqCreateScript without any arguments to see the exact options on your cluster.

```
Usage:

  -h, --help            show this help message and exit
  -n WORKERS, --workers=WORKERS
                        Number of workers to use. Not required. Defaults to 1.
  -c CORES, --cores=CORES
                        Number of cores to request per worker. Defaults to 1.
  -m MEM, --mem=MEM     Memory per worker. Not required. Defaults to 1G
  -w WALLTIME, --walltime=WALLTIME
                        Walltime to request for the Slurm Job in form
                        [[D-]HH:]MM:SS. Not required. Defaults to 1:00:00.
  -q QUEUE, --queue=QUEUE
                        Name of queue to use. Not required. Defaults to
                        general
  -N NAME, --name=NAME  Base job name to use. Not required. Defaults to
                        SimpleQueue.
  --logdir=LOGDIR       Name of logging directory. Defaults to
                        SQ_Files_${SLURM_JOB_ID}.
```

### Step 3: Submit Your Job

Now you can simply submit `run.sh` to the scheduler. All of the important scheduler options (queue, number of tasks, number of cpus per task) will have been set in the script so you needn't worry about them.

Shortly after run.sh begins running, you should see a directory appear called `SQ_Files_jobid` where jobid is the jobid the scheduler assigned your job. This directory contains logs from all the tasks that are run during your job.

In addition, there are a few other files that record information about the job as a whole. Of these, the most important one is `SQ.log`. It should be reviewed if you encounter a problem with a run.

Assuming that all goes well, tasks from the tasklist file will be scheduled automatically onto the cpus you acquired until all the tasks have completed. At that time, the job will terminate, and you'll see several summary files:

* `scheduler_jobid_out.txt`: this is the stdout from simple queue proper (it is generally empty).
* `scheduler_jobid_err.txt`: this is the stderr from simple queue proper (it is generally a copy of `SQ.log`).
* `tasklist.txt.STATUS`: this contains a list of all the tasks that were run, including exit status, start time, end time, pid, node run on, and the command run.
* `tasklist.txt.REMAINING`: Failed or uncompleted tasks will be listed in this file in the same format as tasklist, so that those tasks can be easily rerun. You should review the status files related to these tasks to understand why they did not complete. This list is provided for convenience. It is always a good idea to scan tasklist.STATUS to double check which tasks did in fact complete with a normal exit status.
* `tasklist.txt.ROGUES`: The simple queue system attempts to ensure that all tasks launched eventually exit (normally or abnormally). If it fails to get confirmation that a task has exited, information about the command will be written to this file. This information can be used to hunt down and kill run away processes.

## Other Important Options

If your individual tasks need more than the default memory allocated on your cluster, you can specify a different value using -m. For example: `sqCreateScript -m 10g -n 4 ... tasklist > run.sh` would request 10GiB of RAM for each of your workers.

If your jobs are themselves multithreaded, you can request that your workers have multiple cores using the -c option: `sqCreateScript -c 20 -n 4 ... tasklist > run.sh` This would create 4 workers, each having access to 20 cores.
