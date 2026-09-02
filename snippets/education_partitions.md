=== "education"

    Use the education partition for CPU-only jobs.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the education partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`1-00:00:00`|
    |Maximum CPUs per user|`16`|
    |Maximum memory per user|`200G`|
    |Maximum running jobs per user|`4`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |1|cpugen:turin|192|1487|cpugen:turin, cpumodel:9655, common:yes|
    |4|cpugen:emeraldrapids|64|990|cpugen:emeraldrapids, cpumodel:8562Y+, common:yes|
    |2|cpugen:cascadelake|48|368|cpugen:cascadelake, cpumodel:8268, common:yes|

=== "education_gpu"

    Use the education_gpu partition for jobs that make use of GPUs. You must [request GPUs explicitly](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) with the `--gpus` option in order to use them.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    !!! warning "GPU jobs need GPUs!"
        Jobs submitted to this partition  do not request a GPU by default. You must request one with the [`--gpus`](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) option.
    **Job Limits**

    Jobs submitted to the education_gpu partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`1-00:00:00`|
    |Maximum GPUs per user|`2`|
    |Maximum submitted jobs per user|`1`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |3|cpugen:emeraldrapids|48|479|rtx_5000_ada|4|32|cpugen:emeraldrapids, cpumodel:6542Y, common:yes, gpu:rtx_5000_ada|
    |1|cpugen:sapphirerapids|48|976|a40|4|48|cpugen:sapphirerapids, cpumodel:6442Y, common:yes, gpu:a40|

