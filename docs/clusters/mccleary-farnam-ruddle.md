# McCleary for Farnam and Ruddle Users

McCleary is the successor to both the Farnam and Ruddle clusters, which were retired in summer 2023.

## Key Dates


### Farnam

* April: Migration of purchased nodes and storage from Farnam to McCleary
* June 1st: Access to Farnam login and OnDemand nodes disabled
	* Compute service charges on McCleary commons partitions begin
* July 13: `/gpfs/ysm` no longer be available

### Ruddle

* April: Migration of purchased nodes from Ruddle to McCleary
* June 1st: Official Farnam retirement date, and beginning of compute service charges on McCleary commons partitions. Jobs in the ycga partitions will always be exempt from compute service charge.
* July 24th: Access to Ruddle login and OnDemand nodes disabled. Old `/gpfs/ycga` replaced with new system.


## Accounts

Most Farnam and Ruddle users who have been active in the last year have accounts automatically created on McCleary for them and have received an email to that effect. All other users who conduct life sciences research can request an account using our [Account Request form](https://research.computing.yale.edu/support/hpc/account-request).

!!! warning "Group Membership"
	Check which group your new McCleary account is associated with and make sure that matches your expection.
	This is the group that will be charged (if/when applicable) for your compute usage as well as dictate which private partitions you may have access to.
	Any cluster specific changes previously made on Farnam or Ruddle will not be automatically reflected on McCleary.
	To check, run the following command (replacing `<netid>` with your netid):

	```
	sacctmgr show user <netid>
	```

	If you need your group association changed, please let us know at [hpc@yale.edu](mailto:hpc@yale.edu).


## Access

### Hostname

McCleary can be accessed via SSH (or MobaXterm) at the hostname `mccleary.ycrc.yale.edu`. 

Transfers and transfer applications should be connected via `transfer-mccleary.ycrc.yale.edu`. 

!!! note
	The hostname does *not* use the domain hpc.yale.edu, but uses *ycrc*.yale.edu instead.

[Multifactor authentication via Duo](/clusters-at-yale/access/mfa/) is required for all users on McCleary, similar to how Ruddle is currently configured.
This will be new to Farnam users. For most usage this additional step is minimally invasive and makes our clusters much more secure. 
However, for users who use graphical transfer tools such as Cyberduck, please see our [MFA transfer documentation](/data/transfer/#cyberduck-on-mccleary-and-ruddle).

### Web Portal (Open OnDemand)

McCleary web portal url is available at [ood-mccleary.ycrc.yale.edu](http://ood-mccleary.ycrc.yale.edu).

On McCleary, you are limited to 4 interactive app instances (of any type) through the web portal at one time. 
Additional instances will remain pending in the queue until you terminate older open instances. 
Closing the window does not terminate the interactive app job.
To terminate the job, click the "Delete" button in your "My Interactive Apps" page in the web portal.

!!! note
	Again, the url does *not* use the domain hpc.yale.edu, but uses *ycrc*.yale.edu instead.


## Software

We have installed most commonly used software modules from Farnam and Ruddle onto McCleary. 
Usage of modules on McCleary is similar to the other clusters (e.g. `module avail`, `module load`). 
Some software may only be initially available in a newer version than was installed on Farnam or Ruddle. 

If you cannot find a software package on McCleary that you need, please let us know at [hpc@yale.edu](mailto:hpc@yale.edu) and we can look into installing it for you.

## Partition and Job Scheduler

The most significant changes on transitioning from Farnam or Ruddle to McCleary is in respect to the partition scheme. 
McCleary uses the partition scheme used on the Grace and Milgram clusters, so should be familiar to users of those clusters.
A full list of McCleary partitions can be found on the [cluster page](/clusters/mccleary/).

### Default Time Request

The default walltime on McCleary is 1 hour on *all* partitions, down from 24 hours on Farnam and Ruddle. 
Use the `-t` flag to request a longer time limit.

### Changes to Partitions

Below are notable changes to the partitions relative to Farnam and Ruddle. Many of these changes are reductions to maximum time request. 
If you job cannot run in the available partition time limits, please contact us at [hpc@yale.edu](mailto:hpc@yale.edu) so we can discuss your situation.

#### `general`

McCleary does not have a `general` partition, but instead has `day` and `week` partitions with maximum time limits of 24 hours and 7 days, respectively. 
The `week` partition contains significantly fewer nodes than `day` and will reject any job that request less than 24 hours of walltime, so please think carefully about how long your job needs to run for when selecting a partition.
We strongly encourage checkpointing if it is an option or dividing up your workload into less than 24 hour chunks.
This scheme promotes high turnover of compute resources and reduces the number of idle jobs, resulting in lower overall wait time.

Interactive jobs are blocked from running in the `day` or `week` partitions. See the `interactive` partition below instead.

`day` is the default partition for batch jobs (where your job goes if you do not specify a partition with `-p` or `--partition`).

#### `interactive`

The `interactive` partition is called `devel` and contains a set of dedicated nodes specifically for development or interactive uses (`salloc` jobs).
To ensure high availability of resources, users are limited to one job at time.
That job cannot request more than 6 hours, 4 cpus and 32G of memory.

`devel` is the default partition for jobs started using `salloc` (where your job goes if you do not specify a partition with `-p` or `--partition`).

#### `bigmem`

McCleary has a `bigmem` partition, but the maximum time request is now 24 hours. 
Jobs requesting less than 120G of RAM will be rejected from the partition and we ask you to submit those jobs to `day`.

#### `scavenge`

McCleary has a `scavenge` partition that operates in the same preemptable mode as before, but the maximum time request is now 24 hours. 
 
#### `gpu_devel`

There is no `gpu_devel` on McCleary. We are evaluating the needs and potential solutions for interactive GPU-enabled jobs.
For now, interactive GPU-enabled jobs should be submitted to the `gpu` partition.

### YCGA Compute

YCGA researchers have access to a dedicated set of nodes totally over 3000 cores on McCleary that are prefixed with `ycga`.

* `ycga`: general purpose partition for batch jobs
* `ycga_interactive`: partition for interactive jobs (limit of 1 job at a time in this partition)
* `ycga_bigmem`: for jobs requiring large amount of RAM (>120G)

### Dedicated Nodes

If you have purchased nodes on Farnam or Ruddle that are not in the `haswell` generation, we have coordinated with your group to migrate those nodes to McCleary in April into a partition of the same name.

## Storage and Data

If you have data on the Gibbs filesystem, there was no action required as they are already available on McCleary.

### Farnam Data

Farnam’s primary filesystem, YSM (/gpfs/ysm), was retired on July 13th. If you previously had a Farnam account, you have been give new, empty home and scratch directories for McCleary on our Palmer filesystem and a 1 TiB project space on our Gibbs filesystem. Project quotas can be increased to 4 TiB at no cost by sending a request to [hpc@yale.edu](mailto:hpc@yale.edu). 

### Ruddle Data

The YCGA storage system (`/gpfs/ycga`) has been replaced with a new, larger storage system at the same namespace. All data in the `project` (now at `work`), `sequencers`, `special`, and `pi` directories under `/gpfs/ycga` were migrated by YCRC staff to the new storage system. All other data on `/gpfs/ycga` (Ruddle home and scratch60) was retired with Ruddle on July 24th.

As a McCleary user, you have also been given new, empty home and scratch directories for McCleary on our Palmer filesystem and a 1 TiB project space on our Gibbs filesystem. Project quotas can be increased to 4 TiB at no cost by sending a request to [hpc@yale.edu](mailto:hpc@yale.edu).

!!! attention "Ruddle Project Data"

	Data previously in `/gpfs/ycga/project/<groupname>/<netid>` can now be found at `/gpfs/ycga/work/<groupname>/<netid>`. The `project` symlink in your home directory links to your Gibbs project space, **not** your YCGA storage. 

### Researchers with Purchased Storage

If you have purchased space on `/gpfs/ycga `or `/gpfs/ysm` that has not expired, we have migrated your allocation. **This is the only data that the YCRC automatically migrated from Farnam to McCleary.**  

If you have purchased storage on `/gpfs/ysm` that has expired as of December 31st 2022, you should have received a separate communication from us with information on purchasing replacement storage on Gibbs (which is available on McCleary).
 
If you have any questions or concerns about what has been moved to McCleary and when, please reach out to us.

### Storage@Yale (SAY) Shares

Storage@Yale shares are available on McCleary, but only on the `transfer` node. 
To access your SAY data, make sure to login to the `transfer` node and then copy your data to either `project` or `scratch`. 
Note, this is different than how Ruddle was set up, where SAY shares were available on all nodes. 
