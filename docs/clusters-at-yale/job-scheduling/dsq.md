# Submit Job Arrays with dSQ

[Dead Simple Queue](https://github.com/ycrc/dsq) is a light-weight tool to help submit large batches of homogenous jobs to a [Slurm](https://slurm.schedmd.com/)-based HPC cluster. It wraps around slurm's [sbatch](https://slurm.schedmd.com/sbatch.html) to help you submit independent jobs as [job arrays](https://slurm.schedmd.com/job_array.html). Job arrays have several advantages over submitting your jobs in a loop:

* Your job array will grow during the run to use available resources, up to a limit you can set. Even if the cluster is busy, you probably get work done because each job from your array can be run independently.
* Your job will only use the resources needed to complete remaining jobs. It will shrink as your jobs finish, giving you and your peers better access to compute resources.
* If you run your array on a pre-emptable partition (scavenge on YCRC clusters), only individual jobs are preempted. Your whole array will continue.

dSQ adds a few nice features on top of job arrays:

* Your jobs don't need to know they're running in an array; your job file is a great way to document what was done in a way that you can move to other systems relatively easily.
* You get a simple report of which job ran where and for how long
* dSQAutopsy can create a new job file that has only the jobs that didn't complete from your last run.
* All you need is Python 2.7+, or Python 3.

dSQ is _not_ recommended for situations where the initialization of the job takes most of its execution time and it is re-usable. These situations are much better handled by a worker-based job handler.

## Step 1: Create Your Job File

First, you'll need to generate a job file. Each line of this job file needs to specify exactly what you want run for each job, including any modules that need to be loaded or modifications to your environment variables. Empty lines or lines that begin with `#` will be ignored when submitting your job array. **Note:** slurm jobs start in the directory from which your job was submitted.

For example, imagine that you have 1000 fastq files that correspond to individual samples you want to map to a genome with `bowtie2` and convert to bam files with `samtools`. Given some initial testing, you think that each job needs 4 GB of RAM, and will run in less than 10 minutes.

Create a file with the jobs you want to run, one per line. A simple loop that prints your jobs should usually suffice. A job can be a simple command invocation, or a sequence of commands. You can call the job file anything, but for this example assume it's called "joblist.txt" and contains:

``` bash
module load bowtie2 samtools; bowtie2 -p 8 --local --rg-id sample1 --rg SM:sample1 --rg LB:sci_seq --rg PL:ILLUMINA -x my_genome -U sample1.fastq - | samtools view -Shu - | samtools sort  - sample1
module load bowtie2 samtools; bowtie2 -p 8 --local --rg-id sample2 --rg SM:sample2 --rg LB:sci_seq --rg PL:ILLUMINA -x my_genome -U sample2.fastq - | samtools view -Shu - | samtools sort  - sample2
...
module load bowtie2 samtools; bowtie2 -p 8 --local --rg-id sample1000 --rg SM:sample1000 --rg LB:sci_seq --rg PL:ILLUMINA -x my_genome -U sample1000.fastq - | samtools view -Shu - | samtools sort  - sample1000
```

## Step 2: Generate Batch Script with `dsq`

On YCRC clusters you can load Dead Simple Queue onto your path with:

``` bash
module load dSQ
```

You can also download or clone this repo and use the scripts directly.

`dsq` takes a few arguments, then writes a job submission script (default) or can directly submit a job for you. **The resources you request will be given to each job in the array (each line in your job file)**, e.g. requesting 2 GB of RAM with dSQ will run each individual job with a separate 2 GB of RAM available. Run `sbatch --help` or see the [official Slurm documentation](https://slurm.schedmd.com/sbatch.html) for more info on sbatch options. dSQ will set a default job name of dsq-jobfile (your job file name without the file extension). dSQ will also set the job output file name pattern to dsq-jobfile-%A_%a-%N.out, which will capture each of your jobs' output to a file with the job's ID(%A), its array index or zero-based line number(%a), and the host name of the node it ran on (%N). If you are handling output in each of your jobs, set this to `/dev/null`, which will stop these files from being created.

``` text
Required Arguments:
  --job-file jobs.txt   Job file, one self-contained job per line.

Optional Arguments:
  -h, --help            Show this help message and exit.
  --version             show program's version number and exit
  --batch-file sub_script.sh
                        Name for batch script file. Defaults to dsq-jobfile-YYYY-MM-DD.sh
  -J jobname, --job-name jobname
                        Name of your job array. Defaults to dsq-jobfile
  --max-jobs number     Maximum number of simultaneously running jobs from the job array.
  -o fmt_string, --output fmt_string
                        Slurm output file pattern. There will be one file per line in your job file. To suppress slurm out files, set this to /dev/null. Defaults to dsq-jobfile-%A_%a-%N.out
  --status-dir dir      Directory to save the job_jobid_status.tsv file to. Defaults to working directory.
  --suppress-stats-file  Don't save job stats to job_jobid_status.tsv
  --submit              Submit the job array on the fly instead of creating a submission script.
```

In the example above, we want walltime of 10 minutes and memory=4GB per job. Our invocation would be:

``` bash
dsq --job-file joblist.txt --mem-per-cpu 4g -t 10:00 --mail-type ALL
```

Which will create a file called `dsq-joblist-yyyy-mm-dd.sh`, where the y, m, and d are today's date. After creating the batch script, take a look at its contents. It should look quite familiar.

``` bash
#!/bin/bash
#SBATCH --array 0-999
#SBATCH --output dsq-joblist-%A_%3a-%N.out
#SBATCH --job-name dsq-joblist
#SBATCH --mem-per-cpu 4g -t 10:00 --mail-type ALL

# DO NOT EDIT LINE BELOW
/path/to/dSQBatch.py --job-file /path/to/joblist.txt --status-dir /path/to/here
```

## Step 3: Submit Batch Script

``` bash
sbatch dsq-joblist-yyyy-mm-dd.sh
```

## Manage Your dSQ Job

You can refer to any portion of your job with `jobid_index` syntax, or the entire array with its jobid. The index Dead Simple Queue uses **starts at zero**, so the 3rd line in your job file will have an index of 2. You can also specify ranges.

``` bash
# to cancel job 4 for array job 14567
scancel 14567_4

# to cancel jobs 10-20 for job 14567:
scancel 14567_[10-20]
```

## dSQ Output

You can monitor the status of your jobs in Slurm by using `squeue -u <netid>`, `squeue -j <jobid>`, or `dsqa -j <jobid>`.

dSQ creates a file named `job_jobid_status.tsv`, unless you suppress this output with `--supress-stats-file`. This file will report the success or failure of each job as it finishes. Note this file will not contain information for any jobs that were canceled (e.g. by the user with scancel) before they began. This file contains details about the completed jobs in the following tab-separated columns:

* Job_ID: the zero-based line number from your job file.
* Exit_Code: exit code returned from your job (non-zero number generally indicates a failed job).
* Hostname: The hostname of the compute node that this job ran on.
* Time_Started: time started, formatted as year-month-day hour:minute:second.
* Time_Ended: time started, formatted as year-month-day hour:minute:second.
* Time_Elapsed: in seconds.
* Job: the line from your job file.

## dSQAutopsy

You can use dSQAutopsy or `dsqa` to create a simple report of the array of jobs, and a new jobsfile that contains just the jobs you want to re-run if you specify the original jobsfile. Options listed below

``` text
  -j JOB_ID, --job-id JOB_ID
                        The Job ID of a running or completed dSQ Array
  -f JOB_FILE, --job-file JOB_FILE
                        Job file, one job per line (not your job submission script).
  -s STATES, --states STATES
                        Comma separated list of states to use for re-writing job file. Default: CANCELLED,NODE_FAIL,PREEMPTED
```

Asking for a simple report:

``` bash
dsqa -j 13233846
```

Produces one

``` text
State Summary for Array 13233846
State       Num_Jobs Indices  
-----       -------- -------  
COMPLETED      12    4,7-17   
RUNNING        5     1-3,5-6  
PREEMPTED      1     0 
```

You can redirect the report and the failed jobs to separate files:

``` bash
dsqa -j 2629186 -f jobsfile.txt > re-run_jobs.txt 2> 2629186_report.txt
```
