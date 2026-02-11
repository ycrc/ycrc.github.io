# Monitor Overall Slurm Usage

To enable research groups to monitor their combined utilization of cluster resources, we have developed a suite of `getusage` tools. 
We perform nightly queries of Slurm's database to aggregate usage (in ServiceUnit-hours `su_hours`) broken down by user, account, and partition. 
Service Units are a weighted combination of CPUs, memory, and GPUs allocated for each job. 
The relative weights are derived from the approximate cost of these different resources. 

|  Type | Subtype   | Service Units  | 
|----------------|--------|-----|
| Compute Hour\* |  -     | 1   |
| GPU Hour       | A5000  | 15  |
| GPU Hour       | A100   | 100 |

\* Number of SUs per non-GPU compute job is the maximum of the CPU core count and the total RAM allocation/15GB. 

Usage data are available through each cluster's Open OnDemand and as a command-line utility.

## Open OnDemand Web-app

The Open OnDemand User Portals host an interactive data dashboard that provide tables and visualization of Slurm utilization.

| Cluster                        | OOD site                                                         |
|--------------------------------|------------------------------------------------------------------|
| [Grace](/clusters/grace)       | [ood-grace.ycrc.yale.edu/pun/sys/ycrc_userportal/clusterusage](https://ood-grace.ycrc.yale.edu/pun/sys/ycrc_userportal/clusterusage)         |
| [McCleary](/clusters/mccleary) | [ood-mccleary.ycrc.yale.edu/pun/sys/ycrc_userportal/clusterusage](https://ood-mccleary.ycrc.yale.edu/pun/sys/ycrc_userportal/clusterusage) |
| [Milgram](/clusters/milgram)   | [ood-milgram.ycrc.yale.edu/pun/sys/ycrc_userportal/clusterusage](https://ood-milgram.ycrc.yale.edu/pun/sys/ycrc_userportal/clusterusage)     |

An example of such a view is shown below.

!!! info "Multiple Accounts"
    If you belong to multiple Slurm Accounts, including [priority tier](/clusters-at-yale/job-scheduling/priority-tier) accounts, these will be populated in the pull-down `Account` menu. 

![getusage](/img/ood-getusage.png)

## Command-line `getusage`
These aggrigates are collected from all clusters and made accessible to researchers by running `getusage`:

```sh
[testuser@login1.grace ~]$ getusage --help

 Usage: getusage [OPTIONS]

╭─ Options ──────────────────────────────────────────────────────────────────╮
│ --user       -u      TEXT  User name [default: Current user]               │
│ --group      -g      TEXT  Slurm Account [default: Default Account]        │
│ --cluster    -c      TEXT  Filter usage by cluster CLUSTER [default: All]  │
│ --partition  -p            Break usage down by partition                   │
│ --summary    -s            Only report monthly summary                     │
│ --help                     Show this message and exit.                     │
╰────────────────────────────────────────────────────────────────────────────╯
```

!!! info "Multiple Accounts"
    If you belong to multiple accounts, you can specify them with the `-g` flag. 
    By default, `getusage` displays information about your "default" Slurm Account.
    If you wish to view your secondary account's usage (or for [priority tier](/clusters-at-yale/job-scheduling/priority-tier) accounts, specify them like: `getusage -g prio_account`


Running without any arguments produces a report for the full fiscal year (starting in July):

```sh
[testuser@login1.grace ~]$ getusage
Monthly usage (in su_hours) for testuser
────────────────────────────────────────────────────────────────────────────────
                                 Standard         PI
               Cluster  User
2024 July      grace    user1      456.19       0.00
               mccleary user2       33.67       0.00
2024 August    grace    user1      366.15       0.00
               mccleary user2       46.40       0.00
2024 September grace    user1      360.24       0.00
                        user3        2.02       7.28
                        user5        0.01       0.00
               mccleary user2       39.35       0.00
2024 October   grace    user3      544.93   5,659.68
               mccleary user2        5.28       0.00
2024 November  grace    user4      526.84      14.27
                        user3    4,442.07     169.76
               mccleary user2       32.54       0.00
Monthly Summary
Latest month is in-progress (data updated daily at midnight)
────────────────────────────────────────────────────────────────────────────────
                Standard            PI
2024-07-31        489.87          0.00
2024-08-31        412.55          0.00
2024-09-30        401.62          7.28
2024-10-31        550.22      5,659.68
2024-11-30      5,001.44        184.03

Total usage:          12,706.68 Service-Unit Hours
```

Please reach out to research.computing@yale.edu with any comments or suggestions about how we can improve `getusage`. 

