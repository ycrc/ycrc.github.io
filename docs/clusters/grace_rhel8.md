# Grace Operating System Upgrade

Grace's previous operating system, Red Hat (RHEL) 7, will be officially end-of-life 
in 2024 and will no longer be supported with security patches by the developer.
Therefore Grace has been upgraded to RHEL 8 during the August maintenance window, August 15-17, 2023.
This provides a number of key benefits to Grace:

1. consistency with the McCleary cluster
1. continued security patches and support beyond 2023
1. updated system libraries to better support modern software
1. improved node management system to facilitate the growing number of nodes on Grace
1. shared application tree between McCleary and Grace, which brings software parity between the clusters\*

\* some software and workflows will only be supported by YCRC staff on one of the cluster, e.g. tightly couple MPI codes (Grace) or RELION (McCleary).

## New Host Key

The ssh host key for Grace's login nodes were changed during the August maintenance, which will result in an error similar to the following when you attempt to login for the first time after the maintenance.

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
```

To access the cluster again, first remove the old host keys with the following command (if accessing the cluster via command line):

```
ssh-keygen -R grace.hpc.yale.edu
```

If you are using a GUI, such as MobaXterm, you will need to manually edit your known host file and remove the lines related to Grace. For MobaXterm, this file is located (by default) in `Documents\MobaXterm\home\.ssh`.

Then attempt a new login and accept the new host key. The valid host keys for the login nodes are as follows:

```
3072 SHA256:8jJ/dKJVntzBJQWW8pU901PHbWcIe2r8ACvq30zQxKU login1 (RSA)
256 SHA256:vhmGumY/XI/PAaheWQCadspl22/mqMiUiNXk+ov/zRc login1 (ECDSA)
256 SHA256:NWNrMNoLwcqMm+E2NpsKKmirSbku9iXgbfk8ucn5aZE login1 (ED25519)
```

## New Software Tree

Grace now shares a software module tree with the McCleary cluster, providing a more consistent experience for all our users.
Existing applications will continue to be available during this transition period.
We plan to deprecate and remove the old application tree during the December 2023 maintenance window.

If you experience any issues with software, please let us know at [hpc@yale.edu](mailto:hpc@yale.edu) and we can look into reinstalling.

## Common Errors

### Python not found

Under RHEL8, we have only installed Python 3, which must be executed using `python3` (not `python`). 
As always, if you need additional packages, we strongly recommend setting up your own [conda environment](/clusters-at-yale/guides/conda/).

In addition, Python 2.7 is no longer support and therefore not installed by default. 
To use Python 2.7, we request you setup a [conda environment](/clusters-at-yale/guides/conda/).

### Missing System Libraries

Some of the existing applications may depend on libraries that are no longer installed in the operating system.
If you run into these errors please email [hpc@yale.edu](mailto:hpc@yale.edu) and include which application/version you are using along with the full error message.
We will investigate these on a case-by-case basis and work to get the issue resolved.

There will be a small number of compute nodes reserved with RHEL7 (in a partition named `legacy`) to enable work to continue while we resolve these issues.
This partition will remain available until the December maintenance window.

!!! Warning
    Some of the applications in the new shared apps tree may not work perfectly on the legacy RHEL7 nodes. 
    When running jobs in the legacy partition, you should therefore run `module 
reset` at the beginning of interactive sessions and add it to the start of your batch scripts. 
    This will ensure that you only load modules built for RHEL7.

## Report Issues

If you continue to have or discover new issues with your workflow, feel free to [contact us](/) for assistance. Please include the working directory, the commands that were run, the software modules used, and any more information needed to reproduce the issue.

