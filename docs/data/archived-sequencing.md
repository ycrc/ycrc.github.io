# YCGA Sequence Data Archive

## Retrieve Data from the Archive

In the sequencing archive on [Ruddle](/clusters/ruddle), a directory exists for each run, holding one or more tar files. There is a main tar file, plus a tar file for each project directory. Most users only need the project tar file corresponding to their data.

Although the archive actually exists on tape, you can treat it as a regular directory tree. Many operations such as `ls`, `cd`, etc. are very fast, since directory structures and file metadata are on a disk cache. However, when you actually read the contents of files the tape is mounted and the file is read into a disk cache.

Archived runs are stored in the following locations.

| Original location                           | Archive location                                                                 |
|---------------------------------------------|----------------------------------------------------------------------------------|
| `/panfs/sequencers`                         | `/SAY/archive/YCGA-729009-YCGA/archive/panfs/sequencers`                         |
| `/ycga-ba/ba_sequencers`                    | `/SAY/archive/YCGA-729009-YCGA/archive/ycga-ba/ba_sequencers`                    |
| `/gpfs/ycga/sequencers/illumina/sequencers` | `/SAY/archive/YCGA-729009-YCGA/archive/ycga-gpfs/sequencers/illumina/sequencers` |

You can directly copy or untar the project tarfile into a scratch directory.

``` bash
cd ~/scratch60/somedir
tar –xvf /SAY/archive/YCGA-729009-YCGA/archive/path/to/file.tar
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
    The ycgaFastq tool can also be used to recover archived data.  See [here](/clusters-at-yale/clusters/ruddle/#access-sequencing-data). 
