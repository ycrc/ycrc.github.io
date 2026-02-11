# Grace and McCleary Decommission

## Data Center Migration

The YCRC is in the process of transitioning from the Yale West Campus Data Center to the [MGHPCC data center](https://news.yale.edu/2025/02/26/yale-grows-capacity-high-performance-computing-ai-related-research). The [Bouchet](bouchet.md) cluster, Yale's first cluster hosted at MGHPCC, is the successor to both Grace and McCleary, with HPC infrastructure refreshes and growth deployed at MGHPCC going forward. In 2026, we are decommissioning Grace and McCleary and most data and workloads on those systems will be moved to Bouchet.

## Phased Decommission & Migration

During this phased migration, we will be fully decommissioning Grace as a standalone cluster and the McCleary cluster will be downsized to support exclusively YCGA-affiliated workloads. Newer nodes from Grace and McCleary and some of the attached storage will be moved to MGHPCC and added to Bouchet as additional capacity. The migration will happen in three phases, described below.

- [Phase 1](#phase-1) (first half of 2026): Migration of workloads and data from research groups who do not use dedicated compute nodes or YCGA resources.

- Phase 2 (late 2026, early 2027): Migration of non-YCGA workloads and non-YCGA data from YCGA-affiliated research groups from McCleary.

- Phase 3 (late 2026, early 2027): Migration of newer commons nodes from Grace and McCleary to Bouchet. Migration of newer dedicated nodes along with their associated research groups and data. Grace will be shut down. McCleary will remain as a YCGA-only cluster for the remaining lifetime of that hardware.

![When Will I Move Flow Chart](/img/when_will_i_move.png){: .cluster-diagram}

If you are in Phase 2 or 3, more detailed information will be provided later this year when the hardware migration dates are finalized.

## Phase 1

Research groups who do not use dedicated compute nodes or YCGA resources will move off of Grace and McCleary in Phase 1. 

If you have been active on Grace or McCleary in the last year, you should already have an account on Bouchet. If you have not used the clusters in more than a year, you will need to [request an account](https://research.computing.yale.edu/account-request) on Bouchet. See our [“Getting Started on Bouchet” documentation](bouchet_getting_started.md) to familiarize yourself with the system. 

We will also be holding “Transitioning to Bouchet” sessions over the next couple of months, which will be announced in the YCRC monthly newsletter.

### Phase 1 Timeline

-  April 1st: *Deadline for workload migration.* Grace and McCleary logins for Phase 1 users will be disabled. Grace/McCleary data will remain accessible via Globus for two more months.

- June 1st: *Deadline for data migration.* Access to Grace/McCleary data via Globus will be disabled.

## What about My Existing Data on Grace or McCleary?

**All data on Grace and McCleary (that you want to keep) will need to be transferred off the clusters.** You are responsible for identifying the data you would like to keep from your home, project, and scratch and transferring it either to non-HPC storage or to a Bouchet account. 

If you have current (not expired) paid storage allocations on either the Palmer or Gibbs storage system, an allocation of the same size is now available on Bouchet on the all-flash Roberts storage system for you to transfer data into (Phase 1 only for now.). If your storage allocation is expired, please [contact us](/#get-help) if you would like to purchase a storage allocation on Bouchet.

!!! warning "NIH Controlled Access Data"

	If you have any data on Grace or McCleary that is now covered by the [NIH Controlled Access Data policies](https://sharing.nih.gov/sites/default/files/flmngr/NIH-Security-BPs-for-Users-of-Controlled-Access-Data.pdf), this data cannot be moved to Bouchet but instead must be moved to the [Hopper](hopper.md) HPC cluster. [Submit this form to request Hopper access](https://research.computing.yale.edu/secure-project-request).

We encourage you to use the `getquota` utility on Grace and/or McCleary to examine the data usage by your group and specific group members. In general, we recommend using [Globus](/data/globus/) to migrate data to Bouchet as it is the fastest and most robust method of transferring data between the clusters. 

If you have concerns about transferring your data, such as a particularly large allocation or complicated permission structure, please [reach out to us](/#get-help) for assistance.



## Get Help


As always, our Research Support staff members are available to assist. Please [reach out](/#get-help) if you have any questions or concerns about what will be moved to Bouchet and when.



