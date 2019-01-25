# CESM/CAM

This is a quick start guide for CESM at Yale. You will still need to read the CESM User Guide and work with your fellow research group members to design and run your simulations, but this guide covers the basics that are specific to running CESM at Yale.

## CESM User Guides

* [CESM1.0.4 User’s Guide](http://www.cesm.ucar.edu/models/cesm1.0/cesm/cesm_doc_1_0_4/book1.html)
* [CESM1.1.z User’s Guide](http://www.cesm.ucar.edu/models/cesm1.1/cesm/doc/usersguide/book1.html)
* [CESM User’s Guide (CESM1.2 Release Series User’s Guide) (PDF)](http://www.cesm.ucar.edu/models/cesm1.2/cesm/doc/usersguide/book1.html)

## Modules

CESM 1.0.4, 1.2.2, 2.x are available on Omega and Grace. Other versions may be available on one of the clusters. To find which version are available on your cluster, run

``` bash
module avail cesm
```

Once you have located your module, run

``` bash
module load <module-name>
```

with the module name from above. The module will configure your environment with the Intel compiler, OpenMPI and NetCDF libraries as well as set the location of the Yale’s repository of CESM input data.

If you will be primarily using CESM, you can avoid rerunning the module load command every time you login by saving it to your default environment:

``` bash
module load <module-name>
module save
```

## Input Data

To reduce the amount of data duplication on the cluster, we keep one centralized repository of CESM input data. The YCRC staff are only people who can add to that directory, so if your build fails due to missing inputdata, send your `create_newcase` line to Kaylea ([kaylea.nelson@yale.edu](mailto:kaylea.nelson@yale.edu)) and she will download that data for you.

## Running CESM

CESM needs to be rebuilt separately for each run. As a result, running CESM is more complicated than a standard piece of software where you would just run the executable.

### Create Your Case

Each simulation is called a “case”. Loading a CESM module will put the create_newcase script in your path, so you can call it as follows. This will create a directory with your case name, that we will refer to as `$CASE` s through out the rest of the guide.

``` bash
create_newcase -case <case_name> -compset=<compset> -res=<resolution> -mach=<machine>
# substitute your case name for "$CASE" below
cd <case_name>
```

The mach parameters for Grace and Omega are `yalegrace` and `omega`, respectively. For example

``` bash
# on Grace
create_newcase -case Test_Sim -compset=B2000 -res=f19_f19 -mach=yalegrace
# on Omega
create_newcase -case Test_Sim -compset=B2000 -res=f19_f19 -mach=omega
cd Test_Sim
```

### Setup Your Case

If you are making any changes to the namelist files (such as increasing the duration of the simulation), do those before running the setup scripts below.

#### CESM 1.0.X

If you are using CESM 1.0.X (e.g. 1.0.4), set up your case with

``` bash
./configure -case
```

#### CESM 1.1.X and CESM 1.2.X

If you are using CESM 1.1.X (e.g. 1.1.1) or CESM 1.2.X (e.g. 1.2.2), set up your case with

``` bash
./cesm_setup
```

### Building your case

After you run the setup script, there will be a set of the scripts in your case directory that start with your case name. To compile your simulation executable, first move to an interactive job and then run the build script corresponding to your case.

``` bash
srun --pty -c 4 -p interactive bash
./$CASE.$mach.build
```

For more details on interactive jobs, see our [Slurm documentation](/clusters-at-yale/job-scheduling/slurm#interactive-jobs).

During the build, CESM will create a corresponding directory in your scratch or project directory at

```
# On Omega
ls ~/scratch/CESM/$CASE
# On Grace
ls ~/project/CESM/$CASE
```

This directory will contain all the outputs from your simulation as well as logs and the cesm.exe executable.

#### Common Build Issues

Make sure you compile on an interactive node as described above. If you build fails, it will direct you to look in a bldlog file. If that log complains that it can’t find mpirun, NetCDF or another library or executable, make sure you have the correct CESM module loaded.

### Submit Your Case

Once the build is complete, which can take 5-15 minutes, you can submit your case with the submit script.

``` bash
./$CASE.$mach.submit
```

For more details on monitoring your submitted jobs, see our [Slurm documentation](/clusters-at-yale/job-scheduling/slurm).

### Troubleshoot Your Run

If your run doesn’t complete, there are a few places to look to identify the error. CESM writes to multiple log files for the different components and you will likely have to look in a few to find the root cause of your error.

#### Slurm Log

In your case directory, there will be a file that looks like `slurm-<job_id>.log`. Check that file first to make sure the job started up properly. If the last few lines in the file redirect you to look at `cpl.log.<some_number>` file in your scratch directory, see below. If there is another error, try to address it and resubmit.

#### CESM Run Logs

If the last few lines of the slurm log direct you to look at `cpl.log.<some_number>` file, change directory to your case “run” directory in your scratch directory:

``` bash
cd ~/scratch/CESM/$CASE/run
```

The pointer to the cpl file is often misleading as I have found the error is usually located in one of the other logs. Instead look in the `cesm.log.xxxxxx` file. Towards the end there may be an error or it may signify which component was running. Then look in the log corresponding to that component to track down the issue.

One shortcut to finding the relevant logs is to sort the log files by the time to see which ones were last updated:

``` bash
ls -ltr *log*
```

Look at the end of the last couple logs listed and look for an indication of the error.

#### Resolve Errors

Once you have identified the lines in the logs corresponding to your error:

If your log says something like “Disk quota exceeded”, your group is out of space in the fileset you are writing to. You can run the `getquota` script to get details on your disk usage. Your group will need to reduce their usage before you will be able to run successfully.

If it looks like a model error and you don’t know how to fix it, I strongly recommend Googling your error and/or looking in the [CESM forums](https://bb.cgd.ucar.edu). If you still can’t resolve your error, you can come by Kaylea’s office hours, posted outside KGL 227.

## Alternative Submission Parameters

By default, the submission script will submit to the week partition for 7 days or the geo partition on Omega depending on your group. Sometimes the wait times can be very long in the week partition, so you can either submit day or scavenge partition. To change this, edit your case’s run script and change the partition and time lines. The maximum walltime in the day partition is 24 hours. The maximum walltime in scavenge is 24 hours on Grace and 7 days on Omega. For example:

``` bash
## day partition
#SBATCH --partition=day
#SBATCH --time=1-
```

``` bash
## scavenge partition
#SBATCH --partition=scavenge
#SBATCH --time=1-
```

Note that is your submission script was configured to submit to the geo partition on Omega, you will need to modify the `#SBATCH -A pi_<group_name>` to be just `#SBATCH -A <group_name>` to submit to any other partition.

Then you can submit by running the submit script

``` bash
./$CASE.$mach.submit
```

## Further Reading

* I recommend referencing the User Guides listed at the top of this page.
* [CESM User Forum](https://bb.cgd.ucar.edu)
* [Our Slurm Documentation](/clusters-at-yale/job-scheduling/slurm)
* CESM is a very widely used package, you can often find answers by simply using Google. Just make sure that the solutions you find correspond to the approximate version of CESM you are using. CESM changes in subtle but significant ways between versions.