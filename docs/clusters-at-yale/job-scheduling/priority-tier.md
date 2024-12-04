# Priority Tier

## Overview

Effective December 1st 2024, the current YCRC CPU-Hour based service charges has been replaced with new Priority Tier service charges.
The YCRC has added a new Priority Tier of partitions that is an opt-in, fast lane for computational jobs. 
All computation on the “standard” tier of partitions (e.g. day, week, mpi, gpu)  no longer incur charges.
Private nodes and scavenge partitions continue to not incur charges.

The new compute charging model was developed in close collaboration with faculty, YCRC staff and university administrators to ensure the YCRC service charging models support the researchers who rely on our systems and the needs of the University.

## Access

Access to Priority Tier partitions is granted upon request through the [Priority Tier Access Request Form](https://docs.google.com/forms/d/1gXaOiOwmU-YY1Q5k2mJJRmEHTeJcBs9BlkJ7n1akF1Q).
This form must be submitted by the group’s PI (or delegate).

During the Priority Tier onboarding process, the YCRC will require certain information before access can be granted.

* Charging instructions (COA)
* A list of members in your group who should have access (and therefore the privileges to incur charges). Additional group members can be added to Priority Tier at any time by submitted a request to [hpc@yale.edu](mailto:hpc@yale.edu) (all group members should already have cluster accounts requested through the [Account Request Form](https://research.computing.yale.edu/support/hpc/account-request)).
* We also strongly recommend providing an annual usage limit, beyond which no additional computation on Priority Tier will occur (computation in Standard Tier will still be available at no cost). Note this limit can be changed at any time upon request.

## How to Use Priority Tier Partitions

### Job Submission

Starting on December 1st, there is a new tier of partitions on [Grace](/clusters/grace/), [McCleary](/clusters/mccleary/) and [Milgram](/clusters/milgram/). Priority Tier partitions will be added to [Bouchet](/clusters/bouchet/) when it enters production.
Jobs submitted to a Priority Tier partition precede all pending jobs in the corresponding standard tier partitions in the scheduling queue to provide a “fast-lane”. 
The Priority Tier partitions are composed of the YCRC’s newest nodes and GPUs.
Any compute resources not in use by a Priority Tier partition are available for use by the Standard Tier partitions.

| Partition       | Description       | Grace                             | McCleary                          | Milgram |
|-----------------|-------------------|-----------------------------------|-----------------------------------|-----------|
| `priority`      | similar to `day`  | Intel Ice Lake Nodes              | Intel Ice Lake Nodes              |  Intel Cascade Lake Nodes |
| `priority_gpu`  | similar to `gpu`  | A100, A5000 GPU-enabled Nodes | A100, A5000 GPU-enabled Nodes |  NA | 
| `priority_mpi`  | similar to `mpi`  | Intel Skylake Nodes |  NA | NA  |

At launch all Priority Tier partitions has a 7-day maximum wall time limit. Interactive jobs are permitted on Priority Tier partitions. Priority Tier jobs are still bound by [YCRC policies and best practices](/clusters-at-yale/access/accounts/), so users are expected to use interactive jobs mindfully and terminate their session when they are pausing their work.

The expectation for a job submitted to Priority Tier partition is not necessarily that it will run immediately (as one experiences in `devel` or jobs preempting `scavenge` jobs) but rather that it will start before any Standard Tier jobs, when resources are available and it reaches the top of the Priority Tier queue relative to other Priority Tier jobs.

### Account Selection

When you are granted access to Priority Tier, you will be added to one or more `prio_` Slurm group accounts.
These group account names take the form `prio_groupname`, where `groupname` is the name of the Slurm group account used in the existing Standard Tier partitions.
PIs can elect to have multiple Slurm group accounts for different projects, each with their own COA, for direct connection between certain computation and the associated grant or other source of funds.
In these instances the additional Slurm group accounts will take the form `prio_groupname_projectid`.

In either instance, the Priority Tier Slurm group account *must* be specified in the job submission script using the `-A` flag

```
#SBATCH -A prio_groupname
### or
#SBATCH -A prio_groupname_projectid
```

Only `prio_` groups can access the Priority Tier partitions and they cannot be used in the Standard Tier partitions (see below section on Fairshare for more information on why this is). 

### `priority_gpu` Partitions

To avoid unexpected costs due to the Service Unit differences between A100 GPUs and A5000 GPUs, we strongly recommend being specific about the GPU model if any job submissions.

```
#SBATCH --gpus=a100:1
```

### Fairshare and Concurrent Utilization Limits

All YCRC clusters are governed by a set of "fairness" control. 
"Fairshare” is an algorithm that controls moment-to-moment priority of a job based on recent use of the cluster. 
For example, jobs from heavy recent users/groups start at the end of the queue and work their way forward over time and jobs from new or low-usage users/groups start at the front of the queue. 
CPU core hours, memory consumption and GPU hours all contribute at proportional levels to the usage incurred by running jobs. 
The cluster scheduler also has "concurrent utilization limits" (QOSs) that prevent a single user or group from taking over a whole cluster, regardless of recent use and fairshare status. 

All accounts in the Priority Tier share a distinct fairshare pool from the one shared by Standard Tier accounts.
Computations in Standard Tier will not affect your priority in Priority Tier and vice versa.

At launch there are no concurrent utilization limits on Priority Tier but they may be instated at a later date based on demand and user behavior.
Communications will be sent if and when this is being considered.

## Rate Structure

The new charging model for computations run on a Priority Tier partition is Service Unit (SU) based at a rate of $0.004/SU/hour.
This rate is derived to closely match the prorated cost of a similar dedicated node over a 5 year expected lifetime.
The SUs of a compute job are calculated as follows:

|  Type | Subtype   | Service Units  | Cost per Hour  |
|----------------|--------|-----|--------|
| Compute Hour\* |  -     | 1   | $0.004 |
| GPU Hour       | A5000  | 15  | $0.060 |
| GPU Hour       | A100   | 100 | $0.400 |

\* Number of SUs per non-GPU compute job is the maximum of the CPU core count and the total RAM allocation/15GB

Usage is billed for actual runtime, not requested walltime of a job. 
However, all compute resources (CPUs, memory, GPUs) allocated to a job are billed, regardless of whether a job makes use of those resources.

Usage is billed monthly, with the bills expected the first week of the following month. To assist with cost estimates and budgeting, see below for tools for calculating charges.

### Annual Usage Limit

We strongly encourage every group to set an annual usage limit for Priority Tier accounts to ensure Priority Tier expenses stay within expected bounds.
This limit can be changed at any time but during the onboarding process YCRC can assist with setting a reasonable starting limit.

As the annual usage limit is approached, you will no longer be able to submit any jobs that would (if they ran for their full requested walltime) over run the limit.
If they choose, the PI (or delegate) of the group can request to have the limit increased.
In the meantime, you can continue to run any computations in the Standard Tier of partitions which are always free of charge.

### Estimate Charges and Review Usage

To assist with cost estimates and budgeting, we provide a [Cost Calculator](https://docs.google.com/spreadsheets/d/1607EHXc_aay0O0CeteV9ckkwcrFhJwvx9aNmxFmLIYI/edit?usp=sharing). 

Usage to date can be monitored in the [User Portal](/clusters-at-yale/job-scheduling/getusage/#open-ondemand-web-app) and on the cluster using the `getusage -g prio_groupname` [command](/clusters-at-yale/job-scheduling/getusage/#command-line-getusage).

## Other Upcoming Improvements

In conjunction with the new charging model, the YCRC is committed to making improvements to the ongoing tuning of fairshare and concurrent utilization algorithms and additional practices and tooling to enable users to make efficient use of the systems.
One such improvement available today is the [User Portal](/job-scheduling/getusage/#open-ondemand-web-app) where researchers can view information about their activity on our clusters.
Keep an eye on the YCRC Bulldog User News in coming months for information about these improvements as we roll them out.
