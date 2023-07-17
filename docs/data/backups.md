# Backups and Snapshots

The _only_ storage backed up on every cluster is Home. We do provide local snapshots, covering at least the last 2 days, on Home and Project directories (see below for details). See the [individual cluster](/clusters) documentation for more details about which storage is backed up or has snapshots. 

Please see our [HPC Policies](https://research.computing.yale.edu/services/high-performance-computing/hpc-policies#Backups) page for additional information about backups. 

## Retrieve Data from Home Backups

[Contact us](/#get-help) with your netid and the list of files/directories you would like restored. For any data deleted in the last couple days, first try the self-service snapshots described below.

## Retrieve Data from Snapshots

Our clusters create snapshots nightly on portions of the filesystem so that you can retrieve mistakenly modified or deleted files for yourself. We do not currently provide snapshots of scratch storage.

As long as your files existed in the form you want them in before the most recent midnight and the deletion was in the last few days, they can probably be recovered. Snapshot directory structure mirrors the files that are being tracked with a prefix, listed in the table below. Contact us if you need assistance finding the appropriate snapshot location for your files.

| File set                    | Snapshot Prefix                              |
|-----------------------------|----------------------------------------------|
| `/gpfs/gibbs/project`       | `/gpfs/gibbs/project/.snapshots`	     |
| `/gpfs/gibbs/pi/group`      | `/gpfs/gibbs/pi/group/.snapshots`            |
| `/vast/palmer/home.grace`   | `/vast/palmer/home.grace/.snapshot`          |
| `/vast/palmer/home.mccleary`| `/vast/palmer/home.mccleary/.snapshot`       |
| `/gpfs/ycga`                | `/gpfs/ycga/.snapshots`                      |
| `/gpfs/milgram/home`        | `/gpfs/milgram/home/.snapshots`              |
| `/gpfs/milgram/project`     | `/gpfs/milgram/project/.snapshots`           |
| `/gpfs/milgram/pi/groupname`| `/gpfs/milgram/pi/groupname/.snapshots`      |
| `/gpfs/slayman/pi/gerstein` | `/gpfs/slayman/pi/gerstein/.snapshots`       |

Within the snapshot directory, you will find multiple directories with names that indicate specific dates. For example, if you wanted to recover the file `/gpfs/gibbs/project/bjornson/rdb9/doit.sh` (a file in the bjornson group's project directory owned by rdb9) it would be found at `/gpfs/gibbs/.snapshots/date/project/bjornson/rdb9/doit.sh` .

!!! info "Snapshot Sizes"
    Because of the way snapshots are stored, sizes will not be correctly reported until you copy your files/directories back out of the `.snapshots` directory.
