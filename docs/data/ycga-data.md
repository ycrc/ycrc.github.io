# YCGA Data

Data associated with YCGA projects and sequencers are located on the YCGA storage system, accessible at `/gpfs/ycga/sequencers` on [McCleary](/clusters/mccleary).

## YCGA Access Retention Policy

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
files are available in an archive that allows self-service retrieval, as described in the link
above. Issues or questions about archived data can be addressed to ycga@yale.edu.
4. Users processing sequence data on McCleary should be careful to submit their jobs to the
‘ycga’ partition. Jobs submitted to other partitions may incur additional charges.
5. Members of Yale PI labs using YCGA for library preparation and/or sequencing may
apply for accounts on McCleary with PI’s approval.
6. Each Yale PI lab will have a dedicated secure directory to store their data, and permission
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
10. Users not utilizing the YCGA services will not be provided access to McCleary high-
performance computing system.

### External Collaborators
1. Access to McCleary can be granted to collaborating labs, with the authorization of the
respective Yale PI. A maximum of one account per collaborating lab will be granted.
Furthermore, such approval will be terminated upon request from the PI. Request for a
Sponsored Identity NetID should be made to the Yale PI’s business office. Guest NetID
will be valid for one year. The expectation is that the collaborator, with PI consent, will
download data from the McCleary HPC system to their own internal system for data
analysis.

### Non-Yale Users
 Users not affiliated with Yale University will not be provided access to McCleary high-
performance computing system.

## YCGA Data Retention Policy

Illumina sequence data is initially written to YCGA's main storage system, which is located in the main HPC datacenter at Yale's West Campus. Data stored there is protected against loss by software RAID.  Raw basecall data (bcl files) is immediately transformed into DNA sequences (fastq files).

- ~45 days after sequencing, the raw bcl files are deleted.
- ~60 days after sequencing, the fastq files are written to an archive.  This archive exists in two geographically distinct copies for safety.
- ~365 days after sequencing, all data is deleted from main storage.  Users continue to have access to the data via the archive.  Data is retained on the archive indefinitely.  See below for instructions for retrieving archived data.

All compression of sequence data is lossless.  Gzip is used for data stored on the main storage, and quip is used for data stored on the archive.
Disaster recovery is provided by the archive copy.

YCGA will send you an email informing you that your data is ready, and will include a url that looks like:
http://fcb.ycga.yale.edu:3010/_randomstring_/sample_dir_001

You can use that link to download your data in a browser, but if you plan to process the data on McCleary, it is better to make a soft link to the data, rather than copying it.  

To find the actual location of your data, do:
``` bash
$ readlink -f /ycga-gpfs/project/fas/lsprog/tools/external/data/randomstring/sample_dir_001
```

## Illumina sequencing data

For Illumina data (not singlecell or pacbio data), 
you can browse to the YCGA-provided URL and find a file ruddle_paths.txt that contains the 
true locations of the files.

Alternatively, you can use the ycgaFastq tool to easily make soft links to the sequencing files:

```bash
export PATH=$PATH:/gpfs/gibbs/pi/ycga/mane/ycga_bioinfo/bin_May2023
$ ycgaFastq fcb.ycga.yale.edu:3010/randomstring/sample_dir_001
```

ycgaFastq can also be used to retrieve data that has been archived.  The simplest way to do that is to provide
the sample submitter's netid and the flowcell (run) name:

```bash
$ ycgaFastq rdb9 AHFH66DSXX
```

If you have a path to the original location of the sequencing data, ycgaFastq can retrieve the data using that, even if the run has been archived and deleted:
```bash
$ ycgaFastq /ycga-gpfs/sequencers/illumina/sequencerD/runs/190607_A00124_0104_AHLF3MMSXX/Data/Intensities/BaseCalls/Unaligned-2/Project_Lz438
```

If you have a manifest file that contains the paths to all of the data files in a dataset, you can
use ycgaFastq as well:

```bash
$ ycgaFastq manifest.txt
```

ycgaFastq can be used in a variety of other ways to retrieve data.  For more information, see the [documentation](http://campuspress.yale.edu/knightlab/ruddle/ycgafastq) or contact us.

!!! tip
    Original sequence data are archived pursuant to the YCGA retention policy. For long-running projects we recommend you keep a personal backup of your sequence files. If you need to retrieve archived sequencing data, please see our [below](/data/ycga-data/#retrieve-data-from-the-archive).

## Retrieve Data from the Archive

!!! info
__The sequence archive /SAY/archive/YCGa-72009-YCGA-A2 is only mounted on the transfer node
and transfer partition.__

You must ssh to transfer, or submit a job (batch or interactive) to the transfer partition, in order
to access and download archived sequence data.

In the sequencing data archive, a directory exists for each run, holding one or more tar files. There is a main tar file, plus a tar file for each project directory. Most users only need the project tar file corresponding to their data.

Although the archive actually exists in cloud storage, you can treat it as a regular directory tree. Many operations such as `ls`, `cd`, etc. are very fast, since directory structures and file metadata are on a disk cache. However, when you actually read the contents of files the file is retrieved and read into a disk cache.  This can take some time.

Archived runs are stored in the following locations.

| Original location                           | Archive location                                                                 |
|---------------------------------------------|----------------------------------------------------------------------------------|
| `/panfs/`                         | `/SAY/archive/YCGA-729009-YCGA-A2/archive/panfs/`                         |
| `/ycga-ba/`                    | `/SAY/archive/YCGA-729009-YCGA-A2/archive/ycga-ba/`                    |
| `/gpfs/ycga/sequencers/illumina/` | `/SAY/archive/YCGA-729009-YCGA-A2/archive/ycga-gpfs/sequencers/illumina/` |
| `/gpfs/gibbs/pi/ycga/pacbio/` | `/SAY/archive/YCGA-729009-YCGA-A2/archive/pacbio/` |

You can directly copy or untar the project tarfile into a scratch directory.

!!! info
Very large tar files over 500GB, sometimes fail to download.  If you run into problems, contact us at hpc@yale.edu and we can
manually download it.


``` bash
cd ~/palmer_scratch/somedir
tar –xvf /SAY/archive/YCGA-729009-YCGA-A2/archive/path/to/file.tar
```

Inside the project tar files are the fastq files, which have been compressed using `quip`. If your pipeline cannot read quip files directly, you will need to uncompress them before using them.

``` bash
module load Quip
quip –d M20_ACAGTG_L008_R1_009.fastq.qp
```

If you have trouble locating your files, you can use the utility `locateRun`, using any substring of the original run name. `locateRun` is in the ycga-public module.

``` bash
module load ycga-public
locateRun C9374AN
```

!!! tip
    When retrieving data, run untar/unquip as a job on a compute node, **not a login node** and make sure to allocate sufficient resources to your job, e.g. `–c 20 --mem=100G`.

!!! tip
    The ycgaFastq tool can also be used to recover archived data.  See [above](/data/ycga-data/#access-sequencing-data). 

### Example

Imagine that user rdb9 wants to restore data from run BHJWZZBCX3

**step 1**

Get session on transfer partition
``` bash 
salloc -p transfer
module load ycga-public
```

**step 2**

Find the run location
``` bash
$ locateRun BHJWZZBCX3
/ycga-gpfs/sequencers/illumina/sequencerV/runs/210305_D00306_1337_BHJWZZBCX3.deleted
/SAY/archive/YCGA-729009-YCGA-A2/archive/ycga-gpfs/sequencers/illumina/sequencerV/runs/210305_D00306_1337_BHJWZZBCX3
```

Note that the original run location has been deleted, but the archive location is listed.

**step 3**

List the contents of the archived run, and locate the desired project tarball:
``` bash
$ ls -1 /SAY/archive/YCGA-729009-YCGA-A2/archive/ycga-gpfs/sequencers/illumina/sequencerV/runs/210305_D00306_1337_BHJWZZBCX3
210305_D00306_1337_BHJWZZBCX3_0.tar
210305_D00306_1337_BHJWZZBCX3_0_Unaligned_Project_Jdm222.tar
210305_D00306_1337_BHJWZZBCX3_1_Unaligned-1_Project_Rdb9.tar
210305_D00306_1337_BHJWZZBCX3_2021_05_09_04:00:36_archive.log
```

We want `210305_D00306_1337_BHJWZZBCX3_1_Unaligned-1_Project_Rdb9.tar`, matching our netid.

**step 4**

First, copy the tarball to scratch.  To do this you must be on the transfer partition or transfer node, since /SAY is only mounted there.

``` bash
cd ~/palmer_scratch
rsync -L -v /SAY/archive/YCGA-729009-YCGA-A2/archive/ycga-gpfs/sequencers/illumina/sequencerV/runs/210305_D00306_1337_BHJWZZBCX3/210305_D00306_1337_BHJWZZBCX3_1_Unaligned-1_Project_Rdb9.tar .
```

**step 5**

Submit a batch job to use the restore utility to uncompress the fastq files from the tar file.
In our example we'll use 32 cpus.  This is not done using the transfer partition, but rather the day partition, since day will allow you more cpus.  The restore will likely
take several minutes. To see progress, you can use the `-v` flag.

Put the following code in a batch script (e.g. myrestore.sh):

``` bash
#/bin/bash
#SBATCH -c 32
#SBATCH -p day

module load ycga-public
restore -v -n $SLURM_CPUS_PER_TASK -t 210305_D00306_1337_BHJWKHBCX3_1_Unaligned-1_Project_Rdb9.tar
```

Then submit the job using sbatch:

``` bash
sbatch myrestore.sh
```

The restored fastq files will written to a directory like this: 
``` bash 
210305_D00306_1337_BHJWZZBCX3/Data/Intensities/BaseCalls/Unaligned*/Project_*
```
