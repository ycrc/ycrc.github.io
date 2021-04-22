# Jobs with Dependencies

SLURM offers a tool which can help string jobs together via dependencies. 
When submitting a job, you can specify that it should wait to run until a specified job has finished. 
This provides a mechanism to create simple pipelines for managing complicated workflows. 

## Simple Pipeline
As a toy example, consider a two-step pipeline, first a data transfer followed by an analysis step. 
Here we will use the `--dependency` flag for sbatch and the `afterok` type that requires a job to finish successfully before starting the second step:

The first step is controlled by a `sbatch` submission script called `step1.sh`:

```sh
#!/bin/bash
#SBATCH --job-name=DataTransfer
#SBATCH -t 30:00

rsync -avP remote_host:/path/to/data.csv $HOME/project/

```
The second step is controlled by `step2.sh`:

```sh
#!/bin/bash
#SBATCH --job-name=DataProcess
#SBATCH -t 5:00:00

module load miniconda
source activate my_env
python my_script.py $HOME/project/data.csv

```
When we submit the first step (using the command `sbatch step1.sh`) we obtain the jobid number for that job.
We then submit the second step adding in the `--dependency` flag to tell Slurm that this job requires the first job to finish before it can start:

```sh
sbatch --dependency=afterok:56761133 step2.sh
```

When the 'transfer' job finishes successfully (without an error exit code) the 'processing' step will begin.
While this is a simple dependency structure, it is possible to have multiple dependencies or more complicated structure.

## Job Clean-up

One frequent use-case is a clean-up job that runs after all other jobs have finished. 
This is a common way to collect results from processing multiple files into a single output file. 
This can be done using the `--dependency=singleton:<job_id>` flag that will wait until all previously launched jobs _with the same name and user_ have finished.

```sh

[tl397@grace1 ~]$ squeue -u tl397
             JOBID PARTITION     NAME     USER    ST      SUBMIT_TIME       NODELIST(REASON)
          12345670       day   JobName    tl397   R    2020-05-27T11:54     c01n08
          12345671       day   JobName    tl397   R    2020-05-27T11:54     c01n08
          ...
          12345678       day   JobName    tl397   R    2020-05-27T11:54     c01n08
          12345679       day   JobName    tl397   R    2020-05-27T11:54     c01n08

[tl397@grace1 ~]$ sbatch --dependency=singleton --job-name=JobName cleanup.sh
[tl397@grace1 ~]$ squeue -u tl397
             JOBID PARTITION     NAME     USER    ST      SUBMIT_TIME       NODELIST(REASON)
          12345670       day   JobName    tl397   R    2020-05-27T11:54     c01n08
          12345671       day   JobName    tl397   R    2020-05-27T11:54     c01n08
          ...
          12345678       day   JobName    tl397   R    2020-05-27T11:54     c01n08
          12345679       day   JobName    tl397   R    2020-05-27T11:54     c01n08
          12345680       day   JobName    tl397   R    2020-05-27T11:54     (Dependency)
```

This last job will wait to run until all previous jobs with name `JobName` finish. 


## Further Reading

SLURM provides a number of options for logic controlling dependencies. 
Most common are the two discussed above, but `--dependency=afternotok:<job_id>` can be useful to control behavior if a job fails. 
Full discussion of the options can be found on the SLURM manual page for `sbatch` (https://slurm.schedmd.com/sbatch.html).
A very detailed overview, with examples in both bash and python, can also be found at the NIH computing reference: https://hpc.nih.gov/docs/job_dependencies.html.

