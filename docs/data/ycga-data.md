# YCGA Data

Data associated with YCGA projects and sequencers are located on the YCGA storage system, accessible at `/gpfs/ycga/sequencers` on [Ruddle](/clusters/ruddle) and, coming soon, on [McCleary](/clusters/farnam-decommission).


## YCGA Data Retention Policy

Illumina sequence data is initially written to YCGA's main storage system, which is located in the main HPC datacenter at Yale's West Campus. Data stored there is protected against loss by software RAID.  Raw basecall data (bcl files) is immediately transformed into DNA sequences (fastq files).

- ~45 days after sequencing, the raw bcl files are deleted.
- ~60 days after sequencing, the fastq files are written to an archive.  This archive exists in two geographically distinct copies for safety.
- ~365 days after sequencing, all data is deleted from main storage.  Users continue to have access to the data via the archive.  Data is retained on the archive indefinitely.  See below for instructions for retrieving archived data.

All compression of sequence data is lossless.  Gzip is used for data stored on the main storage, and quip is used for data stored on the archive.
Disaster recovery is provided by the archive copy.

YCGA will send you an email informing you that your data is ready, and will include a url that looks like:
http://fcb.ycga.yale.edu:3010/_randomstring_/sample_dir_001

You can use that link to download your data in a browser, but if you plan to process the data on Ruddle, it is better to make a soft link to the data, rather than copying it.  

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
$ /home/bioinfo/software/knightlab/bin/ycgaFastq  fcb.ycga.yale.edu:3010/randomstring/sample_dir_001
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

ycgaFastq can be used in a variety of other ways to retrieve data.  For more information, see the [documentation](http://campuspress.yale.edu/knightlab/ruddle/ycgafastq) or contact us.

!!! tip
    Original sequence data are archived pursuant to the YCGA retention policy. For long-running projects we recommend you keep a personal backup of your sequence files. If you need to retrieve archived sequencing data, please see our [below](/data/ycga-data/#retrieve-data-from-the-archive).

## Retrieve Data from the Archive

In the sequencing data archive, a directory exists for each run, holding one or more tar files. There is a main tar file, plus a tar file for each project directory. Most users only need the project tar file corresponding to their data.

Although the archive actually exists in cloud storage, you can treat it as a regular directory tree. Many operations such as `ls`, `cd`, etc. are very fast, since directory structures and file metadata are on a disk cache. However, when you actually read the contents of files the file is retrieved and read into a disk cache.  This can take some time.

Archived runs are stored in the following locations.

| Original location                           | Archive location                                                                 |
|---------------------------------------------|----------------------------------------------------------------------------------|
| `/panfs/sequencers`                         | `/SAY/archive/YCGA-729009-YCGA-A2/archive/panfs/sequencers`                         |
| `/ycga-ba/ba_sequencers`                    | `/SAY/archive/YCGA-729009-YCGA-A2/archive/ycga-ba/ba_sequencers`                    |
| `/gpfs/ycga/sequencers/illumina/sequencers` | `/SAY/archive/YCGA-729009-YCGA-A2/archive/ycga-gpfs/sequencers/illumina/sequencers` |
| `/gpfs/ycga/sequencers/pacbio` | `/SAY/archive/YCGA-729009-YCGA-A2/archive/ycga-gpfs/sequencers/pacbio` |

You can directly copy or untar the project tarfile into a scratch directory.

!!! info
Very large tar files over 500GB, sometimes fail to download.  If you run into problems, contact us at hpc@yale.edu and we can
manually download it.


``` bash
cd ~/scratch60/somedir
tar –xvf /SAY/archive/YCGA-729009-YCGA-A2/archive/path/to/file.tar
```

Inside the project tar files are the fastq files, which have been compressed using `quip`. If your pipeline cannot read quip files directly, you will need to uncompress them before using them.

``` bash
module load Quip
quip –d M20_ACAGTG_L008_R1_009.fastq.qp
```

For your convenience, we have a tool, `restore`, that will download a tar file, untar it, and uncompress all quip files.

``` bash
module load ycga-public
restore –t /SAY/archive/YCGA-729009-YCGA/archive/path/to/file.tar
```

If you have trouble locating your files, you can use the utility `locateRun`, using any substring of the original run name. `locateRun` is in the same module as restore.

``` bash
locateRun C9374AN
```

Restore spends most of the time running quip. You can parallelize and thereby speed up that process using the `-n` flag.

``` bash
restore –n 20 ...
```

!!! tip
    When retrieving data, run untar/unquip as a job on a compute node, **not a login node** and make sure to allocate sufficient resources to your job, e.g. `–c 20 --mem=100G`.

!!! tip
    The ycgaFastq tool can also be used to recover archived data.  See [above](/data/ycga-data/#access-sequencing-data). 

### Example

Imagine that user rdb9 wants to restore data from run BHJWZZBCX3

**step 1**

Initialize compute node with 20 cores
``` bash 
salloc -c 20
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

Use the restore utility to copy and uncompress the fastq files from the tar file.  By default, restore will start 20 threads, which matches our srun above.  The restore will likely take several minutes. To see progress, you can use the `-v` flag.
``` bash
restore -v -t /SAY/archive/YCGA-729009-YCGA-A2/archive/ycga-gpfs/sequencers/illumina/sequencerV/runs/210305_D00306_1337_BHJWZZBCX3/210305_D00306_1337_BHJWKHBCX3_1_Unaligned-1_Project_Rdb9.tar
```

The restored fastq files will written to a directory like this: 
``` bash 
210305_D00306_1337_BHJWZZBCX3/Data/Intensities/BaseCalls/Unaligned*/Project_*
```
