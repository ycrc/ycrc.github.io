=== "general"

    Use the general partition for most batch jobs. This is the default if you don't specify one with `--partition`.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the general partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`30-00:00:00`|
    |Maximum CPUs per group|`400`|
    |Maximum memory per group|`2.50T`|
    |Maximum CPUs per user|`200`|
    |Maximum memory per user|`1280G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |18|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard|
    |87|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard, oldest|

=== "interactive"

    Use the interactive partition to jobs with which you need ongoing interaction. For example, exploratory analyses or debugging compilation.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=06:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the interactive partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`1-00:00:00`|
    |Maximum CPUs per user|`20`|
    |Maximum memory per user|`256G`|
    |Maximum running jobs per user|`2`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |18|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard|
    |99|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard, oldest|

=== "gpu"

    Use the gpu partition for jobs that make use of GPUs. You must [request GPUs explicitly](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) with the `--gres` option in order to use them. For example, `--gres=gpu:gtx1080ti:2` would request 2 GeForce GTX 1080Ti GPUs per node.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the gpu partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`2-00:00:00`|
    |Maximum CPUs per user|`32`|
    |Maximum GPUs per user|`12`|
    |Maximum memory per user|`256G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|E5-2637_v4|8|121|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision|
    |2|E5-2660_v3|20|121|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision|
    |8|E5-2637_v4|8|121|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision|

=== "gpu_devel"

    Use the gpu_devel partition to debug jobs that make use of GPUs, or to develop GPU-enabled code.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=00:10:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the gpu_devel partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`02:00:00`|
    |Maximum submitted jobs per user|`1`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|E5-2623_v4|8|59|gtx1080ti|4|11|broadwell, avx2, E5-2623_v4, singleprecision|

=== "bigmem"

    Use the bigmem partition for jobs that have memory requirements other partitions can't handle.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the bigmem partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`3-00:00:00`|
    |Maximum CPUs per user|`32`|
    |Maximum memory per user|`1532G`|
    |Maximum running jobs per user|`2`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |2|E7-4809_v3|32|1507|haswell, avx2, E7-4809_v3, nogpu|
    |3|6240|36|1507|cascadelake, avx2, avx512, 6240, nogpu|

=== "scavenge"

    Use the scavenge partition to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the scavenge partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`7-00:00:00`|
    |Maximum CPUs per user|`800`|
    |Maximum memory per user|`5T`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|E5-2637_v4|8|121|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision|
    |2|E7-4809_v3|32|1507||||haswell, avx2, E7-4809_v3, nogpu|
    |1|E7-4820_v4|40|1507||||broadwell, avx2, E7-4820_v4, nogpu|
    |5|E5-2660_v3|20|121|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision|
    |3|E5-2680_v4|28|247|p100|2|16|broadwell, avx2, E5-2680_v4, doubleprecision|
    |38|E5-2680_v4|28|247||||broadwell, avx2, E5-2680_v4, nogpu, standard|
    |1|6132|28|751||||skylake, avx2, avx512, 6132, nogpu|
    |1|E5-2623_v4|8|59|gtx1080ti|4|11|broadwell, avx2, E5-2623_v4, singleprecision|
    |2|5122|8|183|rtx2080|4|8|skylake, avx2, avx512, 5122, singleprecision|
    |1|6240|36|183||||cascadelake, avx2, avx512, 6240, nogpu|
    |1|6240|36|183|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision|
    |8|5222|8|183|rtx5000|4|16|cascadelake, avx2, avx512, 5222, doubleprecision|
    |24|6240|36|183||||cascadelake, avx2, avx512, 6240, nogpu, standard|
    |4|6240|36|372||||cascadelake, avx2, avx512, 6240, nogpu|
    |20|E5-2637_v4|8|121|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision|
    |1|E5-2637_v4|8|121|titanv|4|12|broadwell, avx2, E5-2637_v4, doubleprecision|
    |1|6242|32|1001|rtx8000|2|48|cascadelake, avx2, avx512, 6242, doubleprecision|
    |117|E5-2660_v3|20|121||||haswell, avx2, E5-2660_v3, nogpu, standard, oldest|
    |2|6132|28|183||||skylake, avx2, avx512, 6132, nogpu, standard|
    |4|6240|36|1507||||cascadelake, avx2, avx512, 6240, nogpu|
    |1|6240|36|372|v100|4|16|cascadelake, avx2, avx512, 6240|
    |4|6240|36|750||||cascadelake, avx2, avx512, 6240, nogpu|

=== "scavenge_gpu"

    Use the scavenge_gpu partition to run preemptable jobs on more GPU resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the scavenge_gpu partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`2-00:00:00`|
    |Maximum GPUs per user|`64`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|E5-2637_v4|8|121|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision|
    |5|E5-2660_v3|20|121|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision|
    |3|E5-2680_v4|28|247|p100|2|16|broadwell, avx2, E5-2680_v4, doubleprecision|
    |1|E5-2623_v4|8|59|gtx1080ti|4|11|broadwell, avx2, E5-2623_v4, singleprecision|
    |2|5122|8|183|rtx2080|4|8|skylake, avx2, avx512, 5122, singleprecision|
    |20|E5-2637_v4|8|121|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision|
    |1|E5-2637_v4|8|121|titanv|4|12|broadwell, avx2, E5-2637_v4, doubleprecision|
    |1|6240|36|372|v100|4|16|cascadelake, avx2, avx512, 6240|

### Private Partitions
With few exceptions, jobs submitted to `pi_` partitions are not considered when calculating your group's [Fairshare](/clusters-at-yale/job-scheduling/fairshare/). Your group can purchase additional hardware for private use, which we will make available as a `pi_groupname` partition. These nodes are purchased by you, but supported and administered by us. After vendor support expires, we retire compute nodes. Compute nodes can range from $10K to upwards of $50K depending on your requirements. If you are interested in purchasing nodes for your group, please [contact us](/#get-help).

??? summary "PI Partitions (click to expand)"
    === "pi_breaker"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |24|E5-2680_v4|28|247|broadwell, avx2, E5-2680_v4, nogpu, standard|

    === "pi_cryoem"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_cryoem partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`365-00:00:00`|
        |Maximum GPUs per user|`12`|
        |Maximum running jobs per user|`2`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |10|E5-2637_v4|8|121|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision|

    === "pi_deng"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|E5-2680_v4|28|247|p100|2|16|broadwell, avx2, E5-2680_v4, doubleprecision|

    === "pi_dunn"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard|

    === "pi_edwards"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard|

    === "pi_falcone"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6240|36|183||||cascadelake, avx2, avx512, 6240, nogpu|
        |1|6240|36|1507||||cascadelake, avx2, avx512, 6240, nogpu|
        |1|6240|36|372|v100|4|16|cascadelake, avx2, avx512, 6240|

    === "pi_gerstein"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|E7-4820_v4|40|1507|broadwell, avx2, E7-4820_v4, nogpu|
        |11|E5-2680_v4|28|247|broadwell, avx2, E5-2680_v4, nogpu, standard|
        |1|6132|28|751|skylake, avx2, avx512, 6132, nogpu|
        |2|6132|28|183|skylake, avx2, avx512, 6132, nogpu, standard|

    === "pi_gerstein_gpu"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |3|E5-2660_v3|20|121|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision|
        |2|E5-2680_v4|28|247|p100|2|16|broadwell, avx2, E5-2680_v4, doubleprecision|
        |1|E5-2637_v4|8|121|titanv|4|12|broadwell, avx2, E5-2637_v4, doubleprecision|

    === "pi_gruen"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|E5-2680_v4|28|247|broadwell, avx2, E5-2680_v4, nogpu, standard|

    === "pi_jadi"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_jadi partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`365-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|E5-2680_v4|28|247|broadwell, avx2, E5-2680_v4, nogpu, standard|

    === "pi_jetz"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |4|6240|36|372|cascadelake, avx2, avx512, 6240, nogpu|
        |4|6240|36|750|cascadelake, avx2, avx512, 6240, nogpu|

    === "pi_kleinstein"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |3|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard, oldest|
        |1|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard|

    === "pi_krauthammer"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard, oldest|

    === "pi_ma"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard, oldest|

    === "pi_ohern"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |5|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard, oldest|

    === "pi_reinisch"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |2|5122|8|183|rtx2080|4|8|skylake, avx2, avx512, 5122, singleprecision|

    === "pi_sigworth"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|E5-2660_v3|20|121||||haswell, avx2, E5-2660_v3, nogpu, standard, oldest|
        |1|6240|36|183|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision|

    === "pi_sindelar"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|E5-2660_v3|20|121||||haswell, avx2, E5-2660_v3, nogpu, standard, oldest|
        |1|E5-2637_v4|8|121|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision|

    === "pi_tomography"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_tomography partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`4-00:00:00`|
        |Maximum GPUs per user|`12`|
        |Maximum running jobs per user|`2`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |8|5222|8|183|rtx5000|4|16|cascadelake, avx2, avx512, 5222, doubleprecision|
        |1|6242|32|1001|rtx8000|2|48|cascadelake, avx2, avx512, 6242, doubleprecision|

    === "pi_townsend"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |5|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, nogpu, standard, oldest|

    === "pi_zhao"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|6240|36|183|cascadelake, avx2, avx512, 6240, nogpu, standard|

