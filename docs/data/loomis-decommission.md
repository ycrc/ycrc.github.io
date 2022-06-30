# Loomis Decommission

After over eight years in service, the primary storage system on Grace, Loomis (/gpfs/loomis), will be retired later this year. Since its inception, Loomis has doubled in size to host over 2 petabytes of data for more than 600 research groups and almost 4000 individual researchers. The usage and capacity on Loomis will be replaced by two existing YCRC storage systems, Palmer and Gibbs, which are already available on Grace. 

## Unified Storage at the YCRC

This year will see the introduction of a more unified approach to storage across the YCRC’s clusters. Each group will have one project and one scratch space that is available on all of the HPC clusters (except for Milgram).

### Project

A single project space to host no-cost project-style storage allocations will be available on the Gibbs storage system, which has until now hosted PI-purchased storage allocations. Purchased allocations will also be on Gibbs under the /gpfs/gibbs/pi space of the storage system.

### Scratch

A single scratch space on Palmer, already available on Grace at /vast/palmer/scratch, will serve both Grace and the upcoming McCleary cluster (replacement for Farnam and Ruddle).  

### Software

In 2023, a new unified software and module tree will be created on Palmer, so the same software will be available for use regardless of which YCRC HPC cluster you are using.


## What about My Existing Data on Loomis?

Your Grace home directory was already migrated to Palmer during the January 2022 maintenance.

During the upcoming Grace Maintenance in August 2022, we will copy all of the Loomis project space (/gpfs/loomis/project) to the Gibbs storage system. After the migration, you will need to update your scripts and workflows to point to the new location (/gpfs/gibbs/project). The "project" symlink in your home directory will be updated during the maintenance to point to your new space (with a few exceptions described below), so script using the symlinked path will not need to be updated. If you have jobs pending going into the maintenance that use the absolute Loomis path, we recommend canceling, updating and then re-submitting those jobs so they do not fail coming out of maintenance.

If you have a project space that exceeds the no-cost allocation (4TB), you should have already or will receive a communication from us to either reduce your usage or create a new “pi” allocation on Gibbs to accommodate the overage, as applicable. In these instances, your group will be granted a new, empty "project" space on Gibbs with the default no-cost quota coming out of the maintenance. Any scripts will need to updated accordingly.

The Loomis scratch space will be frozen during the August 2022 maintenance. It will be put into a read-only mode such that all data will be purged as it reaches its respective 60-day expiration.
Any data in /gpfs/loomis/scratch60 you wish to retain after the freeze will need to be copied into another location (such as your new Gibbs project or Palmer scratch). As you already have a Palmer scratch space today, you can update your scripts and move data into /vast/palmer/scratch at your convenience.

### Conda Environments

While we will be transferring all data in your project directory to Gibbs, conda environments do not tolerate being moved to a new path and therefore will need to be rebuilt.

## Researchers with Purchased Storage on Loomis

If you have purchased space on /gpfs/loomis that is still active (not expired), we will create a new area of the same size for you on Gibbs and will coordinate the transfer of the data with your group. 

If you have purchased storage on /gpfs/loomis that has expired or will be expiring in 2022, you will have received a separate communication from us with information on purchasing replacement storage on Gibbs.
