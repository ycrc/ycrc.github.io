# Mathematica

## Request Interactive Job

To run Mathematica interactively, you need to create an interactive session on a compute node.

You could start an interactive session using 4 cores on 1 node using something like

```
srun --pty --x11 -c 4 -p interactive -t 4:00:00 bash
```

Once your interactive session starts, you can load the appropriate module file and start Mathematica as described above.

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

The module load command sets up your environment, including the PATH to find the proper version of the Mathematica program. If you would like to avoid running the load command every session, you can run `module save` and then the Mathematica module will be loaded everytime you login.

Once you have the appropriate module loaded in an interactive job, start Mathematica. The `&` will put the program in the background so you can continue to use your session.

```
Mathematica &
```

## Configure Environment for Parallel Jobs

In order to run parallel Mathematica jobs on our cluster, you will need to setup your Mathematica environment.

Go to `Evaluate/Parallel Kernel Configuration` in the Mathematica window and change the following settings

1. Disable Local Kernels
1. Go in Cluster Integration and first Enable it if you did not have it Enabled
1. Click Reset To Default
1. From the menu in Cluster Engine select `SLURM`
1. Under Kernels, set desired number (we recommend to set it to lower number first to test)
1. Advanced Settings under Native specification specify time and RAM per kernel, such as  `—time=02:00:00 —mem=20G`
1. Set `While[Length[Kernels[]] == 0, LaunchKernels[]]`  to avoid a timeout issue

## Request Help

If you need any assistance with your Mathematica program, you can reach out the YCRC Mathematica expert Misha Guy at [mikhael.guy@yale.edu](mikhael.guy@yale.edu).
