# Courses

The YCRC Bouchet cluster can be made available for Yale courses with a suitable computational component. The YCRC hosts over a dozen courses on the clusters every semester.

!!! warning
    All course allocations are temporary. All associated accounts and data will be removed one month after the last day of exams for that semester.

## For Instructors
 If you are interested in using a YCRC cluster in your Yale course, please fill out the course account request form. If at all possible, please let us know of your interest in using a cluster at least two weeks prior to start of classes so we can plan accordingly, even if you have used the cluster in a previous semester.

[Submit Course Account Request](https://research.computing.yale.edu/course-request){ .md-button }


## Course ID

Your course will be give a specific `courseid` based on the Yale course catalog number. This `courseid` will be used in the course account names and web portal.

## Course Accounts

All members of a course, including the instructor and TFs will be given temporary course accounts. These accounts take the form of `courseid_netid`. Course accounts are distinct from any research accounts a course member may already have. As with all cluster access, you must be on the [VPN](/clusters-at-yale/access/vpn/) to access the web portal if you are off campus.

All course-related accounts are subject to [the same policies and expectation as standard accounts](/clusters-at-yale/access/accounts/).

### Course-specific Web Portal

Your course also has a course-specific web portal, based on [Open OnDemand](/clusters-at-yale/access/ood/), accessible via the URL (replacing `courseid` with the id given to your course):

```
courseid.ycrc.yale.edu
```

Course members must use the course URL to log in to course accounts on Open OnDemand--the normal cluster portals are not accessible to course accounts. You will then authenticate using your standard NetID (without the courseid prefix) and password. 

!!! warning 
    If you only have a course participant account, but try to log in through the cluster web portal URL, you will get an error in the browser:
    ```
    Error -- can't find user for cpsc424_test
    Run 'nginx_stage --help' to see a full list of available command line options.
    ```
    Use the URL for your course web portal will resolve the problem.

### SSH Access

To access your course account via terminal and [`ssh` authentication](https://docs.ycrc.yale.edu/clusters-at-yale/access/ssh/), connect to the cluster using your course account name. For example:

```
ssh courseid_netid@bouchet.ycrc.yale.edu
```

If you already have a permanent researcher account (one that is just your NetID) on one of the clusters, the course account will already be setup with any ssh keys previously uploaded to your researcher account. To add a new key, [upload your new key](https://sshkeys.ycrc.yale.edu/) and it will be delivered to all of your accounts within a few minutes.


## Course Storage

Courses on the YCRC clusters are typically granted a standard 4TiB project storage quota, as well as 125GiB home directory for each course member. If the course needs additional storage beyond the default 4TiB, please contact us at research.computing@yale.edu.

See our [cluster storage documentation](https://docs.ycrc.yale.edu/data/hpc-storage/) for details about the different classifications of storage.



## Partitions for Courses

Compute resources for courses are available in the `education` or `education_gpu` partitions. You can request these nodes for your jobs using the `-p partition_name` flag. See our [Slurm documentation](/clusters-at-yale/job-scheduling/) for more information on submitting jobs. Note you will be sharing these partitions with other courses. If your jobs need to exceed the restrictions of the partitions, please have your instructor or TF contact us.

Course members are welcome to use the public partitions of the cluster. However, we request that students [be respectful](/clusters-at-yale/access/accounts/) in their usage as not to disrupt ongoing research work.

### Interactive Jobs

```
salloc -p education 
```

or if you need to request a GPU

```
salloc -p education_gpu --gpus=1
```

### Batch Jobs

Add the following to your submission script:

```
#SBATCH -p education
```

or if you need to request a GPU

```
#SBATCH -p education_gpu --gpus=1
```

### Web Portal

In any of the app submission forms, type the correct paritition name into the "Partition" field.

## Cluster Maintenance

Bouchet is inaccessible once a year for a regularly scheduled maintenance. The maintenance schedule is published [here](https://research.computing.yale.edu/system-status).

Please account for the cluster unavailability when developing course schedules and (for students) completing your assignments.

## End of Semester Course Deletion

As mentioned above, all course allocations are temporary. All associated accounts and data will be removed one month after the last day of exams for that semester. If you would like to retain any data in your course account, please download it prior to the deletion date or, if applicable, submit a request to hpc@yale.edu to transfer the data into your research account. 

A reminder of the removal will be sent to the instructor to see if it needs to be delayed for any incompletes (for example). **Students will not receive a reminder.** Instructors, if you would like to retain course materials for future semesters, please submit a request to hpc@yale.edu to have the materials stored in our course repository. 

### Transfer Data to Research Account

If you have a research account on Bouchet, you can transfer data you want to save from your course account's home directory to your research account.

!!! warning
    Make sure there is sufficient free space in your research account storage to accommodate any data you are transferring from your course account using `getquota`.

!!! Note
    If your course and your research accounts are on different clusters, or if you need to transfer data from your course account's project or scratch directory to your research account, please [contact us](/#get-help) for assistance.

1. Login to the cluster using your course account either via Terminal or the Shell app in the OOD web portal.

1. Grant your research account access to your course account home directory (substitute in your courseid and netid in the example).

    ```
    # home directory
    setfacl -m u:netid:rX /home/courseid_netid
    ```

1. Log in as your research account. Check that you can access the above paths.

1. Move to the `transfer` node with `ssh transfer1`. If you are transferring a lot of data, open a [tmux](/clusters-at-yale/guides/tmux/) session so the transfer can continue if you disconnect from the cluster.

1. Initiate a copy of the desired data using `rsync`. For example:

    ```
    mkdir /nfs/roberts/project/group/netid/my_course_data
    rsync -av /home/courseid_netid/mydata /nfs/roberts/project/group/netid/my_course_data
    ```








