# vLLM

[vLLM](https://docs.vllm.ai) is a high-throughput inference engine for large language models. It runs Hugging Face models on GPUs and can be used in two ways:

- **Offline batch inference:** a Python script loads the model and processes a list of prompts. This is the most efficient way to run a large number of prompts.
- **OpenAI-compatible server:** `vllm serve` starts an HTTP API that works with the `openai` Python package, `curl`, [Open WebUI](open-webui.md), and other tools that speak the OpenAI API.

This page assumes familiarity with:

- [Slurm job scheduling](../clusters-at-yale/job-scheduling/index.md)
- [Conda environments](../clusters-at-yale/guides/conda.md)
- [Jobstats](gpu-jobstats.md)

The examples on this page are for Bouchet.

## Intended Usage

vLLM is appropriate for:

- Running many prompts through a model (classification, extraction, summarization, synthetic data)
- Serving a model to your own scripts, notebooks, or Open WebUI during a job
- Models that need several GPUs on one node
- Any model architecture vLLM supports, directly from Hugging Face

vLLM is not intended for:

- Long-running services that outlive a Slurm job
- Model training or fine-tuning
- CPU-only nodes

## vLLM, Ollama, and Hugging Face

| | [Ollama](ollama.md) | [Hugging Face Transformers](huggingface.md) | vLLM |
|---|---|---|---|
| Best for | Getting started, interactive chat | Custom code, fine-tuning, model internals | Fast inference over many prompts, serving an API |
| Models | Ollama library (quantized GGUF) | Hugging Face | Hugging Face |
| Throughput | Moderate | Low to moderate | High |
| Multi-GPU | Limited | Manual | Built in (`--tensor-parallel-size`) |

If you are new to LLMs, start with Ollama. Move to vLLM when you need to process large numbers of prompts or want more control over how a model is served.

## Install vLLM

vLLM installs from PyPI into a Conda environment. Create the environment on a compute node:

```bash
salloc --partition=devel --cpus-per-task=4 --mem=16G --time=1:00:00

module load miniconda
conda create --name vllm python=3.12 uv
conda activate vllm
uv pip install vllm
```

The installation is about 10G and includes its own copy of PyTorch and the CUDA libraries, so you don't need to install PyTorch separately.

vLLM compiles some GPU kernels the first time it uses them, which requires the CUDA compiler. Every time you use vLLM, load the CUDA module **after** activating the environment:

```bash
module load miniconda
conda activate vllm
module load CUDA/12.9.1
```

Without the CUDA module, vLLM fails when generating its first response with `Could not find nvcc`.

To add packages for your own code, such as `openai` or `pandas`, install them into the same environment with `uv pip install`.

## Download a Model

There is currently no shared copy of models on the cluster, so download the models you need into your own storage.

Model weights are large (often tens to hundreds of gigabytes), and your home directory has a 125G quota. Store models in your project directory instead; run `mydirectories` to find its path. Set `HF_HOME` so that Hugging Face downloads and caches go there, replacing the example path with your own, and add the line to your `~/.bashrc` so it applies to every job:

```bash
export HF_HOME=/nfs/roberts/project/pi_abc123/netid/huggingface
```

Download a model with the `hf` command, which is installed with vLLM:

```bash
module load miniconda
conda activate vllm
hf download Qwen/Qwen3-8B
```

You can then refer to the model by its Hugging Face name (`Qwen/Qwen3-8B`) and vLLM finds it in `HF_HOME`. Alternatively, download to a specific directory with `--local-dir` and give vLLM that path:

```bash
hf download Qwen/Qwen3-8B --local-dir /nfs/roberts/project/pi_abc123/netid/models/Qwen3-8B
```

Some models, such as Llama and Gemma, are *gated*: you must accept the license on the model's Hugging Face page and log in with an [access token](https://huggingface.co/settings/tokens) before downloading:

```bash
hf auth login
```

Download models in an interactive job or a batch job on the `day` partition, not on a login node. Large downloads can take an hour or more.

## Choose GPUs

A model needs enough GPU memory for its weights plus a *KV cache*, which holds the prompts and responses being processed. A larger KV cache allows longer prompts and more requests at the same time.

Weight size depends on the number of parameters and the precision of the checkpoint:

| Precision | Memory per billion parameters | Example: 8B model | Example: 70B model |
|---|---|---|---|
| BF16 / FP16 | 2G | 16G | 140G |
| FP8 | 1G | 8G | 70G |
| 4-bit (AWQ, GPTQ) | about 0.5G | about 5G | about 35G |

Plan for weights to use no more than about 70% of the total GPU memory you request, leaving the rest for the KV cache. The checkpoint size listed under **Files and versions** on the Hugging Face model page is a good estimate of the weight size.

Bouchet GPUs available for vLLM:

| GPU | Memory | Partitions | FP8 support |
|---|---|---|---|
| `a5000` | 24G | `gpu` | No |
| `rtx_5000_ada` | 32G | `gpu`, `gpu_devel` | Yes |
| `a40` | 48G | `gpu`, `gpu_devel` | No |
| `l40s` | 48G | `gpu` | Yes |
| `rtx_pro_6000_blackwell` | 96G | `gpu_rtx6000`, `gpu_devel` | Yes |
| `h100` | 80G | `gpu_h100` | Yes |
| `h200` | 141G | `gpu_h200`, `gpu_devel` | Yes |
| `b200` | 192G | `gpu_b200`, `gpu_devel` | Yes |

FP8 checkpoints load on A5000 and A40 GPUs but run more slowly there, because those GPUs have no FP8 hardware. See the [Bouchet partition list](../clusters/bouchet.md) for node counts and limits, and [LLMs and GPU Availability](resources.md) for general guidance.

Request a specific GPU type with `--gpus`:

```bash
salloc --partition=gpu_devel --gpus=rtx_5000_ada:1 --cpus-per-task=8 --mem=64G --time=2:00:00
```

Request at least as much CPU memory (`--mem`) as the size of the model weights. vLLM reads the weights into CPU memory while loading them onto the GPUs.

## Run Offline Batch Inference

For a fixed set of prompts, use vLLM directly from Python. vLLM schedules all prompts together and keeps the GPU busy, which is much faster than sending prompts one at a time.

Save the following as `batch_inference.py`:

```python
from vllm import LLM, SamplingParams

llm = LLM(model="Qwen/Qwen3-8B", max_model_len=16384)
params = SamplingParams(temperature=0.7, max_tokens=512)

prompts = [
    "Summarize the causes of the French Revolution in three sentences.",
    "Explain what a p-value is to a first-year student.",
    "List three common sources of error in a titration experiment.",
]
conversations = [[{"role": "user", "content": p}] for p in prompts]

outputs = llm.chat(conversations, params)
for prompt, output in zip(prompts, outputs):
    print("PROMPT:", prompt)
    print("RESPONSE:", output.outputs[0].text)
    print()
```

`llm.chat` applies the model's chat template to each conversation. Use `llm.generate` instead for raw text completion without a chat template.

Submit it as a batch job:

```bash
#!/bin/bash
#SBATCH --job-name=vllm-batch
#SBATCH --partition=gpu
#SBATCH --gpus=l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=4:00:00

module reset
module load miniconda
conda activate vllm
module load CUDA/12.9.1
export HF_HOME=/nfs/roberts/project/pi_abc123/netid/huggingface

python batch_inference.py > responses.txt
```

For real workloads, read prompts from a file and write results to a CSV or JSON Lines file, and pass all prompts to a single `llm.chat` call rather than calling it in a loop.

## Serve an OpenAI-Compatible API

`vllm serve` starts a server that implements the OpenAI chat completions API. Use it when your code already uses the OpenAI API, when you want to connect Open WebUI or another tool, or when you want to send requests from several programs.

### Start the Server

Compute nodes are shared, so other users on the same node can reach any port your server opens. Always protect your server with an API key, and pick a random port to avoid colliding with other users:

```bash
salloc --partition=gpu_devel --gpus=rtx_5000_ada:1 --cpus-per-task=8 --mem=64G --time=2:00:00

module reset
module load miniconda
conda activate vllm
module load CUDA/12.9.1
export HF_HOME=/nfs/roberts/project/pi_abc123/netid/huggingface

export VLLM_PORT=$(shuf -i 20000-29999 -n 1)
export VLLM_API_KEY=$(openssl rand -hex 16)
echo "Server: http://$(hostname -s):$VLLM_PORT/v1  API key: $VLLM_API_KEY"

vllm serve Qwen/Qwen3-8B \
    --served-model-name qwen3-8b \
    --host 0.0.0.0 \
    --port $VLLM_PORT \
    --max-model-len 16384
```

vLLM reads the API key from the `VLLM_API_KEY` environment variable and rejects requests without it. The server is ready when the log shows `Application startup complete`. Startup takes about two minutes for small models and 20 minutes or more for very large ones.

`--host 0.0.0.0` makes the server reachable from other nodes, which [Open WebUI](#connect-open-webui) needs. If you only send requests from the same job, you can use `--host 127.0.0.1` instead.

### Send Requests

From another terminal in the same job, or from a batch script, check that the server is up and send a request with `curl`:

```bash
curl http://localhost:$VLLM_PORT/v1/models -H "Authorization: Bearer $VLLM_API_KEY"

curl http://localhost:$VLLM_PORT/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $VLLM_API_KEY" \
    -d '{"model": "qwen3-8b", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}'
```

To attach a second terminal to a running interactive job, run `srun --jobid=12345678 --overlap --pty bash` on a login node, replacing `12345678` with your job ID.

From Python, use the `openai` package (`uv pip install openai`):

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url=f"http://localhost:{os.environ['VLLM_PORT']}/v1",
    api_key=os.environ["VLLM_API_KEY"],
)
response = client.chat.completions.create(
    model="qwen3-8b",
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
)
print(response.choices[0].message.content)
```

The `model` value must match `--served-model-name`. Without that option, use the name or path you passed to `vllm serve`.

### Run a Server in a Batch Job

To use the server from a script in a batch job, start it in the background, wait for it to become healthy, run your script, and then stop it. This keeps the GPU busy only while your script runs:

```bash
#!/bin/bash
#SBATCH --job-name=vllm-server
#SBATCH --partition=gpu
#SBATCH --gpus=l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=4:00:00

module reset
module load miniconda
conda activate vllm
module load CUDA/12.9.1
export HF_HOME=/nfs/roberts/project/pi_abc123/netid/huggingface

export VLLM_PORT=$(shuf -i 20000-29999 -n 1)
export VLLM_API_KEY=$(openssl rand -hex 16)

vllm serve Qwen/Qwen3-8B --served-model-name qwen3-8b \
    --host 127.0.0.1 --port $VLLM_PORT --max-model-len 16384 \
    > vllm-server-$SLURM_JOB_ID.log 2>&1 &
VLLM_PID=$!

# Wait for the server to start, and stop if it fails
until curl -sf http://localhost:$VLLM_PORT/health > /dev/null; do
    if ! kill -0 $VLLM_PID 2> /dev/null; then
        echo "vLLM server failed to start; see vllm-server-$SLURM_JOB_ID.log"
        exit 1
    fi
    sleep 10
done

python my_client_script.py

kill $VLLM_PID
```

Your script reads `VLLM_PORT` and `VLLM_API_KEY` from the environment as in the Python example above. Send requests concurrently (for example with a thread pool or `asyncio`) rather than one after another; vLLM processes many requests at once, so concurrent requests finish much faster.

### Connect Open WebUI

To chat with your model in [Open WebUI](open-webui.md), start the server with `--host 0.0.0.0` and add it as a connection under **Admin Panel** > **Settings** > **Connections**, as described in [Use your own models](open-webui.md#use-your-own-models):

- **URL:** `http://a1128u05n01:24137/v1` (your server's node name and port)
- **API key:** the value of `VLLM_API_KEY`

The connection works only while your vLLM job is running.

## Use Multiple GPUs

vLLM uses only one GPU unless you tell it otherwise. There are two ways to use several GPUs on one node:

- **Tensor parallelism** (`--tensor-parallel-size N`) splits one copy of the model across N GPUs. Use it when the model does not fit on one GPU.
- **Data parallelism** (`--data-parallel-size N`) runs N independent copies of the model, one per GPU. Use it when the model fits on one GPU and you want more throughput.

The product of the two must equal the number of GPUs you request. For example, a 70B model in BF16 (about 140G of weights) on four H100 GPUs:

```bash
#SBATCH --partition=gpu_h100
#SBATCH --gpus=h100:4
#SBATCH --cpus-per-task=16
#SBATCH --mem=200G

vllm serve meta-llama/Llama-3.3-70B-Instruct --tensor-parallel-size 4 --max-model-len 32768
```

In offline Python, pass the same settings to `LLM`, for example `LLM(model=..., tensor_parallel_size=4)`.

Tensor parallelism sizes must evenly divide the model's number of attention heads; 1, 2, 4, and 8 work for most models. After the job starts, confirm with [Jobstats](gpu-jobstats.md) that every requested GPU is in use.

## Useful Options

These options apply to `vllm serve`. In Python, pass them to `LLM()` with underscores instead of dashes (for example `max_model_len=16384`).

| Option | Purpose |
|---|---|
| `--max-model-len 16384` | Maximum prompt plus response length in tokens. Many models default to 128K tokens or more, which may not fit in GPU memory. Set this to what your workload needs. |
| `--gpu-memory-utilization 0.9` | Fraction of each GPU's memory vLLM may use (default 0.92). vLLM reserves this memory at startup, so Jobstats shows high GPU memory use even when the server is idle. |
| `--tensor-parallel-size 4` | Split the model across 4 GPUs. See [Use Multiple GPUs](#use-multiple-gpus). |
| `--data-parallel-size 4` | Run 4 copies of the model, one per GPU. |
| `--served-model-name my-model` | Name clients use in the `model` field of requests. |
| `--kv-cache-dtype fp8` | Store the KV cache in FP8, which roughly doubles the number of tokens that fit. Requires a GPU with FP8 support. |
| `--quantization fp8` | Quantize a BF16 model to FP8 while loading it, halving weight memory. Prefer an official FP8 checkpoint when one exists. |
| `--max-num-seqs 64` | Maximum number of requests processed at the same time. Lower it if you run out of memory with many concurrent requests. |
| `--enable-auto-tool-choice --tool-call-parser hermes` | Enable tool (function) calling. The correct parser depends on the model; see the model's Hugging Face page or the [vLLM tool calling docs](https://docs.vllm.ai/en/latest/features/tool_calling.html). |
| `--reasoning-parser qwen3` | For reasoning models, return the model's thinking separately from the answer. |
| `--enforce-eager` | Skip CUDA graph capture. Startup is faster but generation is slower. Useful while testing. |
| `--generation-config vllm` | Use vLLM's default sampling settings instead of the defaults in the model's `generation_config.json`. |

Run `vllm serve --help` for the full list. Model developers often publish recommended settings on the model's Hugging Face page, and the [vLLM recipes](https://recipes.vllm.ai) site has tested commands for popular models.

## Avoid Idle GPU Cancellation

YCRC [cancels jobs whose GPUs show no activity](gpu-jobstats.md#jobstats-terminated-my-job) for an extended time. A vLLM server waiting for requests holds GPU memory but has 0% utilization, so a server left idle in an interactive session can be cancelled.

- Use offline batch inference, or the batch job pattern above, for work that doesn't need a person in the loop.
- Stop interactive servers with ++ctrl+c++ when you are done, and end the job with `exit` or `scancel`.
- Request only as much time as you need.

## Troubleshoot

### Out of Memory or "Not Enough KV Cache" at Startup

Errors such as `CUDA out of memory`, `No available memory for the cache blocks`, or `The model's max seq len is larger than the maximum number of tokens that can be stored in KV cache` mean the model and KV cache do not fit in GPU memory. In order of preference:

1. Lower `--max-model-len`.
1. Use more GPUs with `--tensor-parallel-size`, or a GPU with more memory.
1. Use an FP8 or 4-bit checkpoint of the model, or `--kv-cache-dtype fp8`.
1. Lower `--max-num-seqs`.

### "Could Not Find nvcc"

vLLM needs the CUDA compiler to build some kernels. Run `module load CUDA/12.9.1` after `conda activate vllm`, as shown in [Install vLLM](#install-vllm).

### Home Directory Is Full

vLLM and its libraries cache compiled kernels under `~/.cache` (for example `~/.cache/vllm` and `~/.cache/flashinfer`), and Hugging Face downloads to `~/.cache/huggingface` unless `HF_HOME` is set. Check your usage with `getquota` and `du -sh ~/.cache/*`. Set `HF_HOME` as described in [Download a Model](#download-a-model) and move existing downloads to your project directory.

### Startup Is Slow

The first start of a model on a node reads the weights from storage, compiles the model, and captures CUDA graphs. Large models can take 10 to 20 minutes. Later starts are faster because compiled kernels are cached. Use `--enforce-eager` while testing to skip CUDA graph capture.

### "Address Already in Use"

Another server is using the port, often one of your own from an earlier attempt or another user on the same node. Choose a different port, or stop your old server.

### Requests Return 401 Unauthorized

The request's API key does not match `VLLM_API_KEY` on the server. Check that the client sends `Authorization: Bearer` followed by the key, and that you are connecting to your own server.

### "Model Architecture Not Supported"

The model needs a newer version of vLLM. Upgrade with `uv pip install --upgrade vllm` in your environment, or create a new environment. Very new models sometimes require a vLLM release that is only available as a Docker image; you can run those images with [Apptainer](../clusters-at-yale/guides/containers.md) using `apptainer exec --nv`.

### Multi-GPU Startup Hangs or Fails

Confirm that the number of GPUs in your request equals `--tensor-parallel-size` times `--data-parallel-size`. If startup fails with an error mentioning `custom_all_reduce`, unset `PYTORCH_CUDA_ALLOC_CONF` if you have set it, or add `--disable-custom-all-reduce`.

If you need help, [contact us](https://docs.ycrc.yale.edu/#get-help) with your job ID and the vLLM log.

## Validation

After running a vLLM job:

- Confirm with [Jobstats](gpu-jobstats.md) that every requested GPU shows high utilization while prompts are processed
- Check the vLLM log for the KV cache size and maximum concurrency, which tell you how many tokens and requests fit at once
- Confirm responses look correct on a small sample before running a large batch
