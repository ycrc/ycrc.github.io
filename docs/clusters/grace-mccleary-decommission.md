# Grace and McCleary Decommission

## Data Center Migration

The YCRC is in the process of transitioning from the Yale West Campus Data Center to the [MGHPCC data center](https://news.yale.edu/2025/02/26/yale-grows-capacity-high-performance-computing-ai-related-research). The [Bouchet](bouchet.md) cluster, Yale's first cluster hosted at MGHPCC, is the successor to both Grace and McCleary, with HPC infrastructure refreshes and growth deployed at MGHPCC going forward. In 2026, we are decommissioning Grace and McCleary and most data and workloads on those systems will be moved to Bouchet.

## Phased Decommission & Migration

During this phased migration, we will be fully decommissioning Grace as a standalone cluster and the McCleary cluster will be downsized to support exclusively YCGA-affiliated workloads. Newer nodes from Grace and McCleary and some of the attached storage will be moved to MGHPCC and added to Bouchet as additional capacity. The migration will happen in three phases, described below.

- [Phase 1](#phase-1) (first half of 2026): Migration of workloads and data from research groups who do not use dedicated compute nodes or YCGA resources.

- Phase 2 (late 2026, early 2027): Migration of non-YCGA workloads and non-YCGA data from YCGA-affiliated research groups from McCleary. YCGA data and workloads will remain on McCleary for the remaining lifetime of the YCGA-owned hardware.

- Phase 3 (late 2026, early 2027): Migration of newer commons nodes from Grace and McCleary to Bouchet. Migration of newer dedicated nodes along with their associated research groups and data. Grace will be shut down. McCleary will remain as a YCGA-only cluster for the remaining lifetime of YCGA-owned hardware.

![When Will I Move Flow Chart](/img/when_will_i_move.png){: .cluster-diagram}

If you are in Phase 2 or 3, more detailed information will be provided later this year when the hardware migration dates are finalized.

## Phase 1

Research groups who do not use dedicated compute nodes or YCGA resources will move off of Grace and McCleary in Phase 1. 

If you have been active on Grace or McCleary in the last year, you should already have an account on Bouchet. If you have not used the clusters in more than a year, you will need to [request an account](https://research.computing.yale.edu/account-request) on Bouchet. See our [“Getting Started on Bouchet” documentation](bouchet_getting_started.md) to familiarize yourself with the system. See below for information on transferring data.

### Phase 1 Timeline

-  April 1st: *Deadline for workload migration.* Grace and McCleary logins for Phase 1 users will be disabled. Grace/McCleary data will remain accessible via Globus for two more months.

- June 1st: *Deadline for data migration.* Access to Grace/McCleary data via Globus will be disabled.


## Phase 2

Later on in 2026 we will reach out to groups that use YCGA data and resources about transferring any data and workload to Bouchet that are not associated with YCGA.
Data and workloads associated with YCGA can and should stay on McCleary, which will remain as YCGA-only cluster for another couple years.

You will be responsible for identifying the non-YCGA data you would like to keep from your home, project, and scratch and transferring it either to non-HPC storage or to a Bouchet account but we are available to assist with that process.

## Phase 3

Once the timeline for the hardware migration has been finalized (Summer 2026 or later), we will be in contact about preparing to migrate your workloads and data to Bouchet.


## What about My Existing Data on Grace or McCleary?

!!! alert "Phase 1 Storage Access Available Until June 1st, 2026"

	While Phase 1 accounts are no longer able to log in to Grace or McCleary after April 1st, these accounts can still access Grace and McCleary storage via the ["Yale CRC Grace" Globus Collection](https://docs.ycrc.yale.edu/data/globus/#cluster-collections) until June 1st so they can transfer data off the cluster (to Bouchet or other storage options).


**All (non-YCGA) data on Grace and McCleary (that you want to keep) will need to be transferred off the clusters.** You are responsible for identifying the data you would like to keep from your home, project, and scratch and transferring it either to non-HPC storage or to a Bouchet account. 

!!! warning "NIH Controlled Access Data"

	If you have any data on Grace or McCleary that is now covered by the [NIH Controlled Access Data policies](https://sharing.nih.gov/sites/default/files/flmngr/NIH-Security-BPs-for-Users-of-Controlled-Access-Data.pdf), this data cannot be moved to Bouchet but instead must be moved to the [Hopper](hopper.md) HPC cluster. [Submit this form to request Hopper access](https://research.computing.yale.edu/secure-project-request).

We encourage you to use the `getquota` utility on Grace and/or McCleary to examine the data usage by your group and specific group members. We recommend using [Globus](/data/globus/) to migrate individual data (i.e. home, project, scratch) to Bouchet as it is the fastest and most robust method of transferring data between the clusters. 

If there are members of your group who are no longer active and their directories contain data you would like to retain, please [reach out to us](/#get-help) to change the ownership of those files to an active group member so they can transfer the data. When transferring to Bouchet we recommend uploading the files to either the "shared" directory in project or in the directory of an active group member (rather than perpetuating the inactive group member's directories on Bouchet).

If you have current (not expired) paid storage allocations on either the Palmer or Gibbs storage system, an allocation of the same size is now available on Bouchet on the all-flash Roberts storage system for you to transfer data into (Phase 1 only for now.). If your storage allocation is expired, please [contact us](/#get-help) if you would like to purchase a storage allocation on Bouchet. 

If you would like assistance transferring your paid storage allocation or otherwise have questions or concerns about your data transfer, please [reach out to us](/#get-help) for assistance.

## Get Help

If you are new to Bouchet, we recommend reviewing our [“Getting Started on Bouchet” documentation](bouchet_getting_started.md). You can also find a recording of our "Intro to Bouchet" session [here](https://youtu.be/mQMc8y-Z8sY?si=Ubyd7DvX5I9kuaTr). 

In addition to our [twice-weekly virtual Office Hours](/#office-hours-via-zoom), the YCRC team will be available every week in March for *in-person* Bouchet Migration Support Office Hours offering hands-on support. Stop by our office at 160 St Ronan Street— no registration required.

- Friday, March 6th 2-4pm
- Thursday, March 12th 9-11am
- Tuesday, March 17th 3-5pm
- Wednesday, March 25th 1-3pm
- Monday, March 30th 10-12pm

We also have a recording of our "Transfers with Globus" info session available [here](https://www.youtube.com/watch?v=VCOBLKrWe9M).

As always, our Research Support staff members are available to assist. Please [reach out](/#get-help) if you have any questions or concerns about what will be moved to Bouchet and when.



