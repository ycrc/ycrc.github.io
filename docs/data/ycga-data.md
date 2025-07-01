# YCGA Data

Data associated with YCGA projects and sequencers are located on the YCGA storage system, accessible at `/gpfs/ycga/sequencers` on [McCleary](/clusters/mccleary).

## YCGA Access Policy

The McCleary high-performance computing system has specific resources that are dedicated to
YCGA users. This includes a slurm partition (‘ycga’) and a large parallel storage system
(/gpfs/ycga). The following policy guidelines govern the use of these resources on McCleary for
data storage and analysis.

### Yale University Faculty User
1. All Yale PIs using YCGA for library preparation and/or sequencing will have an
additional 5 TB storage area called ‘work’ for data storage. This is in addition to the 5
TB storage area called ‘project’ that all McCleary groups receive.
2. Currently, neither work or project storage is backed up. Users are responsible for
protecting their own data.
3. All Fastq files are available on the /gpfs/ycga storage system for one year. After that, the
files are available in an archive that allows self-service retrieval, as described below. Issues or questions about archived data can be addressed to ycga@yale.edu.
4. Users processing sequence data on McCleary may submit their jobs to the
‘ycga’ partition. 
5. Members of Yale PI labs using YCGA for library preparation and/or sequencing may
apply for accounts on McCleary with PI’s approval.
6. Each Yale PI lab will have a dedicated 'work' directory to store their data, and permission
to lab members will be granted with the authorization of the respective PI. Furthermore,
such approval will be terminated upon request from the PI or termination of Yale Net ID.
7. Lab members moving to a new university will get access to HPC resources for an
additional six months only upon permission from Yale PI. If Yale NetID is no longer
accessible, former Yale members who were YCGA users should request a Sponsored
Identity NetID from their business office. Sponsored Identity NetIDs will be valid for six
months. Such users will also need to request VPN access.
8. A PI moving to a new university to establish their lab will have access to their data for
one year from the termination of their Yale position. During this time, the PI or one lab
member from the new lab will be provided access to the HPC system. Request for Guest
NetID should be made to their business office. Guest NetID will be valid for one year.
9. Any new Yale faculty member will be given access to McCleary once they start using
YCGA services.

### External Collaborators
1. Access to McCleary can be granted to collaborating labs, with the authorization of the
respective Yale PI. A maximum of one account per collaborating lab will be granted.
Furthermore, such approval will be terminated upon request from the PI.
This requires obtaining a [Sponsored Netid](/clusters-at-yale/access/accounts/#external-collaborators).
The expectation is that the collaborator, with PI consent, will
download data from the McCleary HPC system to their own internal system for data
analysis.

### Non-Yale Users
 Users not affiliated with Yale University will not be provided access to the McCleary high-performance computing system.

## YCGA Data Retention Policy

YCGA-produced sequence data is initially written to YCGA's main storage system, which is located in the main HPC datacenter at Yale's West Campus. Data stored there is protected against loss by software RAID.  Raw basecall data (e.g. bcl files) is immediately transformed into DNA sequences (fastq files).

- ~45 days after sequencing, the raw files are deleted.
- ~60 days after sequencing, the fastq files are written to an archive.  This archive exists in two geographically distinct copies for safety.
- ~365 days after sequencing, all data is deleted from main storage.  Users continue to have access to the data via the archive.  Data is retained on the archive indefinitely.  See
below for instructions for retrieving archived data.

All compression of sequence data is lossless.  Gzip (extension '.gz') is used for data stored on the primary storage.  Illumina sequence files archived prior to 2024 used Quip compression.  (extension '.qp'; see [below](#using-archived-data)).  More recent archived files are stored as Gzip files.
Disaster recovery is provided by the archive copy.

## Accessing Sequence Data

YCGA will send you an email informing you that your data is ready, and will include a url that looks like:
http://fcb.ycga.yale.edu:3010/_randomstring_/_sample_

!!! tip
For standard Illumina data (not 10X/singlecell or pacbio data) 
you can browse to the YCGA-provided URL and open ruddle_paths.txt.  It contains the 
true locations of the files.

### Brief overview of YCGA data delivery
Data produced by YCGA’s instruments is written to specific folders on McCleary in /gpfs/ycga/sequencers.  That space is managed by YCGA and does not count against your disk quota.  You will usually receive a link to your data of this general form: http://fcb.ycga.yale.edu:3010/randomstring/sample

You *may* use that link to download the data to your local computer.  However, most users prefer to work with their data on McCleary.  In that case, there is no need to download or copy the data; instead, you can directly link to and access the files as explained below.  

YCGA maintains this primary sequence data (typically fastq.gz files) on McCleary disk storage for a defined retention period; currently one year.  The data is also saved to a long term archive shortly after being generated.  After the retention period expires, the data is deleted from disk storage but is still available for download from the archive.

### Restricting access to sequencing data to improve security
Effective October 1st, 2024, we tightened permissions and restricted access to fastq sequence data on the Yale McCleary cluster to the group that submitted the sample.  The change only impacts data in directories managed by YCGA; it does not impact sequencing data in your directories.  If you are unable to access data to which you believe you should have access, please contact YCRC support at research.support@yale.edu

!!! tip
To list all members of your groups, go to [http://ood-mccleary.ycrc.yale.edu](http://ood-mccleary.ycrc.yale.edu), navigate to the user portal, and click on My Groups.

If you frequently require access to another group’s sequencing data, we recommend asking the group’s PI to add you to their group, giving you access to all of their sequencing data.  To do that, have the PI send an email to research.computing@yale.edu.


### Accessing current data
Sequencing data that is still within the retention period can be directly accessed in a variety of ways.  You can use the URL that YGCA provided you to do a direct download, either to your own storage on the cluster, or to your own computer.  This can be done using any standard http download tool: a browser, wget, curl, cyberduck, etc.  However, these files are typically very large, and making copies of them will consume your disk space.  It is usually better to make links to the files that YCGA maintains.  Below, we explain how to do that for each sequencer type.

#### Illumina (not 10x) data:  
We recommend that you use the ycgaFastq utility to make links to the fastq files.  ycgaFastq is part of the ycga-public module.  To make links, on any node on McCleary, do:

```bash
$ module load ycga-public
$ ycgaFastq fcb.ycga.yale.edu:3010/randomstring/sample
```
If the run has been archived and deleted, ycgaFastq will retrieve the data

ycgaFastq has several alternative invocations:

If you don't know the URL, you can use the 
sample submitter's netid and the flowcell (run) name:

```bash
$ ycgaFastq rdb9 AHFH66DSXX
```

If you have a path to the original location of the sequencing data, ycgaFastq can retrieve the data using that, even if the run has been archived and deleted:
```bash
$ ycgaFastq /ycga-gpfs/sequencers/illumina/sequencerD/runs/190607_A00124_0104_AHLF3MMSXX/Data/Intensities/BaseCalls/Unaligned-2/Project_Lz438
```

If you have a ruddle_paths.txt file that contains the paths to all of the data files in a dataset, you can
use ycgaFastq as well:

```bash
$ ycgaFastq ruddle_paths.txt
```

ycgaFastq can be used in a variety of other ways to retrieve data.  For more information, see the [documentation](http://campuspress.yale.edu/knightlab/ruddle/ycgafastq) or contact us.

#### 10x or Pacbio data
We recommend that you use the URLFetch utility to make links to the fastq files.  ycgaFastq is part of the ycga-public module.  To make links, on any node on McCleary, do:

```bash
module load ycga-public
URLFetch http://fcb.ycga.yale.edu:3010/randomstring/folder
```

### Accessing archived data 

The sequence archive has been moved from Storage@Yale to AWS Deep Glacier.  This was done for several reasons, including improved performance, security, reliability, and cost.
However, retrieving data from Deep Glacier requires a two step process: an initial retrieval request, followed by the actual download.  Normal retrieval requests take 48 hours, while expedited requests take 12 hours.  Expedited requests are 8x more expensive for YCGA, so please use normal requests when possible.

In order to make this process as convenient as possible, we have developed a web-based archive browser [http://archive.ycga.yale.edu](http://archive.ycga.yale.edu) that you can use to request an archived file.  This browser works for all data types: Illumina, 10x, and Pacbio.  

After submitting your request, the data will be restored in AWS and downloaded to temporary space on McCleary.  You will receive an email when it is ready, at which time you should copy it to your own space.

You may also continue to use the ycgaFastq command for archived Illumina data.  This command currently still accesses the previous Storage@Yale archive, but will soon be migrated to use the AWS Deep Glacier archive.  At that point, ycgaFastq will block for 12 hours while the data is retrieved.


### Using archived data

After downloading an archive tar file, you can unpack it using the tar command:

``` bash
cd ~/scratch60/somedir
tar –xvf /gpfs/ycga/sequencers/restored/netid/file.tar
```

Inside the project tar files are the fastq files.  For older archived data the fastq files have been further compressed using quip. If your pipeline cannot read quip files
directly, you will need to uncompress them before using them.

``` bash
module load Quip
quip –d M20_ACAGTG_L008_R1_009.fastq.qp
```

For your convenience, we have a tool, `restore`, that will untar and uncompress all quip files in a tar file:

``` bash
module load ycga-public
restore –t /SAY/archive/YCGA-729009-YCGA/archive/path/to/file.tar
```

Restore spends most of the time running quip. You can parallelize and speed up that process using the `-n` flag.

``` bash
restore –n 32 ...
```

!!! tip
    When retrieving data, run untar/unquip as a job on a compute node, **not a login node** and make sure to allocate sufficient resources to your job, e.g. `--c 32` 

## Example:

#### step 1
Recover the tar file using the sequence archive browser.  The browser will stash the tar file in a temporary location, and send you an email with that location.  For example:
/gpfs/ycga/sequencers/restored/rdb9/161021_D00596R_0145_BCA1H7ANXX_0_Project_Rdb9.tar

#### step 2
Copy the file to your own space, e.g. ~/scratch
```bash
cp /gpfs/ycga/sequencers/restored/rdb9/161021_D00596R_0145_BCA1H7ANXX_0_Project_Rdb9.tar ~/scratch
cd ~/scratch
```

#### step 3
Create a batch script to uncompress the data

job.script
```bash
#!/bin/bash
#SBATCH -c 32 -p ycga
#SBATCH --mail-type=all

module load ycga-public
restore -v -t 161021_D00596R_0145_BCA1H7ANXX_0_Project_Rdb9.tar
```

#### step 4
Submit the job

```bash
sbatch job.script
```


The restored fastq files will written to a directory like this: 
```bash
161021_D00596R_0145_BCA1H7ANXX/Data/Intensities/BaseCalls/Unaligned/Project_Rdb9/...
```

