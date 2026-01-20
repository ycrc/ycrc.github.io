# Mathematica

## Open OnDemand

We strongly recommend using [Open OnDemand](/clusters-at-yale/access/ood) to launch Mathematica. 

First, open OOD in a browser and navigate to the `Apps` button. Select `All Apps` from the drop-down menu and then select Mathematica from the list. Fill in your resource requests and launch your job. Once started, click `Launch Mathematica` and Mathematica will be opened in a new tab in the browser.

## Interactive Job

Alternatively, you could start an interacgive session with X11 forwarding. 

!!!warning
    The Mathematica program is too large to fit on a login node. If you try to run it there, it will crash. Instead, launch it in an interactive job (see below).

To run Mathematica interactively, you need to request an interactive session on a compute node.

You could start an interactive session using Slurm. For example, to use 4 cores on 1 node:

```
salloc --x11 -c 4 -t 4:00:00
```

Note that if you are on macOS, you will need to install an additional program to use the GUI. See our [X11 Forwarding documentation](/clusters-at-yale/access/x11) for instructions.

See our [Slurm documentation](/clusters-at-yale/job-scheduling) for more detailed information on requesting resources for interactive jobs.

To launch Mathematica, you will first need to make sure you have the correct module loaded. You can search for all available Mathematica versions:

```
module avail mathematica
```

Load the appropriate module file. For example, to run version 14.2.0:

```
module load Mathematica/14.2.0
```

The module load command sets up your environment, including the PATH to find the proper version of the Mathematica program. If you would like to avoid running the load command every session, you can run `module save` and then the Mathematica module will be loaded every time you login.

Once you have the appropriate module loaded in an interactive job, start Mathematica. The `&` will put the program in the background so you can continue to use your terminal session.

```
Mathematica &
```

## Parallel Jobs

Mathematica installed on Yale HPC clusters includes our proprietary scripts to run parallel jobs in Slurm environments. These scripts are designed in a way to allow users to access up to 450 parallel kernels.

When a user asks for a specific number of kernels, the wait time to get them might differ dramatically depending on requested computing resources as well as on how busy the HPC cluster is at that moment. To reduce waiting time, our scripts try to launch as many kernels as possible at the moment the user asks for them. Most of the time you will not get launched with the same number of kernels as you requested. We recommend checking the final number of parallel kernels you’ve gotten after the launching command has completed no matter if you run a Front End Mathematica session or execute Wolfram script. One of the ways to check this would be the Mathematica command `Length[Kernels[]]`.

The following instructions to launch parallel kernels are only applicable to Mathematica version 14.2.0. If you are interested in using an older version, please [contact us](https://docs.ycrc.yale.edu/#get-help).

To launch parallel Mathematica jobs on our cluster, use the command:
```
LaunchSlurmKernels[n]
```
where `n` is the number of kernels you want to use. This command launches as many kernels as possible on the cluster's default partition (e.g. `day` partition on Grace) with default wall time and RAM for this partition. If you need to run on a different partition or with custom resources, use the command:
```
LaunchSlurmKernels[n,"SlurmOptions"]
```
where `SlurmOptions` specifies the [job request options for Slurm](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/#common-job-request-options). Here are some examples: `LaunchSlurmKernels[40,"-t 12:00:00"]` launches 40 kernels for 12 hours in the default partition; `LaunchSlurmKernels[30,"-p week -t 2-12:00:00"]` launches 30 kernels for 2 days and 12 hours in the week partition; and `LaunchSlurmKernels[100,"--mem 30G"]` launches 100 kernels with 30GB of RAM per kernel and default runtime in the default partition. If the Slurm options violate the restrictions on the partition, it will result in an error. The wall time for your parallel kernels should not exceed the remaining wall time of your main Mathematica session. Since the parallel kernels are child processes of your main session, they will be terminated when your session ends. 

You can also manually close the parallel kernels during your session with the following command:
```
CloseKernels[]
```
which will shut down all currently launched parallel kernels. If you need to terminate a specific kernel, you can use commands such as `CloseKernels[k]`, where k is the KernelID, or `CloseKernels[{k1,k2,...}]` to terminate a list of kernelIDs. You can use the command `ParallelKernels[]` to list all the KernelObjects and their KernekIDs. Each KernelObject looks like this:

![file_browser](/img/kernel_object.png){: .medium}

When the process running your parallel kernel is terminated by Slurm due to exceeding its wall time, there may not be any indication of this in your main session. However, you will receive error messages when you try to run any Parallel commands. If this is the case, make sure to close the terminated kernels with `CloseKernels[]` command. 

You can add more parallel kernels to the already launched kernels by using the same command `LaunchSlurmKernels[n]`. The termination time of the newly added parallel kernels will be different from that of the existing kernels.    

## Request Help or Access to Wolfram Alpha Pro

If you need any assistance with your Mathematica program, [contact us](https://docs.ycrc.yale.edu/#get-help).
