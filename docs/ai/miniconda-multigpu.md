# Multi-GPU Usage in Miniconda Environments

This page documents supported and commonly used patterns for running GPU workloads across multiple GPUs using Conda-based environments.

It covers both:

- Single-node multi-GPU usage
- Multi-node multi-GPU usage

!!! Note
    Requesting multiple GPUs will not ensure your job runs faster or that your workflow will use all of the GPUs requested.
    If a job does not use the GPUs requested, it will be terminated by our resource monitoring tool, [Jobstats](../clusters-at-yale/job-scheduling/jobstats.md).

For additional Slurm commands to request resources outside of what is shown below, please see our [Slurm job scheduling](../clusters-at-yale/job-scheduling/index.md) documentation.

The YCRC recommends using Miniconda to create your AI/ML environments, which is available as a [module](../applications/modules.md).

## Single-node vs Multi-node usage

| Pattern | Description | Recommendation | Reason |
|-------|-------------|----------------|-----------------------------------|
| Single-node multi-GPU | One node, multiple GPUs | Preferred whenever possible | Much simpler to implement |
| Multi-node multi-GPU | Multiple nodes, multiple GPUs | Advanced use only | Potential complications with data communication without proper setup = slower jobs |

Single-node multi-GPU should always be attempted before multi-node execution.

## Environment setup - single node

All environments must be created using the Miniconda module on a compute node. Miniconda will fail if you are on the login node.

For single node workflows, either [Tensorflow](https://docs.ycrc.yale.edu/clusters-at-yale/guides/tensorflow/) or [Pytorch](https://docs.ycrc.yale.edu/clusters-at-yale/guides/pytorch/) is recommended.

Please confirm that Tensorflow/Pytorch is installed correctly by having it detect GPUs. If you have issues detecting a GPU, please [contact us](https://docs.ycrc.yale.edu/#get-help).

## Example: single-node multi-GPU training job (Slurm + torchrun)

This example requests one node with 2 GPUs and launches one process per GPU using `torchrun`.

!!! Note
    You may not need all the variables declared within the torchrun portion of the below script, or need different variables. Modify as necessary.

```bash
#!/bin/bash
#SBATCH --job-name=single_node
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=2
#SBATCH --cpus-per-task=2
#SBATCH --mem=10G
#SBATCH --time=10:00

module load miniconda
conda activate YOUR_ENV

###prevents multithreading which will slow down job
export OMP_NUM_THREADS=1

#batch size
bs=16
#number of training cycles
epoch=1
#learning rate
lr=3e-5
#input folder
inputdir="/path/to/my/input"
#gradient accumalation steps
gr=2
#training script
script="/path/to/my/script.py"

torchrun \
  --nproc_per_node=$SLURM_GPUS_ON_NODE \
  ${script} \
  --input_folder_path ${inputdir} \
  --learning_rate ${lr} \
  --batch_size ${bs} \
  --num_train_epochs ${epoch} \
  --gradient_accumulation_steps ${gr}
```

## Environment setup - multi node

All environments must be created using the Miniconda module on a compute node. Miniconda will fail if you are on the login node.

For multi-node workflows, the YCRC recommends [Pytorch](https://docs.ycrc.yale.edu/clusters-at-yale/guides/pytorch/). 
This is to take advantage of torchrun for job launching, however, Tensorflow is also a possible method.

Please confirm that Tensorflow/Pytorch is installed correctly by having it detect GPUs. If you have issues detecting a GPU, please [contact us](https://docs.ycrc.yale.edu/#get-help).


## Example: Multi-node multi-GPU training job (Slurm + torchrun)

This example requests two nodes with 2 GPUs and launches one process per GPU using `torchrun`.

!!! Note
    You may not need all the variables declared within the torchrun portion of the below script, or need different variables. Modify as necessary.

```bash
#!/bin/bash
#SBATCH --job-name=ddp_multi_node
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=2
#SBATCH --cpus-per-task=2
#SBATCH --mem=10G
#SBATCH --time=20:00

module load miniconda
conda activate MY_PYTORCH_ENV

###tells job what node is the master node which is necessary for data communication between nodes
export MASTER_ADDR=$(scontrol show hostnames "$SLURM_NODELIST" | head -n 1)
##stores master node as variable for use in the torchrun execution
export MASTER_PORT=29500

export OMP_NUM_THREADS=1

echo "MASTER_ADDR=${MASTER_ADDR}"
echo "Launching multi-node distributed training"

#batch size
bs=16
#number of training cycles
epoch=1
#learning rate
lr=3e-5
#input folder
inputdir="/path/to/my/input"
#gradient accumalation steps
gr=2
#training script
script="/path/to/my/script.py"

torchrun \
  --nnodes=2 \
  --nproc_per_node=${SLURM_GPUS_ON_NODE} \
  --node_rank=${SLURM_NODEID} \
  --master_addr=${MASTER_ADDR} \
  --master_port=${MASTER_PORT} \
  ${script} \
  --input_folder_path ${INPUT_FOLDER} \
  --learning_rate ${lr} \
  --per_device_batch_size ${bs} \
  --num_train_epochs ${epoch} \
  --gradient_accumulation_steps ${gr}
```
