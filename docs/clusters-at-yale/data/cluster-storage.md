# Cluster Storage

Each research group is provided with storage space for research data on the GPFS parallel filesytems on the clusters. The storage is separated into three tiers: home, project, and scratch. You can monitor your storage usage by running the `getquota` command on a cluster.

!!!warning
    The _only_ storage backed up on every cluster is `home`.

## HPC Storage Locations

### Home

Home storage is a small amount of space to store your scripts, notes, final products (e.g. figures), etc. Home storage is backed up daily.

### Project

In general, project storage is intended to be the primary storage location for HPC research data in active use. Project space is available via the `project` link in your home directory or via the absolute path `/gpfs/<filesystem>/project/<group>/<netid>`.

### 60-Day Scratch (`scratch60`)

Use this space to keep intermediate files that can be regenerated/reconstituted if necessary. **Files older than 60 days will be deleted automatically**. This space is not backed up, and you may be asked to delete files younger than 60 days old if this space fills up. Scratch space is available via the `scratch60` link in your home directory or via the absolute path `/gpfs/<filesystem>/scratch60/<group>/<netid>`.

## HPC Storage Best Practices

### Prevent Large Numbers of Small Files

Parallel fileystems, like the ones attached to our clusters, perform poorly with very large numbers of small files. For this reason, there are file count limits on all accounts to provide a safety net against excessive file creation. However, we expect users to manage their own file counts by altering workflows to reduce file creation, deleting unneeded files, and compressing (using [tar](/online-tutorials/#how-create-and-extract-a-tar-or-targz-archive)) collections of files no longer in use.

## Backups and Snapshots

### Retrieve Data from Home Backups

Contact us at [hpc@yale.edu](mailto:hpc@yale.edu) with your netid and the list of files/directories you would like restored.

### Retrieve Data from Snapshots (Farnam & Milgram)

Farnam and Milgram all run snapshots nightly on portions of their filesystems so that you can retrieve mistakenly modified or removed files for yourself. As long as your files existed in the form you want them in before the most recent midnight, they can probably be recovered. Snapshot directory structure mirrors the files that are being tracked with a prefix, listed in the table below.

| File set                    | Snapshot Prefix                              |
|-----------------------------|----------------------------------------------|
| `/gpfs/ysm`                 | `/gpfs/ysm/.snapshots`                       |
| `/gpfs/slayman/pi/gerstein` | `/gpfs/slayman/pi/gerstein/.snapshots`       |
| `/gpfs/milgram/home`        | `/gpfs/milgram/home/.snapshots`              |
| `/gpfs/milgram/project`     | `/gpfs/milgram/project/groupname/.snapshots` |

For example, if you wanted to recover the most recent snapshot of the file `/gpfs/ysm/home/rdb9/scripts/doit.sh`, its path would be `/gpfs/ysm/.snapshots/$(date +%Y%m%d-0000)/home/rdb9/scripts/doit.sh`. Similarly, the file `/gpfs/milgram/project/bjornson/rdb9/doit.sh` (a file in the bjornson group's project directory owned by rdb9) could be recovered at `/gpfs/milgram/project/bjornson/.snapshots/$(date +%Y%m%d-0000)/rdb9/doit.sh` .

!!! info
    Because of the way snapshots are stored, sizes will not be correctly reported until you copy your files/directories back out of the `.snapshots` directory.