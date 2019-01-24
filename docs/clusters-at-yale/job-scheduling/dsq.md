# Submit Arrays with dSQ

[Dead Simple Queue](https://github.com/ycrc/dsq) is a light-weight successor to SimpleQueue. It wraps around slurm's [sbatch](https://slurm.schedmd.com/sbatch.html) to help you submit independent jobs as job arrays. It has several advantages over SimpleQueue:

* Your job will adapt during the run to the available resources. As more cpus and/or memory are available, it will grow up (up to the per-user limit)
* Your job will only use the resources needed to complete remaining jobs. It will shrink as your jobs finish, giving you and your peers better access to compute resources.
* When run on the scavenge partition, only the subjobs are preempted, and the job as a whole will continue. You can then use dSQAutopsy to create a new job file that has only the jobs that didn't complete.
* All you need is Python 2.7 or higher (Python 3 works too!)

dSQ is _not_ recommended for situations where the initialiazation of the job takes most of its execution time and it is re-usable. These situations are much better handled by a worker-based job handler.

## Step 1: Job File

First, you'll need to generate a job file. Each line of this job file needs to specify exactly what you want run for each job, including any modules that need to be loaded or modifications to your environment variables. Empty lines or lines that begin with `#` will be ignored when submitting your job array. **Note:** slurm jobs begin in the directory from which your job was submitted.

For example, imagine that you have 1000 fastq files that correspond to individual samples you want to map to a genome with `bowtie2` and convert to bam files with `samtools`. Given some initial testing, you think that each job needs 4 GB of RAM, and will run in less than 10 minutes.

You'll create a file with the "tasks" you want to run, one per line. Each task corresponds to what you might otherwise have run as a single job. A task can be a simple command invocation, or a sequence of commands. You can call the task file anything, but for this example assume it's called "joblist.txt" and contains:

```
module load bowtie2 samtools; bowtie2 -p 8 --local --rg-id sample1 --rg SM:sample1 --rg LB:sci_seq --rg PL:ILLUMINA -x my_genome -U sample1.fastq - | samtools view -Shu - | samtools sort  - sample1
module load bowtie2 samtools; bowtie2 -p 8 --local --rg-id sample2 --rg SM:sample2 --rg LB:sci_seq --rg PL:ILLUMINA -x my_genome -U sample2.fastq - | samtools view -Shu - | samtools sort  - sample2
...
module load bowtie2 samtools; bowtie2 -p 8 --local --rg-id sample1000 --rg SM:sample1000 --rg LB:sci_seq --rg PL:ILLUMINA -x my_genome -U sample1000.fastq - | samtools view -Shu - | samtools sort  - sample1000
```

## Step 2: Create Batch Script

Load Dead Simple Queue onto your path with:

On Farnam or Ruddle:

```
module load dSQ
```

On Grace, Omega or Milgram:

```
module load Tools/dSQ
```

`dSQ.py` takes a few arguments, then passes the rest directly to sbatch, either by writing a script to stdout that you should capture to a file. Unlike SimpleQueue, **the resources you request will be given to each job in the array (each line in your job file)**, e.g. requesting 2 GB of RAM with dSQ will run each individual job with a separate 2 GB of RAM available. Without specifying any additional sbatch arguments, some defaults will be set. run `sbatch --help` or see the [official Slurm documentation](https://slurm.schedmd.com/sbatch.html) for more info on sbatch options.

```
dSQ.py --jobfile jobfile [dSQ args] [slurm args] > run.sh

Required dSQ arguments:
  --jobfile JOBFILE   Job file, one job per line

Optional dSQ arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --submit              Submit the job array on the fly instead of printing to stdout.
  --max-jobs MAX_JOBS
                        Maximum number of simultaneously running jobs from the job array
```

In the example above, we want walltime of 10 minutes and memory=4GB per task. Our invocation would be:

```
dSQ --jobfile joblist.txt  --mem-per-cpu=4g -t 10:00 > run.sh
```

After creating the batch script, take a look at its contents. It should look quite familiar.

```
#!/bin/bash

#SBATCH -p general
#SBATCH -t 10:00
#SBATCH --mem-per-cpu=4g
#SBATCH --array=0-999
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<youremail>@yale.edu
#SBATCH --ntasks=1

/ysm-gpfs/apps/software/dSQ/0.92/dSQBatch.py joblist.txt</youremail>
```

## Step 3: Submit Batch Script

```
sbatch run.sh
```

## Manage Your dSQ Job

You can refer to any portion of your job with `jobid_index` syntax, or the entire array with its jobid. The index Dead Simple Queue uses **starts at zero**, so the 3rd line in your job file will have an index of 2\. You can also specify ranges.

```
#to cancel job 4 for array job 14567
scancel 14567_4

#to cancel jobs 3,5 and 10-20 for job 14567:
scancel 14567_[3,5,10-20]
```

## dSQ Output

You can monitor the status of your jobs in Slurm by using `squeue -u <netid>`.

dSQ creates a file named `job_<jobid>_status.tsv`, which will report the success or failure of each job as it finishes. Note this file will not contain information for any jobs that were canceled (e.g. by the user with scancel) before they began. This file contains details about the completed jobs in the following tab-separated columns:

* Job_ID: the zero-based line number from your job file
* Exit_Code: exit code returned from your job (non-zero number generally indicates a failed job)
* Time_Started: time started, formatted as year-month-day hour:minute:second
* Time_Ended: time started, formatted as year-month-day hour:minute:second
* Time_Elapsed: in seconds
* Job: the line from your job file

Additionally, Slurm will honor the `-e,--error` and `-i,--input` arguments you provide to capture stdout and stderr. By default both standard output and standard error are directed to a file of the name "slurm-%j.out", where the "%j" is replaced with the job allocation number and array index, which is conveniently also the 0-based line number from your job file. We recommend inspecting these outputs for troubleshooting individual failed jobss.

## dSQAutopsy

Once the dSQ job is finished, you can use dSQAutopsy to create both a report of the run, as well as a new jobsfile that contains just the jobss that failed.

```
$ dSQAutopsy --help
usage: dSQAutopsy jobsfile status.tsv

Dead Simple Queue Autopsy v0.9
https://github.com/ycrc/dSQ
A helper script for analyzing the success state of your jobss after a dSQ
run has completed. Specify the jobsfile and the status.tsv file generated
by the dSQ job and dSQAutopsy will print the jobss that didn't run or
completed with non-zero exit codes. It will also report count of each to
stderr.

positional arguments:
  jobsfile       jobs file, one jobs per line
  statusfile     The status.tsv file generated from your dSQ run

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

You can conveniently redirect the report and the failed jobss to separate files:

```
dSQAutopsy jobsfile.txt job_2629186_status.tsv > failedjobs.txt 2> report.txt
```