# MPI Partition

Grace has a special common partition called `mpi`. The `mpi` partition is a bit different from other partitions on Grace--it always allocates entire nodes to jobs submitted to the partition. Each node in the `mpi` partition are identical 24 core, 2x Skylake Gold 6136, 96GB RAM (90GB usable) nodes. While this partition is available to all Grace users, only certain types of jobs are allowed on the partition (similar to the restrictions on our GPU partitions).

!!! Note
    The `mpi` partition currently contains 33 nodes and has a nodes-per-user limit of 18 nodes. We will be adding an addition ~50 nodes later on this fall.

## Appropriate Jobs

This partition is specifically designed to support jobs that use tightly-coupled MPI-enabled codes that will run across multiple nodes *and* are sensitive to sharing their nodes with other jobs. Since every node on the `mpi` partition is identical, it can support workloads that are sensitive to hardware difference across a single job. 

We expect most of jobs submitted to `mpi` to use all 24 cores on each node. There are occasionally instances were a tightly coupled code will use multiple nodes but less than all 24 cores due to load balancing or memory limitations. For example, some codes require power of 2 cores in the job, but 24 cores doesn't always divide evenly into those configurations. So we occasionally see jobs that use multiple nodes but only 16 of the 24 cores per node and are also acceptable submissions to the `mpi` partition. 

If there is excess capacity, jobs that will use all the cores on a single node can submit to the `mpi` partition (since the wait to get entire nodes in the `day` partition can be very long). If the `mpi` parition becomes very oversubscribed, this second type of job may be asked to return to the `day` partition.

Jobs that do not require exclusive nodes, even if they use `mpirun` to launch, will run fine and experience normal wait times in the day and week (and scavenge) partitions. As such, we ask you to protect the special `mpi` partition nodes for the more resource sensitive jobs listed above and, therefore, submit any jobs that will not be using whole node(s) to the other partitions.​ If smaller or single core jobs are submitted to the `mpi` partition, they may be cancelled without warning. As with our GPU partitions, if you would like to make use of available cores on any `mpi` nodes for small jobs, the scavenge partition is the correct way to do that.

If you have any questions about whether your workload is appropariate for the `mpi` partition, please contact us at [hpc@yale.edu](mailto:hpc@yale.edu).

## Core Layouts

Please review the [Request Compute Resources](/clusters-at-yale/job-scheduling/resource-requests) documentation for the appropriate Slurm flags for different types of core and node layouts. If you have any questions, feel free to email us at [hpc@yale.edu](mailto:hpc@yale.edu).
