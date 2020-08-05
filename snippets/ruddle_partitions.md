=== "general"

    Use the general partition for most batch jobs. This is the default if you don't specify one with `--partition`.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=7-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the general partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`30-00:00:00`|
    |Maximum CPUs per user|`300`|
    |Maximum memory per user|`1800G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |154|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, oldest|

=== "interactive"

    Use the interactive partition to jobs with which you need ongoing interaction. For example, exploratory analyses or debugging compilation.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the interactive partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`2-00:00:00`|
    |Maximum CPUs per user|`20`|
    |Maximum memory per user|`256G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |154|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, oldest|

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
    |Max job time limit|`7-00:00:00`|
    |Maximum CPUs per user|`32`|
    |Maximum memory per user|`1507G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |2|E7-4809_v3|32|1507|haswell, avx2, E7-4809_v3|

=== "scavenge"

    Use the scavenge partition to run preemptable jobs on more resources than normally allowed. For more information about scavenge, see the [Scavenge documentation](/clusters-at-yale/job-scheduling/scavenge).

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `srun` and `sbatch` options for this partition.

    ``` text
    --time=1-00:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --mem-per-cpu=5120
    ```

    **Job Limits**

    Jobs submitted to the scavenge partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Max job time limit|`7-00:00:00`|
    |Maximum CPUs per user|`300`|
    |Maximum memory per user|`1800G`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Nodes|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |2|E7-4809_v3|32|1507|haswell, avx2, E7-4809_v3|
    |154|E5-2660_v3|20|121|haswell, avx2, E5-2660_v3, oldest|

