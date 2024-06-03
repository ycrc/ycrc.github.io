# Monitor Overall Slurm Usage

To enable research groups to monitor their combined utilization of cluster resources, we have developed a suite of `getusage` tools. 
We perform nightly queries of Slurm's database to aggregate usage (in `cpu_hours`) broken down by user, account, and partition. 
These data are available both through each cluster's Open OnDemand and as a command-line utility.

## Open OnDemand Web-app

The Open OnDemand web portals host an interactive data dashboard that provide tables and visualization of Slurm utilization.

| Cluster                        | OOD site                                                         |
|--------------------------------|------------------------------------------------------------------|
| [Grace](/clusters/grace)       | [ood-grace.ycrc.yale.edu/pun/sys/ycrc_getusage](https://ood-grace.ycrc.yale.edu/pun/sys/ycrc_getusage)         |
| [McCleary](/clusters/mccleary) | [ood-mccleary.ycrc.yale.edu/pun/sys/ycrc_getusage](https://ood-mccleary.ycrc.yale.edu/pun/sys/ycrc_getusage) |
| [Milgram](/clusters/milgram)   | [ood-milgram.ycrc.yale.edu/pun/sys/ycrc_getusage](https://ood-milgram.ycrc.yale.edu/pun/sys/ycrc_getusage)     |

An example of such a view is shown here:

![getusage](/img/ood-getusage.png)

## Command-line `getusage`
These aggrigates are collected from all clusters and made accessible to researchers by running `getusage`:

```sh
[testuser@login1.grace ~]$ getusage --help

 Usage: getusage [OPTIONS]

╭─ Options ──────────────────────────────────────────────────────────────────╮
│ --user       -u      TEXT  User name [default: Current user]               │
│ --cluster    -c      TEXT  Filter usage by cluster CLUSTER [default: All]  │
│ --partition  -p            Break usage down by partition                   │
│ --summary    -s            Only report monthly summary                     │
│ --help                     Show this message and exit.                     │
╰────────────────────────────────────────────────────────────────────────────╯

```

Running without any arguments produces a report for the full fiscal year (starting in July):

```sh
[testuser@login1.grace ~]$ getusage
testuser Group Report

Monthly usage for testuser
────────────────────────────────────────────────────────────────────────────────
                                 CPU Hours Billable
               cluster  User
2023 July      grace    testuser     19.04    18.93
2023 August    grace    testuser      2.94     2.94
               mccleary testuser      2.48     2.48
2023 September grace    testuser      1.11     1.11
               mccleary testuser      3.54     3.54
2023 October   grace    testuser      0.99     0.99
               mccleary testuser      1.46     1.46
2023 November  grace    testuser      1.07     1.07
2024 January   grace    testuser      0.16     0.00
               mccleary testuser      4.35     4.35
               milgram  testuser      0.01     0.00
2024 February  grace    testuser      0.00     0.00
               mccleary testuser      1.41     1.41
               milgram  testuser      0.14     0.14
2024 March     mccleary testuser      0.00     0.00
               milgram  testuser      6.61     6.61
Monthly Summary
Latest month is in-progress (data updated daily at midnight)
────────────────────────────────────────────────────────────────────────────────
               CPU Hours      Billable
2023-07-31         19.04         18.93
2023-08-31          5.42          5.42
2023-09-30          4.65          4.65
2023-10-31          2.45          2.45
2023-11-30          1.07          1.07
2023-12-31          0.00          0.00
2024-01-31          4.52          4.35
2024-02-29          1.55          1.55
2024-03-31          6.61          6.61

Total usage:          45.31 CPU Hours
Total billable usage: 45.03 CPU Hours
Remaining No Cost Allotment: 24,954.97 CPU Hours

```

Please reach out to hpc@yale.edu with any comments or suggestions about how we can improve `getusage`. 

