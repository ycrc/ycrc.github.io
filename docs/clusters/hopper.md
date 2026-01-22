# Hopper

![Grace Hopper](/img/Grace-Hopper.jpg){: .cluster-portrait}

Hopper is a shared-use resource for all researchers at Yale University for high performance computation of [electronic Protected Health Information (ePHI)](https://en.wikipedia.org/wiki/Protected_health_information), [NIH Controlled-Access Data](https://docs.ycrc.yale.edu/data/nih-data), [Controlled Unclassified Information (CUI)](https://en.wikipedia.org/wiki/Controlled_Unclassified_Information) and [certain other types of sensitive data](https://cybersecurity.yale.edu/data-classification).
Hopper consists of a variety of standard compute and GPU-enabled nodes and mounts an encrypted shared filesystem.
The Hopper cluster is named for the computer scientist and United States Navy Rear Admiral [Grace Murray Hopper](https://en.wikipedia.org/wiki/Grace_Hopper), who received her Ph.D. in Mathematics from Yale in 1934. 

Hopper is jointly supported by the YCRC and [Health Sciences Information Technology (HSIT)](https://healthsciencesit.yale.edu/) to ensure a high level of service and facilitate secure computational research.
Hopper is one of a number of secure computing environments, such as [SpinupPlus](https://medicine.yale.edu/ybic/computational-resources/yale/) and [CHP/SAFE](https://medicine.yale.edu/ybic/computational-resources/ynhhs/#computational-health-platform), developed to support a variety of secure computing needs.
Support staff are available to assist researchers with identifying and accessing the most suitable compute resources for their research projects.


!!! info "Upcoming Maintenance"
    The next quarterly maintenance for Hopper is scheduled for March 2026. During this time the cluster will be unavailable.

## Access the Cluster

### Projects

Unlikely other YCRC HPC systems, access to the system is granted on a per project basis, so a single PI may have multiple projects.
Projects are named `<pi_netid>_<project_code>`.
A request for a specific project will need to be submitted by a PI and approved before user accounts can be created.

Once a project is approved, the project's PI is responisible for the approval of additional user accounts.
PIs are also required to conduct a quarterly review of user accounts on their projects.
Failure to complete the review by the due date will result deactivation of the project (inability to submit jobs or access data for the project) until the review is complete.

Projects will also be deactivated if their expiration date has elapsed (if applicable) or otherwise at the PI's discretion.

Email us at [research.computing@yale.edu](mailto:research.computing@yale.edu) to inquire about using Hopper.

### Accounts

All accounts must be associated with an active project and approved by projects' PIs.

Additional accounts on *existing* projects (see above to request a new project) can be requested
by submitting the [Hopper Account Request Form](https://research.computing.yale.edu/hopper-account-request).

!!! warning "Sponsored Netids"
    At the moment we cannot provide Hopper accounts for Sponsored Netids due to the current background screening security requirements. Yale Information Security is exploring other avenues for granting access approval but we do not have an estimate for availability. We apologize for any inconvenience.

Before access is granted, users must successfully complete the training program linked below,
which includes NIST 800-171 and HIPAA training. 
All users must complete the full training program, regardless of the risk classification of their data,
but they will not be required to retake any training that is up-to-date (e.g. HIPAA training).
This training must be renewed annually.

[Hopper Required Training](http://research.computing.yale.edu/regulated-research-training){ .md-button }

Accounts will be deactivated when any of the following occurs: 

- Account is no longer associated with any active projects 
- Account is inactive for more than one year 
- Owner leaves the university
- Owner fails to renew required training
- Owner fails to follow security measures (e.g. takes photos of screens, does not segment work into projects with specific personnel permissions, includes non-authorized data, etc.)

### Log In

!!! info
    Connections to Hopper can only be made from the Yale VPN (`access.yale.edu`)--even if you are already on campus (YaleSecure or ethernet). See our [VPN page](/clusters-at-yale/access/vpn) for setup instructions.

!!! warning
    Connections to the VPN need to be younger than 24 hours to connect to Hopper. If you are unable to connect to Hopper, please try disconnecting from and reconnecting to the Yale VPN.

Once you have an account, the cluster can be accessed through the Virtual Desktop Infrastructure (VDI).
The VDI functions as the ‘login node’ and isolates the user from their host computer.
The VDI provides a virtual desktop with the standard YCRC cluster interfaces, such as the [Open OnDemand Web Portal](/clusters-at-yale/access/ood) and command line terminal access, to access files, run commands, and launch jobs.

To access the VDI, navigate to `hopper1.ycrc.yale.edu` in a web browser.

[Hopper Login (VPN required)](https://hopper1.ycrc.yale.edu){ .md-button }

### Security Restrictions

To protect the security of the data on Hopper and to comply with NIST 800-171 and HIPAA regulations, Hopper has a number of addition restrictions beyond other YCRC systems.

- The VDI prevents copy/pasting to the host computer, prevents file transfers (see below for how to transfer files) and enforces idle session timeouts. (See below for tips on copy/paste *within* Hopper).
- Screenshots, screen recording and screen sharing (e.g. via Zoom) are strictly prohibited (see below for how to record and report issues).
- If you know you will be away from your computer for more than 10 minutes, you must disconnect from the VDI. This can be easily done by simply closing the browser tab.
- You must access Hopper from a private location, such as your home or office. Access from public locations such as coffee shopts, transportation hubs or libraries is not allowed.
- Do not put sensitive data (e.g. patient information, personal identifiers) in directory names or job names, which might inadvertently expose this information.


## Report an Issue

If you run into an issue on Hopper and would think it would be helpful to take a picture of your session (e.g. to record an error message), click the "Report an Issue" icon on your VDI desktop.
This will place a capture of your screen in a folder where it can be reviewed by YCRC staff.
Please notify YCRC staff in [your help request](/) if you have recorded your issue in this way.

## Transfer Data

Data may only be transferred to and from Hopper using an approved method as described below.
By default, all internet access is blocked, with only certain approved remote sites whitelisted.
All transfers of any type will be logged, and users remain responsible for following the restrictions that apply to their data. 

### Low-Risk Data

Low-risk files, such as scripts or low-risk data, can be uploaded to Hopper using Globus via the "Yale CRC Hopper Low Risk" collection into a user-specific staging directory.
For details on using Globus, please read our [Globus documentation](/data/globus).
The user then must submit a request to the YCRC to have the transfer approved and then the data will be transferred to the desired location on Hopper by YCRC staff.
If your data is large (>200G), please submit your request _prior_ to uploading the data so we can facilitate the larger transfer.

Downloading of low-risk files from the cluster is the same process, but in reverse.
submit a request to the YCRC to export your data, and once approved staff will transfer the data to a user-specific directory on the Globus server.
Then you can retrieve your data using Globus at your convenience.

[Submit Low-Risk Transfer Request](https://research.computing.yale.edu/hopper-low-risk-transfer){ .md-button }

### All Other Data

Transfers of any data other than low-risk data (see above), either onto or out of the cluster, require approval.

[Submit Incoming Sensitive Data Transfer Request](https://research.computing.yale.edu/hopper-sensitive-transfer){ .md-button }

For outgoing transfers of high-risk classification data, contact us at [research.computing@yale.edu](mailto:research.computing@yale.edu).

## Software

All software must be approved and installed by YCRC staff, typically as [software modules](/applications/modules).
No software may be installed by users.
A researcher's own analysis scripts, such as Python, R, MATLAB or bash scripts, do 
not qualify as software and are permissible to upload and run on the cluster without approval.
If you are unclear if your workflow qualifies as software, please contact your administrator for clarifications.

To request software be installed on Hopper, contact us at [research.computing@yale.edu](mailto:research.computing@yale.edu).

### R and Python Packages

We have set up a monitored proxy to PyPI and CRAN to allow you to install your own 
Python and R packages using the standard methods (i.e. `pip`, `install.packages`). 
From the `hopper1` login node (where you go when you connect via the ThinLinc VDI), you can 
use conda with the default Conda repo (not conda-forge or bioconductor) and `pip` to create your own environments.

### Open OnDemand

To access the [Open OnDemand Web Portal](/clusters-at-yale/access/ood/) on Hopper, open Firefox (available on the top menu bar) within the ThinLinc VDI and
navigate to `ood-hopper.ycrc.yale.edu`.
You will need to reauthenticate on Open OnDemand with your netid, password and DUO.

### LLM Models

LLM models, such as Llama, qualify as software so must be approved and installed by YCRC staff.

We have made commonly requested LLM models available as [software modules](/applications/modules) for easier offline use.

To use an offline LLM model, run `module load <module name>`.
Run `module display <module name>` to determine the environment variable for the model path.
Reference the environment variable (e.g. `LLM_LLAMA`) for the model path in your python commands. For example: 

```
model_path = os.environ["LLM_LLAMA"]
model = LlamaForCausalLM.from_pretrained(model_path, local_files_only=True)

OR

model_path = os.environ["LLM_LLAMA"]
pipeline = transformers.pipeline("text-generation", model=model_path, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")
```

If you need additional LLM models that are not yet installed, [contact us](/#get-help) to request that we add it.
Please be selective when requesting very large models (e.g. > 100B parameters)--due to their large size we can only host a limited number of these models.

## Submit Jobs

Jobs are run [using Slurm in the usual way](/clusters-at-yale/job-scheduling), either using interactive or batch allocations.  
All jobs must specify a ‘project’ account using the `-A` flag.
By default, nodes are shared with multiple jobs and users.
If the security of your project requires isolation, you must submit your jobs with `-X` flag to ensure an exclusive allocation.
Such projects will be clearly identified during the approval and onboarding process.

At the moment, Slurm will not send job status emails, so please login to check the status of your jobs.

While the VDI will lock sessions after 20 minutes of idle time, jobs submitted to the scheduler and sessions in the Web Portal will continue to run until they either complete (in the case of batch jobs), reach the limit of the requested wall time or are terminated by the user.


## Copy/Paste

The VDI prevents copy/pasting to the host computer in order to prevent unrestricted, unmonitored transfer of data between Hopper and the host computer.
This restrictions allows Hopper users to access the environment from their own personal machines rather than a secure computer.

There is the ability to copy/paste *within* Hopper using the Linux Terminal keyboard shortcuts (as well as right-clicking), Shift+Control+C and Shift+Control+V. 
These keyboard shortcuts can be customized on a per-user basis by:

- Right-click in Terminal and click "Show Menubar"
- Select Edit > Keyboard Shortcuts...
- Modified the desired keyboard shortcuts


## Rate Structure

Early access usage on Hopper is at no-cost. Computations and storage on Hopper will be subject to the following charges starting February 1st, 2026.

Compute and storage charges are billed monthly, with the bills expected the first week of the following month. 
To assist with cost estimates and budgeting, we provide a [Hopper Cost Calculator](https://docs.google.com/spreadsheets/d/1zoQq5uqMb37Nbf11cFdvRXk2Lm411R1zo2n8AEHRE_M).

### Compute

|  Type          | Subtype(s)     | Service Units  | Cost per Hour  |
|----------------|----------------|------|-------|
| Compute Hour\* |  -               | 1    |  $0.004 |
| GPU Hour       | A40, L40s, A5000 | 122.5 | $0.490 |
| GPU Hour       | H100            | 247.5 | $0.990 |
| GPU Hour       | H200            | 372.5 | $1.490 |

\* *Number of Service Units (SUs) per non-GPU compute job is the maximum of the CPU core count and the total RAM allocation/15GB*

Usage is billed for actual runtime, not requested walltime of a job. 
However, all compute resources (CPUs, memory, GPUs) allocated to a job are billed, regardless of whether a job makes use of those resources.

### Additional Storage

Additional work-style storage beyond the no-cost allocation described below can be provided at a rate of $5.15 per TiB per month.
Storage charges are based on requested allocation, not actual usage.
Purchased storage will be located at `/nfs/weston/pi/<pi>_<projectcode>`. 
Storage charges are based on requested allocation, not actual usage.
[Contact us](/#get-help) to request additional storage allocations.


## Partitions and Hardware

See each tab below for more information about the available common use partitions.

--8<-- "snippets/hopper_partitions.md"

## Storage

Hopper has access to one filesystem called `weston`. 
Weston is a VAST filesystem similar to the `palmer` filesystem on Grace and McCleary, with the addition of encryption-at-rest for all user data.
For more details on the different storage spaces, see our [Cluster Storage](/data/hpc-storage) documentation.

You can check your current storage usage & limits by running the `getquota` command. 
You have shortcuts in your home directory to each project's storage spaces that follow the form `~/work_<project>` and `~/scratch_<project>`.
You can also get a list of the absolute paths to your directories with the `mydirectories` command. 
Top-level folder permissions are managed by YCRC and cannot be modified by users.
Only users in a specific project will be able to access that project's storage spaces. 

See [Purchased Storage rates](/clusters/hopper/#purchase-storage) above for details on purchasing storage.

For information on data recovery, see the [Backups and Snapshots](/data/backups) documentation.

!!! Warning
    Files stored in `scratch` are purged if they are older than 60 days. You will receive an email alert one week before they are deleted. Artificial extension of scratch file expiration is forbidden without explicit approval from the YCRC. Please [purchase storage](/data/#purchase-additional-storage) if you need additional longer term storage.

|Fileset       | Root Directory                              | Storage          | File Count | Backups | Snapshots | Notes |
|--------------|---------------------------------------------|------------------|------------|---------|-----------|-------|
| home         | `/home`                                     | 125GiB/user      | 500,000    | No      | 7 days    |       |
| work         | `/nfs/weston/work/<pi>_<projectcode>`       | 1TiB/project     | 5,000,000  | No      | 7 days    |       |
| scratch      | `/nfs/weston/scratch/<pi>_<projectcode>`    | 10TiB/project    | 15,000,000 | No      | No        |       |
| pi           | `/nfs/weston/pi/<pi>_<projectcode>`         | varies           | varies     | No      | No        |       |
