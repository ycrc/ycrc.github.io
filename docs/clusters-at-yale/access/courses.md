# Courses

The YCRC Grace and McCleary clusters can be made available for Yale courses with a suitable computational component. The YCRC hosts over a dozen courses on the clusters every semester.

!!! warning
    All course allocations are temporary. All associated accounts and data will be removed one month after the last day of exams for that semester.


!!! info "For Instructors"
    If you are interested in using a YCRC cluster in your Yale course, contact us at research.computing@yale.edu. If at all possible, please let us know of your interest in using a cluster at least two weeks prior to start of classes so we can plan accordingly, even if you have used the cluster in a previous semester.


## Course ID

Your course will be give a specific `courseid` based on the Yale course catalog number. This `courseid` will be used in the course account names and web portal.

## Course Accounts

All members of a course, including the instructor and TFs will be give temporary course accounts. These accounts take the form of `courseid_netid`. Course accounts are district from any research accounts a course member may already have. Use this account if connecting to the cluster [via `ssh`](https://docs.ycrc.yale.edu/clusters-at-yale/access/ssh/). All course-related accounts are subject to [the same policies and expectation as standard accounts](/clusters-at-yale/access/accounts/). 

## Course Storage

Courses on the YCRC clusters are typically granted a standard 1TiB project storage quota, as well as 125GiB home directory for each course member. If the course needs additional storage beyond the default 1TiB, please contact us at research.computing@yale.edu.

See our [cluster storage documentation](https://docs.ycrc.yale.edu/data/hpc-storage/) for details about the different classifications of storage.

## Course-specific Web Portal

Your course also has a course-specific web portal, based on [Open OnDemand](/clusters-at-yale/access/ood/), accessible via the URL (replacing `courseid` with the id given to your course):

```
courseid.ycrc.yale.edu
```

Course members must use the course URL to log in to course accounts on Open OnDemand--the normal cluster portals are not accessible to course accounts. You will then authenticate using your standard NetID (without the courseid prefix) and password. As with all cluster access, you must be on the [VPN](/clusters-at-yale/access/vpn/) to access the web portal if you are off campus.

## Node Reservations

*If* the instructor has coordinated with the YCRC for dedicated nodes for the course, they are available in an `education` or `education_gpu` partition. The nodes can be requested using the `-p partition_name` flag. See our [Slurm documentation](/clusters-at-yale/job-scheduling/) for more information on submitting jobs. Note you will be sharing the partitions with any other courses that also requested nodes. If your jobs need to exceed the restrictions of the partitions, please have your instructor or TF contact us.

Course members are welcome to use the public partitions of the cluster. However, we request that students [be respectful](/clusters-at-yale/access/accounts/) in their usage as not to disrupt ongoing research work.

### Interactive Jobs

```
salloc -p education 
```

or if your instructor has reserved GPU nodes

```
salloc -p education_gpu --gpus=1
```

### Batch Jobs

Add the following to your submission script:

```
#SBATCH -p education
```

or if your instructor has reserved GPU nodes

```
#SBATCH -p education_gpu --gpus=1
```

### Web Portal

In any of the app submission forms, type the correct paritition name into the "Partition" field.

## Cluster Maintenance

Each cluster is inaccessible twice a year for a three day regularly scheduled maintenance. The maintenance schedule is published [here](https://research.computing.yale.edu/support/hpc/system-status).

Please account for the cluster unavailability when developing course schedules and (for students) completing your assignments.

## End of Semester Course Deletion

As mentioned above, all course allocations are temporary. All associated accounts and data will be removed one month after the last day of exams for that semester. If you would like to retain any data in your course account, please download it prior to the deletion date or, if applicable, submit a request to hpc@yale.edu to transfer the data into your research account. 

A reminder of the removal will be sent to the instructor to see if it needs to be delayed for any incompletes (for example). **Students will not received a reminder.** Instructors, if you would like to retain course materials for future semesters, please copy them off the cluster or to a research account.

### Transfer Data to Research Account

If you have a research account on the cluster, you can transfer any data you want to save from your course account to your research account.

!!! warning
    Make sure there is sufficient free space in your research account storage to accomodate any data you are transferring from your course account using `getquota`.

1. Login to the cluster using your course account either via Terminal or the Shell app in the OOD web portal.

1. Grant your research account access to your course accounts directories (substitute in your courseid and netid in the example).

    ```
    # home directory
    setfacl -m u:netid:rX /home/courseid_netid

    # project directory on Grace and McCleary
    setfacl -m u:netid:rX /gpfs/gibbs/project/courseid/courseid_netid

    ```

1. Log in as your research account. Check that you can access the above paths.

1. Move to the `transfer` node with `ssh transfer`. If you are transferring a lot of data, open a [tmux](/clusters-at-yale/guides/tmux/) session so the transfer can continue if you disconnect from the cluster.

1. Initiate a copy of the desired data using `rsync`. For example:

    ```
    mkdir /gpfs/gibbs/project/group/netid/my_course_data
    rsync -av /gpfs/gibbs/project/courseid/courseid_netid/mydata /gpfs/gibbs/project/group/netid/my_course_data
    ```








