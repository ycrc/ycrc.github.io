# Mathematica

## Request an Interactive Job

!!!warning
    The Mathematica program is too large to fit on a login node. If you try to run it there, it will crash. Instead, launch it in an interactive job (see below).

To run Mathematica interactively, you need to request an interactive session on a compute node.

You could start an interactive session using Slurm. For example, to use 4 cores on 1 node:

```
srun --pty --x11 -c 4 -p interactive -t 4:00:00 bash
```

Note that if you are on macOS, you will need to install an additional program to use the GUI. See our [X11 Forwarding documentation](/clusters-at-yale/access/x11) for instructions.

See our [Slurm documentation](/clusters-at-yale/job-scheduling) for more detailed information on requesting resources for interactive jobs.

## Start Mathematica

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

In order to run parallel Mathematica jobs on our cluster, you will need to configure your Mathematica environment.

Go to `Evaluate/Parallel Kernel Configuration` in the Mathematica window and change the following settings.

1. Disable `Local Kernels` if it is enabled.
1. Go in `Cluster Integration` and first Enable it if it is not Enabled
1. Click `Reset to Default` if you have previously configured a different `Cluster Engine` than `SLURM`. Then from the menu in `Cluster Engine`, select `SLURM`
1. Under `Kernels`, set desired number (we recommend to set it to lower number first to test)
1. Advanced Settings under Native specification, specify time and RAM per kernel, such as  `—time=02:00:00 —mem=20G`
1. If you are using Mathematica 12.3 and above, and if `RemoteKernel Objects` is enabled, disable it and restart Mathematica.
1. Use `While[Length[Kernels[]] == 0, LaunchKernels[]]` to avoid a timeout issue.

## Request Help or Access to Wolfram Alpha Pro

If you need any assistance with your Mathematica program, [contact us](/#get-help).
