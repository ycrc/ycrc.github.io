# Overview

We use a scheduler called "Slurm" to submit jobs to the compute nodes.

* [Submit Jobs with Slurm](/node/9761)

Here is a pdf from the Slurm folks giving you [similar commands in several schedulers](https://slurm.schedmd.com/rosetta.pdf)

If your jobs are taking a long time to start, see our [Job Scheduling documentation](/fairshare) to review the factors that affect the order in which jobs start.

If you are submitting a large number of similar jobs, please look at the [Dead Simple Queue](/node/12756) tool for bundling your jobs.

[Measuring Memory and CPU Usage](/node/3765)
[Optimize Job I/O](/node/3743)
[Preserve Sessions with `tmux`](/node/12826)
[Get Info About Compute Nodes](/node/3766)

[Example Submission and Parallel R, Matlab and Python Scripts](https://github.com/ycrc/ycrc_example_scripts)