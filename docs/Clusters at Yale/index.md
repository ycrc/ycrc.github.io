# Getting Started

### Our Clusters

![](/sites/default/files/images/cluster.png)

Broadly speaking, a compute cluster is a collection of computers (nodes). Our clusters are only accessible remotely. You will primarily connect to a computer that we call a **login node**, which is meant exclusively for maintinaing your connection to the cluster. From this computer, you will be able to view your files and dispatch jobs to one or several other computers across the cluster that we call **compute nodes**. The tool we use to submit these jobs is called a **job scheduler**. All compute nodes on a cluster mount a **shared filesystem**; a file server or set of servers that keeps track of all files on a large array of disks, so that you can access and edit your data from any compute node. Detailed information about each of our clusters is available [here](/node/4093).

### Request an Account

The first step in gaining access to our clusters is requesting an account. There are several HPC clusters available at Yale. There is no charge for using these clusters. To understand which cluster is appropriate for you and to request an account, visit the [account request page](/node/3822).

### <a>Log in</a>

All of Yale's clusters are accessed via a protocol called secure shell (ssh). You can use ssh directly, or via a graphical ssh tool. The details vary depending on the operating system of the computer in front of you. If you want to access the clusters from outside Yale, you must use the [Yale VPN.](/node/8841)

[

For specifics on ssh and how to connect to the clusters with your application and operating system of choice, please see our documentation:

](/node/8841)

[](/node/8841)
*   [](/node/8841)[Login from macOS or Linux](/node/3784)
*   [Login from Windows](/node/3786)

### Schedule a Job

On our clusters, you control your jobs using a job scheduling system called slurm that dedicates and manages compute resources for you. Schedulers are usually used in one of two ways. For testing and small jobs you may want to run a job **interactively**. This way you can directly interact with the compute node(s) in real time to make sure your jobs will behave as expected. The other way, which is the preferred way for large and long-running jobs, involves writing your job commands in a script and submitting that to the job scheduler. Please see our [slurm documentation](/node/9761) or attend the [HPC bootcamp](/node/15261) for more info.

### New to Linux?

A basically familiarity with Linux commands is required for interacting with the clusters. We periodically run an [Intro to Linux Bootcamp](/node/11691) to get you started. There are also many excellent beginner tutorials available for free online, including the following:

*   [Unix Tutorial for Beginners](http://www.ee.surrey.ac.uk/Teaching/Unix/index.html)
*   [Interactive Command Line Bootcamp](http://rik.smith-unna.com/command_line_bootcamp/)

### Move Your Files

You will likely find it necessary to copy files between your local machines and the clusters. Just as with logging in, there are different ways to do this, depending on your local operating system. See the documentation on [transferring files](/node/3753#data) for more information.

### Use Software

To best serve the diverse needs of all the software that a scientist needs in an HPC environment, we use a module system to manage software. This allows you to swap between different application and versions of those applications with relative ease and focus on getting your work done, not compiling software. See the [Modules documentation](/node/3769#software) in our User Guide for more information. If you find software that you'd like to use that isn't available, let us know and we will do our best to make it available.

### Rules of the road

Before you begin using the cluster, here are some important things to remember:

*   Do not run jobs or do real work on the login node. Always allocate a compute node and run programs there.
*   Never give your password or ssh key to anyone else.
*   Do not store any protected or regulated data on the cluster (e.g. PHI data)

Use of the clusters is also governed by our [official guidelines](/node/12336).

### Hands on Training

We offer several courses that will assist you with your work on our clusters. They range from orientation for absolute beginners to advanced topics on application-specific optimization. Please peruse [our catalog of training](/node/4186) to see what is available.

### Need Additional Help?

If you have additional questions/comments, please [contact the HPC team](mailto:hpc@yale.edu). If possible, please include the following information:

*   Your netid
*   Cluster
*   Queue/partition name
*   Job ID(s)
*   Error messages
*   Command used to submit the job(s)
*   Path(s) to scripts called by the submission command
*   Path(s) to output files from your jobs