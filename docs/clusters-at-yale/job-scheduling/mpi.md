# MPI Partition

Grace has a special common partition called `mpi`. The `mpi` partition is a bit different from other partitions on Grace--it always allocates entire nodes to jobs submitted to the partition. Each node in the `mpi` partition are identical 24 core, 2x Skylake Gold 6136, 96GiB RAM (90GiB usable) nodes. While this partition is available to all Grace users, only certain types of jobs are allowed on the partition (similar to the restrictions on our GPU partitions).

In addition the the common partition `mpi`, there is a `scavenge_mpi` partition. This partition is has the same purpose and limitations as the regular `mpi` partition, but allows users to run a lower priority (e.g. subject to preemption if nodes are requested in the `mpi` partition ) without incurring cpu charges.

## Appropriate Jobs

This partition is specifically designed to support jobs that use tightly-coupled MPI-enabled applications that will run across multiple nodes *and* are sensitive to sharing their nodes with other jobs. Since every node on the `mpi` partition is identical, it can support workloads that are sensitive to hardware difference across a single job. 

We expect most of jobs submitted to `mpi` to use all 24 cores on each node. There are occasionally instances where a tightly coupled application will use multiple nodes but less than all 24 cores due to load balancing or memory limitations. For example, some applications require power of 2 cores in the job, but 24 cores doesn't always divide evenly into those configurations. So we occasionally see jobs that use multiple nodes but only 16 of the 24 cores per node and are also acceptable submissions to the `mpi` partition. 

Jobs that do not require exclusive nodes, even if they use `mpirun` to launch, will run fine and experience normal wait times in the day and week (and scavenge) partitions. As such, we ask you to protect the special `mpi` partition nodes for the more resource sensitive jobs listed above and, therefore, submit any jobs that will not be using whole node(s) to the other partitions. If smaller or single core jobs are submitted to the `mpi` partition, they may be cancelled without warning. As with our GPU partitions, if you would like to make use of available cores on any `mpi` nodes for small jobs, the scavenge partition is the correct way to do that.

If you have any questions about whether your workload is appropriate for the `mpi` partition, please [contact us](/#get-help).

## Compilation

There is one node in the `devel` partition that is identical to the `mpi` partition nodes. If you choose to compile your code with advanced optimization flags specific to the new generation of compute nodes, you can request that node in the `devel` partition with the `-C skylake` submission flag.

## Core Layouts

Please review the [Request Compute Resources](/clusters-at-yale/job-scheduling/resource-requests) documentation for the appropriate Slurm flags for different types of core and node layouts. If you have any questions, feel free to [contact us](/#get-help).
