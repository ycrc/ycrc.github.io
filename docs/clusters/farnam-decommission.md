# McCleary Cluster

After several years in service, we will be retiring the Farnam and Ruddle HPC clusters in 2023. 

Farnam and Ruddle are being replaced with the new HPC cluster, McCleary. McCleary is named for Beatrix McCleary Hamburg, who received her medical degree in 1948 and was the first female African American graduate of Yale School of Medicine. The McCleary HPC cluster is Yale's first direct-to-chip liquid cooled cluster, moving the YCRC and the Yale research computing community into a more environmentally friendly future.
 
## McCleary HPC Cluster

The [McCleary HPC cluster](/clusters/mccleary) is comprise over 3000 direct-to-chip water cooled cores, latest generation GPU nodes and our first 4TB large memory nodes.
Later generation nodes from Farnam will also be added to McCleary to complement the new resources, while Farnam and Ruddle’s oldest nodes will be retired. 

McCleary’s home and scratch spaces are on the all-flash storage system, Palmer. 

Project and PI-purchased storage is available on the Gibbs storage system. YCGA users have additional access to `/gpfs/ygca`, which is also mounted on Ruddle. At a later date there will be a drop-in replacement for project and sequencers data from Ruddle. 
 
## How to Get a McCleary Account

We have automatically created accounts for most users who have been active on either cluster in 2022. If this applies to you, you will have received a "Welcome to McCleary" email with instructions on logging in.

If you have not used Farnam or Ruddle since January 1st, 2022, you will need to request an account on McCleary on [our account request form](https://research.computing.yale.edu/support/hpc/account-request).

## What about My Existing Data on Farnam?

Farnam’s primary filesystem, YSM (/gpfs/ysm), will be retired with the Farnam cluster. **All data on YSM (that you want to keep) will need to be transferred off the cluster, either to non-HPC storage or to a McCleary account.** More information and instructions on transferring data is available [here](/data/mccleary-transfer/.

## What about My Existing Data on Ruddle?

All data in project storage as well as sequencer data on Ruddle will be transferred to a new filesystem, which will be a drop in a replacement on McCleary for the existing `/gpfs/ycga` storage.

All data you would like to keep from your Ruddle home and scratch60 directories will need to manually transferred either to non-HPC storage or to a McCleary account prior to Ruddle decommission.
 
If you have data on the Gibbs, there is no action required as they will be available on McCleary.

## Researchers with Purchased Nodes or Storage

If you have purchased space on /gpfs/ycga or /gpfs/ysm that is still active (not expired), we will migrate your allocation at a mutually agreeable time. **This is the only data that the YCRC will be automatically migrating from Farnam to McCleary.**  

If you have purchased storage on /gpfs/ysm that has expired as of December 31st 2022, you should have received a separate communication from us with information on purchasing replacement storage on Gibbs (which will be available on McCleary).
 
Likewise, if you have purchased nodes on Farnam that are at their end of life (`haswell` generation nodes), you should have received a separate communication from us with more information. All newer nodes will be transferred to McCleary and placed in similarly named partitions as on Farnam and Ruddle. Communications about node migrations will be sent when McCleary becomes available.
 
If you have any questions or concerns about what will be moved to McCleary and when, please reach out to us.