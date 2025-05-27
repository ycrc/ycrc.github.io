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
    |Maximum CPUs per user|`32`|
    |Maximum submitted jobs per user|`2`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |2|cpugen:emeraldrapids|64|487|cpugen:emeraldrapids, cpumodel:8562Y+, common:yes|

=== "gpu"

    Use the gpu partition for jobs that make use of GPUs. You must [request GPUs explicitly](/clusters-at-yale/job-scheduling/resource-requests/#request-gpus) with the `--gpus` option in order to use them. For example, `--gpus=rtx5000ada:2` would request 2 NVIDIA RTX 5000 Ada GPUs per node.

    !!! alert "H200 GPUs Coming Soon!"
        Bouchet will soon have 80 H200 GPU cards available. These cards have 141G of VRAM and each node has 8 cards. 
        Additionally, the nodes feature dedicated Infiniband links for each GPU to enable high-speed GPU-to-GPU 
        communication. 

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
    |Maximum GPUs per user|`16`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.
    
    **Note:** H200 compute nodes are coming soon. 

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |10|cpugen:emeraldrapids|48|479|rtx5000ada|4|32|cpugen:emeraldrapids, cpumodel:6542Y, common:yes, gpu:rtx5000ada|
    |9|cpugen:emeraldrapids|48|2000|h200|8|141|cpugen:emeraldrapids, cpumodel:6542Y, common:yes, gpu:h200|
    

=== "gpu_devel"

    Use the gpu_devel partition to debug jobs that make use of GPUs, or to develop GPU-enabled code.

    !!! alert "H200 GPUs Coming Soon!"
        Bouchet will soon have 80 H200 GPU cards available. These cards have 141G of VRAM and each node has 8 cards. 
        Additionally, the nodes feature dedicated Infiniband links for each GPU to enable high-speed GPU-to-GPU 
        communication. 
    
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
    |Maximum GPUs per user|`4`|
    |Maximum submitted jobs per user|`2`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.
    
    **Note:** H200 compute nodes are coming soon. 
    
    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|GPU Type|GPUs/Node|vRAM/GPU (GB)|Node Features|
    |---|---|---|---|---|---|---|---|
    |2|cpugen:emeraldrapids|48|479|rtx5000ada|4|32|cpugen:emeraldrapids, cpumodel:6542Y, common:yes, gpu:rtx5000ada|
    |1|cpugen:emeraldrapids|48|2000|h200|8|141|cpugen:emeraldrapids, cpumodel:6542Y, common:yes, gpu:h200|

=== "mpi"

    Use the mpi partition for tightly-coupled parallel programs that make efficient use of multiple nodes. See our [MPI documentation](/clusters-at-yale/job-scheduling/mpi) if your workload fits this description.

    **Request Defaults**

    Unless specified, your jobs will run with the following options to `salloc` and `sbatch` options for this partition.

    ``` text
    --time=01:00:00 --nodes=1 --ntasks=1 --cpus-per-task=1 --exclusive --mem=498688
    ```

    **Job Limits**

    Jobs submitted to the mpi partition are subject to the following limits:

    |Limit|Value|
    |---|---|
    |Maximum job time limit|`7-00:00:00`|
    |Maximum nodes per group|`32`|
    |Maximum nodes per user|`32`|

    **Available Compute Nodes**

    Requests for `--cpus-per-task` and `--mem` can't exceed what is available on a single compute node.

    |Count|CPU Type|CPUs/Node|Memory/Node (GiB)|Node Features|
    |---|---|---|---|---|
    |58|cpugen:emeraldrapids|64|487|cpugen:emeraldrapids, cpumodel:8562Y+, common:yes|

