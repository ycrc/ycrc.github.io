# Request Compute Resources

## Request Cores and Nodes

When [running jobs with Slurm](/clusters-at-yale/job-scheduling/), you must be explicit about requesting CPU cores and nodes. See our page on [monitoring usage](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/jobstats/) for tips on verifying your jobs are using the resources you expect. The three options `--nodes` or `-N`, `--ntasks` or `-n`, and `--cpus-per-task` or `-c` can be a bit confusing at first but are necessary to understand for applications that use more than one CPU.

!!! Tip
    If your application references threads or cores but makes no mention of MPI, only use `--cpus-per-task` to request CPUs. You cannot request more cores than there are on a single compute node where your job runs.

### Multi-thread, Multi-process, and MPI

The majority of applications in the world were written to use one or more cores on a single computer.  Most can only use one core, and do not benefit from being given more cores. The best way to speed these applications up is to run many separate jobs at once, using [job arrays](/clusters-at-yale/job-scheduling/dsq/). 

If an application is able to use multiple cores, it usually achieves this by either spawning threads and sharing memory (multi-threaded) or starting entire new processes (multi-process). Some applications are written to use the Message Passing Interface (MPI) standard to run across many compute nodes. This allows such applications to scale computation in a way not limited by the number of cores on a single node. MPI translates what Slurm calls tasks to separate workers or processes. Because each of these processes can communicate across compute nodes, Slurm does not constrain them to the same node by default. Though tasks can be distributed across nodes, Slurm will not split the CPUs allocated to individual tasks. For this reason a single task that has multiple CPUs allocated will always be on a single node. In some cases using `--ntasks=4` (or `-n 4`) and `--cpus-per-task=4` (or `-c 4`) achieves the same job allocation by luck, but you should only use `--cpus-per-task` when using non-MPI applications to guarantee that the CPUs you expect your program to use are all accessible.

Some MPI programs are also multi-threaded, so each process can use multiple CPUs. Only these applications can use `--ntasks` *and* `--cpus-per-task` to run faster.

#### MPI Applications

For more control over how Slurm lays out your job, you can add the `--nodes` and `--ntasks-per-node` flags. `--nodes` specifies how many nodes to allocate to your job. Slurm will allocate your requested number of cores to a minimal number of nodes on the cluster, so it is likely if you request a small number of tasks that they will all be allocated on the same node. However, to ensure they are on the same node, set `--nodes=1` (obviously this is contingent on the number of CPUs on your cluster's nodes and requesting too many may result in a job that will never run). Conversely, if you would like to ensure a specific layout, such as one task per node for memory, I/O or other reasons, you can also set `--ntasks-per-node=1`. Note that the following must be true:

``` text
ntasks-per-node * nodes >= ntasks
```

#### Hybrid (MPI+OpenMP) Applications

For the most predictable performance for hybrid applications, you will need to use all three of the `--ntasks`, `--cpus-per-task`, and `--nodes` flags, where `--ntasks` equals the number of MPI tasks, `--cpus-per-task` equals the number of `OMP_NUM_THREADS` and `--nodes` is the number of nodes required to fit `--ntasks * --cpus-per-task`.

## Request Memory (RAM)

Slurm strictly enforces the memory your job can use. If you request 5GiB of memory for your job and the total used by all processes you launch hits that limit, some of your processes may die and [you will get errors](/clusters-at-yale/job-scheduling/common-job-failures/#running-out-of-memory). Make sure you either request the right amount of memory per core on each node in your job with `--mem-per-cpu` or memory per node in your job with `--mem`. You can request more memory than you think you might need for an example job, then [make note of its actual usage](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/jobstats/) to better tune future requests for similar jobs.

## Request GPUs

Some of our clusters have nodes that contain GPU co-processors. Please refer to the [individual cluster pages](/clusters) regarding node configurations that include GPUs. There are several `salloc`/`sbatch` options that allow you to request GPUs and specify your job layout relative to the GPUs requested.

|Long Option<img width=200/>|Short Option|Description                                                                                                                  |
|---------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------|
| `--cpus-per-gpu`          |            |  Use instead of `--cpus-per-task` to specify number of CPUs per allocated GPU.                                               |
| `--gpus`                  | `-G`       |  Specify the _total number_ of GPUs required for the job either with number or type:number.                                  |
| `--gpus-per-node`         |            |  Specify the number of GPUs _per node_, either with number or type:number. New option similar to `--gres=gpu`.               |
| `--gpus-per-task`         |            |  Specify the number of GPUs _per task_, either with number or type:number.                                                   |
| `--mem-per-gpu`<sup>*</sup>|            |  Request system memory that scales per GPU. The `--mem`, `--mem-per-cpu` and `--mem-per-gpu` options are mutually exclusive |
| `--constraint`           | `-C`       |  Request a selection of GPU types (separate types with `|`). This option requires the `--gpus` option for GPU selection.| 


In order for your job to be able to access gpus, you must submit your job to a partition that contains nodes with GPUs and request them - **the default GPU request for jobs is to not request any**. The Slurm options `--mem`, `--mem-per-gpu` and `--mem-per-cpu` do not request memory on GPUs, sometimes called vRAM. Instead you are allocated the GPU(s) requested and all attached GPU memory for your jobs. Memory accessible on GPUs is limited by their model, and is also listed on each cluster page. 

### Request Specific GPU Types

If your job can only run on a subset of the GPU types available in the partition, you can request one or more specific types of GPUs. 

To request a specific type of GPU, use `type:number` notation. For example, to request an NVIDIA RTX 5000 Ada GPU:

``` text
sbatch --cpus-per-gpu=2 --gpus=rtx_5000_ada:1 --time=6:00:00 --partition gpu my_gpu_job.sh
```

To submit your job to a number of GPU options (such as NVIDIA L40S, A40 or RTX 5000 Ada), use a combination of the constraint flag (`--constraint`) and the `--gpus` flag (with just a number). For the [constraint flag](/clusters-at-yale/job-scheduling/resource-requests/#features-and-constraints), separate the different GPU type features with the pipe character (`|`). Your job will then start on a node with any of those GPU types. This is not guaranteed to work as expected if you are requesting multiple nodes. GPU type names can be found in the partition tables on each respective cluster page.

``` text
sbatch --constraint="gpu:l40s|gpu:a40|gpu:rtx_5000_ada" --gpus=1 --time=6:00:00 --partition gpu my_gpu_job.sh
```


!!! tip
    As with requesting multiple cores or multiple nodes, we strongly recommend that you test your jobs using the `gpu_devel` partition to make sure they can well utilize multiple GPUs before requesting them; allocating more GPUs does not speed up code that can only use one at a time. Here is an example interactive request that would allocate two GPUs and four CPUs for thirty minutes:
    
    ``` text
    salloc --cpus-per-gpu=2 --gpus=2 --time=30:00 --partition gpu_devel
    ```

For more documentation on using GPUs on our clusters, please see [GPUs and CUDA](/clusters-at-yale/guides/gpus-cuda).

## Features and Constraints

You may want to run programs that require specific hardware. To ensure your job runs on specific types of nodes, use the `--constraint` flag.

You can use the processor codename feature (e.g. `cpugen:emeraldrapids`) or processor model number feature (e.g. `cpumodel:8268`) to limit your job to specific node types. See the individual cluster pages for the exact tags for the different node features. Multiple requirements ("AND") are separated by a comma (`,`) and multiple options ("OR") should be separated by the pipe character (`|`).

``` bash

# run on a node with an Intel Emerald Rapids codenamed CPU
sbatch --constraint=cpugen:emeraldrapids submit.sh

# only run on nodes with Intel Cascadelake 8268 CPUs
sbatch --constraint=cpumodel:8268 submit.sh

```

!!!tip
    Use the command `scontrol show node <hostname>`, replacing `<hostname>` with the node's name you're interested in, to see more information about the node including its features.
