# AICR

[AICR](https://www.mass.gov/news/governor-healey-advances-states-ai-leadership-with-major-investments-in-massachusetts-ai-hub) is a multi-institution AI-focused computing cluster at MGHPCC designed to support large-scale AI and AI-enabled research.

AICR is a partnership between the Commonwealth of Massachusetts and MGHPCC's six member universities: Boston University, Harvard University, MIT, Northeastern University, the University of Massachusetts, and Yale University. The system is shared across the participating institutions and provides large, tightly connected GPU resources that are particularly well suited to distributed, multi-node GPU workloads.

## Is AICR Right for My Research?

AICR is a specialized resource intended for experienced researchers with established, large-scale AI/ML workloads that cannot be effectively accommodated by Yale's existing HPC resources.

Yale already provides substantial GPU capacity on its existing HPC systems. Bouchet includes H200, B200, and other GPU resources for low-risk research data, while Hopper provides substantial H200 and B200 GPU capacity for research involving regulated or other high-risk data. **Most GPU workloads should continue to run on Bouchet or Hopper, as appropriate for the data involved.** This includes single-GPU workloads and many workloads using multiple GPUs within a single node.

AICR is intended primarily for established workloads that have demonstrated the ability to effectively use large GPU allocations and need to scale beyond the resources that can reasonably be provided on Bouchet, particularly for large multi-node GPU jobs. Examples include distributed model training and other AI or AI-enabled workflows that require many GPUs simultaneously.

### A Shared Institutional Resource

AICR is shared among multiple universities. Yale receives an institutional share of the system, and usage by Yale researchers collectively affects Yale's scheduling priority.

As a result, heavy AICR usage by one Yale project can affect the scheduling priority of other Yale projects. Yale researchers may be able to use additional resources when capacity is otherwise idle, but this additional capacity is not guaranteed.

For this reason, AICR access is intentionally limited to projects whose computational requirements particularly benefit from the resource. Researchers whose workloads can be effectively supported on Bouchet, Hopper, or other YCRC systems should continue to use those resources.

### Data Restrictions

AICR is not approved for high-risk data. Research involving regulated or other high-risk data should use an approved Yale secure computing environment such as Hopper. If you are unsure whether your data is appropriate for AICR, contact YCRC Research Support before transferring data to the system.

## Request AICR Early Access

AICR is currently in Early Access. During this period, YCRC is providing access to a limited number of projects while evaluating workloads and developing the longer-term allocation process.

Researchers requesting Early Access should:

- have an established AI/ML workflow and experience running it on an HPC system such as Bouchet or a national HPC resource;
- have demonstrated effective use of substantial multi-GPU resources and a need to scale to larger, particularly multi-node, GPU workloads; and
- have computational requirements that cannot be effectively accommodated by the available GPU resources on Bouchet.

As part of the Early Access review, YCRC may consider a research group's existing GPU usage on Yale clusters, including the scale and frequency of GPU jobs, multi-GPU and multi-node usage, GPU utilization and scaling characteristics, and the amount of GPU capacity required simultaneously.

Researchers do not need to meet a single GPU-count or utilization threshold. Requests are considered based on the overall computational requirements of the project and whether AICR is an appropriate resource for the workload.

### PIs and User Accounts

AICR access is granted for approved research workflows. PIs approve the workflows and the students or other researchers who will use AICR for the project; PI approval does not automatically create an AICR account for the PI. Accounts are created for the researchers who will directly log in and run the approved workloads.

### How to Request Early Access

If you believe your research meets the criteria above, contact [research.computing@yale.edu](mailto:research.computing@yale.edu) to request the AICR Early Access form.

In your email, please briefly describe your anticipated GPU requirements and why your workload cannot be effectively accommodated on Bouchet or Hopper, as appropriate. YCRC Research Support will provide the Early Access request form when appropriate. For student or research-staff workflows, the PI will be asked to approve the workflow and the researchers who will receive access.

!!! note
    Early Access is not intended for developing or learning a new AI/ML workflow. Researchers who are new to AI on HPC should first develop and test their workflows using Bouchet or another appropriate HPC resource.

Later in 2026, AICR access will transition to an internal Yale proposal process. Current Early Access users will also be expected to apply through that process to continue using AICR.

## AICR User Documentation

This page contains Yale-specific information about using AICR. General documentation for the system, including job submission and software information, is maintained by AICR.

[AICR User Documentation](https://docs.aicr.ai){ .md-button }

## Access the Cluster

Once your project has been approved for AICR access, you can connect using Open OnDemand or SSH.

### Certificate-signed SSH Keys

AICR uses certificate-signed SSH keys that are generated for you and put into your account. To get these keys you:

- Log into [http://ood.aicr.ai](http://ood.aicr.ai) with your Yale netid and password (**not** your AICR username)
- Open the File Browser and download the `aicr_keys.zip` file

To install these keys follow these steps:

```sh
# copy keys to local $HOME/.ssh directory
cp aicr_keys/id_ed25519_aicr* $HOME/.ssh/

# fix permissions on private key
cd $HOME/.ssh/
chmod 600 id_ed25519_aicr

# To change passphrase (initial passphrase is in aicr_keys/.passphrase):
ssh-keygen -p -f $HOME/.ssh/id_ed25519_aicr

# Then (needs passphrase):
ssh-add id_ed25519_aicr

#To log in:
ssh aicr_username@login.aicr.ai
```

Your AICR username is your netid followed by `_yale`, for example: `abc123_yale`.

## Get Help

Support for Yale researchers on AICR is provided by the YCRC.
Users can contact us for assistance with AICR at [research.computing@yale.edu](mailto:research.computing@yale.edu) and other ways of [engaging with YCRC Research Support](/#get-help).

## Installed Applications

A large number of software and applications are installed on our clusters, including AICR.
AICR software will be made available to researchers via [software modules](/applications/modules/).

If you need a specific application that is not present, let us know and we can install it for you.

## Partitions and Hardware

AICR initially contains 248 B200 GPUs and 152 RTX Pro 6000 Blackwell GPUs, grouped into [Slurm partitions](/clusters-at-yale/job-scheduling) meant to serve different purposes.
AICR provides several partitions for different workload types, including:

- `cpu`: a small CPU-only partition for jobs which do not require GPU cards
- `rtx-devel` and `b200-devel`: interactive access to GPUs, comprised of ~10% of the available cards
- `rtx-batch` and `b200-batch`: standard batch-job partitions for RTX Pro 6000 Blackwell and B200 GPUs
- `b200-fullnode`: a full-node B200 partition for jobs requesting 8 or more GPUs in multiples of 8. It is intended for large-memory, multi-GPU, and fabric-bound workloads such as distributed training across multiple GPUs or nodes. This partition is currently being evaluated as part of a four-week trial, and its size and policies may change. Smaller GPU jobs should continue to use the standard B200 or RTX partitions.
- `preemptable`: a preemptable partition available to all AICR users. Jobs submitted here may be preempted to make resources available for higher-priority workloads. The default time limit is 15 minutes and the maximum time limit is 24 hours. This partition is most appropriate for workloads that can tolerate interruption and restart.

All nodes feature the same AMD 9575F CPUs with 128 cores (across two sockets).
The CPU nodes offer 1TB of RAM, while the GPU nodes all have 2.2TB.

Note, the default job parameters are slightly different than YCRC clusters.
The most notable differences are the default time-limit of 15 minutes and the default memory allocation of 1GB.

More information on AICR partitions and associated limits can be found in the [AICR Documentation](https://docs.aicr.ai/running-jobs/slurm-basics/#partitions).

## Storage

AICR has access to an all-flash, NFS filesystem similar to the Roberts filesystem on Bouchet and the Palmer filesystem on Grace and McCleary.

Note: Scratch is a per user directory and quota, not a shared directory like other YCRC clusters.

No storage on AICR is backed up.
Self-service snapshots are available for home and work on the main AICR filesystem but do not provide protection against many types of storage failures.
We encourage you to back up all critical data to a secondary storage location.

|Partition       | Root Directory            | Storage                                 | File Count | Backups | Snapshots | Notes |
|----------------|---------------------------|-----------------------------------------|------------|---------|-----------|-------|
| home           | `/home/<username>` | 100GiB/user                             | 500,000    | No     | 7 days  |       |
| work           | `/work/yale/<project>` | 1TiB/project* | 5,000,000 | No | 7 days | |
| scratch        | `/scratch/<username>` | 10TiB/user | 15,000,000 | No | No | 30-day purge |

\* Additional storage quota may be available upon request with appropriate justification.
