# Courses

The YCRC Grace and Farnam clusters can be made available for Yale courses with a suitable computational component. The YCRC hosts over a dozen courses on the clusters every semester.

!!! warning
    All course allocations are temporary. All associated accounts and data will be removed one month after the last day of exams for that semester.


!!! info "For Instructors"
    If you are interested in using a YCRC cluster in your Yale course, contact us at research.computing@yale.edu. If at all possible, please let us know of your interest in using a cluster at least two weeks prior to start of classes so we can plan accordingly, even if you have used the cluster in a previous semester.


## Course ID

Your course will be give a specific `courseid` based on the Yale course catalog number. This `courseid` will be used in the course account names, web portal and, if applicable, node reservation.

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

*If* the instructor has coordinated with the YCRC for dedicated nodes for the course, they are available via a "reservation". The nodes can be requested using the `--reservation=courseid` flag. See our [Slurm documentation](/clusters-at-yale/job-scheduling/) for more information on submitting jobs. In each of the following examples, replace `courseid` with the id given to your course. Jobs on course reservations are subject to the restrictions of their parent partition (e.g. 24 hour walltime limit on `day` or 2-day walltime limit on `gpu`). If your jobs need to exceed those restrictions, please have your instructor or TF contact us.

Course members are welcome to use the public partitions of the cluster. However, we request that students [be respectful](/clusters-at-yale/access/accounts/) in their usage as not to disrupt ongoing research work.

### Interactive Jobs

```
salloc -p day --reservation=courseid
```

or if the reservation is for GPU nodes

```
salloc -p gpu --gpus=1 --reservation=courseid
```

### Batch Jobs

Add the following to your submission script:

```
#SBATCH --reservation=courseid
```

### Web Portal

In any of the app submission forms, type the `courseid` into the "Reservation" field. For standard (non-gpu) nodes, select `day` (Grace) or `general` (Farnam) in the "Partition" field. If your node reservation contains GPU-enabled nodes, select `gpu`.

Any course-specific apps listed under the "Courses" dropdown will automatically send all submitted jobs to the reservation, if one exists.

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

    # project directory on Grace
    setfacl -m u:netid:rX /gpfs/gibbs/project/courseid/courseid_netid

    # project directory on Farnam
    setfacl -m u:netid:rX /gpfs/ysm/project/courseid/courseid_netid
    ```

1. Log in as your research account. Check that you can access the above paths.

1. Move to the `transfer` node with `ssh transfer`. If you are transferring a lot of data, open a [tmux](/clusters-at-yale/guides/tmux/) session so the transfer can continue if you disconnect from the cluster.

1. Initiate a copy of the desired data using `rsync`. For example:

    ```
    mkdir /gpfs/gibbs/project/group/netid/my_course_data
    rsync -av /gpfs/gibbs/project/courseid/courseid_netid/mydata /gpfs/gibbs/project/group/netid/my_course_data
    ```








