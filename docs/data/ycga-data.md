# YCGA Data

Data associated with YCGA projects and sequencers are located on the YCGA storage system, accessible at `/gpfs/ycga/sequencers` on [McCleary](/clusters/mccleary).

!!! Important
On Oct 1, 2024, we will be tightening access restrictions to the primary sequence data.  More information is available
[here](/data/ycga-permissions).

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
4. Users processing sequence data on McCleary should be careful to submit their jobs to the
‘ycga’ partition. Jobs submitted to other partitions may incur additional charges.
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
- ~365 days after sequencing, all data is deleted from main storage.  Users continue to have access to the data via the archive.  Data is retained on the archive indefinitely.  See below for instructions for retrieving archived data.

All compression of sequence data is lossless.  Gzip is used for data stored on the main storage, and quip is used for data stored on the archive.
Disaster recovery is provided by the archive copy.

## Accessing Sequence Data

YCGA will send you an email informing you that your data is ready, and will include a url that looks like:
http://fcb.ycga.yale.edu:3010/_randomstring_/_sample_

!!!tip
To find the actual location of your data, do:
``` bash
$ readlink -f /gpfs/ycga/work/lsprog/tools/external/data/randomstring/sample_dir_YourSampleNumber
```
For standard Illumina data (not 10X/singlecell or pacbio data) 
you can browse to the YCGA-provided URL and open ruddle_paths.txt.  It contains the 
true locations of the files.

### Retrieving Illumina sequencing data

If you want to copy the data to your own computer, you can use that link to download your data using a browser or a tool such
as wget.  However, if you plan to process the data on McCleary, there are better alternatives.

We recommend using the ycgaFastq tool to link to the sequencing files:
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

!!! tip
    Original sequence data are archived pursuant to the YCGA retention policy. For long-running projects we recommend you keep a personal backup of your sequence files. If you need to retrieve archived sequencing data, please see our [below](/data/ycga-data/#retrieve-data-from-the-archive).

### Retrieving 10X or Pacbio sequencing data
You will be provided with a URL to your data that looks like:
http://fcb.ycga.yale.edu:3010/_randomstring_/sample

If you want to copy the data to your own computer, you can use that link to download your data using a browser or a tool such
as wget.  However, if you plan to process the data on McCleary, there are better alternatives.

We recommend using the URLFetch tool to link to the sequencing files:
```bash
$ module load ycga-public
$ URLFetch fcb.ycga.yale.edu:3010/randomstring/sample
```

URLFetch will simply link to the data if it has not been deleted.  If it is archived and deleted, it will
download a tarball of the data, which you can then untar.


