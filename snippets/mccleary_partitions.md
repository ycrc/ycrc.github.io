=== "day"

    Use the day partition for most batch jobs. This is the default if you don't specify one with `--partition`.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the day partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`1-00:00:00`|
    |Maximum CPUs per group|`512`|
    |Maximum memory per group|`6000G`|
    |Maximum CPUs per user|`256`|
    |Maximum memory per user|`3000G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |33|8358|64|983|icelake, avx512, 8358, nogpu, bigtmp, common|
    |18|6240|36|180|cascadelake, avx512, 6240, nogpu, bigtmp, standard, common|

=== "devel"

    Use the devel partition to jobs with which you need ongoing interaction. For example, exploratory analyses or debugging compilation.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the devel partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`06:00:00`|
    |Maximum CPUs per user|`4`|
    |Maximum memory per user|`32G`|
    |Maximum submitted jobs per user|`1`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |12|E5-2680_v4|28|227|broadwell, E5-2680_v4, nogpu, standard, oldest, common|

=== "week"

    Use the week partition for jobs that need a longer runtime than day allows.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the week partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`7-00:00:00`|
    |Maximum CPUs per group|`64`|
    |Maximum memory per group|`983G`|
    |Maximum CPUs per user|`64`|
    |Maximum memory per user|`983G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |7|8358|64|983|icelake, avx512, 8358, nogpu, bigtmp, common|

=== "transfer"

    Use the transfer partition to stage data for your jobs to and from [cluster storage](/clusters-at-yale/data/#staging-data).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the transfer partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`1-00:00:00`|
    |Maximum CPUs per user|`1`|
    |Maximum running jobs per user|`2`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |2|72|8|227|milan, 72F3, nogpu, standard, common|

=== "gpu"

    Use the gpu partition for jobs that make use of GPUs. You must [request GPUs explicitly](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) with the `--gpus` option in order to use them. For example, `--gpus=gtx1080ti:2` would request 2 GeForce GTX 1080Ti GPUs per node.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the gpu partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`2-00:00:00`|
    |Maximum GPUs per group|`24`|
    |Maximum GPUs per user|`12`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|8358|64|983|a100|4|40|icelake, avx512, 8358, doubleprecision, bigtmp, common, a100|
    |4|5222|8|163|rtx5000|4|16|cascadelake, avx512, 5222, doubleprecision, common, bigtmp, rtx5000|
    |4|5222|8|163|rtx3090|4|24|cascadelake, avx512, 5222, doubleprecision, common, rtx3090|
    |5|E5-2637_v4|8|101|gtx1080ti|4|11|broadwell, E5-2637_v4, singleprecision, oldest, common, gtx1080ti|

=== "bigmem"

    Use the bigmem partition for jobs that have memory requirements other partitions can't handle.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the bigmem partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`1-00:00:00`|
    |Maximum CPUs per user|`32`|
    |Maximum memory per user|`3960G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |4|6346|32|3960|icelake, avx512, 6346, nogpu, bigtmp, common|
    |2|6234|16|1486|cascadelake, avx512, 6234, nogpu, common, bigtmp|

=== "scavenge"

    Use the scavenge partition to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the scavenge partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`1-00:00:00`|
    |Maximum CPUs per user|`1000`|
    |Maximum memory per user|`20000G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |48|8362|64|479||||icelake, avx512, 8362, nogpu, standard, pi|
    |1|8358|64|983|a100|4|40|icelake, avx512, 8358, doubleprecision, bigtmp, pi, a100|
    |4|6346|32|3960||||icelake, avx512, 6346, nogpu, bigtmp, common|
    |40|8358|64|983||||icelake, avx512, 8358, nogpu, bigtmp, common|
    |1|8358|64|983|a100|4|40|icelake, avx512, 8358, doubleprecision, bigtmp, common, a100|
    |4|6346|32|1991||||icelake, avx512, 6346, nogpu, pi|
    |4|6240|36|730||||cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|
    |4|6240|36|352||||cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|
    |18|6240|36|180||||cascadelake, avx512, 6240, nogpu, bigtmp, standard, common|
    |11|6240|36|163||||cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|
    |4|5222|8|163|rtx5000|4|16|cascadelake, avx512, 5222, doubleprecision, common, bigtmp, rtx5000|
    |10|8268|48|352||||cascadelake, avx512, 8268, nogpu, bigtmp, pi|
    |1|6248r|48|352||||cascadelake, avx512, 6248r, nogpu, pi, bigtmp|
    |1|6242|32|981|rtx8000|2|48|cascadelake, avx512, 6242, doubleprecision, pi, bigtmp, rtx8000|
    |2|6234|16|1486||||cascadelake, avx512, 6234, nogpu, common, bigtmp|
    |4|5222|8|163|rtx3090|4|24|cascadelake, avx512, 5222, doubleprecision, common, rtx3090|
    |1|6240|36|352|rtx3090|8|24|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, rtx3090|
    |1|6240|36|163|rtx3090|4|24|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, rtx3090|
    |1|6240|36|163|rtx3090|8|24|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, rtx3090|
    |1|6240|36|1486||||cascadelake, avx512, 6240, nogpu, pi, bigtmp|
    |2|6240|36|163|rtx2080ti|4|11|cascadelake, avx512, 6240, singleprecision, pi, bigtmp, rtx2080ti|
    |8|5222|8|163|rtx5000|4|16|cascadelake, avx512, 5222, doubleprecision, pi, bigtmp, rtx5000|
    |1|6226r|32|163|rtx3090|4|24|cascadelake, avx512, 6226r, doubleprecision, pi, rtx3090|
    |1|6240|36|352|v100|4|16|cascadelake, avx2, avx512, 6240, pi, v100|
    |2|6240|36|352|a100|4|40|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, a100|
    |1|6420|36|730|a100|4|40|cascadelake, avx512, 6420, doubleprecision, pi, bigtmp, a100|
    |1|6132|28|730||||skylake, avx512, 6132, nogpu, standard, bigtmp, pi|
    |2|6132|28|163||||skylake, avx512, 6132, nogpu, standard, bigtmp, pi|
    |2|5122|8|163|rtx2080|4|8|skylake, avx512, 5122, singleprecision, pi, rtx2080|
    |39|E5-2680_v4|28|227||||broadwell, E5-2680_v4, nogpu, standard, oldest, pi|
    |5|E5-2637_v4|8|101|gtx1080ti|4|11|broadwell, E5-2637_v4, singleprecision, oldest, common, gtx1080ti|
    |1|E7-4820_v4|40|1486||||broadwell, E7-4820_v4, nogpu, pi|
    |3|E5-2660_v4|28|227|p100|2|16|broadwell, E5-2660_v4, doubleprecision, pi, p100|
    |11|E5-2637_v4|8|101|gtx1080ti|4|11|broadwell, E5-2637_v4, singleprecision, pi, gtx1080ti|
    |1|E5-2637_v4|8|101|titanv|4|12|broadwell, E5-2637_v4, doubleprecision, pi, bigtmp, titanv|

=== "scavenge_gpu"

    Use the scavenge_gpu partition to run preemptable jobs on more GPU resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the scavenge_gpu partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`1-00:00:00`|
    |Maximum GPUs per group|`4`|
    |Maximum GPUs per user|`2`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|8358|64|983|a100|4|40|icelake, avx512, 8358, doubleprecision, bigtmp, pi, a100|
    |1|8358|64|983|a100|4|40|icelake, avx512, 8358, doubleprecision, bigtmp, common, a100|
    |4|5222|8|163|rtx5000|4|16|cascadelake, avx512, 5222, doubleprecision, common, bigtmp, rtx5000|
    |1|6242|32|981|rtx8000|2|48|cascadelake, avx512, 6242, doubleprecision, pi, bigtmp, rtx8000|
    |4|5222|8|163|rtx3090|4|24|cascadelake, avx512, 5222, doubleprecision, common, rtx3090|
    |1|6240|36|352|rtx3090|8|24|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, rtx3090|
    |1|6240|36|163|rtx3090|4|24|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, rtx3090|
    |1|6240|36|163|rtx3090|8|24|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, rtx3090|
    |2|6240|36|163|rtx2080ti|4|11|cascadelake, avx512, 6240, singleprecision, pi, bigtmp, rtx2080ti|
    |8|5222|8|163|rtx5000|4|16|cascadelake, avx512, 5222, doubleprecision, pi, bigtmp, rtx5000|
    |1|6226r|32|163|rtx3090|4|24|cascadelake, avx512, 6226r, doubleprecision, pi, rtx3090|
    |1|6240|36|352|v100|4|16|cascadelake, avx2, avx512, 6240, pi, v100|
    |2|6240|36|352|a100|4|40|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, a100|
    |1|6420|36|730|a100|4|40|cascadelake, avx512, 6420, doubleprecision, pi, bigtmp, a100|
    |2|5122|8|163|rtx2080|4|8|skylake, avx512, 5122, singleprecision, pi, rtx2080|
    |5|E5-2637_v4|8|101|gtx1080ti|4|11|broadwell, E5-2637_v4, singleprecision, oldest, common, gtx1080ti|
    |3|E5-2660_v4|28|227|p100|2|16|broadwell, E5-2660_v4, doubleprecision, pi, p100|
    |11|E5-2637_v4|8|101|gtx1080ti|4|11|broadwell, E5-2637_v4, singleprecision, pi, gtx1080ti|
    |1|E5-2637_v4|8|101|titanv|4|12|broadwell, E5-2637_v4, doubleprecision, pi, bigtmp, titanv|

### Private Partitions
With few exceptions, jobs submitted to private partitions are not considered when calculating your group's [Fairshare](/clusters-at-yale/job-scheduling/fairshare/). Your group can purchase additional hardware for private use, which we will make available as a `pi_groupname` partition. These nodes are purchased by you, but supported and administered by us. After vendor support expires, we retire compute nodes. Compute nodes can range from $10K to upwards of $50K depending on your requirements. If you are interested in purchasing nodes for your group, please [contact us](/#get-help).

??? summary "PI Partitions (click to expand)"
    === "pi_breaker"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_breaker partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |23|E5-2680_v4|28|227|broadwell, E5-2680_v4, nogpu, standard, oldest, pi|

    === "pi_bunick"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_bunick partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6240|36|352|a100|4|40|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, a100|

    === "pi_butterwick"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_butterwick partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6240|36|352|a100|4|40|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, a100|

    === "pi_chenlab"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_chenlab partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|8268|48|352|cascadelake, avx512, 8268, nogpu, bigtmp, pi|

    === "pi_cryo_realtime"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_cryo_realtime partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`14-00:00:00`|
        |Maximum GPUs per user|`12`|
        |Maximum running jobs per user|`2`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|E5-2637_v4|8|101|gtx1080ti|4|11|broadwell, E5-2637_v4, singleprecision, pi, gtx1080ti|

    === "pi_cryoem"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_cryoem partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`2-00:00:00`|
        |Maximum CPUs per user|`32`|
        |Maximum GPUs per user|`12`|
        |Maximum running jobs per user|`2`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |9|E5-2637_v4|8|101|gtx1080ti|4|11|broadwell, E5-2637_v4, singleprecision, pi, gtx1080ti|

    === "pi_deng"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_deng partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|E5-2660_v4|28|227|p100|2|16|broadwell, E5-2660_v4, doubleprecision, pi, p100|

    === "pi_dewan"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_dewan partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|6240|36|163|cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|

    === "pi_dijk"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_dijk partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6240|36|352|rtx3090|8|24|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, rtx3090|

    === "pi_dunn"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_dunn partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|163|cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|

    === "pi_edwards"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_edwards partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|163|cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|

    === "pi_falcone"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_falcone partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6240|36|163||||cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|
        |1|6240|36|1486||||cascadelake, avx512, 6240, nogpu, pi, bigtmp|
        |1|6240|36|352|v100|4|16|cascadelake, avx2, avx512, 6240, pi, v100|

    === "pi_galvani"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_galvani partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |7|8268|48|352|cascadelake, avx512, 8268, nogpu, bigtmp, pi|

    === "pi_gerstein"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_gerstein partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6132|28|730|skylake, avx512, 6132, nogpu, standard, bigtmp, pi|
        |2|6132|28|163|skylake, avx512, 6132, nogpu, standard, bigtmp, pi|
        |11|E5-2680_v4|28|227|broadwell, E5-2680_v4, nogpu, standard, oldest, pi|
        |1|E7-4820_v4|40|1486|broadwell, E7-4820_v4, nogpu, pi|

    === "pi_gerstein_gpu"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_gerstein_gpu partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6240|36|163|rtx3090|4|24|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, rtx3090|
        |1|6240|36|163|rtx3090|8|24|cascadelake, avx512, 6240, doubleprecision, pi, bigtmp, rtx3090|
        |2|E5-2660_v4|28|227|p100|2|16|broadwell, E5-2660_v4, doubleprecision, pi, p100|
        |1|E5-2637_v4|8|101|titanv|4|12|broadwell, E5-2637_v4, doubleprecision, pi, bigtmp, titanv|

    === "pi_gruen"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_gruen partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|E5-2680_v4|28|227|broadwell, E5-2680_v4, nogpu, standard, oldest, pi|

    === "pi_jadi"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_jadi partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`365-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|E5-2680_v4|28|227|broadwell, E5-2680_v4, nogpu, standard, oldest, pi|

    === "pi_jetz"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_jetz partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |4|6240|36|730|cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|
        |4|6240|36|352|cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|

    === "pi_kleinstein"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_kleinstein partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|6240|36|163|cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|

    === "pi_krishnaswamy"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_krishnaswamy partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6420|36|730|a100|4|40|cascadelake, avx512, 6420, doubleprecision, pi, bigtmp, a100|

    === "pi_ma"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_ma partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|8268|48|352|cascadelake, avx512, 8268, nogpu, bigtmp, pi|

    === "pi_medzhitov"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_medzhitov partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|6240|36|163|cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|

    === "pi_miranker"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_miranker partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6248r|48|352|cascadelake, avx512, 6248r, nogpu, pi, bigtmp|

    === "pi_ohern"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_ohern partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|E5-2680_v4|28|227|broadwell, E5-2680_v4, nogpu, standard, oldest, pi|

    === "pi_reinisch"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_reinisch partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |2|5122|8|163|rtx2080|4|8|skylake, avx512, 5122, singleprecision, pi, rtx2080|

    === "pi_sigworth"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_sigworth partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6240|36|163|rtx2080ti|4|11|cascadelake, avx512, 6240, singleprecision, pi, bigtmp, rtx2080ti|

    === "pi_sindelar"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_sindelar partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6240|36|163|rtx2080ti|4|11|cascadelake, avx512, 6240, singleprecision, pi, bigtmp, rtx2080ti|
        |1|E5-2637_v4|8|101|gtx1080ti|4|11|broadwell, E5-2637_v4, singleprecision, pi, gtx1080ti|

    === "pi_tomography"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_tomography partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`4-00:00:00`|
        |Maximum CPUs per user|`32`|
        |Maximum GPUs per user|`12`|
        |Maximum running jobs per user|`2`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6242|32|981|rtx8000|2|48|cascadelake, avx512, 6242, doubleprecision, pi, bigtmp, rtx8000|
        |8|5222|8|163|rtx5000|4|16|cascadelake, avx512, 5222, doubleprecision, pi, bigtmp, rtx5000|

    === "pi_ya-chi_ho"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_ya-chi_ho partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|8268|48|352|cascadelake, avx512, 8268, nogpu, bigtmp, pi|

    === "pi_yong_xiong"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_yong_xiong partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6226r|32|163|rtx3090|4|24|cascadelake, avx512, 6226r, doubleprecision, pi, rtx3090|

    === "pi_zhao"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_zhao partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`7-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|6240|36|163|cascadelake, avx512, 6240, nogpu, bigtmp, standard, pi|

### YCGA Partitions
The following partitions are intended for projects related to the [Yale Center for Genome Analysis](http://ycga.yale.edu/). Please do not use these partitions for other proejcts. Access is granted on a group basis. If you need access to these partitions, please [contact us](/#get-help) to get approved and added.

??? summary "YCGA Partitions (click to expand)"
    === "ycga"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the ycga partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`2-00:00:00`|
        |Maximum CPUs per group|`512`|
        |Maximum memory per group|`3934G`|
        |Maximum CPUs per user|`256`|
        |Maximum memory per user|`1916G`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |40|8362|64|479|icelake, avx512, 8362, nogpu, standard, pi|

    === "ycga_admins"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|8362|64|479|icelake, avx512, 8362, nogpu, standard, pi|

    === "ycga_bigmem"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the ycga_bigmem partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`4-00:00:00`|
        |Maximum CPUs per user|`64`|
        |Maximum memory per user|`1991G`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |4|6346|32|1991|icelake, avx512, 6346, nogpu, pi|

    === "ycga_long"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the ycga_long partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`14-00:00:00`|
        |Maximum CPUs per group|`64`|
        |Maximum memory per group|`479G`|
        |Maximum CPUs per user|`32`|
        |Maximum memory per user|`239G`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |6|8362|64|479|icelake, avx512, 8362, nogpu, standard, pi|

