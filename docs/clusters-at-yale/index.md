# Getting Started


!!! info "New to HPC?"
    Are you new to HPC clusters? Or used one before but new to Yale's systems? We encourage you to watch our [Introduction to HPC workshop](https://www.youtube.com/watch?v=SaiXaC0jRjE&t=2s).

## HPC Clusters

[![HPC Cluster Diagram](/img/cluster.png)](/img/clusters.png){: .cluster-diagram}

A high performance computing (HPC) cluster is a collection of networked computers and data storage. We refer to individual servers in this network as nodes. Our clusters are only accessible to researchers remotely; your gateways to the cluster are the **login nodes**. From these nodes, you view files and dispatch jobs to other nodes across the cluster configured for computation, called  **compute nodes**. The tool we use to manage these jobs is called a **job scheduler**. All compute nodes on a cluster mount a **shared filesystem**; a file server or set of servers store files on a large array of disks. This allows your jobs to access and edit your data from any compute node. 

- [Compute and storage systems](/clusters)

## Request an Account

The first step in gaining access to [one of our clusters](/clusters) is to request an account. All users must adhere to the YCRC [HPC Policies](https://research.computing.yale.edu/services/high-performance-computing/hpc-policies).

- [Account Request Form](https://research.computing.yale.edu/account-request)

## Log in

Once you have an account, you can connect to the cluster either via our Web Portal or more traditional SSH access. If you want to access the clusters from outside Yale's network, you must use the [Yale VPN.](access/vpn)

- [Log in to the Clusters ](access)

## Submit a Job

You control your computations using a job scheduling system called Slurm that allocates and manages compute resources for you. For testing and small jobs you may want to run a job **interactively**, which lets you interact with the compute node(s) in real time. Batch submission, the preferred way for multiple jobs or long-running jobs, involves writing your job commands in a script and submitting that to the job scheduler. 

- [Slurm Job Submissions](job-scheduling)

## Use Software

We use [software modules](/applications/modules) to make multiple versions of popular software available. Modules allow you to swap between different applications and versions of those applications with relative ease. We also provide assistance for installing less commonly used packages.

- [Applications & Software](/applications)

## Transfer Your Files

There are a number of methods for transferring file between your computer and the cluster, and the best for each situation usually depends on the size and number of files you would like to transfer. For most situations, uploading files through Open OnDemand's upload interface is the best option. This can be done directly through the file viewer interface by clicking the **Upload** button and dragging and dropping your files into the upload window. 

- [Transfer data using the Web Portal](/clusters-at-yale/access/ood/#file-browser)
- [Other ways to transfer data](/data/transfer) (for larger transfers)

## Get Help

!!! abstract "Additional Training"

	We offer several courses that range from orientation for beginners to advanced topics on application-specific optimization. Please peruse [our catalog of training](https://research.computing.yale.edu/training) to see what is available.

	Our clusters run the Linux operating system, where we support the use of the Bash shell. If you are new to linux, check out our [Intro to Linux Workshop](https://research.computing.yale.edu/training/ycrc-bootcamps/practical-introduction-linux).

If you have additional questions/comments, please [contact us](/#get-help).