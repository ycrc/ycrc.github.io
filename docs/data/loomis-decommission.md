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

During the Grace Maintenance in August 2022, we migrated all of the Loomis project space (`/gpfs/loomis/project`) to the Gibbs storage system at `/gpfs/gibbs/project`. You will need to update your scripts and workflows to point to the new location (`/gpfs/gibbs/project/<group>/<netid>`). The "project" symlink in your home directory has been updated to point to your new space (with a few exceptions described below), so scripts using the symlinked path will not need to be updated.

If you had a project space that exceeds the no-cost allocation (4TiB), you have received a separate communication from us with details about your data migration. In these instances, your group has been granted a new, empty "project" space with the default no-cost quota. Any scripts will need to be updated accordingly.

The Loomis scratch space was decommissioned and purged on October 3, 2022.

### Conda Environments

By default, all conda environments are installed into your project directory. However, most conda environments do not survive being moved from one location to another, so you may need to regenerate your conda environment(s). To assist with this, we provide [documentation and a helper script](https://docs.ycrc.yale.edu/clusters-at-yale/guides/conda-clone/).

### R Packages 

Similarly, in 2022 we started redirecting user R packages to your project space to conserve home directory usage. If your R environment is not working as expected, we recommend deleting the old installation (found in `~/project/R/<version>`) and rerunning install.packages.

### Custom Software Installations

If you or your group had any self-installed software in the project directory, it is possible that the migration will have broken the software and it will need to be recompiled.

## Researchers with Purchased Storage on Loomis

If you have purchased space on `/gpfs/loomis` that is still active (not expired), we will create a new area of the same size for you on Gibbs and will coordinate the transfer of the data with your group. 

If you have purchased storage on `/gpfs/loomis` that has expired or will be expiring in 2022, you will have received a separate communication from us with information on purchasing replacement storage on Gibbs.
