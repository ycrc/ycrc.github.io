# Request Compute Resources

## Request Cores and Nodes

Slurm is very explicit in how one requests cores and nodes. While extremely powerful, the three flags, `--nodes`, `--ntasks`, and `--cpus-per-task` can be a bit confusing at first. We attempt to disambiguate them below.

### `--ntasks` vs `--cpus-per-task`

The term "task" in this context can be thought of as a "process". Therefore, a multi-process program (e.g. MPI) is comprised of multiple tasks. And a multi-threaded program is comprised of a single task, which can in turn use multiple CPUs. In Slurm, tasks are requested with the `--ntasks` flag. CPUs, for the multithreaded programs, are requested with the `--cpus-per-task` flag.

### 1\. Multi-threaded & multi-process programs

To request CPUs for your multi-threaded program, use the `--cpus-per-task` flag. Individual tasks cannot be split across multiple compute nodes, so requesting a number of CPUs with `--cpus-per-task` flag will always result in all your CPUs allocated on the same compute node.

### 2\. MPI programs

In Slurm, the `--ntasks` flag specifies the number of MPI tasks created for your job. Note that, even within the same job, multiple tasks do not necessarily run on a single node. Therefore, requesting the same number of CPUs as above, but with the `--ntasks` flag, could result in those CPUs being allocated on several, distinct compute nodes.

For many users, differentiating between `--ntasks` and `--cpus-per-task` is sufficient. However, for more control over how Slurm lays out your job, you can add the `--nodes` and `--ntasks-per-node` flags. `--nodes` specifies how many nodes to allocate to your job. Slurm will allocate your requested number of cores to a minimal number of nodes on the cluster, so it is extremely likely if you request a small number of tasks that they will all be allocated on the same node. However, to ensure they are on the same node, set `--nodes=1` (obviously this is contingent on the number of CPUs on your cluster's nodes and requesting too many may result in a job that will never run). Conversely, if you would like to ensure a specific layout, such as one task per node for memory, I/O or other reasons, you can also set `--ntasks-per-node=1`. Note that the following must be true:

```
ntasks-per-node * nodes >= ntasks
```

### 3\. Hybrid (MPI+OpenMP) programs

For the most predictable performance for hybrid codes, you will need to use all three of the `--ntasks`, `--cpus-per-task`, and `--nodes` flags, where `--ntasks` equals the number of MPI tasks, `--cpus-per-task` equals the number of OMP_NUM_THREADS and `--nodes` is the number of nodes required to fit `--ntasks * --cpus-per-task`.

## Request GPUs

Some of our clusters have nodes that contain GPU co-processors. Please refer to the cluster-specific documentation regarding the node configurations that include GPUs. In order for your job to be able to access gpus, you must request them as a Slurm "Generic Resource" or gres. You specify the gres configuration per-node for a job with the `--gres` flag and a number of GPUs. If you are agnostic about the kind of GPU your job gets, `--gres=gpu:1` will allocate one of any kind of GPU per node. To specifically request, for example, a P100 for each node in your job you would use the flag `--gres=gpu:p100:1`. Some codes require double-precision capable GPUs--if so, see the next section for using "features" to request any node with compatible GPUs.

!!!tip
    As with requesting multiple cores or multiple nodes, we strongly recommend that you test your jobs using the `gpu_devel` partition to make sure they can well utilize multiple GPUs before requesting them; allocating more GPUs does not magically speed up code that can only use one at a time.

For more documentation on using GPUs on our clusters, please see [Python Deep Learning with GPUs](/clusters-at-yale/guides/deep-learning-gpus) and [GPUs and CUDA](/clusters-at-yale/guides/gpus-cuda).

## Features and Constraints

You may want to run programs that require specific hardware. To ensure your job runs on specific types of nodes, use the `--constraint` flag.

You can use the processor codename (e.g. `haswell`) or processor type (e.g. `E5-2660_v3`) to limit your job to specific node types. You can also specify an instruction set (e.g. `avx2`) to require that no matter what CPU your job runs on, it must understand at least these instructions. See the individual cluster pages for the exact tags for the different node types.

``` bash

# run on a node with a haswell codenamed CPU (e.g. a E5-2660 v3)
sbatch --constraint=haswell submit.sh

# only run on nodes with E5-2660 v4 CPUs
sbatch --constraint=E5-2660_v4 submit.sh

# run on any node that understands avx2 instructions
# Your job may also launch on an avx512 node
sbatch --constraint=avx2 submit.sh

```

We also have keyword features to help you constrain your jobs to certain categories of nodes.

- `oldest`: the oldest generation of node on the cluster. Use this constraint when compiling code if you wish to ensure it can run on any standard node on the cluster.
- `nogpu`: nodes without GPUs.
- `standard`: nodes without GPUs or extra memory. Useful for protecting special nodes in a private partition for jobs that can use the extra capabilities.
- `singleprecision`: nodes with single-precision only capable GPUs (e.g. GTX 1080s, RTX 2080s).
- `doubleprecision`: nodes with double-precision capable GPUs (e.g. K80s, P100s and V100s).

!!!tip
    Use the command `scontrol show node <hostname>`, replacing `<hostname>` with the node's name you're interested in, to see more information about the node including its features.