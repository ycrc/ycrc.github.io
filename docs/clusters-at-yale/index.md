# Getting Started

## HPC Clusters

[![](/img/cluster.png)](/img/clusters.png){: .cluster-diagram}

Broadly speaking, a high performance computing (HPC) cluster is a collection of networked computers and data storage. We refer to individual servers in this network as nodes. Our clusters are only accessible to researchers remotely; your gateways to the cluster are the **login nodes**. From these nodes, you view files and dispatch jobs to other nodes across the cluster configured for computation, called  **compute nodes**. The tool we use to manage these jobs is called a **job scheduler**. All compute nodes on a cluster mount a **shared filesystem**; a file server or set of servers store files on a large array of disks. This allows your jobs to access and edit your data from any compute node. See our summary of the [compute and storage hardware](/clusters-at-yale/clusters) we maintain, from which you can navigate to a detailed description of each cluster.

## Request an Account

The first step in gaining access to our clusters is to request an account. There are several HPC clusters available at Yale. There is no charge for using these clusters, but all users must adhere to the YCRC [HPC Policies](https://research.computing.yale.edu/services/high-performance-computing/hpc-policies). To understand which cluster is appropriate for you and to request an account, visit the [account request page](https://research.computing.yale.edu/account-request). 

## Be a Good Cluster Citizen

While using HPC resources, here are some important things to remember:

* Do not run jobs or computation on a login node, instead [submit jobs](/clusters-at-yale/job-scheduling/).
* Never give your password or ssh key to anyone else.
* Do not store any [high risk data](https://cybersecurity.yale.edu/protectyourdata) on the clusters, except [Milgram](/clusters-at-yale/clusters/milgram).
* Do not run larger numbers of very short (less than a minute) jobs 

Use of the clusters is also governed by our [official guidelines](https://research.computing.yale.edu/services/high-performance-computing/hpc-principles).

## Log in

Once you have an account, go to our [Log on to the Clusters page](access) login information and configuration.

If you want to access the clusters from outside Yale's network, you must use the [Yale VPN.](access/vpn)

## Schedule a Job

On our clusters, you control your jobs using a job scheduling system called Slurm that allocates and manages compute resources for you. You can submit your jobs in one of two ways. For testing and small jobs you may want to run a job **interactively**. This way you can directly interact with the compute node(s) in real time. The other way, which is the preferred way for multiple jobs or long-running jobs, involves writing your job commands in a script and submitting that to the job scheduler. Please see our [Slurm documentation](job-scheduling) or attend the [Introduction to HPC workshop](https://research.computing.yale.edu/training/introduction-hpc) for more details.

## Use Software

To best serve the diverse needs of all our researchers, we use [software modules](/clusters-at-yale/applications/modules) to make multiple versions of popular software available. Modules allow you to swap between different applications and versions of those applications with relative ease.

We also provide assistance for installing less commonly used packages. See our [Applications & Software documentation](applications) for more details.

## Tutorial to Get Started

To begin, access the cluster through [Open OnDemand](//clusters-at-yale/access/ood) and open the shell window. This can be done by by going to the top navigation bar, clicking on the **Clusters** tab and selecting the **Shell Access** button.

![cluster_navigation_bar_showing_shell_dropdown_tab](/img/intro_tutorial_navbar.jpg){: .medium}

Once the new shell window is loaded, you will be able use this interface like your local command interface. Now that you're setup in a shell window, you can begin the task like so:

### Part 1: Interactive Jobs
Inside of the shell window, start an interactive job with the default resource requests. Once you are allocated space off the login node, load the Miniconda module and create a [Conda environment](/clusters-at-yale/guides/conda) for this exercise. This can be done like so:

``` bash
# Ask for an interactive session
srun --pty -pinteractive bash

# Load the Miniconda module
module load miniconda

# Create a test environment with Conda that contains the default Python version
conda create -yn tutorial_env python

# Activate the new environment
conda activate tutorial_env

# Deactivate the new environment
conda deactivate

# Exit your interactive job to free the resources
exit
```

### Part 2: Batch Jobs
Going off of the environment we created in **part 1**, navigate to the **Files** tab in OOD and select your **project** directory. Click the '+ New File' button and name the file `message_decode_tutorial.py`. Once the new file is created, open this file in the OOD text editor by going to the file, clicking the three-dot **more** button, and selecting **edit** in the dropdown menu like so:

![file_browser_interface_showing_dropdown_options](/img/intro_tutorial_textedit.jpg){: .medium}


Once the text editor is open, paste this python example inside of the file:

``` python

def message_decode_tutorial(message, c):
    holder = ""
    for letter in range(0, len(message)):
        if (letter + 1) % c == 0:
            holder = holder + message[letter]
    return holder

message = 'gT baZu lWp Kjv uXyeS nViU fdlH gJr KaIc tBpl Sy\
Jox MtUl Qbm kGTp UdHe hdLJf Nu IcPRu XhBtDjf TsmPf\
o DoKfw xP qyTcJ tUpYrv Pk ArBCf Wrtp JfRcX JqPdKLC'

cypher = message_decode_tutorial(message, 10)

with open('/home/NETID/scratch60/decoded_example.txt','w+') as output:
    print(cypher, file=output)

```

This python function takes a given message and parses through it against the parameters of a cypher, which in our case writes every 10th letter. **Make sure to replace the placeholder 'NETID' in the second to last line with your personal NetID.** This will allow your output file to go into your scratch60 space, and will automatically be deleted should you forget to do so.

From here, navigate back to your project directory and select the '+ New File' button, this time naming it `batch_tutorial.sh`. Using [Slurm options](/clusters-at-yale/job-scheduling/#common-job-request-options) to define resource requests for this job, paste the following code inside of this file like you did the previous file:

``` bash

#!/bin/bash

#SBATCH --job-name=message_decode_tutorial
#SBATCH --time=1:00
#SBATCH --mem-per-cpu=2MB
#SBATCH --mail-type=ALL

module load miniconda

source activate tutorial_env

python message_decode_tutorial.py

```

Because the partition isn't specified for this job, it will run on the cluster's default partition. From there, you can go back to the shell window, navigate to your project directory and run the sbatch command to begin your batch job like so:

``` bash

# Navigate to the project directory
cd project

# Use Slurm to start a batch job
sbatch batch_tutorial.sh

```

Once you receive an email saying the job is complete, navigate to your scratch60 space through the shell window on Open OnDemand. Within this directory you will find a file called `decoded_example.txt`. To quickly see the file contents, use the `cat` command to print the file's contents on the standard output, revealing the decoded message like so:

``` bash

# Navigate to your scratch60 space
cd ../scratch60

# Print out the decoded message
cat decoded_example.txt

```

## Transfer Your Files

You will likely want to copy files between your computer and the clusters. There are a couple methods available to you, and the best for each situation usually depends on the size and number of files you would like to transfer. For most situations, uploading files through Open OnDemand's upload interface is the best option. This can be done directly through the file viewer interface by clicking the **Upload** button and dragging and dropping your files into the upload window. For more information on this as well as other upload methods, see our [transferring data](data/transfer) page.

## Linux

Our clusters run the Linux operating system, where we support the use of the Bash shell. A basically familiarity with Linux commands is required for interacting with the clusters. We periodically run an [Intro to Linux Bootcamp](https://research.computing.yale.edu/training/ycrc-bootcamps/practical-introduction-linux) to get you started. There are also many excellent beginner tutorials available for free online, including the following:

* [Unix Tutorial for Beginners](http://www.ee.surrey.ac.uk/Teaching/Unix/index.html)
* [Interactive Command Line Bootcamp](http://rik.smith-unna.com/command_line_bootcamp/)

## Hands on Training

We offer several courses that will assist you with your work on our clusters. They range from orientation for absolute beginners to advanced topics on application-specific optimization. Please peruse [our catalog of training](https://research.computing.yale.edu/training) to see what is available.

## Get Help

If you have additional questions/comments, please [contact us](/#get-help). Where applicable, please include the following information:

* Your netid
* Cluster
* Partition name
* Job ID(s)
* Error messages
* Command used to submit the job(s)
* Path(s) to scripts called by the submission command
* Path(s) to output files from your jobs
