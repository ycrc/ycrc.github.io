=== "general"

    Use the general partition for most batch jobs. This is the default if you don't specify one with `--partition`.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the general partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`30-00:00:00`|
    |Maximum CPUs per group|`400`|
    |Maximum memory per group|`2.50T`|
    |Maximum CPUs per user|`200`|
    |Maximum memory per user|`1280G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |68|E5-2660_v3|20|117|haswell, avx2, E5-2660_v3, nogpu, standard, oldest, common|

=== "interactive"

    Use the interactive partition to jobs with which you need ongoing interaction. For example, exploratory analyses or debugging compilation.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=06:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the interactive partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`1-00:00:00`|
    |Maximum CPUs per user|`20`|
    |Maximum memory per user|`256G`|
    |Maximum running jobs per user|`2`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |83|E5-2660_v3|20|117|haswell, avx2, E5-2660_v3, nogpu, standard, oldest, common|

=== "transfer"

    Use the transfer partition to stage data for your jobs to and from [cluster storage](/clusters-at-yale/data/#staging-data).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the transfer partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`1-00:00:00`|
    |Maximum running jobs per user|`2`|
    |Maximum CPUs per job|`1`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |2|E5-2660_v3|20|117|haswell, avx2, E5-2660_v3, nogpu, standard, oldest, common|

=== "gpu"

    Use the gpu partition for jobs that make use of GPUs. You must [request GPUs explicitly](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) with the `--gpus` option in order to use them. For example, `--gpus=gtx1080ti:2` would request 2 GeForce GTX 1080Ti GPUs per node.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the gpu partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`2-00:00:00`|
    |Maximum CPUs per user|`32`|
    |Maximum GPUs per user|`12`|
    |Maximum memory per user|`256G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|6240|36|370|a100|4|40|cascadelake, avx2, avx512, 6240, doubleprecision, common, bigtmp, a100|
    |2|5222|8|181|rtx5000|4|16|cascadelake, avx2, avx512, 5222, doubleprecision, common, bigtmp, rtx5000|
    |5|E5-2637_v4|8|119|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision, common, gtx1080ti|
    |2|E5-2660_v3|20|119|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, common, k80|

=== "gpu_devel"

    Use the gpu_devel partition to debug jobs that make use of GPUs, or to develop GPU-enabled code.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=00:10:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the gpu_devel partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`02:00:00`|
    |Maximum submitted jobs per user|`1`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|E5-2623_v4|8|57|gtx1080ti|4|11|broadwell, avx2, E5-2623_v4, singleprecision, common, gtx1080ti|

=== "bigmem"

    Use the bigmem partition for jobs that have memory requirements other partitions can't handle.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the bigmem partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`3-00:00:00`|
    |Maximum CPUs per user|`32`|
    |Maximum memory per user|`1505G`|
    |Maximum running jobs per user|`2`|
    |Maximum nodes per job|`1`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |3|6240|36|1505|cascadelake, avx2, avx512, 6240, nogpu, common, bigtmp|
    |2|E7-4809_v3|32|1505|haswell, avx2, E7-4809_v3, nogpu, common|

=== "scavenge"

    Use the scavenge partition to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the scavenge partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`7-00:00:00`|
    |Maximum CPUs per user|`800`|
    |Maximum memory per user|`5T`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|6240|36|181||||cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|
    |1|6240|36|370|a100|4|40|cascadelake, avx2, avx512, 6240, doubleprecision, common, bigtmp, a100|
    |3|6240|36|1505||||cascadelake, avx2, avx512, 6240, nogpu, common, bigtmp|
    |5|E5-2637_v4|8|119|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision, common, gtx1080ti|
    |1|E5-2623_v4|8|57|gtx1080ti|4|11|broadwell, avx2, E5-2623_v4, singleprecision, common, gtx1080ti|
    |16|E5-2660_v3|20|119||||haswell, avx2, E5-2660_v3, nogpu, standard, oldest, pi|
    |85|E5-2660_v3|20|117||||haswell, avx2, E5-2660_v3, nogpu, standard, oldest, common|
    |2|E7-4809_v3|32|1505||||haswell, avx2, E7-4809_v3, nogpu, common|
    |3|E5-2660_v3|20|119|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, pi, k80|
    |2|E5-2660_v3|20|119|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, common, k80|

=== "scavenge_gpu"

    Use the scavenge_gpu partition to run preemptable jobs on more GPU resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the scavenge_gpu partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`2-00:00:00`|
    |Maximum GPUs per user|`64`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|6240|36|370|a100|4|40|cascadelake, avx2, avx512, 6240, doubleprecision, common, bigtmp, a100|
    |5|E5-2637_v4|8|119|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision, common, gtx1080ti|
    |1|E5-2623_v4|8|57|gtx1080ti|4|11|broadwell, avx2, E5-2623_v4, singleprecision, common, gtx1080ti|
    |3|E5-2660_v3|20|119|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, pi, k80|
    |2|E5-2660_v3|20|119|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, common, k80|

### Private Partitions
With few exceptions, jobs submitted to private partitions are not considered when calculating your group's [Fairshare](/clusters-at-yale/job-scheduling/fairshare/). Your group can purchase additional hardware for private use, which we will make available as a `pi_groupname` partition. These nodes are purchased by you, but supported and administered by us. After vendor support expires, we retire compute nodes. Compute nodes can range from $10K to upwards of $50K depending on your requirements. If you are interested in purchasing nodes for your group, please [contact us](/#get-help).

??? summary "PI Partitions (click to expand)"
    === "pi_gerstein_gpu"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_gerstein_gpu partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`14-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |3|E5-2660_v3|20|119|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, pi, k80|

    === "pi_jadi"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
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
        |3|E5-2660_v3|20|117|haswell, avx2, E5-2660_v3, nogpu, standard, oldest, common|

    === "pi_kleinstein"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_kleinstein partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`14-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |3|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, oldest, pi|

    === "pi_krauthammer"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_krauthammer partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`14-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, oldest, pi|

    === "pi_ma"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_ma partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`14-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, oldest, pi|

    === "pi_ohern"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_ohern partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`14-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |3|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, oldest, pi|

    === "pi_sigworth"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_sigworth partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`14-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, oldest, pi|

    === "pi_sindelar"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_sindelar partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`14-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, oldest, pi|

    === "pi_townsend"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_townsend partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`14-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |5|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, oldest, pi|

    === "pi_tucci"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_tucci partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`14-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|

