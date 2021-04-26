# Archive Your Data

## Clean Out Unnecessary Files

Not every file created during a project needs to be archived. If you proactively reduce the number of extraneous files in your archive, you will both reduce storage costs and increase the usefulness of that data upon retrieval. Common files that can be deleted when archiving data include:

* Compiled codes, such as `.o` or `.pyc` files. These files will likely not even work on the next system you may restore these data to and they can contribute significantly to your file count limit. Just keep the source code and clean installation instructions.
* Some log files. Many log created by the system are not necessary to store indefinitely. Any Slurm logs from failed runs (prior to a successful run) or outputs from Matlab (e.g. `hs_error_pid*.log`, `java.log.*`) can often safely be ignored.
* Crash files such are core dumps (e.g. `core.*`, `matlab_crash_dump.`).

## Compress Your Data

Most archive locations (S@Y Archive Tier, Google Drive) perform much better with a smaller number of larger files. In fact, Google Shared Drives have a file count limit of 400,000 files. Therefore, it is highly recommended that your compress, using zip or [tar](/online-tutorials), portions of your data for ease of storage and retrieval.
For example, to create a compressed archive of a directory you can do the following:

```sh
tar -cvzf archive-2021-04-26.tar.gz ./data_for_archival

```
This will create a new file (`archive-2021-04-26.tar.gz`) which contains all the data from within `data_for_archival` and is compressed to minimize storage requirements.
This file can then be transferred to any off-site backup or archive location.

## List and Extract Data From Existing Archive

You can list the contents of an archive file like this:

```sh
tar -ztvf archive-2021-04-26.tar.gz
```
which will print the full list of every file within the archive.
The clusters also have the `lz` tool installed that provides a shorter way to list the contents:

```sh
lz archive-2021-04-26.tar.gz
```

You can then extract a single file from a large tar-file without decompressing the full thing:

```sh
tar -zxvf archive-2021-04-26.tar.gz path/to/file.txt
```
There is an alternative syntax that is more legible:

```sh
tar --extract --file=archive-2021-04-26.tar.gz file.txt
```
Either should work fine on the clusters.

## Tips for S@Y Archive Tier (or Any Tape Archive)

The archive tier of Storage@Yale is a tape-based system. To use it effectively, you need to be aware of how it works and follow some best practices.

When you write to the archive, you are actually copying to a large hard disk-based cache, so writes are normally fast. Your copy will appear to complete as soon as the file is in the disk cache. It is NOT yet on tape. In the background, the system will flush files to tape and delete them from the cache. If you read a file very soon after you write it, it is probably still in the cache, and your read will be quick.

However, once some time has elapsed and the file has been moved to tape, it can take several minutes or even longer to copy a file from the archive. This is because the system has to:

1. Wait until a tape drive is free (there are a limited number of drives)
1. Load the correct tape
1. Find the file on the tape
1. And finally, copy it out to a disk cache in front of the tape

Only then is the file available to your copy command. There are only a handful of tape drives, so you may have to wait for one to be available.

Some key takeaways:

* Operations that only read the metadata of files will be fast (ls, find, etc) even if the file is on tape, since metadata is kept in the disk cache.
* Operations that actually read the file (cp, wc -l, tar, etc) will require recovering the entire file to disk cache first, and can take several minutes or longer depending on how nusy the system is.
* If many files will need to be recovered together, it is much better to store them as a single file first with tar or zip, then write that file to the archive.
* Please do NOT write huge numbers of small files. They will be difficult or impossible to restore in large numbers.
* Please do NOT do repetitive operations like rsyncs to the archive, since they overload the system.
