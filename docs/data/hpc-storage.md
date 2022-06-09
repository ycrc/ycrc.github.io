# HPC Storage

Along with access to the compute clusters we provide each research group with cluster storage space for research data. The storage is separated into three quotas: Home, Project, and 60-day Scratch. Each of these quotas limit both the amount in bytes and number of files you can store. Hitting your quota stops you from being able to write data, and can cause [jobs to fail](/clusters-at-yale/job-scheduling/common-job-failures/#disk-quotas). You can monitor your storage usage by running the `getquota` command on a cluster. No sensitive data can be stored on any cluster storage, except for [Milgram](/clusters/milgram/).

!!! warning "Backups"
    The _only_ storage backed up on every cluster is Home. We do provide local snapshots, covering at least the last 2 days, on Home and Project directories (see below for details). Please see our [HPC Policies](https://research.computing.yale.edu/services/high-performance-computing/hpc-policies#Backups) page for additional information about backups.

## Storage Spaces

For an overview of which filesystems are mounted on each cluster, see the [HPC Resources](/clusters/#storage) documentation.

### Home

Quota: 125 GiB and 500,000 files per person

Your home directory is where your sessions begin by default. Its intended use is for storing scripts, notes, final products (e.g. figures), etc.  Its path is `/home/netid` (where `netid` is your Yale netid) on every cluster. Home storage is backed up daily. If you would like to restore files, please [contact us](/#get-help) with your netid and the list of files/directories you would like restored.

### Project

Quota: 1 TiB and 5,000,000 files per group, expanded to 4 TiB on request

Project storage is shared among all members of a specific group. Project storage is **not backed up**, so we strongly recommend that you have a second copy somewhere off-cluster of any valuable data you have stored in project.

You can access this space through a symlink, or shortcut, in your home directory called `project`. See our [Sharing Data](/data/permissions) documentation for instructions on sharing data in your project space with other users.


#### Purchased Storage

Quota: varies

Storage purchased for the dedicated use by a single group or collection of groups provides similar functionality as `project` storage and is also not backed up.
See [below](/data/#purchase-additional-storage) for details on purchasing storage. 
Purchased storage, if applicable, is located on the Gibbs filesystem in a `/gpfs/gibbs/pi/` directory under the group's name. 

### 60-Day Scratch

Quota: 20 TiB and 15,000,000 files per group

60-day scratch is intended to be used for storing temporary data. Any file in this space older than 60 days will automatically be deleted. We send out a weekly warning about files we expect to delete the following week. Like project, scratch60 quota is shared by your entire research group. If we begin to run low on storage, you may be asked to delete files younger than 60 days old. 

You can access this space through a symlink, or shortcut, in your home directory called `scratch60` (and `palmer_scratch` on [Grace](/clusters/grace)). See our [Sharing Data](/data/permissions) documentation for instructions on sharing data in your scratch space with other users.

## Check Your Usage and Quotas

To inspect your current usage, run the command `getquota`. Here is an example output of the command:

``` text
This script shows information about your quotas on the current gpfs filesystem.
If you plan to poll this sort of information extensively, please contact us
for help at hpc@yale.edu

## Usage Details for hpcprog (as of Nov 20 2019 05:00)
Fileset       User  Usage (GiB) File Count
------------- ----- ---------- -------------
project       ahs3          82        33,788
project       cag94          0             1
project       kln26        366       533,998
project       njc2           0             1
project       pl543        115       259,212
project       tl397        370       529,026
----
scratch60     ahs3           0            89
scratch60     cag94          0             1
scratch60     kln26       2510       714,703
scratch60     njc2           0             1
scratch60     pl543          0             6
scratch60     tl397      13056       282,212

## Quota Summary for hpcprog (as of right now)
Fileset       Type    Usage (GiB)   Quota (GiB)  File Count    File Limit    Backup    Purged
------------- ------- ------------ ----------- ------------- ------------- --------- ---------
home.grace    USR               39         100       190,055       200,000 Yes        No
project       GRP              707        6144     1,611,981     5,000,000 No         No
scratch60     GRP             4054       20480       987,336     5,000,000 No         60 days
```

The per-user breakdown is only generated periodically, and the summary at the bottom is close to real-time. Purchased storage allocations will only appear in the `getquota` output for users who have data in that directory.

## Purchase Additional Storage

For long-term allocations, additional project storage spaces can be purchased on our Gibbs filesystem, which provides similar functionality to the primary project storage. This storage currently costs $200/TiB (minimum of 10 TiB, with exact pricing to be confirmed before a purchase is made). The price covers all costs, including administration, power, cooling, networking, etc. YCRC commits to making the storage available for 5 years from the purchase date, after which the storage allocation will need to be renewed, or the allocation will expire and be removed (see [Storage Expiration Policy](https://research.computing.yale.edu/services/high-performance-computing/storage-expiration-policy)).

For shorter-term or smaller allocations, we have a monthly billing option. More details on this option can be found [here](https://research.computing.yale.edu/billing-hpc-services) (CAS login required).

Please note that, as with existing project storage, purchased storage will not be backed up, so you should make arrangements for the safekeeping of critical files off the clusters. Please [contact us](/#get-help) with your requirements and budget to start the purchasing process.

Purchased storage, as with all storage allocations, are subject to corresponding file count limit to preserve the health of the shared storage system. The file count limits for different size allocations are listed above. 
If you need additional files beyond your limit, contact us to discuss as increases may be granted on a case-by-case basis and at the YCRC's discretion.

| Allocation Quota | File Count Limit |
|------------------|------------------|
| < 50 TiB         | 10 million       |
| 50-99 TiB        | 20 million       |
| 100-499 TiB      | 40 million       |
| >= 500 TiB       | 50 million       |



## HPC Storage Best Practices

### Stage Data

Large datasets are often stored off-cluster on departmental servers, Storage@Yale, in cloud storage, etc.
If these data are too large to fit in your current quotas and you do not plan on purchasing more storage (see above), you must 'stage' your data.
Since the _permanent_ copy of the data remains on off-cluster storage, you can [transfer](/data/transfer/) a working copy to `scrach60`, for example.
Both Grace and Farnam have dedicated `transfer` partitions where you can submit long-running transfer jobs.
When your computation finishes you can remove the copy and transmit or copy results to a permanent location.
Please see the [Staging Data](/data/staging/) documentation for more details and examples.

### Prevent Large Numbers of Small Files

The parallel filesystems the clusters use perform poorly with very large numbers of small files.
This is one reason we enforce file count quotas.
If you are running an application that unavoidably make large numbers of files, do what you can to reduce file creation.
Additionally you can reduce load on the filesystem by spreading the files across multiple subdirectories.
Delete unneeded files between jobs and compress or [archive](/data/archive/) collections of files.
