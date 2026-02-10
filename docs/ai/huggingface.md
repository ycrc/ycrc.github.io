# Hugging Face

Hugging Face can be used on YCRC systems to run large language models through Python scripts or Jupyter notebooks. This approach provides explicit control over model loading, precision, and GPU placement and is appropriate for scripted workflows and exploratory analysis.


## Intended usage

Hugging Face is appropriate for:

- Scripted inference workflows
- Jupyter notebook
- Workflows requiring explicit control over model loading and precision
- Multi-GPU inference on a single node
- Retrieval Augmented Generation
- Fine Tuning

##Ollama vs Hugging Face

The YCRC supports all AI/ML workflows. However, we generally recommend [Ollama](ollama.md) because it is simpler to use
as a beginner. Hugging Face provides significantly more flexibility in model development and control and is suitable
for high level users. Hugging Face also provides access to more open-source models than Ollama. 

Ultimately, there is no wrong choice. If you run into any issues with your workflows, please [contact us](https://docs.ycrc.yale.edu/#get-help).

## Environment setup

Hugging Face must be installed inside a Miniconda environment. Environments must be created on a compute node.

```bash
salloc --partition=devel --cpus-per-task=2 --time=1:00:00 --mem=32G
module load miniconda
conda create --name huggingface python=3.11 transformers accelerate tokenizers datasets notebook
conda activate huggingface
```

[PyTorch](../clusters-at-yale/guides/pytorch.md) must be installed separately. Make sure to install a version with CUDA.

To make the environment available in Open OnDemand Jupyter:

```bash
module reset
ycrc_conda_env.sh update
```

## Interactive usage

Interactive Hugging Face workflows are best run using the Jupyter Notebook application in
[Open OnDemand](../clusters-at-yale/access/ood.md).

Scripts may also be executed directly from the command line within an interactive allocation.

## GPU selection and constraints

By default, Slurm assigns the lowest-memory GPU available in the selected partition. Many LLMs require more vRAM than the smallest available GPU.

If a model requires more GPU memory, specify a GPU constraint explicitly.

Interactive example of requesting a specific GPU:

```bash
salloc --partition=gpu_devel --constraint="rtx5000|v100"
```

Batch script example of requesting a specific GPU:

```bash
#SBATCH --constraint="rtx5000|v100"
```

## Model loading and precision

Automatic dtype selection during model loading is discouraged. Using automatic dtype selection can result in:

- Inefficient memory usage
- Unexpected precision choices
- Failure to load on GPUs with limited vRAM

Recommended practice:

- Explicitly specify model precision (fp16,int8, etc)
- Validate memory usage on the target GPU type

Precision selection should be guided by the GPU memory available and the model size.

## Multi-GPU usage on a single node

Requesting multiple GPUs does not automatically distribute a model across devices. Multi-GPU usage requires explicit configuration in user code.

When using multiple GPUs on a single node:

- Ensure all GPUs are allocated in the Slurm request
- Configure the framework to share or distribute the model
- Validate that all GPUs are being used

Please see [here](miniconda-multigpu.md) for instructions on multi-GPU jobs.

After execution, confirm GPU memory usage and utilization using
[Jobstats](gpu-jobstats.md).

**Note:** Failing to use all requested GPUs will result in cancellation of your jobs by Jobstats to ensure resource availability
for other workflows.

## Batch usage

Once a workflow is validated interactively, it can be converted to a batch job.

For notebook-based workflows, Jupyter notebooks can be executed non-interactively using `papermill`. Guidance is available under
[Command-Line Execution of Jupyter Notebooks](/clusters-at-yale/access/ood-jupyter).

For script-based workflows, submit the script directly using a Slurm batch script.

The YCRC does not provide examples for HuggingFace workflows as they change based on the model desired by the user.

## Validation

After running a Hugging Face job:

- Confirm the job requested the expected GPU resources
- Inspect GPU memory usage and utilization using Jobstats
- Confirm the number of active GPUs matches the request
- Verify that the model loaded at the intended precision
