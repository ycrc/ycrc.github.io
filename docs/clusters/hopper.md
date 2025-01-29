# Hopper

![Grace Hopper](/img/Grace-Hopper.jpg){: .cluster-portrait}

Hopper is a shared-use resource for all researchers at Yale University.
The Hopper cluster is named for the computer scientist and United States Navy Rear Admiral [Grace Murray Hopper](https://en.wikipedia.org/wiki/Grace_Hopper), who received her Ph.D. in Mathematics from Yale in 1934. 

When in production, Hopper will have been assessed by an external auditor for NIST 800-171 and HIPAA compliance, ensuring it is suitable for high performance computation of ePHI, CUI and certain other types of sensitive data.
Hopper consists of a variety of standard compute and GPU-enabled nodes and mounts an encrypted shared filesystem.

Hopper will be jointly support by the YCRC and HSIT to ensure a high level of service and facilitate secure computational research.
Hopper is one of a number of secure computing environments, such as SpinUp+ and [CHP](https://medicine.yale.edu/ybic/computational-resources/ynhhs/#computational-health-platform), developed to support a variety of secure computing needs.
As the Hopper production launch approaches, support staff will be available to assist researchers with identifying and accessing the most suitable compute resources for their research projects.

- - -

The Hopper HPC cluster will be available in a closed beta early 2025.
Beta access is by invitation only.
Hopper is expected to be in production and available to Yale researchers for use with ePHI, CUI and certain other types of sensitive data in summer 2025.

If you have any questions about Yale’s partnership at MGHPCC or the Hopper cluster, please [reach out to us](/).


!!! info
    All details on the account process and user experience is currently in development and subject to change depending on compliance and as we assess researcher needs. The following information describes the current envisioned environment.

## Access the Cluster

### Accounts

Before using Hopper, all users must successfully complete the a training program which includes NIST 800-171 and HIPAA training.
(Coming soon--for Beta Testing, you will be required to complete the training once it is available).
This training must be renewed annually.
Unlikely other YCRC HPC systems, access to the system is granted on a per project basis.
(During beta, your project will be called `<pi_netid>_beta`.)
A request for a specific project will need to be submitted by a PI and approved before user accounts can be created.

Once a project is approved, the project's PI is responisible for the approval of additional user accounts.
PIs are also required to conduct a regular review of user accounts on their projects (frequency TBD).
Failure to complete the review by the due date will result in the locking of all accounts associated with the project until the review is complete. 

Accounts will be deactivated when any of the following occurs: 

- Account is inactive for more than one year 
- Owner leaves the project 
- Owner leaves the university
- Owner fails to renew required training

### Log In

!!! info
    Connections to Hopper can only be made from the Yale VPN (`access.yale.edu`)--even if you are already on campus (YaleSecure or ethernet). See our [VPN page](/clusters-at-yale/access/vpn) for setup instructions.

Once you have [an account](https://research.computing.yale.edu/support/hpc/account-request), the cluster can be accessed through the Virtual Desktop Infrastructure (VDI).
The VDI functions as the ‘login node’ and isolates the user from their host computer.
The VDI will provide a virtual desktop with the standard YCRC cluster interfaces, such as the [Open OnDemand Web Portal](/clusters-at-yale/access/ood) and command line terminal access, to access files, run commands, and launch jobs.
To protect the security of the data on Hopper, the VDI prevents copy/pasting to the host computer, prevents file transfers (see below for how to transfer files) and enforces idle session timeouts.

To access the VDI, navigate to (URL Coming Soon) in a web browser.

## Transfer Data

Data may only be transferred to and from Hopper using an approved method as described below.
By default, all internet access is blocked, with only certain approved remote sites whitelisted.
All transfers of any type will be logged, and users remain responsible for following the restrictions that apply to their data. 

### High-Risk Data

All high-risk data transfers, either onto or out of the cluster, require approval.
Please contact us for approval and transfer assistance, including details on the data.

### Low-Risk Data

Low-risk files, such as scripts or low-risk data, can be uploaded to Hopper using Globus via the "Yale Hopper Low Risk" collection into a user-specific staging directory.
For details on using Globus, please read our [Globus documentation](/data/globus).
The user then must submit a request to the YCRC to have the transfer approved and then the data will be transferred to the desired location on Hopper by YCRC staff.
If your data is large (>100G), please submit your request _prior_ to uploading the data so we can facilitate the larger transfer.

Downloading of low-risk files from the cluster is the same process, but in reverse.
Submit a request to export your data, and once approved staff will transfer the data to a user-specific directory on the Globus server.
For data exporting, an additional attestion is required that the data is low-risk.
Then you can retrieve your data using Globus at your convenience.
Data will be purged from the staging area after a TBD amount of time.

## Software

All software must be approved and installed by YCRC staff, typically as [modules](/applications/modules).
No software may be installed by users, including conda environments and R packages.
A researcher's own analysis scripts, such as Python, R, MATLAB or bash scripts, do not qualify as software and are permissable to upload and run on the cluster without approval.
If you are unclear if your workflow qualifies as software, please contact your administrator for clarifications.
In the future, YCRC plans to make certain approved R and Python libraries available via a local clone of the repositories. 

## Submit Jobs

Jobs are run using Slurm in the usual way, either using interactive or batch allocations.  
All jobs must specify a ‘project’ account using the `-A` flag.
By default, nodes are shared with multiple jobs and users.
If the security of your project requires isolation, you must submit your jobs with `-X` flag to ensure an exclusive allocation.
Such projects will be clearly identified during the approval and onboarding process.
Data written to a node’s local disk is not visible to any other job and is automatically removed after the run completes (this is not in place for beta).

While the VDI will lock sessions after a certain amount of idle time, jobs submitted to the scheduler and sessions in the Web Portal will continue to run until they either complete (in the case of batch jobs), reach the limit of the requested wall time or are terminated by the user.

## Partitions and Hardware

Details on the partitions and concurrent usage limits will be posted at a later date.

## Storage

Hopper has access to one filesystem called `weston`. 
Weston is a VAST filesystem similar to the `palmer` filesystem on Grace and McCleary, with the additional of encryption-at-rest for all user data.
For more details on the different storage spaces, see our [Cluster Storage](/data/hpc-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. 
You have shortcuts in your home directory to each project's storage spaces that follow the form `~/work_<project>` and `~/scratch_<project>`.
You can also get a list of the absolute paths to your directories with the `mydirectories` command. 
Top-level folder permissions are managed by YCRC and cannot be modified by users.
Only users in a specific project will be able to access that project's storage spaces. 

For information on data recovery, see the [Backups and Snapshots](/data/backups) documentation.

!!! Warning
    Files stored in `scratch` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted. Artificial extension of scratch file expiration is forbidden without explicit approval from the YCRC. Please [purchase storage](/data/#purchase-additional-storage) if you need additional longer term storage.

|Fileset       | Root Directory                     | Storage          | File Count | Backups | Snapshots | Notes |
|--------------|------------------------------------|------------------|------------|---------|-----------|-------|
| home         | `/home`                            | 125GiB/user      | 500,000    | Not Yet | >=2 days  |       |
| work         | `/nfs/weston/work_<project>`       | 4TiB/project     | 5,000,000  | Not Yet | >=2 days  |       |
| scratch      | `/nfs/weston/scratch_<project>`    | 10TiB/project    | 15,000,000 | No      | No        |       |
