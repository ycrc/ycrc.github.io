# Scripting with the YCRC-hosted model

YCRC hosts a large language model on Bouchet, currently Qwen3.8-Flash-Next, that you can call from your own code with the standard OpenAI or Anthropic Python packages, `curl`, or any tool that speaks the OpenAI API. Use it to classify, extract, summarize, or annotate data in scripts and batch jobs **at no cost, without requesting GPUs, and without a commercial AI account**. Prompts and data are processed by YCRC rather than a commercial AI provider.

This is the same model used by [Local Coding Agents](local-coding-agents.md) and [Open WebUI](open-webui.md).

This page assumes familiarity with [Slurm job scheduling](../clusters-at-yale/job-scheduling/index.md) and [Conda environments](../clusters-at-yale/guides/conda.md).

## Which option should I use?

| I want to... | Use |
| --- | --- |
| Call an LLM from my own scripts, notebooks, or batch jobs | This page |
| Chat with a model in the browser, or ask about my jobs and files | [Open WebUI](open-webui.md) |
| Have an AI agent write and run code on the cluster | [Local Coding Agents](local-coding-agents.md) |
| Use a different or fine-tuned model, or run very large offline batches on my own GPUs | [vLLM](vllm.md), [Ollama](ollama.md), or [Hugging Face](huggingface.md) |
| Use a commercial model, or process data classified above what Bouchet allows | [Clarity](clarity.md) |

## Quick start

Requests must come from inside a Slurm job on a Bouchet compute node, not a login node. The model runs on YCRC's server, so your job needs no GPU and very little CPU or memory:

```bash
salloc --partition=devel --cpus-per-task=1 --mem=4G --time=2:00:00
```

Load the `ycrc-llm` module, which points the OpenAI and Anthropic packages, `curl`, and other OpenAI-compatible tools at the YCRC server:

```bash
module load ycrc-llm
```

The module sets `OPENAI_BASE_URL` and `ANTHROPIC_BASE_URL` to the YCRC server, and `OPENAI_API_KEY` and `ANTHROPIC_API_KEY` to your NetID followed by `.api`. The key identifies you for fair sharing and usage reporting; it is not a password and does not need to be kept secret. Unloading the module restores any values you had set before. To configure a tool by hand instead, run `module show ycrc-llm` to see the values.

Test the connection with `curl`:

```bash
curl $OPENAI_BASE_URL/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{"model": "ycrc-local", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}'
```

From Python, install the `openai` package in a [Conda environment](../clusters-at-yale/guides/conda.md) (`pip install openai`). The package reads `OPENAI_BASE_URL` and `OPENAI_API_KEY` from the environment:

```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="ycrc-local",
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
)
print(response.choices[0].message.content.strip())
```

The `anthropic` package works the same way, reading `ANTHROPIC_BASE_URL` and `ANTHROPIC_API_KEY` from the module; use the same model names.

## Models and reasoning

| Model | Behavior |
| --- | --- |
| `ycrc-local` | Reasons briefly before answering. A good default for most tasks. |
| `ycrc-local-think` | Extended reasoning. Slower and produces more output; use it for difficult problems such as multi-step calculations or statistics. |

`ycrc-local` always refers to the model YCRC currently hosts, so your scripts do not need a new model name when YCRC updates the service. To find out which model is being served, list the models with `curl $OPENAI_BASE_URL/models -H "Authorization: Bearer $OPENAI_API_KEY"`. The model can read up to 262,144 tokens per request, including its answer.

**Turn reasoning off for simple, high-volume tasks.** For classification, extraction, and similar short-answer tasks, reasoning adds time without improving results. Set `reasoning_effort="none"`:

```python
response = client.chat.completions.create(
    model="ycrc-local",
    reasoning_effort="none",
    messages=[{"role": "user", "content": "Is this abstract about cancer? Answer yes or no.\n\n..."}],
)
```

In YCRC testing, this made a sentiment-classification job about eight times faster with the same accuracy.

When reasoning is on, the model's reasoning is returned separately in `response.choices[0].message.reasoning`, and the answer in `content` may begin with blank lines; use `.strip()`. Reasoning also counts toward `max_tokens`: if you set a small `max_tokens` with reasoning on, `content` can be empty because the limit was reached during reasoning.

## Process many items

Send requests **concurrently** rather than one after another. The server processes many requests at once, so a few parallel requests finish several times faster. This example labels every line of a text file and saves each completed result as it arrives. If interrupted, restarting skips saved items; requests that finished but were not yet written may run again:

```python
# label.py: python label.py abstracts.txt labels.jsonl
import json, os, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from openai import OpenAI

client = OpenAI(max_retries=10)   # retry automatically if the server is busy
LABELS = ["relevant", "not relevant"]

def label(item):
    i, text = item
    response = client.chat.completions.create(
        model="ycrc-local",
        reasoning_effort="none",
        messages=[{"role": "user",
                   "content": "Is this abstract about climate adaptation? Answer "
                              f"'relevant' or 'not relevant'.\n\n{text}"}],
        extra_body={"structured_outputs": {"choice": LABELS}},
        temperature=0,
    )
    return {"id": i, "label": response.choices[0].message.content}

infile, outfile = sys.argv[1], sys.argv[2]
done = set()
if os.path.exists(outfile):
    done = {json.loads(line)["id"] for line in open(outfile)}
items = [(i, t) for i, t in enumerate(open(infile).read().splitlines()) if i not in done]

with ThreadPoolExecutor(max_workers=8) as pool, open(outfile, "a") as out:
    futures = [pool.submit(label, item) for item in items]
    for future in as_completed(futures):
        result = future.result()
        out.write(json.dumps(result) + "\n")
        out.flush()
```

Run it as a batch job. The job needs only one CPU, since the work happens on YCRC's server:

```bash
#!/bin/bash
#SBATCH --job-name=label-abstracts
#SBATCH --partition=day
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=6:00:00

module reset
module load miniconda ycrc-llm
conda activate myenv

python label.py abstracts.txt labels.jsonl
```

Results are saved in completion order, not necessarily input order; use the `id` field to match them to input lines. With reasoning off and 8 concurrent requests, YCRC testing labeled about 30 short items per second, so 10,000 items take roughly 5 to 15 minutes, depending on how busy the server is and how long the items are.

## Useful features

### Structured output

To get output your code can parse reliably, constrain it to a JSON schema. The OpenAI package can fill in a [Pydantic](https://docs.pydantic.dev/) model directly:

```python
from pydantic import BaseModel

class Study(BaseModel):
    species: str
    sample_size: int
    randomized: bool

response = client.chat.completions.parse(
    model="ycrc-local",
    reasoning_effort="none",
    messages=[{"role": "user", "content": f"Extract the study details:\n\n{abstract}"}],
    response_format=Study,
)
study = response.choices[0].message.parsed
```

You can also restrict the answer to a fixed list of choices with `extra_body={"structured_outputs": {"choice": [...]}}` (as in the example above) or to a regular expression with `extra_body={"structured_outputs": {"regex": "..."}}`.

!!! warning "Name the allowed answers in your prompt"
    A constraint controls only the format of the answer; it does not tell the model what the choices mean. If you ask "Is this abstract about climate adaptation?" but allow only `relevant` or `not relevant`, the model's natural answer ("Yes") is not allowed, and its forced choice can be wrong for every item. In YCRC testing, that prompt labeled every abstract `not relevant`, while adding "Answer 'relevant' or 'not relevant'" to the same prompt labeled all of them correctly. Likewise, describe the fields you want in a JSON schema. A valid format does not guarantee correct extracted values or classifications. Always check a sample of results.

### Confidence scores

Set `logprobs=True` and `top_logprobs=5` (up to 20) to get the probability of each generated token and its most likely alternatives. For a single-token label, these probabilities can help compare candidate answers, but they are **not necessarily calibrated confidence scores**. Probability can be split between different spellings of the same answer (in YCRC testing, `negative` 0.48 and `Negative` 0.38); account for such alternatives when interpreting results. Turn reasoning off so the first generated token is the answer, and validate any confidence-based decisions against labeled examples.

### Reproducible results

Set `seed` to improve reproducibility when repeating a request with the same parameters, including when `temperature` is above 0. Identical results are not guaranteed, especially if the underlying model or serving configuration changes. Record the model name returned in `response.model` alongside your results, since `ycrc-local` can point to a different model after a YCRC update.

### Images

Send images as base64 data URLs, or as `https://` addresses the server can download. The model reads charts, figures, and text in images well:

```python
import base64

image = base64.b64encode(open("figure.png", "rb").read()).decode()
response = client.chat.completions.create(
    model="ycrc-local",
    messages=[{"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image}"}},
        {"type": "text", "text": "What value does each bar show?"},
    ]}],
)
```

### Video

Send video the same way, with a `video_url` part. The model can describe what happens and when, including estimated event times that should be checked against the original video:

```python
import base64

video = base64.b64encode(open("trial.mp4", "rb").read()).decode()
response = client.chat.completions.create(
    model="ycrc-local",
    messages=[{"role": "user", "content": [
        {"type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{video}"}},
        {"type": "text", "text": "List each event in this video with the time it starts."},
    ]}],
)
```

Video uses many tokens: in YCRC testing, two minutes of 640x360 video used about 12,000. To fit longer videos, reduce the resolution with [FFmpeg](../applications/modules.md) (`module load FFmpeg`, then `ffmpeg -i in.mp4 -vf scale=320:-2 out.mp4`), which preserved useful timing estimates while using 30% fewer tokens in that test. Lowering the frame rate also saves tokens but can make event timing less reliable. Video is available through the OpenAI-format API only.

### PDFs and other documents

The server does not read PDF files directly. Extract the text in your script first, for example with [PyMuPDF](https://pymupdf.readthedocs.io/) (`pip install pymupdf`):

```python
import pymupdf

text = "\n".join(page.get_text() for page in pymupdf.open("paper.pdf"))
response = client.chat.completions.create(
    model="ycrc-local",
    messages=[{"role": "user", "content": f"Summarize the methods section:\n\n{text}"}],
)
```

For scanned PDFs, or pages where layout and figures matter, render each page as an image (`page.get_pixmap(dpi=150).tobytes("png")`) and send the pages as images.

### Tool calling

The model supports OpenAI-style function calling (`tools` and `tool_choice`), including several tool calls in one response, for example to extract records into a defined structure.

## Limits and fair use

The model is shared by everyone who uses it. Each user can have a limited number of requests in progress at once; the limit is larger when the server is quiet and shrinks as more people use it. Requests from scripts can use up to three quarters of your allowance, so your own coding-agent or Open WebUI sessions stay responsive while a batch job runs.

Requests over the limit wait their turn. If a request waits too long, the server returns HTTP 429 (`rate_limit_exceeded`); retry it after a short delay. The OpenAI and Anthropic packages retry automatically (set `max_retries` higher for long jobs, as in the example above).

Good practice:

- Use about 4 to 16 concurrent requests. More than your allowance only makes requests wait.
- Turn reasoning off when you don't need it.
- Test your prompts on a small sample before processing a whole dataset.
- Check a sample of the model's answers yourself. AI output can be wrong, and errors in a dataset are easy to miss.

**Not available:** embeddings, reranking, audio input, direct PDF input, the OpenAI Batch and Files APIs, and the `min_p` and `logit_bias` sampling options. If your work needs these, [contact YCRC](https://docs.ycrc.yale.edu/#get-help); for embeddings in the meantime, you can run a small embedding model yourself with [Hugging Face](huggingface.md) or [vLLM](vllm.md).

## Privacy and usage records

Requests are processed on YCRC's server and are not sent to a commercial AI provider. YCRC does not store prompts or responses. For each request, YCRC records your NetID, how you accessed the model (here, `api`), and the number of tokens processed, to manage capacity and report usage.

## Coding agents

The `.api` key is for your own scripts. Coding agents such as Claude Code, Codex, Copilot, Pi, and similar tools are supported through [Local Coding Agents](local-coding-agents.md), which run them in a sandbox that protects your files and credentials. Requests that come from a coding agent using the `.api` key are refused with a message pointing to the module. If a script of yours is refused this way by mistake, please [let us know](https://docs.ycrc.yale.edu/#get-help).

If you use a coding agent to write a script that calls the model, ask it to use the settings in [Quick start](#quick-start).

## Troubleshoot

### "No API key was sent" or "The API key is not in the form &lt;netid&gt;.&lt;label&gt;"

Run `module load ycrc-llm` in the same shell or job script that runs your code. If you set the variables yourself, the key is your NetID followed by `.api`, for example `OPENAI_API_KEY=$(id -un).api` (or `ANTHROPIC_API_KEY` for the Anthropic package).

### "The key must start with your own NetID"

The part of the key before the dot must be your NetID. Check the value with `echo $OPENAI_API_KEY`.

### "... is not a recognised label in the key"

The part after the dot must be `api`, for example `abc123.api`.

### "... has no running Slurm job on ..."

Run your code inside a Slurm job (`salloc` or `sbatch`) on a compute node, not on a login node.

### "This request looks like it comes from a coding agent"

Use [Local Coding Agents](local-coding-agents.md) for coding agents. If your own script was refused, [let us know](https://docs.ycrc.yale.edu/#get-help).

### "Too many concurrent requests"

Your requests waited longer than the server allows. Reduce the number of concurrent requests, and retry refused requests after a short delay.

### "The model ... does not exist"

Use `ycrc-local` or `ycrc-local-think`. Other names, such as `gpt-4o`, are not available.

### "This model's maximum context length is ..."

The prompt and requested answer together exceed 262,144 tokens. Shorten the input, split long documents into sections, or lower `max_tokens`.

### `content` is empty or cut off

The answer reached `max_tokens`, possibly while the model was still reasoning. Increase `max_tokens`, or set `reasoning_effort="none"`.
