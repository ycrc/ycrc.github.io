# Loomis Decommission

After over eight years in service, the primary storage system on Grace, Loomis (/gpfs/loomis), was retired in December 2022. Since its inception, Loomis  doubled in size to host over 2 petabytes of data for more than 600 research groups and almost 4000 individual researchers. The usage and capacity on Loomis has been replaced by two existing YCRC storage systems, Palmer and Gibbs. 

## Unified Storage at the YCRC

2022 saw the introduction of a more unified approach to storage across the YCRC’s clusters. Each group will have one project and one scratch space that is available on all of the HPC clusters (except for Milgram).

### Project

A single project space to host no-cost project-style storage allocations is available on the Gibbs storage system. Purchased allocations are also on Gibbs under the /gpfs/gibbs/pi space of the storage system. Grace users are using this space as of the August 2022 maintenance.

### Scratch

A single scratch space on Palmer, available for Grace users at /vast/palmer/scratch, serves both Grace and McCleary cluster (replacement for Farnam and Ruddle). The Loomis scratch space was decommissioned and purged on October 3, 2022.

### Software

In 2023, a new unified software and module tree was created on Palmer, so the same software will be available for use regardless of which YCRC HPC cluster you are using. 

We have migrated the software located in /gpfs/loomis/apps/avx to Palmer at /vast/palmer/apps/grace.avx. To continue to support this software without interruption, we are maintaining a symlink at /gpfs/loomis/apps/avx to the new location on Palmer, so software will continue to appear as if it is on Loomis even after the maintenance, despite being hosted on Palmer. In August 2023, Grace was upgraded to Red Hat 8 and this old software tree was deprecated and is no longer supported.

## What about Existing Data on Loomis?

Your Grace home directory was already migrated to Palmer during the January 2022 maintenance.

During the Grace Maintenance in August 2022, we migrated all of the Loomis project space (`/gpfs/loomis/project`) to the Gibbs storage system at `/gpfs/gibbs/project`. You will need to update your scripts and workflows to point to the new location (`/gpfs/gibbs/project/<group>/<netid>`). The "project" symlink in your home directory has been updated to point to your new space (with a few exceptions described below), so scripts using the symlinked path will not need to be updated.

If you had a project space that exceeds the no-cost allocation (4TiB), your data was migrated to a new allocation under `/gpfs/gibbs/pi`. In these instances, your group has been granted a new, empty "project" space with the default no-cost quota. Any scripts will need to be updated accordingly.

The Loomis scratch space was decommissioned and purged on October 3, 2022.

### Conda Environments

By default, all conda environments are installed into your project directory. However, most conda environments do not survive being moved from one location to another, so you may need to regenerate your conda environment(s). To assist with this, we provide [conda-export documentation](/clusters-at-yale/guides/conda-export/).

### R Packages

Similarly, in 2022 we started redirecting user R packages to your project space to conserve home directory usage. If your R environment is not working as expected, we recommend deleting the old installation (found in `~/project/R/<version>`) and rerunning install.packages.

### Custom Software Installations

If you or your group had any self-installed software in the project directory, it is possible that the migration will have broken the software and it will need to be recompiled.

### Decommission of Old, Deprecated Software Trees

As part of the Loomis Decommission, we did not be migrating the old software trees located at /gpfs/loomis/apps/hpc, /gpfs/loomis/apps/hpc.rhel6 and /gpfs/loomis/apps/hpc.rhel7. The deprecated modules can be identified as being prefixed with "Apps/", "GPU/", "Libs/" or "MPI/" rather than beginning with the software name. If you are using software modules in one of the old trees, please find an alternative in the current supported tree or reach out to us to install a replacement.

## Researchers with Purchased Storage on Loomis

If you had purchased space that is still active (not expired), we created a new area of the same size for you on Gibbs and transferred your data. 

If you have purchased storage on `/gpfs/loomis` that has expired or will be expiring in 2022 and you chose not to renew, any data in that allocation is now retired.
