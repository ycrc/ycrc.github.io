# Grace and McCleary Decommission

## Data Center Migration

The YCRC is in the process of transitioning from the Yale West Campus Data Center to the [MGHPCC data center](https://news.yale.edu/2025/02/26/yale-grows-capacity-high-performance-computing-ai-related-research). The [Bouchet](bouchet.md) cluster, Yale's first cluster hosted at MGHPCC, is the successor to both Grace and McCleary, with HPC infrastructure refreshes and growth deployed at MGHPCC going forward. In 2026, we are decommissioning Grace and McCleary and all non-YCGA data and workloads will be moved to Bouchet.

## Phased Decommission & Migration

During this phased migration, we will be fully decommissioning Grace as a standalone cluster and the McCleary cluster will be downsized to support exclusively YCGA-affiliated workloads. Newer nodes from Grace and McCleary and some of the attached storage will be moved to MGHPCC and added to Bouchet as additional capacity. The migration will happen in three phases, described below.

- [Phase 1](#phase-1) (**Complete**): Migration of workloads and data from research groups who do not use dedicated compute nodes, CyroEM resources or YCGA resources.

- Phase 2 (late 2026, early 2027): Migration of non-YCGA workloads and non-YCGA data from YCGA-affiliated research groups from McCleary. YCGA data and workloads will remain on McCleary for the remaining lifetime of the YCGA-owned hardware.

- Phase 3 (late 2026, early 2027): Migration of newer commons nodes from Grace and McCleary to Bouchet. Migration of newer dedicated nodes along with their associated research groups and data. Grace will be shut down. McCleary will remain as a YCGA-only cluster for the remaining lifetime of YCGA-owned hardware (at least late 2027).

![When Will I Move Flow Chart](/img/when_will_i_move.png){: .cluster-diagram}

If you are in Phase 2 or 3, more detailed information will be provided later this year when the hardware migration dates are finalized.

## Phase 1

Research groups who do not use dedicated compute nodes or YCGA resources were moved off of Grace and McCleary in Phase 1.
As of June 1st, users in Phase 1 no longer have access to Grace and McCleary.

## Groups that use YCGA resources

YCGA users, whether or not you use additional dedicated nodes, will retain access to McCleary for the rest of its lifetime for YCGA-related workloads (likely another couple years). This winter we will reach out to YCGA users about moving non-YCGA data and workflows to Bouchet, but there is no action required at this time.

When you do move your data, you will be responsible for identifying the non-YCGA data you would like to keep from your home, project, and scratch and transferring it either to non-HPC storage or to a Bouchet account but we will be available to assist with that process.

## Groups that use dedicated partitions

All non-YCGA hardware will either be moved to Bouchet or decommissioned, depending on age. All dedicated partitions on Grace and McCleary (other than YCGA) will be decommissioned at the time of the data center migration this winter. Only nodes still under warranty as of January 1st, 2027 will be deployed into dedicated partitions at MGHPCC onto the Bouchet cluster. We will contact each partition’s PI to confirm the future status of their dedicated partitions.

**Non-YCGA users who use dedicated nodes** will lose access to Grace, which will be shut down permanently, and/or McCleary. Later this fall we will reach out about moving data and workflows to Bouchet but there is nothing to do at this time.


## What about My Existing Data on Grace or McCleary?

We are currently experiencing a storage shortage on Bouchet, so **we kindly request that you leave any existing data on Grace and/or McCleary on those clusters for now**. We have purchased additional storage for Bouchet that should be available this fall. When that is available we will reach out again to provide information about data transfers.

If you have a paid storage allocation, only current (not expired) paid storage allocations will be considered for migration, so please respond in a timely manner to communications from the YCRC regarding renewing agreements to avoid losing access to your data.

!!! warning "NIH Controlled Access Data"

	If you have any data on Grace or McCleary that is now covered by the [NIH Controlled Access Data policies](https://sharing.nih.gov/sites/default/files/flmngr/NIH-Security-BPs-for-Users-of-Controlled-Access-Data.pdf), this data cannot be moved to Bouchet but instead must be moved to the [Hopper](hopper.md) HPC cluster. [Submit this form to request Hopper access](https://research.computing.yale.edu/secure-project-request)


## Get Help

As always, our Research Support staff members are available to assist, including at our [twice-weekly virtual Office Hours](/#office-hours-via-zoom). Please [reach out](/#get-help) if you have any questions or concerns about what will be moved to Bouchet and when.



