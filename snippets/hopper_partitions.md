=== "day"

    Use the day partition for most batch jobs. This is the default if you don't specify one with `--partition`.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=UNLIMITED
    ```

    **Job Limits**

    Jobs submitted to the day partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`1-00:00:00`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |52|cpugen:emeraldrapids|64|976|cpugen:emeraldrapids, cpumodel:8562Y+, common:yes|
    |4|cpugen:emeraldrapids|64|1953|cpugen:emeraldrapids, cpumodel:8562Y+, common:yes|

=== "devel"

    Use the devel partition to jobs with which you need ongoing interaction. For example, exploratory analyses or debugging compilation.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=UNLIMITED
    ```

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |2|cpugen:emeraldrapids|64|976|cpugen:emeraldrapids, cpumodel:8562Y+, common:yes|

=== "week"

    Use the week partition for jobs that need a longer runtime than day allows.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=UNLIMITED
    ```

    **Job Limits**

    Jobs submitted to the week partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`7-00:00:00`|
    |Maximum CPUs per group|`192`|
    |Maximum memory per group|`2949G`|
    |Maximum CPUs per user|`192`|
    |Maximum memory per user|`2949G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |6|cpugen:emeraldrapids|64|976|cpugen:emeraldrapids, cpumodel:8562Y+, common:yes|

=== "gpu"

    Use the gpu partition for jobs that make use of GPUs. You must [request GPUs explicitly](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) with the `--gpus` option in order to use them. For example, `--gpus=gtx1080ti:2` would request 2 GeForce GTX 1080Ti GPUs per node.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=UNLIMITED
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the gpu partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`2-00:00:00`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |9|cpugen:emeraldrapids|48|976|a5000|4|24|cpugen:emeraldrapids, cpumodel:6542Y, gpumodel:a5000, common:yes|
    |4|cpugen:sapphirerapids|48|1953|h200|8|140|cpugen:sapphirerapids, cpumodel:6542Y, gpumodel:h200, common:yes|
    |9|cpugen:sapphirerapids|48|976|l40s|4|48|cpugen:sapphirerapids, cpumodel:6442Y, gpumodel:l40s, common:yes|
    |10|cpugen:sapphirerapids|48|976|a40|4|48|cpugen:sapphirerapids, cpumodel:6442Y, gpumodel:a40, common:yes|
    |15|cpugen:sapphirerapids|48|976|h100|4|80|cpugen:sapphirerapids, cpumodel:6442Y, gpumodel:h100, common:yes|

=== "gpu_devel"

    Use the gpu_devel partition to debug jobs that make use of GPUs, or to develop GPU-enabled code.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=UNLIMITED
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |1|cpugen:emeraldrapids|48|976|a5000|4|24|cpugen:emeraldrapids, cpumodel:6542Y, gpumodel:a5000, common:yes|
    |1|cpugen:sapphirerapids|48|1953|h200|8|140|cpugen:sapphirerapids, cpumodel:6542Y, gpumodel:h200, common:yes|
    |1|cpugen:sapphirerapids|48|976|l40s|4|48|cpugen:sapphirerapids, cpumodel:6442Y, gpumodel:l40s, common:yes|
    |1|cpugen:sapphirerapids|48|976|a40|4|48|cpugen:sapphirerapids, cpumodel:6442Y, gpumodel:a40, common:yes|
    |1|cpugen:sapphirerapids|48|976|h100|4|80|cpugen:sapphirerapids, cpumodel:6442Y, gpumodel:h100, common:yes|

=== "bigmem"

    Use the bigmem partition for jobs that have memory requirements other partitions can't handle.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem=UNLIMITED
    ```

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |4|cpugen:emeraldrapids|64|1953|cpugen:emeraldrapids, cpumodel:8562Y+, common:yes|
    |2|cpugen:emeraldrapids|64|3906|cpugen:emeraldrapids, cpumodel:8562Y+, common:yes|

