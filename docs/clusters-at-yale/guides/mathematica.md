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

Load the appropriate module file. For example, to run version 12.0.0:

```
module load Mathematica/12.0.0
```

The module load command sets up your environment, including the PATH to find the proper version of the Mathematica program. If you would like to avoid running the load command every session, you can run `module save` and then the Mathematica module will be loaded every time you login.

Once you have the appropriate module loaded in an interactive job, start Mathematica. The `&` will put the program in the background so you can continue to use your terminal session.

```
Mathematica &
```

## Configure Environment for Parallel Jobs

Mathematica installed on Yale HPC clusters includes our proprietary scripts to run parallel jobs in SLURM environments. These scripts are designed in a way to allow users to access up to 450 parallel kernels.

When a user asks for a specific number of kernels, the wait time to get them might differ dramatically depending on requested computing resources as well as on how busy the HPC cluster is at that moment. To reduce waiting time, our scripts try to launch as many kernels as possible at the moment the user asks for them. Most of the time you will not get launched with the same number of kernels as you requested. We recommend checking the final number of parallel kernels you’ve gotten after the launching command has completed no matter if you run a Front End Mathematica session or execute Wolfram script. One of the ways to check this would be the Mathematica command `Length[Kernels[]]`.

In order to run parallel Mathematica jobs on our cluster, you will need to configure your Mathematica environment. You have to do this within a Front End session. If you run Wolfram script you need to run a Front End session to set your parallel environment before executing your script.

Once Mathematica is started, open a new document in the Mathematica window and go to `Edit` > `Preferences`. From there, go to `Evaluate/Parallel` Kernel Configuration and change the following settings:

1. Under `Local Kernels`, disable `Local Kernels` if it is enabled
2. Go in `Cluster Integration` and first `enable cluster integration` it if it is not enabled
3. Under the `Cluster Integration` tab, expand the `Advanced Settings` arrow. When you configure parallel kernels for the first time, please select `SLURM` from the `Cluster Engine` pull-down menu
    + Matching parallel kernel versions with your main Mathematica version is important, especially if you’ve already had SLURM selected by running different Mathematica versions previously (you might see different versions in Kernel program) In this case, select Windows CCS from Cluster Engine and a red error will appear in Advanced Settings. After this select SLURM again as this should set the correct engine for you.
4. Under `Kernels`, set your desired number (we recommend to set it lower first to test)
5. In `Advanced Settings` under `Native specification`, specify time and RAM per kernel, such as `—time=02:00:00 —mem=20G` (please note that this is RAM per one kernel)
6. If you are using Mathematica 12.3 and above, and if `RemoteKernel Objects` is enabled, disable it and restart your Mathematica session
7. We recommend to use these commands to start kernels and to check how many kernels have actually been launched (please keep them in the same Mathematica cell and separate by semicolons; Do not use semicolon at the end)
```
$DefaultKernels=$ConfiguredKernels; LaunchKernels[]; Length[Kernels[]]
```

## Request Help or Access to Wolfram Alpha Pro

If you need any assistance with your Mathematica program, [contact us](https://docs.ycrc.yale.edu/#get-help).
