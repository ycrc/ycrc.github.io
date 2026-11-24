# Grace and McCleary Decommission

## Data Center Migration

The YCRC is in the process of transitioning from the Yale West Campus Data Center to the [MGHPCC data center](https://news.yale.edu/2025/02/26/yale-grows-capacity-high-performance-computing-ai-related-research). The [Bouchet](bouchet.md) cluster, Yale's first cluster hosted at MGHPCC, is the successor to both Grace and McCleary, with HPC infrastructure refreshes and growth deployed at MGHPCC going forward. In 2026, we are decommissioning Grace and McCleary and all non-YCGA data and workloads will be moved to Bouchet.

## Phased Decommission & Migration

During this phased migration, we will be fully decommissioning Grace as a standalone cluster and the McCleary cluster will be downsized to support exclusively YCGA-affiliated workloads. Newer nodes from Grace and McCleary and the Palmer storage system will be moved to MGHPCC and added to Bouchet as additional capacity.

!!! info "How am I Impacted by the Migration?"

	To provide an individual picture of impacts of the next two phases of the migration, you can run the `mymigration` command line utility on Grace and McCleary to describe your specific migration timeline and impacts.

## [Phase 1](#phase-1) (**Complete**)

Migration of workloads and data from research groups who do not use dedicated compute nodes, CryoEM resources or YCGA resources. **As of June 1st, users in Phase 1 no longer have access to Grace and McCleary.**

## December 9th Air-Cooled Node Decommission and Migration

The vast majority of air-cooled compute nodes from Grace and McCleary will be decommissioned or migrated as additional capacity to Bouchet, depending on age. We expect the migrated capacity to be available on Bouchet by winter break.

### Changes to Commons Partitions

After December 9th, both clusters will have the following commons nodes until the final migration in February.

- `devel` will be updated with 2 `icelake` generation nodes
- `day` and `week` will remain with an aggregate 82 nodes (Grace) and 38 nodes (McCleary)
- `gpu_devel` will contain 1 4xA100 nodes
- `gpu` will contain 3 4xA100 nodes
- `bigmem` will no longer be present. Jobs requiring large amounts of RAM should be run in `day`, `ycga_bigmem` or moved to Bouchet as appropriate.

### Changes to Dedicated Partitions

PIs of dedicated partitions have been individually contacted to confirm the future status of their nodes.

## February 2027 Migration & Grace Decommission

In February (exact date TBD), the remaining nodes from Grace and remaining non-`ycga` nodes on McCleary will be added as additional capacity to Bouchet. Grace will be fully decommissioned at this time.  McCleary will remain as a YCGA-only cluster for the remaining lifetime of YCGA-owned hardware (at least late 2027).

**YCGA Users.** All YCGA users will retain access to McCleary for the rest of its lifetime for YCGA-related workloads (likely another couple years). In early 2027, we will reach out to YCGA users about moving non-YCGA data and workflows to Bouchet, but there is no action required at this time.

**Non-YCGA Users.** Grace will be shut down and access will be deactivated for all users. Access to McCleary for non-YCGA users will be deactivated. Storage will remain available via Globus for a short time for data transfer.

To provide an individual picture of impacts of the next two phases of the migration, we have created a `mymigration` utility that can be run on Grace and McCleary to clarify your specific migration timeline and impacts.

## What about My Existing Data on Grace or McCleary?

**All non-YCGA data on Grace and McCleary (that you want to keep) will need to be transferred off the clusters.** You are responsible for identifying the data you would like to keep from your home, project, and scratch and transferring it either to non-HPC storage or to a Bouchet account. 

!!! warning "NIH Controlled Access Data"

	If you have any data on Grace or McCleary that is now covered by the [NIH Controlled Access Data policies](https://sharing.nih.gov/sites/default/files/flmngr/NIH-Security-BPs-for-Users-of-Controlled-Access-Data.pdf), this data cannot be moved to Bouchet but instead must be moved to the [Hopper](hopper.md) HPC cluster. [Submit this form to request Hopper access](https://research.computing.yale.edu/secure-project-request).

We encourage you to use the `getquota` utility on Grace and/or McCleary to examine the data usage by your group and specific group members. We recommend using [Globus](/data/globus/) to migrate individual data (i.e. home, project, scratch) to Bouchet as it is the fastest and most robust method of transferring data between the clusters. 

If there are members of your group who are no longer active and their directories contain data you would like to retain, please [reach out to us](/#get-help) to change the ownership of those files to an active group member so they can transfer the data. When transferring to Bouchet we recommend uploading the files to either the "shared" directory in project or in the directory of an active group member (rather than perpetuating the inactive group member's directories on Bouchet).

### Storage Allocations

**If you have a paid storage allocation on the Palmer filesystem, there is no need to transfer that data to Bouchet.**  Shortly ahead of the final February node migration, the Palmer filesystem will be removed from Grace and McCleary and added to Bouchet. Groups with paid storage allocations on Palmer will be contacted separately regarding the Palmer migration.

The Gibbs filesystem will stay on McCleary at West Campus. Non-YCGA groups with current (not expired) paid storage allocations on Gibbs will be contacted individually to transfer their allocation and data to Bouchet's new Boyd filesystem.

If your storage allocation is expired, please [contact us](/#get-help) if you would like to purchase a storage allocation on Bouchet. 

If you would like assistance transferring your paid storage allocation or otherwise have questions or concerns about your data transfer, please [reach out to us](/#get-help) for assistance.

## Get Help

As always, our Research Support staff members are available to assist, including at our [twice-weekly virtual Office Hours](/#office-hours-via-zoom). Please [reach out](/#get-help) if you have any questions or concerns about what will be moved to Bouchet and when.



