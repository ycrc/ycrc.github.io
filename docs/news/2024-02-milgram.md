---
date: '2024-02-08'
---

## Milgram Maintenance
_Februrary 6-8, 2024_

### Software Updates

- Slurm updated to 23.02.7
- NVIDIA drivers updated to 545.23.08
- Apptainer updated to 1.2.5
- Lmod updated to 8.7.32

### Upgrade to Red Hat 8
 
As part of this maintenance, the operating system on Milgram has been upgraded to Red Hat 8.

Jobs submitted prior to maintenance that were held and now released will run under RHEL8 (instead of RHEL7).  This may cause some jobs to not run properly, so we encourage you to check on your job output.  Our [docs page](/clusters/milgram_rhel8/) provides information on the RHEL8 upgrade, including fixes for common problems.  Please notify hpc@yale.edu if you require assistance. 

### Changes to Interactive Partitions and Jobs
 
We have made the following changes to interactive jobs during the maintenance.  

The 'interactive' and 'psych_interactive` partitions have been renamed to 'devel' and 'psych_devel', respectively, to bring Milgram in alignment with the other clusters.  This change was made on other clusters in recognition that interactive-style jobs (such as OnDemand and 'salloc' jobs) are commonly run outside of the 'interactive' partition.  Please adjust your workflows accordingly after the maintenance.

Additionally, all users are limited to 4 interactive app instances (of any type) at one time.  Additional instances will be rejected until you delete older open instances.  For OnDemand jobs, closing the window does not terminate the interactive app job.  To terminate the job, click the "Delete" button in your "My Interactive Apps" page in the web portal.

Please visit the status page at [research.computing.yale.edu/system-status](research.computing.yale.edu/system-status) for the latest updates.  If you have questions, comments, or concerns, please contact us at hpc@yale.edu.