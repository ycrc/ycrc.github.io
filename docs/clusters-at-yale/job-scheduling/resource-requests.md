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

Some of our clusters have nodes that contain GPU co-processors. Please refer to the cluster-specifc documentation regarding the node configurations that include gpus. In order for your job to be able to access gpus, you must request them as a slurm "Generic Resource" or gres. You spcify the gres configuration per-node for a job with the `--gres` flag, optionally a type of resource, and a number of gpus. For example, to request one nvidia p100 for each node in your job, you would use the flag `--gres=gpu:p100:1`. In cases where there are multiple gpus on a node, it is often a good idea to also specify the `--gres-flags=enforce-binding` flag, which tells slurm to force CPU(s) your job is allocated to share a PCIe Host Bridge with the GPU(s). Depending on your application, this can lead to improved performance, especially in transferring data to and from the GPU.

For more documentation on using GPUs on our clusters, please see [Python Deep Learning with GPUs](/clusters-at-yale/applications/guides/deep-learning-gpus) and [GPUs and CUDA](/clusters-at-yale/applications/guides/gpus-cuda).

## Features and Constraints

You may want to run programs that require more specific hardware than slurm may be willing to allocate to your job. To ensure your job runs on specific types of nodes, use the `--constraint` flag. You can use the processor type (e.g. `E5-2660_v3`) or processor codename (e.g. `haswell`) to limit your job to specific node types. You can also specify an instruction set (e.g. `avx`) to require that no matter what CPU your job runs on, it must understand at least these instructions. See the individual cluster pages for the exact tags for the different node types.

```
# run on a node with a haswell codenamed CPU (e.g. a E5-2660 v3)
sbatch --constraint=haswell submit.sh

# only run on nodes with E5-2660 v4 CPUs
sbatch --constraint=E5-2660_v4 submit.sh

# run on any node that understands avx instructions
# Your job could also run on an avx2 node
sbatch --constraint=avx submit.sh

```

!!!tip
    Use the command `scontrol show node <hostname>`, replacing `<hostname>` with the node's name you're interested in, to see more information about the node including its features.