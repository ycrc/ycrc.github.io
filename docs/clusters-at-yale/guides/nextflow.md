# Nextflow

[Nextflow](https://www.nextflow.io/) is a very popular workflow tool, especially in bioinformatics.  It automates workflow processing, is very portable, and has excellent reporting.
Nextflow is able to make effective use of slurm when running  on our clusters, using slurm submissions for running processes and achieving a high level of parallelism.  However, there are a few gotchas and things to know about.

First, to specify slurm as the executor, add the following executor default to the process specification in nextflow.config. 

``` bash
Process { 
    …
   executor = 'slurm'
    …
}
```

You can add other slurm-related options, for example:

``` bash
process {
    executor = 'slurm'
    queue = 'day'
    memory = '200 GB'
    cpus = 32
    Time = 4h
}
```

This sets the initial default for the slurm partition, memory, cpus, and time.  Note that nextflow uses different names for many of these values than slurm.
These same options can be added to specific processes or labels to customize processes more specifically.
Arbitrary slurm options can be added using clusterOptions, e.g. clusterOptions = '--qos priority’
More information can be found on nextflow's [slurm](https://www.nextflow.io/docs/latest/executor.html#slurm) page.

Setting executor to slurm will cause all processes to be submitted as slurm jobs, unless otherwise specified (see below).

## Nextflow installation

You can either use our installed module, or install your own copy of nextflow (for example if you want the very latest version of nextflow).  If you use your own nextflow, be sure to load the Java module.  Our nextflow module does that automatically.

## Using conda or apptainer/singularity

It is common for nextflow pipelines to use a containerization to manage code, such as conda or apptainer (aka singularity).  However, conda is not installed as a system tool on our clusters.  Therefore, if using conda for your process code, you should load the miniconda module in your batch script before invoking nextflow.  The nextflow submissions will inherit this module in the usual way.  Apptainer/singularity is installed as a system tool, but only on compute nodes.  Therefore, you must run nextflow on a properly allocated compute node (which should be the case anyway), not on the login node.

## Scheduling quirks

When running nextflow with slurm executor, you may notice some scheduling oddities.  This is due to the fact that multiple barriers can pend jobs.

Internally, nextflow limits the number of submitted slurm jobs to the value of ‘queueSize’, by default 100.  This can be modified in the configuration or using the -qs command line option.   This is why nextflow can report a large number of pending jobs, while squeue only shows 100.  Slurm (squeue) will not show the jobs pended by queueSize, since nextflow has not actually submitted them yet.  

Once jobs are actually submitted, the usual slurm queuing will occur.  This can include: per user or group limits, lack of available resources, etc.  These pended jobs will show in squeue as PD.


## Submission threshold

In order to prevent abusive job submission, most of our partitions have a limit of 200 individual submissions per user per hour.  Normally not a problem, this limit can cause problems with nextflow, since by default when using slurm all processes are submissions, and many workflows submit hundreds of very short jobs.  When the threshold is exceeded, subsequent submissions fail, and typically the nextflow workflow fails.  In addition, running very short processes as slurm submissions is very inefficient.

We recommend that you configure your workflow to specify small, short jobs as using the local executor, leaving the larger and longer running jobs to the slurm executor.
The cleanest way to do this is to give those processes a specific ‘label’, e.g. process_local, and then set the executor for that label to be ‘local’.

For example:

``` bash 
 process Fastqc {
   label 'process_local'
   …
}

Process {
    …
     withLabel:process_local {
          executor = 'local'
    …
}
```

Oftentimes, if you are using a well developed workflow, the configuration will already use labels to “classify” each of the processes, so that resource requirements are only mentioned once per class, rather than for every process.  For example, a workflow might define the class ‘process_single’, which is used to tag small, quick running processes.  In that case, you can simply add executor = local to the withLabel for that label:

``` bash
Process {
     …
     withLabel:process_single {
         executor = 'local'
         cpus = 1
         memory = { maxMem(2.GB * task.attempt) }
     }
     …
}

```

## Running a hybrid workflow

When running a workflow that uses both slurm and local executors, you should submit the run as a batch job of a single task and multiple cpus.  Give the batch job a reasonable number of cpus, depending on how many local processes you want to run simultaneously (e.g. 32).  The local processes will all run within the main batch job, and the slurm processes will be submitted as separate slurm jobs.  If done correctly this should keep you below the 200 submissions/hour threshold.

You may also try reducing queueSize to a value less than 100.  If you cannot find a way to reduce your submission rate to an acceptable level, we will consider turning off the submission threshold.  Contact us for more information.



