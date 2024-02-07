# Milgram

![Stanley](/img/Stanley-Milgram.jpg){: .cluster-portrait}

Milgram is a HIPAA aligned cluster intended for use on projects that may involve sensitive data. This applies to both storage and computation. If you have any questions about this policy, please [contact us](/#get-help).

Milgram is named for Dr. Stanley Milgram, a psychologist who researched the behavioral motivations behind social awareness in individuals and obedience to authority figures. He conducted several famous experiments during his professorship at Yale University including the lost-letter experiment, the small-world experiment, and the Milgram experiment.

## Milgram Usage Policies

Users wishing to use Milgram must agree to the following:

* All Milgram users must have fulfilled and be current with Yale's HIPAA training requirement.
* Since Milgram's resources are limited, we ask that you only use Milgram for work on and storage of sensitive data, and that you do your other high performance computing on our other clusters.  

!!! warning "Operating System Upgrade""
    Milgram has been upgraded to RHEL 8 during the February maintenance window, February 6-8, 2024. For more information see our [Milgram Operating System Upgrade documentation](/clusters/milgram_rhel8).

- - -

## Access the Cluster

Once you have [an account](https://research.computing.yale.edu/support/hpc/account-request), the cluster can be accessed [via ssh](/clusters-at-yale/access) or through the [Open OnDemand web portal](/clusters-at-yale/access/ood/).

!!! info
    Connections to Milgram can only be made from the Yale VPN (`access.yale.edu`)--even if you are already on campus (YaleSecure or ethernet). See our [VPN page](/clusters-at-yale/access/vpn) for setup instructions.

## System Status and Monitoring

For system status messages and the schedule for upcoming maintenance, please see the [system status page](https://research.computing.yale.edu/support/hpc/system-status). For a current node-level view of job activity, see the [cluster monitor page (VPN only)](http://cluster.ycrc.yale.edu/milgram/).

## Partitions and Hardware

Milgram is made up of several kinds of compute nodes. We group them into  (sometimes overlapping) [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes. By combining the `--partition` and [`--constraint`](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) Slurm options you can more finely control what nodes your jobs can run on.

--8<-- "snippets/submission_rate_limit.md"


!!! warning "Interactive Partition Name Change"
    The 'interactive' and 'psych_interactive partitions have been renamed to 'devel' and 'psych_devel', respectively.  Please adjust your job submissions accordingly.

### Public Partitions

See each tab below for more information about the available common use partitions.

--8<-- "snippets/milgram_partitions.md"

## Storage

`/gpfs/milgram` is Milgram's primary filesystem where home, project, and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/data/hpc-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage breakdown only update once daily.

For information on data recovery, see the [Backups and Snapshots](/data/backups) documentation.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted. Artificial extension of scratch file expiration is forbidden without explicit approval from the YCRC. Please [purchase storage](/data/#purchase-additional-storage) if you need additional longer term storage.

|Partition  | Root Directory            | Storage                                 | File Count | Backups | Snapshots |
|-----------|---------------------------|-----------------------------------------|------------|---------|-----------|
| home      | `/gpfs/milgram/home`      | 125GiB/user                             | 500,000    | Yes     | >=2 days  |
| project   | `/gpfs/milgram/project`   | 1TiB/group, increase to 4TiB on request | 5,000,000  | Yes     | >=2 days  |
| scratch60 | `/gpfs/milgram/scratch60` | 20TiB/group                             | 15,000,000 | No      | No        |
