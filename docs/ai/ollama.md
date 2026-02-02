# Ollama

Ollama provides a local runtime for running large language models and is supported on YCRC as a software module.

On YCRC systems, Ollama is wrapped to make it safe to use on shared GPU nodes. The wrapper provides per-user, per-job isolation and prevents port collisions when multiple Ollama servers are launched on the same node.

This page assumes familiarity with:
- [Slurm job scheduling](../clusters-at-yale/job-scheduling/index.md)
- [Jobstats](../clusters-at-yale/job-scheduling/jobstats.md)

## Loading the module

Ollama is provided as a YCRC module and must be loaded inside a Slurm allocation on a compute node.

```bash
module avail ollama
module load ollama
```

## Intended usage

Ollama is appropriate for:

- interactive prompting  
- Jupyter Lab notebooks
- batch inference  
- Single Node workflows
- use as a backend for OpenWebUI  

Ollama is not intended for:

- Multi-node inference (not compatible)
- model training
- long-running shared services outside a job allocation  

## Interactive usage

It is recommended to start your research with interactive sessions and then once common bugs have been eliminated, to 
move to batch submissions where stronger resources are available.

By default, Slurm provisions GPU requests with available GPUs having the lowest vRAM. LLMs often require more vRAM 
than the smallest GPU available, so they won't run on the GPU Slurm provides by default.

For example, say your LLM needs 16 GB of vRAM and you request a single GPU. If the smallest available GPU in your 
partition has 11 GB (e.g., an rtx2080ti), Slurm may give you this GPU by default. This would cause your job to fail 
due to a lack of vRAM.

To see a better summary of resources available, see [here](resources.md)

In this case, you can specify GPUs with more vRAM using the `--constraint` flag. In the example below, you could 
specify rtx5000 or v100 GPUs, which have more vRAM.


```bash
#####interactive
salloc --partition gpu_devel --constraint="rtx5000|v100"

#####submission script
#SBATCH --constraint="rtx5000|v100"
```

Within an interactive allocation, models can be run directly from a terminal like so:

```bash
###request compute node with GPU (add --Constraint=GPUTYPES if needed)
salloc --partition=gpu_devel --cpus-per-task=1 --time=4:00:00 --mem=5G --gpus=1

###load ollama module if it isn't loaded
module load ollama

####launch server to access models.
ollama serve

#####hit enter to proceed for more input
###run model of interest, replace llama3.2:3b with model of interest
ollama run llama3.2:3b

###enter prompts
why is the sky blue?
```

If an Ollama server is not already running for the current job, one will be started automatically in the background.

## Batch usage

A typical batch workflow starts the Ollama server in the background, waits for initialization, and then submits 
inference requests.

```bash
#######launch the ollama server, the & tells it to run in the background, allowing the script to continue
module reset
module load ollama

ollama serve

######make slurm wait 10 seconds before advancing in the script, this gives the necessary time to launch the LLM server
######this time may need updating for larger models, llama 3.3:70b requires 60 seconds for example
sleep 10

######runs the LLM model 3.1 with the prompt, why is the sky blue and passes the response into a file called response.txt
ollama run llama3.1 why is the sky blue > response.txt
```

For Ollama, it is necessary to output the prompts response into a separate file because Slurm is unable to convert 
some of the symbols that are outputted in the traditional .out file from a batch submission.

## GPU usage

When GPUs are allocated, Ollama will use available GPUs on the node. If no usable NVIDIA GPU is detected, Ollama will fall back to CPU execution and emit a warning.

GPU usage must be validated using Jobstats.

##Hands on Examples

The YCRC hosts a github repository for hands-on examples from the Ollama on HPC workshop provided by YCRC. You can
access the examples [here](exercises.md)

## YCRC module behavior

The YCRC Ollama module replaces the vendor-provided `ollama` binary with a wrapper that manages server lifecycle and networking behavior.

Key properties:

- one Ollama server per user, per job, per GPU set: Avoids issues with multiple users using Ollama on same node.  
- Provides method to cleanly close server
- Warns immediately if no GPU is present
- Prevents users from launching multiple servers in the same job
- Automatically stores server location for future instances of Ollama in same job


## Automatic port collision prevention

Due to the shared nature of YCRC Computing Systems, issues arised where multiple people would use Ollama on the same
GPU node, which would cause Ollama to error out and fail for any user on that node. The YCRC Ollama automatically 
detects a free port and assigns to the user when they run Ollama serve. That port is then exported as OLLAMA_HOST.

If a user wants to use a specific port, they can set the port value prior to ollama serve like so:

```bash
export OLLAMA_PORT=11434
```

If the requested port is already in use, a different free port will be selected automatically.

## Discovering the active Ollama server

The module provides helper commands to query the active server.

Print the active host and port:

    ollama-host

If no server is running for the current job, `NOT RUNNING` is returned.

## Stopping the server

To stop the background Ollama server associated with the current job:

    ollama-down

The server process is terminated cleanly when possible.

## Validation

After running inference:

- confirm GPU memory usage and utilization using Jobstats  
- confirm responses are produced as expected  

