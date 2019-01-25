# Cluster Storage

Each research group is provided with storage space for research data on the GPFS parallel filesytems on the clusters. The storage is separated into three tiers: home, project, and scratch. You can monitor your storage usage by running the `getquota` command on a cluster.

!!!warning
    The _only_ storage backed up on every cluster is `home`.

## HPC Storage Locations

### Home

Home storage is a small amount of space to store your scripts, notes, final products (e.g. figures), etc. Home storage is backed up daily.

### Project

In general, project storage is intended to be the primary storage location for HPC research data in active use.

### 60-Day Scratch (`scratch60`)

Use this space to keep intermediate files that can be regenerated/reconstituted if necessary. **Files older than 60 days will be deleted automatically**. This space is not backed up, and you may be asked to delete files younger than 60 days old if this space fills up.

## HPC Storage Best Practices

### Prevent Large Numbers of Small Files

Parallel fileystems, like the ones attached to our clusters, perform poorly with very large numbers of small files. For this reason, there are file count limits on all accounts to provide a safety net against excessive file creation. However, we expect users to manage their own file counts by altering workflows to reduce file creation, deleting unneeded files, and compressing (using [tar](online-tutorials/#how-create-and-extract-a-tar-or-targz-archive)) collections of files no longer in use.

## Backups and Snapshots

### Retrieve Data from Home Backups

Contact us at [hpc@yale.edu](mailto:hpc@yale.edu) with your netid and the list of files/directories you would like restored.

### Retrieve Data from Snapshots (Farnam & Milgram)

