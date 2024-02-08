# Accounts & Best Practices

The YCRC HPC Policies can found [here](https://research.computing.yale.edu/services/high-performance-computing/hpc-policies). All users are required to abide by the described policies.

## HPC Policies

* Do not run jobs, transfers or computation on a login node, instead [submit jobs](/clusters-at-yale/job-scheduling/).
* Similarly, transfer nodes are only for data transfers. Do not run jobs or computation on the transfer nodes.
* Never give your password or ssh key to anyone else.
* Do not store any [high risk data](https://cybersecurity.yale.edu/protectyourdata) on the clusters, except [Milgram](/clusters/milgram).
* Do not run large numbers of very short (less than a minute) jobs.
* Terminate interactive or Open OnDemand session when no longer in use. Idle sessions may be canceled without warning.
* Avoid workflows that generate numerous (thousands) of files as these put great stress on the shared filesystem.
* Artificial extension of scratch file expiration is forbidden without explicit approval from the YCRC. Please [purchase storage](/data/#purchase-additional-storage) if you need additional longer term storage.
* Each YCRC cluster undergoes regular scheduled maintenance twice a year, see [our maintenance schedule](/clusters/maintenance) for more details. 


## Group Allocations

A research group may request an allocation on one of [Yale's HPC clusters](/clusters). Each group is granted access to the common compute resources and a [limited cluster storage allocation](/data). 

## External Collaborators

The YCRC can provide access to the clusters and Yale’s network for collaborators at other institutions through Yale’s “Sponsored NetID” service. To request access for a new collaborator or extend access for a departing student or post doc, have your business office fill out the [Sponsored NetID Request Form](https://yale.service-now.com/it?id=service_offering&sys_id=6b4a8551db967e402de17ecfbf96193f) and [VPN Access Request Form](https://yale.service-now.com/it?id=service_offering&sys_id=c4684dcd6fbb31007ee2abcf9f3ee4f2). After receiving the sponsored NetID, you may submit the [HPC Account Request Form](https://research.computing.yale.edu/node/3822).

### Request an Account

You may request an account on a cluster using the [account request form](https://research.computing.yale.edu/account-request).  User accounts are personal to individual users and may not be shared. Under no circumstances may any user make use of another user’s account.

## Inactive Accounts and Account Deletion

For security and communication purposes, you must have a valid email address associated with your account. Login privileges will be disable on a regular basis for any accounts without a valid email address. Therefore, if you are leaving Yale, but will continue to use the cluster on a ["Sponsored netid"](https://research.computing.yale.edu/services/collaboration-support), please [contact us](/#get-help) to update the email address associated with your account as soon as possible. If you find your login has been disabled, please contact us to provide a valid email address to have your login reinstated.

Additionally, an annual account audit is performed on **November 1st** and any accounts associated with an inactive netids (regular and Sponsored netids) will be deactivated at that time. Note that Sponsored netids need to be renewed annually through the appropriate channels.

When an account is deactivated, logins and scheduler access are disabled, the home directory is archived for 5 years and all project data owned by the account is reassigned to the group's PI. The group's PI will receive a report once a year in November with a list of deactivated group members. 

Every group must have a PI with a valid affiliation with Yale. If your PI has left Yale, you may be asked to identify a new faculty sponsor for your account in order to continue accessing the cluster.

