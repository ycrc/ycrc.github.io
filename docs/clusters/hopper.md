# Hopper

![Grace Hopper](/img/Grace-Hopper.jpg){: .cluster-portrait}

Hopper is a shared-use resource for all researchers at Yale University.
The Hopper cluster is named for the computer scientist and United States Navy Rear Admiral [Grace Murray Hopper](https://en.wikipedia.org/wiki/Grace_Hopper), who received her Ph.D. in Mathematics from Yale in 1934. 

When in production, Hopper will have been assessed by an external auditor for NIST 800-171 and HIPAA compliance, ensuring it is suitable for high performance computation of ePHI, [NIH Controlled-Access Data](https://docs.ycrc.yale.edu/data/nih-data), CUI and certain other types of sensitive data.
Hopper consists of a variety of standard compute and GPU-enabled nodes and mounts an encrypted shared filesystem.

Hopper is jointly supported by the YCRC and HSIT to ensure a high level of service and facilitate secure computational research.
Hopper is one of a number of secure computing environments, such as SpinUp+ and [CHP](https://medicine.yale.edu/ybic/computational-resources/ynhhs/#computational-health-platform), developed to support a variety of secure computing needs.
As the Hopper production launch approaches, support staff will be available to assist researchers with identifying and accessing the most suitable compute resources for their research projects.

- - -

The Hopper HPC cluster is currently in a closed beta as of early 2025.
Beta access is by invitation only.
Hopper is expected to be in production and available to Yale researchers for use with ePHI, [NIH Controlled-Access Data](https://docs.ycrc.yale.edu/data/nih-data, CUI and certain other types of sensitive data in summer 2025.

Researchers using NIH Controlled-Access Data and Repositories [can use McCleary until July](/data/nih-data).

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

To access the VDI, navigate to `hopper1.ycrc.yale.edu` in a web browser.

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
The user then must [submit a request to the YCRC](https://forms.gle/YigxQdbvobaH7YDT6) to have the transfer approved and then the data will be transferred to the desired location on Hopper by YCRC staff.
If your data is large (>200G), please submit your request _prior_ to uploading the data so we can facilitate the larger transfer.

Downloading of low-risk files from the cluster is the same process, but in reverse.
[submit a request to the YCRC](https://forms.gle/YigxQdbvobaH7YDT6) to export your data, and once approved staff will transfer the data to a user-specific directory on the Globus server.
Then you can retrieve your data using Globus at your convenience.
Data will be purged from the staging area after a TBD amount of time.

## Software

All software must be approved and installed by YCRC staff, typically as [software modules](/applications/modules).
No software may be installed by users.
A researcher's own analysis scripts, such as Python, R, MATLAB or bash scripts, do 
not qualify as software and are permissible to upload and run on the cluster without approval.
If you are unclear if your workflow qualifies as software, please contact your administrator for clarifications.

### R and Python Packages

We have set up a monitored proxy to PyPI and CRAN to allow you to install your own 
Python and R packages using the standard methods (i.e. `pip`, `install.packages`). 
From the hopper1 login node (where you go when you connect via ThinLinc), you can now 
use conda with the default Conda repo (not conda-forge or bioconductor) and pip to create your own environments.

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

Jobs are run using Slurm in the usual way, either using interactive or batch allocations.  
All jobs must specify a ‘project’ account using the `-A` flag.
By default, nodes are shared with multiple jobs and users.
If the security of your project requires isolation, you must submit your jobs with `-X` flag to ensure an exclusive allocation.
Such projects will be clearly identified during the approval and onboarding process.
Data written to a node’s local disk is not visible to any other job and is automatically removed after the run completes (this is not in place for beta).

At this stage of the beta, Slurm will not send job status emails, so please login to check the status of your jobs.

While the VDI will lock sessions after a certain amount of idle time, jobs submitted to the scheduler and sessions in the Web Portal will continue to run until they either complete (in the case of batch jobs), reach the limit of the requested wall time or are terminated by the user.

## Partitions and Hardware

See each tab below for more information about the available common use partitions.

--8<-- "snippets/hopper_partitions.md"

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
| home         | `/home`                            | 125GiB/user      | 500,000    | Not Yet | 7 days  |       |
| work         | `/nfs/weston/work_<project>`       | 4TiB/project     | 5,000,000  | Not Yet | 7 days  |       |
| scratch      | `/nfs/weston/scratch_<project>`    | 10TiB/project    | 15,000,000 | No      | No        |       |
