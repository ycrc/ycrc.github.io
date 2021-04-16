=== "day"

    Use the day partition for most batch jobs. This is the default if you don't specify one with `--partition`.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the day partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`1-00:00:00`|
    |Maximum CPUs per group|`1500`|
    |Maximum CPUs per user|`750`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |124|6240|36|181||||cascadelake, avx2, avx512, 6240, nogpu, standard, common, bigtmp|
    |1|E5-2660_v4|28|245||||broadwell, avx2, E5-2660_v4, nogpu, standard, pi|
    |77|E5-2660_v4|28|245||||broadwell, avx2, E5-2660_v4, nogpu, standard, common|
    |24|E5-2660_v3|20|119||||haswell, avx2, E5-2660_v3, nogpu, standard, common|
    |1|E5-2660_v3|20|245|k80|2|12|haswell, avx2, E5-2660_v3, doubleprecision, pi|
    |22|E5-2660_v2|20|119||||ivybridge, E5-2660_v2, nogpu, standard, oldest, common|

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

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |1|6126|24|174|skylake, avx2, avx512, 6126, nogpu, standard, common|
    |2|E5-2660_v2|20|119|ivybridge, E5-2660_v2, nogpu, standard, oldest, common|

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
    |Maximum CPUs per user|`108`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |8|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, common, bigtmp|
    |30|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, common|

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

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |2|E5-2660_v2|20|119|ivybridge, E5-2660_v2, nogpu, standard, oldest, common|

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

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |4|6240|36|370|v100|4|16|cascadelake, avx2, avx512, 6240, doubleprecision, common|
    |5|6240|36|181|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, common, bigtmp|
    |6|5222|8|181|rtx5000|4|16|cascadelake, avx2, avx512, 5222, doubleprecision, common, bigtmp|
    |2|6136|24|90|v100|2|16|skylake, avx2, avx512, 6136, doubleprecision, common, bigtmp|
    |6|E5-2660_v4|28|245|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, common|
    |3|E5-2660_v3|20|119|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, common|

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

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|6240|36|370|v100|4|16|cascadelake, avx2, avx512, 6240, doubleprecision, common|

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

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |1|6240|36|1505|cascadelake, avx2, avx512, 6240, nogpu, standard, common, bigtmp|
    |2|6240|36|1505|cascadelake, avx2, avx512, 6240, nogpu, common, bigtmp|
    |2|6234|16|1505|cascadelake, avx2, avx512, nogpu, 6234, common, bigtmp|
    |2|E7-4820_v4|40|1505|broadwell, avx2, E7-4820_v4, nogpu, common|

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

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |12|6136|24|90|hdr, skylake, avx2, avx512, 6136, nogpu, standard, pi, bigtmp|
    |120|6136|24|90|hdr, skylake, avx2, avx512, 6136, nogpu, standard, common, bigtmp|

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

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |80|6240|36|181||||cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|
    |135|6240|36|181||||cascadelake, avx2, avx512, 6240, nogpu, standard, common, bigtmp|
    |1|6240|36|1505||||cascadelake, avx2, avx512, 6240, nogpu, standard, common, bigtmp|
    |2|6240|36|1505||||cascadelake, avx2, avx512, 6240, nogpu, common, bigtmp|
    |20|8260|96|181||||cascadelake, avx2, avx512, 8260, nogpu, pi|
    |4|6240|36|370|v100|4|16|cascadelake, avx2, avx512, 6240, doubleprecision, common|
    |5|6240|36|181|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, common, bigtmp|
    |2|6234|16|1505||||cascadelake, avx2, avx512, nogpu, 6234, common, bigtmp|
    |2|6240|36|181|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, pi, bigtmp|
    |8|6240|36|370||||cascadelake, avx2, avx512, 6240, nogpu, pi, bigtmp|
    |3|6142|32|181||||skylake, avx2, avx512, 6142, nogpu, standard, pi, bigtmp|
    |16|6136|24|90||||edr, skylake, avx2, avx512, 6136, nogpu, standard, pi, bigtmp|
    |120|6136|24|90||||hdr, skylake, avx2, avx512, 6136, nogpu, standard, common, bigtmp|
    |28|6136|24|90||||hdr, skylake, avx2, avx512, 6136, nogpu, standard, pi, bigtmp|
    |2|6136|24|90|v100|2|16|skylake, avx2, avx512, 6136, doubleprecision, common, bigtmp|
    |1|6136|24|749||||skylake, avx2, avx512, 6136, nogpu, pi, bigtmp|
    |9|6136|24|181|p100|4|16|skylake, avx2, avx512, 6136, doubleprecision, pi|
    |2|5122|8|181|rtx2080|4|8|skylake, avx2, avx512, 5122, singleprecision, pi|
    |82|E5-2660_v4|28|245||||broadwell, avx2, E5-2660_v4, nogpu, standard, pi|
    |79|E5-2660_v4|28|245||||broadwell, avx2, E5-2660_v4, nogpu, standard, common|
    |2|E7-4820_v4|40|1505||||broadwell, avx2, E7-4820_v4, nogpu, common|
    |6|E5-2660_v4|28|245|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, common|
    |2|E7-4820_v4|40|1505||||broadwell, avx2, E7-4820_v4, nogpu, pi|
    |1|E5-2660_v4|28|245|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, pi|
    |1|E5-2637_v4|8|119|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision, pi, bigtmp|
    |60|E5-2660_v3|20|119||||haswell, avx2, E5-2660_v3, nogpu, standard, common|
    |1|E5-2660_v3|20|119||||haswell, avx2, E5-2660_v3, nogpu, standard, common, bigtmp|
    |51|E5-2660_v3|20|119||||haswell, avx2, E5-2660_v3, nogpu, standard, pi|
    |19|E5-2660_v3|20|245||||haswell, avx2, E5-2660_v3, nogpu, standard, pi|
    |8|E5-2660_v3|20|245|k80|2|12|haswell, avx2, E5-2660_v3, doubleprecision, pi|
    |6|E5-2660_v3|20|119|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, common|
    |1|E7-4809_v3|32|2009||||haswell, avx2, E7-4809_v3, nogpu, pi|
    |58|E5-2660_v2|20|119||||ivybridge, E5-2660_v2, nogpu, standard, oldest, common|
    |14|E5-2660_v2|20|119||||ivybridge, E5-2660_v2, nogpu, standard, oldest, pi|
    |1|E7-4820_v2|32|1001||||ivybridge, E7-4820_v2, nogpu, pi|

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

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |4|6240|36|370|v100|4|16|cascadelake, avx2, avx512, 6240, doubleprecision, common|
    |5|6240|36|181|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, common, bigtmp|
    |1|6240|36|181|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, pi, bigtmp|
    |2|6136|24|90|v100|2|16|skylake, avx2, avx512, 6136, doubleprecision, common, bigtmp|
    |9|6136|24|181|p100|4|16|skylake, avx2, avx512, 6136, doubleprecision, pi|
    |2|5122|8|181|rtx2080|4|8|skylake, avx2, avx512, 5122, singleprecision, pi|
    |6|E5-2660_v4|28|245|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, common|
    |1|E5-2660_v4|28|245|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, pi|
    |1|E5-2637_v4|8|119|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision, pi, bigtmp|
    |8|E5-2660_v3|20|245|k80|2|12|haswell, avx2, E5-2660_v3, doubleprecision, pi|
    |6|E5-2660_v3|20|119|k80|4|12|haswell, avx2, E5-2660_v3, doubleprecision, common|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |16|E5-2660_v4|28|245|broadwell, avx2, E5-2660_v4, nogpu, standard, pi|
        |15|E5-2660_v3|20|245|haswell, avx2, E5-2660_v3, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|E7-4809_v3|32|2009|haswell, avx2, E7-4809_v3, nogpu, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |7|E5-2660_v3|20|245|k80|2|12|haswell, avx2, E5-2660_v3, doubleprecision, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |3|E5-2660_v3|20|245|haswell, avx2, E5-2660_v3, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |9|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|
        |30|E5-2660_v4|28|245|broadwell, avx2, E5-2660_v4, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|

    === "pi_chem_chase"

        **Request Defaults**

        Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

        ``` text
        --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=3840
        ```

        !!! warning "GPU jobs need GPUs!"
            Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gres`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
        **Job Limits**

        Jobs submitted to the pi_chem_chase partition are subject to the following limits:

        |Limit|Value|
        |---|---|
        |Max job time limit|`28-00:00:00`|

        **Available Compute Nodes**

        Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |8|6240|36|181||||cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|
        |1|6240|36|181|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |13|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |10|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |6|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |5|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |36|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |12|6136|24|90|hdr, skylake, avx2, avx512, 6136, nogpu, standard, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|
        |1|E5-2660_v4|28|245|broadwell, avx2, E5-2660_v4, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |29|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, pi|
        |1|E7-4820_v2|32|1001|ivybridge, E7-4820_v2, nogpu, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|E5-2660_v3|20|245|haswell, avx2, E5-2660_v3, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |8|6240|36|181||||cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|
        |1|6240|36|181|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, pi, bigtmp|
        |16|6136|24|90||||edr, skylake, avx2, avx512, 6136, nogpu, standard, pi, bigtmp|
        |1|6136|24|749||||skylake, avx2, avx512, 6136, nogpu, pi, bigtmp|
        |2|5122|8|181|rtx2080|4|8|skylake, avx2, avx512, 5122, singleprecision, pi|
        |1|E5-2637_v4|8|119|gtx1080ti|4|11|broadwell, avx2, E5-2637_v4, singleprecision, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |8|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|
        |2|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |2|E5-2660_v4|28|245|broadwell, avx2, E5-2660_v4, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |7|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6254|36|1505|rtx4000,rtx8000,v100|4,2,2|8,48,16|cascadelake, avx2, avx512, 6254, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |20|8260|96|181|cascadelake, avx2, avx512, 8260, nogpu, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |4|6136|24|90|hdr, skylake, avx2, avx512, 6136, nogpu, standard, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |3|E5-2660_v4|28|245|broadwell, avx2, E5-2660_v4, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |4|6240|36|181||||cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|
        |8|E5-2660_v4|28|245||||broadwell, avx2, E5-2660_v4, nogpu, standard, pi|
        |2|E7-4820_v4|40|1505||||broadwell, avx2, E7-4820_v4, nogpu, pi|
        |1|E5-2660_v4|28|245|p100|1|16|broadwell, avx2, E5-2660_v4, doubleprecision, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |2|6240|36|181||||cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|
        |9|6136|24|181|p100|4|16|skylake, avx2, avx512, 6136, doubleprecision, pi|
        |3|E5-2660_v4|28|245||||broadwell, avx2, E5-2660_v4, nogpu, standard, pi|
        |14|E5-2660_v2|20|119||||ivybridge, E5-2660_v2, nogpu, standard, oldest, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |5|E5-2660_v4|28|245|broadwell, avx2, E5-2660_v4, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
        |---|---|---|---|---|---|---|---|
        |1|6254|36|370|rtx2080ti|8|11|cascadelake, avx2, avx512, 6254, singleprecision, pi, bigtmp|
        |2|6240|36|370|v100|4|16|cascadelake, avx2, avx512, 6240, doubleprecision, pi|
        |3|6240|36|181|rtx2080ti|4|11|cascadelake, avx2, avx512, 6240, singleprecision, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |8|6240|36|370|cascadelake, avx2, avx512, 6240, nogpu, pi, bigtmp|
        |10|E5-2660_v4|28|245|broadwell, avx2, E5-2660_v4, nogpu, standard, pi|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|6240|36|181|cascadelake, avx2, avx512, 6240, nogpu, standard, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |3|6142|32|181|skylake, avx2, avx512, 6142, nogpu, standard, pi, bigtmp|

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

        |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
        |---|---|---|---|---|
        |1|E5-2660_v3|20|119|haswell, avx2, E5-2660_v3, nogpu, standard, pi|

