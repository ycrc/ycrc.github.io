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
    |Maximum CPUs per user|`324`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |18|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, common|

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
    |2|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, common|

=== "gpu_commons"

    Use the gpu partition for jobs that make use of GPUs. You must [request GPUs explicitly](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) with the `--gres` option in order to use them. For example, `--gres=gpu:gtx1080ti:2` would request 2 GeForce GTX 1080Ti GPUs per node.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the gpu_commons partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`2-00:00:00`|
    |Maximum GPUs per user|`4`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |2|5222|8|181|rtx5000|4|16|cascadelake, avx2, avx512, 5222, common|

=== "scavenge_all"

    Use the scavenge partition to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the scavenge_all partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`1-00:00:00`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |18|6240|36|181||||cascadelake, avx2, avx512, 6240, nogpu, standard, common|
    |2|5222|8|181|rtx5000|4|16|cascadelake, avx2, avx512, 5222, common|

### Private Partitions
With few exceptions, jobs submitted to private partitions are not considered when calculating your group's [Fairshare](/clusters-at-yale/job-scheduling/fairshare/). Your group can purchase additional hardware for private use, which we will make available as a `pi_groupname` partition. These nodes are purchased by you, but supported and administered by us. After vendor support expires, we retire compute nodes. Compute nodes can range from $10K to upwards of $50K depending on your requirements. If you are interested in purchasing nodes for your group, please [contact us](/#get-help).

??? summary "PI Partitions (click to expand)"
    === "psych_gpu"

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
        |Max job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6240|36|372|rtx2080ti|4|11|cascadelake, 6240|
        |4|6240|36|372|rtx2080ti|4|11|cascadelake, 6240|

    === "long"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the long partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`2-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |48|E5-2660_v4|28|247|broadwell, E5-2660_v4|

    === "psych_scavenge"

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
        |Max job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6240|36|372|rtx2080ti|4|11|cascadelake, 6240|
        |48|E5-2660_v4|28|247||||broadwell, E5-2660_v4|
        |4|6240|36|372|rtx2080ti|4|11|cascadelake, 6240|

    === "short"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the short partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`06:00:00`|
        |Maximum CPUs per group|`1158`|
        |Maximum memory per group|`10176G`|
        |Maximum CPUs per user|`772`|
        |Maximum memory per user|`6784G`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |48|E5-2660_v4|28|247|broadwell, E5-2660_v4|

    === "verylong"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the verylong partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |48|E5-2660_v4|28|247|broadwell, E5-2660_v4|

