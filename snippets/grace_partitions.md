=== "day"

    Use the day partition for most batch jobs. This is the default if you don't specify one with `--partition`.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the day partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`1-00:00:00`|
    |Maximum CPUs per group|`1500`|
    |Maximum CPUs per user|`750`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
[{'Nodes': '48', 'CPU Type': 'E5-2660_v2', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'ivybridge, E5-2660_v2, nogpu, standard, oldest'}, {'Nodes': '40', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}, {'Nodes': '79', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E5-2660_v4, nogpu, standard'}, {'Nodes': '67', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}, {'Nodes': '60', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, pi'}]
    |60|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, pi|
    |67|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, common|
    |79|E5-2660_v4|28|247|broadwell, avx2, E5-2660_v4, nogpu, standard|
    |40|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard|
    |48|E5-2660_v2|20|121|ivybridge, E5-2660_v2, nogpu, standard, oldest|

=== "interactive"

    Use the interactive partition to jobs with which you need ongoing interaction. For example, exploratory analyses or debugging compilation.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the interactive partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`06:00:00`|
    |Maximum CPUs per user|`4`|
    |Maximum memory per user|`32G`|
    |Maximum running jobs per user|`1`|
    |Maximum submitted jobs per user|`1`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
[{'Nodes': '2', 'CPU Type': 'E5-2660_v2', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'ivybridge, E5-2660_v2, nogpu, standard, oldest'}, {'Nodes': '1', 'CPU Type': '6126', 'CPUs/Node': '24', 'Memory/Node (GiB)': '176', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'skylake, avx2, avx512, 6126, nogpu, standard, pi'}]
    |1|6126|24|176|skylake, avx2, avx512, 6126, nogpu, standard, pi|
    |2|E5-2660_v2|20|121|ivybridge, E5-2660_v2, nogpu, standard, oldest|

=== "week"

    Use the week partition for jobs that need a longer runtime than day allows.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the week partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`7-00:00:00`|
    |Maximum CPUs per group|`250`|
    |Maximum CPUs per user|`100`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
[{'Nodes': '34', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}, {'Nodes': '8', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, pi'}]
    |8|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, pi|
    |34|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard|

=== "transfer"

    Use the transfer partition to stage data for your jobs to and from [cluster storage](/clusters-at-yale/data/#staging-data).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the transfer partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`1-00:00:00`|
    |Maximum running jobs per user|`2`|
    |Maximum CPUs per job|`1`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
[{'Nodes': '2', 'CPU Type': 'E5-2660_v2', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'ivybridge, E5-2660_v2, nogpu, standard, oldest'}]
    |2|E5-2660_v2|20|121|ivybridge, E5-2660_v2, nogpu, standard, oldest|

=== "gpu"

    Use the gpu partition for jobs that make use of GPUs. You must [request GPUs explicitly](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) with the `--gres` option in order to use them. For example, `--gres=gpu:gtx1080ti:2` would request 2 GeForce GTX 1080Ti GPUs per node.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the gpu partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`2-00:00:00`|
    |Maximum GPUs per user|`24`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
[{'Nodes': '5', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': 'k80', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '12', 'Node Features': 'haswell, avx2, E5-2660_v3, doubleprecision, common'}, {'Nodes': '6', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': 'p100', 'GPUs/Node': '1', 'vRAM/GPU (GB)': '16', 'Node Features': 'broadwell, avx2, E5-2660_v4, doubleprecision, common'}, {'Nodes': '2', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '90', 'GPU Type': 'v100', 'GPUs/Node': '2', 'vRAM/GPU (GB)': '16', 'Node Features': 'skylake, avx2, avx512, 6136, doubleprecision, common'}, {'Nodes': '4', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '372', 'GPU Type': 'v100', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '16', 'Node Features': 'cascadelake, avx2, avx512, 6240, doubleprecision, common'}, {'Nodes': '5', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': 'rtx2080ti', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '11', 'Node Features': 'cascadelake, avx2, avx512, 6240, singleprecision, common'}]
    |4|6240|36|372|v100|4|16|cascadelake, avx2, avx512, 6240, doubleprecision, common|
    |5|6240|36|183|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, common|
    |2|6136|24|90|v100|2|16|skylake, avx2, avx512, 6136, doubleprecision, common|
    |6|E5-2660_v4|28|247|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, common|
    |5|E5-2660_v3|20|121|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, common|

=== "gpu_devel"

    Use the gpu_devel partition to debug jobs that make use of GPUs, or to develop GPU-enabled code.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the gpu_devel partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`04:00:00`|
    |Maximum CPUs per user|`10`|
    |Maximum submitted jobs per user|`1`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': 'k80', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '12', 'Node Features': 'haswell, avx2, E5-2660_v3, doubleprecision, common'}, {'Nodes': '1', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '372', 'GPU Type': 'v100', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '16', 'Node Features': 'cascadelake, avx2, avx512, 6240, doubleprecision, common'}]
    |1|6240|36|372|v100|4|16|cascadelake, avx2, avx512, 6240, doubleprecision, common|
    |1|E5-2660_v3|20|121|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, common|

=== "bigmem"

    Use the bigmem partition for jobs that have memory requirements other partitions can't handle.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the bigmem partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`1-00:00:00`|
    |Maximum CPUs per user|`40`|
    |Maximum memory per user|`1500G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
[{'Nodes': '2', 'CPU Type': 'E7-4820_v4', 'CPUs/Node': '40', 'Memory/Node (GiB)': '1507', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E7-4820_v4, nogpu, common'}, {'Nodes': '1', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '1506', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}, {'Nodes': '2', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '1506', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, common'}]
    |1|6240|36|1506|cascadelake, avx2, avx512, 6240, nogpu, standard, common|
    |2|6240|36|1506|cascadelake, avx2, avx512, 6240, nogpu, common|
    |2|E7-4820_v4|40|1507|broadwell, avx2, E7-4820_v4, nogpu, common|

=== "mpi"

    Use the mpi partition for tightly-coupled parallel programs that make efficient use of multiple nodes. See our [MPI documentation](/clusters-at-yale/job-scheduling/mpi) if your workload fits this description.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --exclusive --mem=92160
    ```

    **Job Limits**

    Jobs submitted to the mpi partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`1-00:00:00`|
    |Maximum nodes per group|`48`|
    |Maximum nodes per user|`32`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
[{'Nodes': '120', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '90', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'hdr, skylake, avx2, avx512, 6136, nogpu, standard, common'}]

=== "scavenge"

    Use the scavenge partition to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the scavenge partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`1-00:00:00`|
    |Maximum CPUs per user|`10000`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': 'E7-4809_v3', 'CPUs/Node': '32', 'Memory/Node (GiB)': '2011', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E7-4809_v3, nogpu, pi'}, {'Nodes': '2', 'CPU Type': 'E7-4820_v4', 'CPUs/Node': '40', 'Memory/Node (GiB)': '1507', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E7-4820_v4, nogpu, common'}, {'Nodes': '2', 'CPU Type': 'E7-4820_v4', 'CPUs/Node': '40', 'Memory/Node (GiB)': '1507', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E7-4820_v4, nogpu, pi'}, {'Nodes': '128', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}, {'Nodes': '161', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E5-2660_v4, nogpu, standard'}, {'Nodes': '6', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': 'p100', 'GPUs/Node': '1', 'vRAM/GPU (GB)': '16', 'Node Features': 'broadwell, avx2, E5-2660_v4, doubleprecision, common'}, {'Nodes': '2', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '90', 'GPU Type': 'v100', 'GPUs/Node': '2', 'vRAM/GPU (GB)': '16', 'Node Features': 'skylake, avx2, avx512, 6136, doubleprecision, common'}, {'Nodes': '136', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '90', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'hdr, skylake, avx2, avx512, 6136, nogpu, standard, common'}, {'Nodes': '16', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '90', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'edr, skylake, avx2, avx512, 6136, nogpu, standard'}, {'Nodes': '20', 'CPU Type': '8260', 'CPUs/Node': '96', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 8260, nogpu, pi'}, {'Nodes': '1', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '1506', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}, {'Nodes': '76', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, pi'}, {'Nodes': '1', 'CPU Type': 'E7-4820_v2', 'CPUs/Node': '32', 'Memory/Node (GiB)': '1003', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'ivybridge, E7-4820_v2, nogpu, pi'}, {'Nodes': '73', 'CPU Type': 'E5-2660_v2', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'ivybridge, E5-2660_v2, nogpu, standard, oldest'}, {'Nodes': '20', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}, {'Nodes': '8', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '247', 'GPU Type': 'k80', 'GPUs/Node': '2', 'vRAM/GPU (GB)': '12', 'Node Features': 'haswell, avx2, E5-2660_v3, doubleprecision, pi'}, {'Nodes': '6', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': 'k80', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '12', 'Node Features': 'haswell, avx2, E5-2660_v3, doubleprecision, common'}, {'Nodes': '1', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': 'p100', 'GPUs/Node': '1', 'vRAM/GPU (GB)': '16', 'Node Features': 'broadwell, avx2, E5-2660_v4, doubleprecision, pi'}, {'Nodes': '1', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '751', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'skylake, avx2, avx512, 6136, nogpu, pi'}, {'Nodes': '3', 'CPU Type': '6142', 'CPUs/Node': '32', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'skylake, avx2, avx512, 6142, nogpu, standard'}, {'Nodes': '1', 'CPU Type': 'E5-2637_v4', 'CPUs/Node': '8', 'Memory/Node (GiB)': '121', 'GPU Type': 'gtx1080ti', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '11', 'Node Features': 'broadwell, avx2, E5-2637_v4, singleprecision, pi'}, {'Nodes': '9', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '183', 'GPU Type': 'p100', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '16', 'Node Features': 'skylake, avx2, avx512, 6136, doubleprecision, pi'}, {'Nodes': '2', 'CPU Type': '5122', 'CPUs/Node': '8', 'Memory/Node (GiB)': '183', 'GPU Type': 'rtx2080', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '8', 'Node Features': 'skylake, avx2, avx512, 5122, singleprecision, pi'}, {'Nodes': '1', 'CPU Type': '6254', 'CPUs/Node': '36', 'Memory/Node (GiB)': '1506', 'GPU Type': 'rtx4000,rtx8000,v100', 'GPUs/Node': '4,2,2', 'vRAM/GPU (GB)': '8,48,16', 'Node Features': 'cascadelake, avx2, avx512, 6254, pi'}, {'Nodes': '131', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}, {'Nodes': '4', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '372', 'GPU Type': 'v100', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '16', 'Node Features': 'cascadelake, avx2, avx512, 6240, doubleprecision, common'}, {'Nodes': '2', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '1506', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, common'}, {'Nodes': '2', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': 'rtx2080ti', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '11', 'Node Features': 'cascadelake, avx2, avx512, 6240, singleprecision, pi'}, {'Nodes': '8', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '372', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, pi'}, {'Nodes': '5', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': 'rtx2080ti', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '11', 'Node Features': 'cascadelake, avx2, avx512, 6240, singleprecision, common'}]
    |8|6240|36|372||||cascadelake, avx2, avx512, 6240, nogpu, standard, pi|
    |131|6240|36|183||||cascadelake, avx2, avx512, 6240, nogpu, standard, common|
    |76|6240|36|183||||cascadelake, avx2, avx512, 6240, nogpu, standard, pi|
    |1|6240|36|1506||||cascadelake, avx2, avx512, 6240, nogpu, standard, common|
    |20|8260|96|183||||cascadelake, avx2, avx512, 8260, nogpu, pi|
    |1|6254|36|1506|rtx4000,rtx8000,v100|4,2,2|8,48,16|cascadelake, avx2, avx512, 6254, pi|
    |4|6240|36|372|v100|4|16|cascadelake, avx2, avx512, 6240, doubleprecision, common|
    |2|6240|36|1506||||cascadelake, avx2, avx512, 6240, nogpu, common|
    |2|6240|36|183|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, pi|
    |5|6240|36|183|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, common|
    |3|6142|32|183||||skylake, avx2, avx512, 6142, nogpu, standard|
    |2|6136|24|90|v100|2|16|skylake, avx2, avx512, 6136, doubleprecision, common|
    |1|6136|24|751||||skylake, avx2, avx512, 6136, nogpu, pi|
    |9|6136|24|183|p100|4|16|skylake, avx2, avx512, 6136, doubleprecision, pi|
    |2|5122|8|183|rtx2080|4|8|skylake, avx2, avx512, 5122, singleprecision, pi|
    |161|E5-2660_v4|28|247||||broadwell, avx2, E5-2660_v4, nogpu, standard|
    |2|E7-4820_v4|40|1507||||broadwell, avx2, E7-4820_v4, nogpu, common|
    |2|E7-4820_v4|40|1507||||broadwell, avx2, E7-4820_v4, nogpu, pi|
    |6|E5-2660_v4|28|247|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, common|
    |1|E5-2660_v4|28|247|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, pi|
    |1|E5-2637_v4|8|121|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision, pi|
    |20|E5-2660_v3|20|247||||haswell, avx2, E5-2660_v3, nogpu, standard|
    |128|E5-2660_v3|20|121||||haswell, avx2, E5-2660_v3, nogpu, standard|
    |1|E7-4809_v3|32|2011||||haswell, avx2, E7-4809_v3, nogpu, pi|
    |8|E5-2660_v3|20|247|k80|2|12|haswell, avx2, E5-2660_v3, doubleprecision, pi|
    |6|E5-2660_v3|20|121|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, common|
    |73|E5-2660_v2|20|121||||ivybridge, E5-2660_v2, nogpu, standard, oldest|
    |1|E7-4820_v2|32|1003||||ivybridge, E7-4820_v2, nogpu, pi|

=== "scavenge_gpu"

    Use the scavenge_gpu partition to run preemptable jobs on more GPU resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the scavenge_gpu partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`1-00:00:00`|
    |Maximum GPUs per user|`30`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
[{'Nodes': '6', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': 'p100', 'GPUs/Node': '1', 'vRAM/GPU (GB)': '16', 'Node Features': 'broadwell, avx2, E5-2660_v4, doubleprecision, common'}, {'Nodes': '2', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '90', 'GPU Type': 'v100', 'GPUs/Node': '2', 'vRAM/GPU (GB)': '16', 'Node Features': 'skylake, avx2, avx512, 6136, doubleprecision, common'}, {'Nodes': '4', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '372', 'GPU Type': 'v100', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '16', 'Node Features': 'cascadelake, avx2, avx512, 6240, doubleprecision, common'}, {'Nodes': '8', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '247', 'GPU Type': 'k80', 'GPUs/Node': '2', 'vRAM/GPU (GB)': '12', 'Node Features': 'haswell, avx2, E5-2660_v3, doubleprecision, pi'}, {'Nodes': '6', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': 'k80', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '12', 'Node Features': 'haswell, avx2, E5-2660_v3, doubleprecision, common'}, {'Nodes': '1', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': 'p100', 'GPUs/Node': '1', 'vRAM/GPU (GB)': '16', 'Node Features': 'broadwell, avx2, E5-2660_v4, doubleprecision, pi'}, {'Nodes': '1', 'CPU Type': 'E5-2637_v4', 'CPUs/Node': '8', 'Memory/Node (GiB)': '121', 'GPU Type': 'gtx1080ti', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '11', 'Node Features': 'broadwell, avx2, E5-2637_v4, singleprecision, pi'}, {'Nodes': '9', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '183', 'GPU Type': 'p100', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '16', 'Node Features': 'skylake, avx2, avx512, 6136, doubleprecision, pi'}, {'Nodes': '2', 'CPU Type': '5122', 'CPUs/Node': '8', 'Memory/Node (GiB)': '183', 'GPU Type': 'rtx2080', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '8', 'Node Features': 'skylake, avx2, avx512, 5122, singleprecision, pi'}, {'Nodes': '1', 'CPU Type': '6254', 'CPUs/Node': '36', 'Memory/Node (GiB)': '1506', 'GPU Type': 'rtx4000,rtx8000,v100', 'GPUs/Node': '4,2,2', 'vRAM/GPU (GB)': '8,48,16', 'Node Features': 'cascadelake, avx2, avx512, 6254, pi'}, {'Nodes': '5', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': 'rtx2080ti', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '11', 'Node Features': 'cascadelake, avx2, avx512, 6240, singleprecision, common'}]
    |4|6240|36|372|v100|4|16|cascadelake, avx2, avx512, 6240, doubleprecision, common|
    |1|6254|36|1506|rtx4000,rtx8000,v100|4,2,2|8,48,16|cascadelake, avx2, avx512, 6254, pi|
    |5|6240|36|183|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, common|
    |2|6136|24|90|v100|2|16|skylake, avx2, avx512, 6136, doubleprecision, common|
    |9|6136|24|183|p100|4|16|skylake, avx2, avx512, 6136, doubleprecision, pi|
    |2|5122|8|183|rtx2080|4|8|skylake, avx2, avx512, 5122, singleprecision, pi|
    |6|E5-2660_v4|28|247|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, common|
    |1|E5-2660_v4|28|247|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, pi|
    |1|E5-2637_v4|8|121|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision, pi|
    |8|E5-2660_v3|20|247|k80|2|12|haswell, avx2, E5-2660_v3, doubleprecision, pi|
    |6|E5-2660_v3|20|121|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, common|

### Private Partitions
With few exceptions, jobs submitted to private partitions are not considered when calculating your group's [Fairshare](/clusters-at-yale/job-scheduling/fairshare/). Your group can purchase additional hardware for private use, which we will make available as a `pi_groupname` partition. These nodes are purchased by you, but supported and administered by us. After vendor support expires, we retire compute nodes. Compute nodes can range from $10K to upwards of $50K depending on your requirements. If you are interested in purchasing nodes for your group, please [contact us](/#get-help).

??? summary "PI Partitions (click to expand)"
    === "pi_altonji"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_altonji partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '2', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}]
        |2|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard|

    === "pi_anticevic"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_anticevic partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`100-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '16', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}, {'Nodes': '16', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E5-2660_v4, nogpu, standard'}]
        |16|E5-2660_v4|28|247|broadwell, avx2, E5-2660_v4, nogpu, standard|
        |16|E5-2660_v3|20|247|haswell, avx2, E5-2660_v3, nogpu, standard|

    === "pi_anticevic_bigmem"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_anticevic_bigmem partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`100-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': 'E7-4809_v3', 'CPUs/Node': '32', 'Memory/Node (GiB)': '2011', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E7-4809_v3, nogpu, pi'}]
        |1|E7-4809_v3|32|2011|haswell, avx2, E7-4809_v3, nogpu, pi|

    === "pi_anticevic_gpu"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_anticevic_gpu partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`100-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
[{'Nodes': '7', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '247', 'GPU Type': 'k80', 'GPUs/Node': '2', 'vRAM/GPU (GB)': '12', 'Node Features': 'haswell, avx2, E5-2660_v3, doubleprecision, pi'}]
        |7|E5-2660_v3|20|247|k80|2|12|haswell, avx2, E5-2660_v3, doubleprecision, pi|

    === "pi_anticevic_z"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_anticevic_z partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`100-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '3', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}]
        |3|E5-2660_v3|20|247|haswell, avx2, E5-2660_v3, nogpu, standard|

    === "pi_balou"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_balou partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '30', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E5-2660_v4, nogpu, standard'}, {'Nodes': '9', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}]
        |9|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, common|
        |30|E5-2660_v4|28|247|broadwell, avx2, E5-2660_v4, nogpu, standard|

    === "pi_berry"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_berry partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}, {'Nodes': '1', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}]
        |1|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, common|
        |1|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard|

    === "pi_cowles"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_cowles partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|
        |Maximum CPUs per user|`120`|
        |Maximum nodes per user|`5`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '14', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}]
        |14|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard|

    === "pi_cowles_nopreempt"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_cowles_nopreempt partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|
        |Maximum CPUs per user|`120`|
        |Maximum nodes per user|`5`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '10', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}]
        |10|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard|

    === "pi_econ_io"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_econ_io partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '6', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}]
        |6|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, common|

    === "pi_econ_lp"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_econ_lp partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '5', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}]
        |5|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, common|

    === "pi_esi"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_esi partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|
        |Maximum CPUs per user|`648`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '36', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}]
        |36|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, common|

    === "pi_fedorov"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=3840
        ```

        **Job Limits**

        Jobs submitted to the pi_fedorov partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '12', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '90', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'hdr, skylake, avx2, avx512, 6136, nogpu, standard, common'}]

    === "pi_gelernter"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_gelernter partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E5-2660_v4, nogpu, standard'}, {'Nodes': '1', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}]
        |1|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, common|
        |1|E5-2660_v4|28|247|broadwell, avx2, E5-2660_v4, nogpu, standard|

    === "pi_gerstein"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_gerstein partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': 'E7-4820_v2', 'CPUs/Node': '32', 'Memory/Node (GiB)': '1003', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'ivybridge, E7-4820_v2, nogpu, pi'}, {'Nodes': '30', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}]
        |30|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard|
        |1|E7-4820_v2|32|1003|ivybridge, E7-4820_v2, nogpu, pi|

    === "pi_glahn"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_glahn partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`100-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}]
        |1|E5-2660_v3|20|247|haswell, avx2, E5-2660_v3, nogpu, standard|

    === "pi_hammes_schiffer"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=3840
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_hammes_schiffer partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
[{'Nodes': '16', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '90', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'edr, skylake, avx2, avx512, 6136, nogpu, standard'}, {'Nodes': '1', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '751', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'skylake, avx2, avx512, 6136, nogpu, pi'}, {'Nodes': '1', 'CPU Type': 'E5-2637_v4', 'CPUs/Node': '8', 'Memory/Node (GiB)': '121', 'GPU Type': 'gtx1080ti', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '11', 'Node Features': 'broadwell, avx2, E5-2637_v4, singleprecision, pi'}, {'Nodes': '2', 'CPU Type': '5122', 'CPUs/Node': '8', 'Memory/Node (GiB)': '183', 'GPU Type': 'rtx2080', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '8', 'Node Features': 'skylake, avx2, avx512, 5122, singleprecision, pi'}]
        |1|6136|24|751||||skylake, avx2, avx512, 6136, nogpu, pi|
        |2|5122|8|183|rtx2080|4|8|skylake, avx2, avx512, 5122, singleprecision, pi|
        |1|E5-2637_v4|8|121|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision, pi|

    === "pi_hodgson"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_hodgson partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}]
        |1|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, common|

    === "pi_holland"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_holland partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '2', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}, {'Nodes': '8', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, pi'}]
        |8|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, pi|
        |2|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard|

    === "pi_howard"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_howard partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}]
        |1|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, common|

    === "pi_jetz"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_jetz partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '2', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E5-2660_v4, nogpu, standard'}]
        |2|E5-2660_v4|28|247|broadwell, avx2, E5-2660_v4, nogpu, standard|

    === "pi_kaminski"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_kaminski partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '8', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}]
        |8|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard|

    === "pi_lederman"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_lederman partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': '6254', 'CPUs/Node': '36', 'Memory/Node (GiB)': '1506', 'GPU Type': 'rtx4000,rtx8000,v100', 'GPUs/Node': '4,2,2', 'vRAM/GPU (GB)': '8,48,16', 'Node Features': 'cascadelake, avx2, avx512, 6254, pi'}]
        |1|6254|36|1506|rtx4000,rtx8000,v100|4,2,2|8,48,16|cascadelake, avx2, avx512, 6254, pi|

    === "pi_levine"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=1952
        ```

        **Job Limits**

        Jobs submitted to the pi_levine partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '20', 'CPU Type': '8260', 'CPUs/Node': '96', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 8260, nogpu, pi'}]
        |20|8260|96|183|cascadelake, avx2, avx512, 8260, nogpu, pi|

    === "pi_lora"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=3840
        ```

        **Job Limits**

        Jobs submitted to the pi_lora partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '4', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '90', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'hdr, skylake, avx2, avx512, 6136, nogpu, standard, common'}]

    === "pi_mak"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_mak partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '3', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E5-2660_v4, nogpu, standard'}]
        |3|E5-2660_v4|28|247|broadwell, avx2, E5-2660_v4, nogpu, standard|

    === "pi_manohar"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_manohar partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`180-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
[{'Nodes': '2', 'CPU Type': 'E7-4820_v4', 'CPUs/Node': '40', 'Memory/Node (GiB)': '1507', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E7-4820_v4, nogpu, pi'}, {'Nodes': '8', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E5-2660_v4, nogpu, standard'}, {'Nodes': '1', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': 'p100', 'GPUs/Node': '1', 'vRAM/GPU (GB)': '16', 'Node Features': 'broadwell, avx2, E5-2660_v4, doubleprecision, pi'}, {'Nodes': '4', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}]
        |4|6240|36|183||||cascadelake, avx2, avx512, 6240, nogpu, standard, common|
        |8|E5-2660_v4|28|247||||broadwell, avx2, E5-2660_v4, nogpu, standard|
        |2|E7-4820_v4|40|1507||||broadwell, avx2, E7-4820_v4, nogpu, pi|
        |1|E5-2660_v4|28|247|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, pi|

    === "pi_ohern"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_ohern partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
[{'Nodes': '15', 'CPU Type': 'E5-2660_v2', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'ivybridge, E5-2660_v2, nogpu, standard, oldest'}, {'Nodes': '3', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E5-2660_v4, nogpu, standard'}, {'Nodes': '9', 'CPU Type': '6136', 'CPUs/Node': '24', 'Memory/Node (GiB)': '183', 'GPU Type': 'p100', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '16', 'Node Features': 'skylake, avx2, avx512, 6136, doubleprecision, pi'}, {'Nodes': '2', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}]
        |2|6240|36|183||||cascadelake, avx2, avx512, 6240, nogpu, standard, common|
        |9|6136|24|183|p100|4|16|skylake, avx2, avx512, 6136, doubleprecision, pi|
        |3|E5-2660_v4|28|247||||broadwell, avx2, E5-2660_v4, nogpu, standard|
        |15|E5-2660_v2|20|121||||ivybridge, E5-2660_v2, nogpu, standard, oldest|

    === "pi_owen_miller"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_owen_miller partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '5', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E5-2660_v4, nogpu, standard'}]
        |5|E5-2660_v4|28|247|broadwell, avx2, E5-2660_v4, nogpu, standard|

    === "pi_panda"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_panda partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': '6254', 'CPUs/Node': '36', 'Memory/Node (GiB)': '372', 'GPU Type': 'rtx2080ti', 'GPUs/Node': '8', 'vRAM/GPU (GB)': '11', 'Node Features': 'cascadelake, avx2, avx512, 6254, pi'}, {'Nodes': '2', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '372', 'GPU Type': 'v100', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '16', 'Node Features': 'cascadelake, avx2, avx512, 6240, doubleprecision, common'}, {'Nodes': '3', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': 'rtx2080ti', 'GPUs/Node': '4', 'vRAM/GPU (GB)': '11', 'Node Features': 'cascadelake, avx2, avx512, 6240, singleprecision, pi'}]
        |1|6254|36|372|rtx2080ti|8|11|cascadelake, avx2, avx512, 6254, pi|
        |2|6240|36|372|v100|4|16|cascadelake, avx2, avx512, 6240, doubleprecision, common|
        |3|6240|36|183|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, pi|

    === "pi_poland"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_poland partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '10', 'CPU Type': 'E5-2660_v4', 'CPUs/Node': '28', 'Memory/Node (GiB)': '247', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'broadwell, avx2, E5-2660_v4, nogpu, standard'}, {'Nodes': '8', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '372', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, pi'}]
        |8|6240|36|372|cascadelake, avx2, avx512, 6240, nogpu, standard, pi|
        |10|E5-2660_v4|28|247|broadwell, avx2, E5-2660_v4, nogpu, standard|

    === "pi_polimanti"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_polimanti partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': '6240', 'CPUs/Node': '36', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'cascadelake, avx2, avx512, 6240, nogpu, standard, common'}]
        |1|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard, common|

    === "pi_seto"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_seto partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '3', 'CPU Type': '6142', 'CPUs/Node': '32', 'Memory/Node (GiB)': '183', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'skylake, avx2, avx512, 6142, nogpu, standard'}]
        |3|6142|32|183|skylake, avx2, avx512, 6142, nogpu, standard|

    === "pi_tsmith"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_tsmith partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
[{'Nodes': '1', 'CPU Type': 'E5-2660_v3', 'CPUs/Node': '20', 'Memory/Node (GiB)': '121', 'GPU Type': '', 'GPUs/Node': '', 'vRAM/GPU (GB)': '', 'Node Features': 'haswell, avx2, E5-2660_v3, nogpu, standard'}]
        |1|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard|

