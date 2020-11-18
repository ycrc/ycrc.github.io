# Milgram

![Stanley](/img/Stanley-Milgram.jpg){: .cluster-portrait}

Milgram is a HIPAA aligned cluster intended for use on projects that may involve sensitive data. This applies to both storage and computation. If you have any questions about this policy, please [contact us](/#get-help).

Milgram is named for Dr. Stanley Milgram, a psychologist who researched the behavioral motivations behind social awareness in individuals and obedience to authority figures. He conducted several famous experiments during his professorship at Yale University including the lost-letter experiment, the small-world experiment, and the Milgram experiment.

!!! info
    Connections to Milgram can only be made from the Yale VPN (`access.yale.edu`)--even if you are already on campus (YaleSecure or ethernet). See our [VPN page](/clusters-at-yale/access/vpn) for setup instructions. If your group has a workstation (see [list](/clusters-at-yale/clusters/milgram-workstations)), you can connect using one of those.

- - -

## Partitions and Hardware

Milgram is made up of several kinds of compute nodes. We group them into  (sometimes overlapping) [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes. By combining the `--partition` and [`--constraint`](/clusters-at-yale/job-scheduling/resource-requests#features-and-constraints) Slurm options you can more finely control what nodes your jobs can run on.

--8<-- "snippets/submission_rate_limit.md"

### Public Partitions

See each tab below for more information about the available common use partitions.

--8<-- "snippets/milgram_partitions.md"

## Storage

`/gpfs/milgram` is Milgram's primary filesystem where home, project, and scratch60 directories are located. For more details on the different storage spaces, see our [Cluster Storage](/clusters-at-yale/data/index) documentation.

You can check your current storage usage & limits by running the `getquota` command. Note that the per-user usage breakdown only update once daily.

!!! Warning
    Files stored in `scratch60` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted.

| Partition      | Root Directory             | Storage     | File Count   | Backups |
|----------------|----------------------------|-------------|--------------|---------|
| home           | `/gpfs/milgram/home`       | 20GiB/user  | 500,000      | Yes     |
| project        | `/gpfs/milgram/project`    | varies      | varies       | No      |
| scratch60      | `/gpfs/milgram/scratch60`  | varies      | 5,000,000    | No      |
