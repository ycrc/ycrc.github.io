# Help Requests

See our [Get Help](/#get-help) section for ways to get assistance, from email support to setting up 1-on-1 appointments with our staff. 
When requesting assistance provide the information described below (where applicable), so we can most effectively assist you.
Before requesting assistance, we encourage you to take a look at the relevant documentation on this site.

If you are new to the cluster, please watch our [Intro to HPC tutorial](https://www.youtube.com/watch?v=5U-9GCavX0s) available on the [YCRC YouTube Channel](https://ycrc.yale.edu/youtube) as it covers many common usages of the systems.

## Trouble Logging In

If you are having trouble logging in to the cluster, please see our [Troubleshoot Login](clusters-at-yale/troubleshoot/) guide.

## Information to Provide with Help Requests

Whenever requesting assistance with HPC related issues, please provide the YCRC staff with the following information (where applicable) so we can investigate the problem you are encountering.
To assist with providing this information, we have included instructions below on retreiving the information if you are working in the command line interface.

* Your NetID
* name of the cluster you are working on (e.g. Grace, Farnam, Milgram or Ruddle)
* instructions on how to repeat your issue. Please include the following:
	* which directory are you working in or where you submitted your job
		* Run the command `pwd` when you are in the directory where you encountered the issue
	* the [software modules](/clusters-at-yale/applications/modules/) you have loaded
		* Run `module list` when you encounter the issue
	* the commands you ran that resulted in the error or issue
	* the name of the submission script your submitted to the schedule with `sbatch` (if reporting an issue with a batch job)

* the error message you received, and, if applicable, the path to the output file containing the error message
	* if you are using the default Slurm output options, this will look `slurm-<your job id>.out`
	* certain software may output additional information to other log files and, if applicable, include the paths to those files as well

* job ids for your Slurm job
	* you can get the job ids for recently run jobs by running the command `sacct`
	* identify the job(s) that contained the error and provide the job id

If possible, please paste the output into the email or include in a text file as an attachment. Screenshots or pictures are very hard for us to work with.

We look forwarding to assisting you!
