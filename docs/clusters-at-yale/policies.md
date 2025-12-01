# Cluster Usage Policies 

The YCRC’s HPC resources are shared by many users. 
The YCRC uses a workload management system (Slurm) to implement and enforce policies that aim to provide each PI group with fair, but limited, access to the HPC clusters. 
Users may not run computationally intensive workloads or compilations on the login or transfer nodes. 
Instead, users must submit such workloads as jobs to Slurm, specifying the amount of resources to be allocated for the jobs. 
Jobs running for longer than one week are discouraged. 
Slurm will terminate jobs exceeding their requested resource amounts with little or no warning. 
To avoid data loss if jobs terminate unexpectedly, users are strongly encouraged to checkpoint running jobs at regular intervals.

Users are expected to abide by the stated purposes and limits of the cluster partitions and submit jobs in alignment with YCRC best practices, such as not running large numbers of very short jobs or workflows that create an excessive number of small files. 
Jobs found making inappropriate use of a cluster may be canceled without prior notice and repeated offenses after a warning has been issued by YCRC staff can result in account suspension. 
In extreme cases, where a particular workflow threatens the system’s stability, the YCRC may temporarily lock an account without prior notice, with account restoration requiring consultation with YCRC staff to address the workflow.

## GPU Resource Utilization

As the number of GPUs on our clusters has increased, so too has the demand for them. 
These resources are expensive to procure and operate and therefore should not sit idle for extended periods of time.
All jobs are monitored for their resource utilization, which can be queried via `jobstats JOBID`. 
We recommend all researchers to monitor their jobs' performance and resource utilization efficiency. 
Jobs which request more resources than necessary will wait longer to start and have a larger impact on scheduling priority (see our discussion of FairShare [here](/clusters-at-yale/job-scheduling/fairshare)). 

To ensure the utilization of these scarce resources, we have a daemon that searches for jobs which have idle GPUs. 
Initially researchers are sent warnings to alert them of the idle resources. 
If these resources continue to be unused the job is then cancelled and the researcher notified.


