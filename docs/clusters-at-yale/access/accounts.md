# Accounts & Best Practices

The YCRC HPC Policies can found [here](https://research.computing.yale.edu/services/high-performance-computing/hpc-policies). All users are required to abide by the described policies.

## User Responsibilities

* User accounts are personal to individual users and may not be shared. Never give your password or ssh key to anyone else. Never allow another individual to use your account. 
* Do not run jobs, transfers or computation on a login node, instead [submit jobs](/clusters-at-yale/job-scheduling/).
* Similarly, transfer nodes are only for data transfers. Do not run jobs or computation on the transfer nodes.
* Do not store any [high risk data](https://cybersecurity.yale.edu/protectyourdata) on the clusters, except [Milgram](/clusters/milgram).
* Jobs must be submitted to partitions in alignment with the stated purposes and limits of those partitions.
* Do not run large numbers of very short (less than a minute) jobs.
* Terminate interactive or Open OnDemand session when no longer in use. Idle sessions may be canceled without warning.
* Avoid workflows that generate numerous (thousands) of files as these put great stress on the shared filesystem.
* Use of scratch for long term storage, (through artificial extension of file expiration or other means) is forbidden without explicit approval from the YCRC. Please [purchase storage](/data/#purchase-additional-storage) if you need additional longer term storage.
* Any data covered by a DUA must be explicitly approved by the YCRC before it is stored on a cluster.
* Each YCRC cluster undergoes regular scheduled maintenance twice a year, see [our maintenance schedule](/clusters/maintenance) for more details. Please plan accordingly.

## Group Allocations

A research group may request an allocation on one of [Yale's HPC clusters](/clusters). Each group is granted access to the common compute resources and a [limited cluster storage allocation](/data). 

## Secondary Account Affiliations

If you belong to multiple research groups, you can be added to them through a secondary account affiliation. This can be requested through our [Group Change Request Form](http://research.computing.yale.edu/group-change).

On non-Bouchet or Hopper clusters, your PI name is the primary group of your account. On Bouchet, your primary group is your NetID, and secondary groups are assigned for any PI group you belong to. This setup makes the process of group change easier and can also accommodate "project"-based secondary groups rather than PI-based secondary groups.

On Hopper, access to the system is granted on a per project basis, so a single PI may have multiple projects. A request for a specific project will need to be submitted by a PI and approved before user accounts can be created.

Regardless of cluster access, users are responsible for storing their data within the appropriate storage affiliations as well as using the `--account` flag when appropriate to ensure the correct group is being referenced within Slurm.

## External Collaborators

The YCRC can provide access to the clusters and Yale’s network for collaborators at other institutions through Yale’s “Sponsored NetID” service. To request access for a new collaborator or extend access for a departing student or post doc, have your business office fill out the [Sponsored NetID Request Form](https://yale.service-now.com/it?id=service_offering&sys_id=6b4a8551db967e402de17ecfbf96193f) and [VPN Access Request Form](https://yale.service-now.com/it?id=service_offering&sys_id=c4684dcd6fbb31007ee2abcf9f3ee4f2). After receiving the sponsored NetID, you may submit the [HPC Account Request Form](https://research.computing.yale.edu/account-request).

### Request an Account

You may request an account on a cluster using the [account request form](https://research.computing.yale.edu/account-request).  User accounts are personal to individual users and may not be shared. Under no circumstances may any user make use of another user’s account.

## Inactive Accounts and Account Deletion

For security and communication purposes, you must have a valid email address associated with your account. Login privileges will be disable on a regular basis for any accounts without a valid email address. Therefore, if you are leaving Yale, but will continue to use the cluster on a ["Sponsored netid"](https://research.computing.yale.edu/services/collaboration-support), please [contact us](/#get-help) to update the email address associated with your account as soon as possible. If you find your login has been disabled, please contact us to provide a valid email address to have your login reinstated.

Additionally, an annual account audit is performed on **November 1st** and any accounts associated with an inactive netids (regular and Sponsored netids) will be deactivated at that time. Note that Sponsored netids need to be renewed annually through the appropriate channels.

When an account is deactivated, logins and scheduler access are disabled, the home directory is archived for 5 years and all project data owned by the account is reassigned to the group's PI. The group's PI will receive a report once a year in November with a list of deactivated group members. 

Every group must have a PI with a valid affiliation with Yale. If your PI has left Yale, you may be asked to identify a new faculty sponsor for your account in order to continue accessing the cluster.

