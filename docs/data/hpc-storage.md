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

Project quotas are global to the whole project space, so if the group ownership on a file is your group, it will count towards your quota, regardless of its location within `project`. This can occasionally create confusion for users who belong to multiple groups and they need to be mindful of which files are owned by which of their group affiliations to ensure proper accounting.

#### Purchased Storage

Quota: varies

Storage purchased for the dedicated use by a single group or collection of groups provides similar functionality as `project` storage and is also not backed up.
See [below](/data/#purchase-additional-storage) for details on purchasing storage. 
Purchased storage, if applicable, is located on the Gibbs filesystem in a `/gpfs/gibbs/pi/` directory under the group's name. 

Unlike project space described above, all files in your purchased storage count towards your quotas, regardless of file ownership.

### 60-Day Scratch

Quota: 10 TiB and 15,000,000 files per group

60-day scratch is intended to be used for storing temporary data. Any file in this space older than 60 days will automatically be deleted. We send out a weekly warning about files we expect to delete the following week. Like project, scratch quota is shared by your entire research group. If we begin to run low on storage, you may be asked to delete files younger than 60 days old. **Artificial extension of scratch file expiration is forbidden without explicit approval from the YCRC. Please [purchase storage](/data/#purchase-additional-storage) if you need additional longer term storage.**

You can access this space through a symlink, or shortcut, in your home directory called `palmer_scratch` (or `scratch60` on [Milgram](/clusters/milgram)). See our [Sharing Data](/data/permissions) documentation for instructions on sharing data in your scratch space with other users.

## Check Your Usage and Quotas

To inspect your current usage, run the command `getquota`. Here is an example output of the command:

``` text
This script shows information about your quotas on grace.
If you plan to poll this sort of information extensively,
please contact us for help at hpc@yale.edu

## Usage Details for support (as of Jan 25 2023 12:00)
Fileset                User  Usage (GiB) File Count   
---------------------- ----- ---------- -------------
gibbs:project          ahs3         568       121,786
gibbs:project          kln26        435       423,219
gibbs:project          ms725        233       456,736
gibbs:project          pl543        427     1,551,959
gibbs:project          rdb9        1952     1,049,346
gibbs:project          tl397        605     2,573,824
----
gibbs:pi_support       ahs3           0             1
gibbs:pi_support       kln26       5886    14,514,143
gibbs:pi_support       ms725      19651     2,692,158
gibbs:pi_support       pl543        328       142,936
gibbs:pi_support       rdb9        1047       165,553
gibbs:pi_support       tl397        175       118,038

## Quota Summary for support (as of right now [*palmer stats are gathered once a day])
Fileset                Type    Usage (GiB)  Quota (GiB) File Count    File Limit    Backup    Purged   
---------------------- ------- ------------ ----------- ------------- ------------- --------- ---------
palmer:home.grace      USR               63         125       216,046       500,000 Yes       No        
gibbs:project          GRP             3832       10240     3,350,198    10,000,000 No        No        
palmer:scratch         GRP                0       10240           903    15,000,000 No        60 days        
gibbs:pi_support       FILESET        27240       30720    17,647,694    22,000,000 No        No
```

The per-user breakdown is only generated periodically, and the summary at the bottom is close to real-time. Purchased storage allocations will only appear in the `getquota` output for users who have data in that directory.

## Purchase Additional Storage

For long-term allocations, additional project storage spaces can be purchased on one of our shared filesystems, which provides similar functionality to the primary project storage. This storage currently costs $280/TiB (minimum of 10 TiB, with exact pricing to be confirmed before a purchase is made). The price covers all costs, including administration, power, cooling, networking, etc. YCRC commits to making the storage available for 5 years from the purchase date, after which the storage allocation will need to be renewed, or the allocation will expire and be removed (see [Storage Expiration Policy](https://research.computing.yale.edu/services/high-performance-computing/storage-expiration-policy)).

For shorter-term or smaller allocations, we have a monthly billing option. More details on this option can be found [here](https://research.computing.yale.edu/billing-hpc-services) (CAS login required).

Please note that, as with existing project storage, purchased storage will not be backed up, so you should make arrangements for the safekeeping of critical files off the clusters. Please [contact us](/#get-help) with your requirements and budget to start the purchasing process.

Purchased storage, as with all storage allocations, are subject to corresponding file count limit to preserve the health of the shared storage system. The file count limits for different size allocations are listed above. 
If you need additional files beyond your limit, contact us to discuss as increases may be granted on a case-by-case basis and at the YCRC's discretion.

| Allocation Quota | File Count Limit |
|------------------|------------------|
| < 50 TiB         | 10 million       |
| 50-99 TiB        | 20 million       |
| 100-499 TiB      | 40 million       |
| 500-999 TiB      | 50 million       |
| >= 1 PiB         | 75 million       |



## HPC Storage Best Practices

### Stage Data

Large datasets are often stored off-cluster on departmental servers, Storage@Yale, in cloud storage, etc.
If these data are too large to fit in your current quotas and you do not plan on purchasing more storage (see above), you must 'stage' your data.
Since the _permanent_ copy of the data remains on off-cluster storage, you can [transfer](/data/transfer/) a working copy to `palmer_scratch`, for example.
Both Grace and McCleary have dedicated `transfer` partitions where you can submit long-running transfer jobs.
When your computation finishes you can remove the copy and transmit or copy results to a permanent location.
Please see the [Staging Data](/data/staging/) documentation for more details and examples.

### Prevent Large Numbers of Small Files

The parallel filesystems the clusters use perform poorly with very large numbers of small files.
This is one reason we enforce file count quotas.
If you are running an application that unavoidably make large numbers of files, do what you can to reduce file creation.
Additionally you can reduce load on the filesystem by spreading the files across multiple subdirectories.
Delete unneeded files between jobs and compress or [archive](/data/archive/) collections of files.

