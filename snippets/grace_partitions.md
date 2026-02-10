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
    |Maximum CPUs per group|`2500`|
    |Maximum CPUs per user|`1500`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |66|6342|48|487|icelake, avx512, 6342, nogpu, standard, common, bigtmp|
    |18|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, common, bigtmp, oldest|
    |72|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, common, bigtmp, oldest|

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
    |10|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, common, bigtmp, oldest|

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
    |Maximum CPUs per group|`252`|
    |Maximum CPUs per user|`108`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |18|6342|48|487|icelake, avx512, 6342, nogpu, standard, common, bigtmp|

=== "gpu"

    Use the gpu partition for jobs that make use of GPUs. You must [request GPUs explicitly](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) with the `--gpus` option in order to use them. For example, `--gpus=a5000:2` would request 2 NVIDIA RTX A5000 GPUs per node.

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
    |Maximum GPUs per group|`48`|
    |Maximum GPUs per user|`24`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |2|6342|48|984|a100|4|80|icelake, avx512, 6342, doubleprecision, bigtmp, common, gpu, a100, a100-80g|
    |1|6326|32|984|a100|4|80|icelake, avx512, 6326, doubleprecision, bigtmp, common, gpu, a100, a100-80g|
    |11|6326|32|206|a5000|4|24|icelake, avx512, 6326, doubleprecision, a5000, common|
    |2|6240|36|361|a100|4|40|cascadelake, avx512, 6240, doubleprecision, bigtmp, common, a100, a100-40g, oldest|
    |4|6240|36|370|v100|4|16|cascadelake, avx512, 6240, doubleprecision, common, v100, oldest|
    |2|6136|24|90|v100|2|16|skylake, avx512, 6136, doubleprecision, common, bigtmp, v100|

=== "gpu_devel"

    Use the gpu_devel partition to debug jobs that make use of GPUs, or to develop GPU-enabled code.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the gpu_devel partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`06:00:00`|
    |Maximum CPUs per user|`10`|
    |Maximum GPUs per user|`3`|
    |Maximum submitted jobs per user|`2`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|6326|32|984|a100|4|80|icelake, avx512, 6326, doubleprecision, bigtmp, common, gpu, a100, a100-80g|
    |1|6326|32|206|a5000|4|24|icelake, avx512, 6326, doubleprecision, a5000, common|
    |1|6240|36|370|v100|4|16|cascadelake, avx512, 6240, doubleprecision, common, v100, oldest|
    |2|6240|36|166|rtx3090|4|24|cascadelake, avx512, 6240, doubleprecision, bigtmp, common, rtx3090, oldest|

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
    |Maximum CPUs per user|`40`|
    |Maximum memory per user|`4000G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |4|6346|32|3935|cascadelake, avx512, 6346, common, nogpu, bigtmp, oldest|
    |1|6240|36|1505|cascadelake, avx512, 6240, nogpu, common, bigtmp, oldest|
    |2|6234|16|1505|cascadelake, avx512, nogpu, 6234, common, bigtmp, oldest|

=== "mpi"

    Use the mpi partition for tightly-coupled parallel programs that make efficient use of multiple nodes. See our [MPI documentation](/clusters-at-yale/job-scheduling/mpi) if your workload fits this description.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --exclusive --mem=184320
    ```

    **Job Limits**

    Jobs submitted to the mpi partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`1-00:00:00`|
    |Maximum nodes per group|`48`|
    |Maximum nodes per user|`32`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |52|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, common, bigtmp, oldest|

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
    |Maximum CPUs per user|`10000`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |20|6442|48|487||||sapphirerapids, avx512, 6442Y, nogpu, standard, pi, bigtmp|
    |6|6342|48|1999||||icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
    |50|6342|48|487||||icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
    |1|6326|32|983|l40s|4|48|icelake, avx512, 6326, pi, standard, bigtmp, l40s|
    |84|6342|48|487||||icelake, avx512, 6342, nogpu, standard, common, bigtmp|
    |2|6342|48|984|a100|4|80|icelake, avx512, 6342, doubleprecision, bigtmp, common, gpu, a100, a100-80g|
    |2|6326|32|984|a100|4|80|icelake, avx512, 6326, doubleprecision, bigtmp, common, gpu, a100, a100-80g|
    |2|6326|32|468|a5000|4|24|icelake, avx512, 6326, doubleprecision, a5000, pi|
    |11|6326|32|206|a5000|4|24|icelake, avx512, 6326, doubleprecision, a5000, common|
    |2|6326|32|206|a5000|4|24|icelake, avx512, 6326, doubleprecision, a5000, pi|
    |72|8268|48|355||||cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|
    |28|6240|36|181||||cascadelake, avx512, 6240, nogpu, standard, common, bigtmp, oldest|
    |81|6240|36|181||||cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|
    |72|8268|48|355||||cascadelake, avx512, 8268, nogpu, standard, common, bigtmp, oldest|
    |4|6346|32|3935||||cascadelake, avx512, 6346, common, nogpu, bigtmp, oldest|
    |2|6240|36|361|a100|4|40|cascadelake, avx512, 6240, doubleprecision, bigtmp, common, a100, a100-40g, oldest|
    |20|8260|96|181||||cascadelake, avx512, 8260, nogpu, pi, oldest|
    |4|6240|36|370|v100|4|16|cascadelake, avx512, 6240, doubleprecision, common, v100, oldest|
    |1|6240|36|1505||||cascadelake, avx512, 6240, nogpu, common, bigtmp, oldest|
    |1|6326|32|1001|a100|4|80|cascadelake, avx512, 6326, doubleprecision, bigtmp, pi, a100, a100-80g, oldest|
    |1|6254|36|370|rtx2080ti|8|11|cascadelake, avx512, 6254, singleprecision, pi, bigtmp, rtx2080ti, oldest|
    |2|6240|36|370|v100|4|16|cascadelake, avx512, 6240, doubleprecision, pi, v100, oldest|
    |4|6240|36|181|rtx2080ti|4|11|cascadelake, avx512, 6240, singleprecision, pi, bigtmp, rtx2080ti, oldest|
    |2|6240|36|179|rtx3090|4|24|cascadelake, avx512, 6240, doubleprecision, bigtmp, pi, rtx3090, oldest|
    |8|6240|36|370||||cascadelake, avx512, 6240, nogpu, pi, bigtmp, oldest|
    |2|6234|16|1505||||cascadelake, avx512, nogpu, 6234, common, bigtmp, oldest|
    |3|6234|16|1505||||cascadelake, avx512, nogpu, 6234, pi, bigtmp, oldest|
    |3|6142|32|181||||skylake, avx512, 6142, nogpu, standard, pi, bigtmp|
    |12|6136|24|90||||hdr, skylake, avx512, 6136, nogpu, standard, pi, bigtmp|
    |4|6136|24|88||||hdr, skylake, avx512, 6136, nogpu, standard, pi, bigtmp|
    |2|6136|24|90|v100|2|16|skylake, avx512, 6136, doubleprecision, common, bigtmp, v100|

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
    |Maximum GPUs per user|`30`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |2|6342|48|984|a100|4|80|icelake, avx512, 6342, doubleprecision, bigtmp, common, gpu, a100, a100-80g|
    |1|6326|32|984|a100|4|80|icelake, avx512, 6326, doubleprecision, bigtmp, common, gpu, a100, a100-80g|
    |11|6326|32|206|a5000|4|24|icelake, avx512, 6326, doubleprecision, a5000, common|
    |2|6240|36|361|a100|4|40|cascadelake, avx512, 6240, doubleprecision, bigtmp, common, a100, a100-40g, oldest|
    |4|6240|36|370|v100|4|16|cascadelake, avx512, 6240, doubleprecision, common, v100, oldest|
    |2|6136|24|90|v100|2|16|skylake, avx512, 6136, doubleprecision, common, bigtmp, v100|

### Private Partitions
With few exceptions, jobs submitted to private partitions are not considered when calculating your group's [Fairshare](/clusters-at-yale/job-scheduling/fairshare/). Your group can purchase additional hardware for private use, which we will make available as a `pi_groupname` partition. These nodes are purchased by you, but supported and administered by us. After vendor support expires, we retire compute nodes. Compute nodes can range from $10K to upwards of $50K depending on your requirements. If you are interested in purchasing nodes for your group, please [contact us](/#get-help).

??? summary "PI Partitions (click to expand)"
    === "pi_anticevic"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_anticevic partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`100-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |2|6342|48|1999||||icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |15|6342|48|487||||icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |2|6326|32|206|a5000|4|24|icelake, avx512, 6326, doubleprecision, a5000, pi|

    === "pi_balou"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_balou partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |14|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|
        |9|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_berry"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_berry partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|
        |1|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_chem_chase"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=3840
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_chem_chase partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |8|6240|36|181||||cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|
        |1|6240|36|181|rtx2080ti|4|11|cascadelake, avx512, 6240, singleprecision, pi, bigtmp, rtx2080ti, oldest|

    === "pi_cholab"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_cholab partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`100-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |2|6342|48|1999||||icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |15|6342|48|487||||icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |2|6326|32|206|a5000|4|24|icelake, avx512, 6326, doubleprecision, a5000, pi|

    === "pi_cowles"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_cowles partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|
        |Maximum CPUs per user|`120`|
        |Maximum nodes per user|`5`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |9|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|

    === "pi_econ_io"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_econ_io partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |6|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_econ_lp"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_econ_lp partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |6|6342|48|487|icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |7|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|
        |5|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|
        |1|6234|16|1505|cascadelake, avx512, nogpu, 6234, pi, bigtmp, oldest|

    === "pi_esi"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_esi partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|
        |Maximum CPUs per user|`648`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |36|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_fedorov"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=3840
        ```

        **Job Limits**

        Jobs submitted to the pi_fedorov partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |6|6342|48|487|icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |12|6136|24|90|hdr, skylake, avx512, 6136, nogpu, standard, pi, bigtmp|

    === "pi_gelernter"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_gelernter partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_hammes_schiffer"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=3840
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_hammes_schiffer partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |8|6240|36|181||||cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|
        |6|8268|48|355||||cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|
        |1|6240|36|181|rtx2080ti|4|11|cascadelake, avx512, 6240, singleprecision, pi, bigtmp, rtx2080ti, oldest|

    === "pi_hodgson"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_hodgson partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_holland"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_holland partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|6342|48|487|icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |8|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_howard"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_howard partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_jorgensen"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_jorgensen partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |3|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_kim_theodore"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_kim_theodore partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|
        |1|6234|16|1505|cascadelake, avx512, nogpu, 6234, pi, bigtmp, oldest|

    === "pi_korenaga"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_korenaga partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |3|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|

    === "pi_lederman"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_lederman partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6254|36|1505|rtx4000,rtx8000,v100|4,2,2|8,48,16|cascadelake, avx512, 6254, pi, bigtmp, rtx8000, oldest|

    === "pi_levine"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=1952
        ```

        **Job Limits**

        Jobs submitted to the pi_levine partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |20|8260|96|181|cascadelake, avx512, 8260, nogpu, pi, oldest|

    === "pi_lora"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=3840
        ```

        **Job Limits**

        Jobs submitted to the pi_lora partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |5|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|
        |4|6136|24|88|hdr, skylake, avx512, 6136, nogpu, standard, pi, bigtmp|

    === "pi_manohar"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_manohar partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`180-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |6|6342|48|487|icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |2|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|
        |4|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_mingarelli"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_mingarelli partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |6|6442|48|487|sapphirerapids, avx512, 6442Y, nogpu, standard, pi, bigtmp|
        |4|6342|48|1999|icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |6|6342|48|487|icelake, avx512, 6342, nogpu, standard, pi, bigtmp|

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
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|6342|48|487|icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |8|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|

    === "pi_owen_miller"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_owen_miller partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|6442|48|487|sapphirerapids, avx512, 6442Y, nogpu, standard, pi, bigtmp|
        |2|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|
        |1|6234|16|1505|cascadelake, avx512, nogpu, 6234, pi, bigtmp, oldest|

    === "pi_padmanabhan"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_padmanabhan partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |3|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_panda"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_panda partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |2|6342|48|487||||icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |2|6326|32|468|a5000|4|24|icelake, avx512, 6326, doubleprecision, a5000, pi|
        |1|6326|32|1001|a100|4|80|cascadelake, avx512, 6326, doubleprecision, bigtmp, pi, a100, a100-80g, oldest|
        |1|6254|36|370|rtx2080ti|8|11|cascadelake, avx512, 6254, singleprecision, pi, bigtmp, rtx2080ti, oldest|
        |2|6240|36|370|v100|4|16|cascadelake, avx512, 6240, doubleprecision, pi, v100, oldest|
        |3|6240|36|181|rtx2080ti|4|11|cascadelake, avx512, 6240, singleprecision, pi, bigtmp, rtx2080ti, oldest|

    === "pi_poland"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_poland partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |8|6240|36|370|cascadelake, avx512, 6240, nogpu, pi, bigtmp, oldest|

    === "pi_polimanti"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_polimanti partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|6342|48|487|icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |2|6240|36|181|cascadelake, avx512, 6240, nogpu, standard, pi, bigtmp, oldest|

    === "pi_seto"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_seto partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |3|6142|32|181|skylake, avx512, 6142, nogpu, standard, pi, bigtmp|

    === "pi_spielman"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_spielman partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|

    === "pi_sweeney"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_sweeney partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |2|6240|36|179|rtx3090|4|24|cascadelake, avx512, 6240, doubleprecision, bigtmp, pi, rtx3090, oldest|

    === "pi_tsmith"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_tsmith partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|6342|48|487|icelake, avx512, 6342, nogpu, standard, pi, bigtmp|
        |1|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|

    === "pi_vaccaro"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_vaccaro partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6342|48|487|icelake, avx512, 6342, nogpu, standard, pi, bigtmp|

    === "pi_ying_rex"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_ying_rex partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6326|32|983|l40s|4|48|icelake, avx512, 6326, pi, standard, bigtmp, l40s|

    === "pi_zhu"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
        ```

        **Job Limits**

        Jobs submitted to the pi_zhu partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Maximum job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |12|6442|48|487|sapphirerapids, avx512, 6442Y, nogpu, standard, pi, bigtmp|
        |12|8268|48|355|cascadelake, avx512, 8268, nogpu, standard, pi, bigtmp, oldest|

