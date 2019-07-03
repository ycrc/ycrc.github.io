# Milgram

![Stanley](/img/Stanley-Milgram.jpg){: .cluster-portrait}

Milgram is named for Dr. Stanley Milgram, a psychologist who researched the behavioral motivations behind social awareness in individuals and obedience to authority figures. He conducted several famous experiments during his professorship at Yale University including the lost-letter experiment, the small-world experiment, and the Milgram experiment on obedience to authority figures.

Milgram is a HIPAA aligned Department of Psychology cluster intended for use on projects that may involve sensitive data. This applies to both storage and computation. If you have any questions about this policy, please [contact us](mailto:hpc@yale.edu).

!!! note
    Connections to Milgram can only be made from the HIPAA VPN (`access.yale.edu/hipaa`). See our [VPN page](/clusters-at-yale/access/vpn) for setup instructions. If your group has a workstation (see [list](/clusters-at-yale/clusters/milgram-workstations)), you can connect using one of those.

- - -

## Hardware

Milgram is made up of a couple kinds of compute nodes. The Features column below lists the features that can be used to request different node types using the `--constraints` flag (see our [Slurm documentation](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) for more details). The RAM listed below is the amount of memory available for jobs.

!!! Warning
    Care should be taken if when scheduling your job if you are running programs/libraries optimized for specific hardware.
    See the [guide on how to compile software](/clusters-at-yale/applications/compile) for specific guidance.

### Compute Node Configurations

| Count | CPU           | CPU Cores | RAM   | Features                          |
|-------|---------------|-----------|-------|-----------------------------------|
| 12    | 2x E5-2660 v3 | 20        | 121G  | haswell, E5-2660_v3, oldest       |
| 48    | 2x E5-2660 v4 | 28        | 250G  | broadwell, E5-2660_v4             |

## Slurm Partitions

Nodes on the clusters are organized into partitions, to which you submit your jobs with [Slurm](/clusters-at-yale/job-scheduling). The default resource requests for all jobs is 1 core and 5GB of memory per core. The short partition is where most batch jobs should run, and is the default if you don't specify a partition. The interactive partition is dedicated to jobs with which you need ongoing interaction. The long and verylong partitions are meant for jobs with projected walltimes that are too long to run in short. For courses using the cluster we set aside the education partition. The scavenge partition allows you to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

The limits listed below are for all running jobs combined. Per-node limits are bound by the node types, as described in the [hardware](#hardware) table.

| Partition    | Group Limits           | User Limits             | Walltime Default/Max | Node Type (count)               |
|--------------|------------------------|-------------------------|----------------------|---------------------------------|
| short*       | 1158 CPUs, 10176 G RAM | 772 CPUs, 6784 G RAM    | 1h/6h                | E5-2660_v3 (9), E5-2660_v4 (48) |
| interactive  |                        | 1 job, 4 CPUs, 20 G RAM | 1h/6h                | E5-2660_v3 (1)                  |
| long         |                        | 1188 CPUs, 5940 G RAM   | 1h/2d                | E5-2660_v3 (9), E5-2660_v4 (48) |
| verylong     |                        | 792 CPUs, 3960 G RAM    | 1h/7d                | E5-2660_v3 (9), E5-2660_v4 (48) |
| education    |                        |                         | 1h/6h                | E5-2660_v3 (2)                  |
| scavenge     |                        |                         | none                 | E5-2660_v3 (9), E5-2660_v4 (48) |

\* default

## Storage

`/gpfs/milgram` is Milgram's primary filesystem where home, project, and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/cluster-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage breakdown only update once daily.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

| Partition      | Root Directory             | Storage     | File Count   | Backups |
|----------------|----------------------------|-------------|--------------|---------|
| home           | `/gpfs/milgram/home`       | 20G/user    | 500,000      | Yes     |
| project        | `/gpfs/milgram/project`    | varies      | varies       | No      |
| scratch60      | `/gpfs/milgram/scratch60`  | varies      | 5,000,000    | No      |

### Data Fileset

There is a `data` fileset on `/gpfs/milgram` designed to host shared, public datasets to prevent duplication of data across the machine. Each dataset in the `data` fileset has one curator who is in charge of populating the dataset, managing permissions and requesting access to that dataset. See below for a list of datasets. If you have questions about or would like read access to a specific dataset, please contact the listed curator.

| Dataset            |  Directory                              |Owner               | Curator            |
|--------------------|-----------------------------------------|--------------------|--------------------|
| ABCD               | `/gpfs/milgram/data/ABCD`               | TBD                | TBD                |
| bold5000           | `/gpfs/milgram/data/bold500`            | TBD                | TBD                |
| brainiak_tutorials | `/gpfs/milgram/data/brainiak_tutorials` | TBD                | TBD                |
| bsnip1             | `/gpfs/milgram/data/bsnip1`             | TBD                | TBD                |
| GSP                | `/gpfs/milgram/data/GSP`                | TBD                | TBD                |
| HCP                | `/gpfs/milgram/data/HCP`                | TBD                | TBD                |
| HealthyBrain       | `/gpfs/milgram/data/HealthyBrain`       | TBD                | TBD                |
| NKI                | `/gpfs/milgram/data/NKI`                | TBD                | TBD                |
| PartlyCloudy       | `/gpfs/milgram/data/PartlyCloudy`       | TBD                | TBD                |
| PING               | `/gpfs/milgram/data/PING`               | TBD                | TBD                |
| UKB                | `/gpfs/milgram/data/UKB`                | TBD                | TBD                |
| yale_smart         | `/gpfs/milgram/data/yale_smart`         | TBD                | TBD                |

### For Dataset Curators

The appointed curators for each dataset has the following responsibilities.

#### Manage Datasets and Reset Permissions

The curator for a specific fileset is the only user with `write` access to that directory. It is their responsibility to manage the data in that directory.

In order to add new data, the curator will need to temporarily grant themselves read permission to the directory where they will be populating the data:

``` bash
cd /gpfs/milgram/data/[destination_for_data]
chmod u+w .
```

To move or clean out data, the curator will also need to temporarily grant themselves write permission for the relevant data using `chmod u+w [file]` or `chmod -R u+w [directory]`.

After data management is complete, *the permissions must be reset to read-only* to prevent accidental contamination of the dataset. To reset the permissions, run the following command at the highest level directory where the data was manipulated:

```bash
cd /gpfs/milgram/data/[destination_for_data]
chmod -R ugo-w .
```

#### Request Access for New User

The curator is responsible for fielding access requests to their directory. Once a new user has been given permission to access the directory, the curator themselves will submit a permission change request to hpc@yale.edu.

#### Appropriate Data Only

The data fileset should only be used for raw datasets. Approval must be requested from ????? to add data products generated at Yale to the fileset. Intermediate data products and temporary files (such as slurm logs) should *never* be placed in the data directory.


