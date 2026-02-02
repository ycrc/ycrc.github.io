# Data Center Migration

## Overview

The YCRC is in the process of transitioning from the Yale West Campus Data Center to the [MGHPCC data center](https://news.yale.edu/2025/02/26/yale-grows-capacity-high-performance-computing-ai-related-research). The [Bouchet](bouchet.md) cluster, Yale's first cluster hosted at MGHPCC, is the successor to both Grace and McCleary, with HPC infrastructure refreshes and growth deployed at MGHPCC going forward. In 2026, we are decommissioning Grace and McCleary and most data and workloads on those systems will be moved to Bouchet.

## Phased Migration

During this phased migration, we will be fully decommissioning Grace as a standalone cluster and the McCleary cluster will be downsized to support exclusively YCGA-affiliated workloads. Newer nodes from Grace and McCleary and some of the attached storage will be moved to MGHPCC and added to Bouchet as additional capacity. The migration will happen in three phases, described below.

-  Phase 1 (first half of 2026): Migration of workloads and data from research groups without dedicated compute nodes and are not YCGA-affiliated.

- Phase 2 (late 2026, early 2027): Migration of non-YCGA workloads and non-YCGA data from YCGA-affiliated research groups from McCleary.

- Phase 3 (late 2026, early 2027): Migration of newer commons nodes from Grace and McCleary to Bouchet. Migration of newer dedicated nodes along with their associated research groups and data. Grace will be shut down. McCleary will remain as a YCGA-only cluster for the remaining lifetime of that hardware.

![When Will I Move Flow Chart](/img/when_will_i_move.png){: .cluster-diagram}

If you are in Phase 1, you will receive an email shortly with a detailed timeline and instructions on migrating your workloads and data off of Grace and McCleary.

If you are in Phase 2 or 3, more detailed information will be provided later this year when the hardware migration dates are finalized.

As always, if you have any questions or concerns, please contact us at research.computing@yale.edu.
