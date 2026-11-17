# Archive Your Data

## Clean Out Unnecessary Files

Not every file created during a project needs to be archived. If you proactively reduce the number of extraneous files in your archive, you will both reduce storage costs and increase the usefulness of that data upon retrieval. Common files that can be deleted when archiving data include:

* Compiled codes, such as `.o` or `.pyc` files. These files will likely not even work on the next system you may restore these data to and they can contribute significantly to your file count limit. Just keep the source code and clean installation instructions.
* Some log files. Many logs created by the system are not necessary to store indefinitely. Any Slurm logs from failed runs (prior to a successful run) or outputs from Matlab (e.g. `hs_error_pid*.log`, `java.log.*`) can often safely be ignored.
* Crash files such as core dumps (e.g. `core.*`, `matlab_crash_dump.`).

## Compress Your Data

Most archive locations (S@Y Archive Tier, Google Drive) perform much better with a smaller number of larger files. In fact, Google Shared Drives have a file count limit of 400,000 files. Therefore, it is highly recommended that you compress, using zip or [tar](/resources/online-tutorials), portions of your data for ease of storage and retrieval.
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

## Storing and Accessing Data on the S@Y Archive Tier

!!!note
    * S@Y Archive has a single-filesize limit of 5 TB, so plan your data compressions accordingly.
    * Please note that direct access from the cluster is only authorized for Low and Moderate risk data.

The archive tier of Storage@Yale is a cloud-based system. It provides an archive location for long-term data, featuring professional systems management, security, and protection from data loss via redundant, enterprise-grade hardware.  Data is dual-written to two locations.  The cost per TB is substantially lower than for the active-access S@Y tier.  For current pricing, see [ITS Data Rates](https://yale.service-now.com/it?id=rates_charges&service_group=e0502b7a1b3d3704f61dfeeccd4bcbab&service_offering=f4688dcd6fbb31007ee2abcf9f3ee400).

Use [Globus](/data/globus) to transfer cluster data to and from S@Y archive storage ('Yale CRC McCleary' mount point and path: '/SAY').

This works much the same as for the [S@Y Active Tier](/data/#storage-yale). However, when you write files to the archive, you are actually copying to a large hard disk-based cache. Writes are normally fast. Your copy will appear to complete as soon as the file is in the disk cache. 

To use S@Y (Archive) effectively, **please review carefully the following notes** on how it works and some best practices:

!!!warning "Do not move or rename files and folders that are already in the archive"
    * This will not work with either Globus or any other method (such as the Linux 'mv' command, i.e. within the /SAY folder on the transfer node)
    * The only operations that work successfully inside the S@Y archive are adding files to the archive and removing them.
    * If you accidentally **do** try to move a file/folder, it will fail and will potentially introduce faulty information in the S@Y indexing system.
    * If you encounter this or any related issue while working with S@Y archives, **please contact us ASAP** at [research.support@yale.edu](mailto:research.support@yale.edu) !

!!!warning "Do NOT write huge numbers of small files"
    * They will be difficult or impossible to restore in large numbers.
    * Groups of many small files should be first **compressed into a single file** with tar or zip (see [above](#compress-your-data)), before storing to the archive.

!!!warning "Similarly, do NOT run many parallel operations (like rsyncs) on the archive"
    * This may overload the system.

!!!note "Other key takeaways"
    * A copy to the archive will appear to complete relatively quickly, but at this point it will NOT yet in be the cloud. In the background, the system will flush files to the cloud and delete them from the cache as it does so.
    * If you read a file very soon after you write it, it is probably still in the cache, and your read will be quick.
    * Once some time has elapsed and the file has been moved to the cloud, read speed will be somewhat slower.
    * Operations that only read the metadata of files will be fast (ls, find, etc) even if the file is in the cloud, since metadata is kept in the disk cache.
    * Operations that actually read the file (cp, wc -l, tar, etc) will require recovering the entire file to disk cache first, and can take several minutes or longer depending on how busy the system is.

## S@Y Backup Tier

Yale ITS offers dedicated offsite "S3"-style object storage for data backup and archive to the cloud.  Clients are responsible for the data transfers and recovery via the S3 protocol, such as by using [RClone](/data/transfer/#rclone).

The Backup Tier is authorized for Low, Moderate, and High Risk data.

As with the Archive Tier, the Backup Tier is low-speed and not meant for daily use.

For current pricing, see [ITS Data Rates](https://yale.service-now.com/it?id=rates_charges&service_group=e0502b7a1b3d3704f61dfeeccd4bcbab&service_offering=f4688dcd6fbb31007ee2abcf9f3ee400).

