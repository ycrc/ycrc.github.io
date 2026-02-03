# Available Resources and Recommendations

YCRC Research Computing Infrastructure can be used to run localized large language models on GPU-enabled clusters.

Running LLMs locally provides the following advantages:

- User data remains local to the cluster [(Security concerns with non-local models)](clarity.md)
- Researchers can control model versions and configurations
- YCRC GPUs are free of charge (Except the secure data cluster, [Hopper](../clusters/hopper.md)
- Models up to 1100 GB of aggregate GPU memory can be run on a single node (Bouchet Only)

## GPU availability on YCRC resources

Once an LLM workflow is configured, models can be run on any GPU partition:

- McCleary and Grace: `gpu_devel`, `gpu`, `gpu_scavenge`
- Milgram: `gpu`, `scavenge`
- Bouchet: `gpu`, `gpu_h200`, `gpu_devel`
- Hopper: `gpu`, `gpu_devel`

GPU memory capacity varies significantly by GPU type. Some models will not run unless sufficient vRAM is available.

All YCRC GPU nodes, except H200s (contain 8 GPUs) contain four GPUs. When a job requests four GPUs on the same node, the available GPU memory is the sum of all four devices.

For example:

- Requesting four A100-80GB GPUs provides 320 GB of aggregate GPU memory

## Cluster GPU summary

| Cluster  | Largest GPU | Max vRAM (4 GPUs) | # of Largest GPUs available | # of Other GPUs available | Workflow Recommendations |
|---------|------------|-------------------|------------------------|----------------------|----------------------------|
| Bouchet | H200       | 1120 GB           | 80                     | 40                   | Very large models, multi-GPU inference, large-scale experimentation |
| Hopper  | H200       | 1120 GB           | 32                     | 172                  | HIPPA, PHI, PII Data Analysis |
| Grace   | A100-80G   | 320 GB            | 16                     | 132                  | Large inference workloads, memory-bound models |
| McCleary| A100-80G   | 320 GB            | 12                     | 92                   | General-purpose inference, development, testing |
| Milgram | H100       | 320 GB            | 12                     | 8                    | Medium risk data workflows |

Detailed hardware information is available on the cluster pages:

- [Bouchet](../clusters/bouchet.md)
- [Hopper](../clusters/hopper.md)
- [Grace](../clusters/grace.md)
- [McCleary](../clusters/mccleary.md)
- [Milgram](../clusters/milgram.md)

Navigate to the Public Partitions section and select `gpu` or `gpu_devel` to view available hardware.

## Scheduling considerations

YCRC operates on a queued scheduling system. Larger GPUs are in higher demand and typically have longer wait times.

Recommendations:

- Begin development using smaller models that fit on lower-memory GPUs
- Validate workflows interactively, including GPU detection
- Scale model size only after confirming proper detection of resources by your script

This approach reduces queue time and avoids failed jobs.

## Choosing a local LLM

Models are available through:

- [Ollama](https://ollama.com/library)
- [Hugging Face](https://huggingface.co/models)

Model names commonly include parameter counts:

- `7B` = 7 billion parameters
- `13B`, `30B`, `70B`, etc.

Approximate GPU memory requirements for inference without quantization:

| Parameter size | Inference vRAM (GB) |
|---------------|---------------------|
| 7B            | 10+               |
| 13B           | 20+               |
| 30B           | 40+               |
| 70B           | 80+                 |
| 305B          | 400+                |

Exact requirements are listed on the model's Hugging Face or Ollama page.

Domain-specific models are often smaller and more efficient than general-purpose models and should be preferred when available.
e.g., if seeking to performan analysis on Law or Medical data, you may find better success finding a model that was developed
specifically for Law or Medical Documents.

If vRAM requirements are uncertain, run the model on a larger GPU and inspect usage using [Jobstats](gpu-jobstats.md).

## Advanced methods (overview only)

More complex workflows require additional GPU memory:

| Method | vRAM Required |
|------|------------------|
| Inference | Size of model |
| RAG | Additional 10-30+ GB than inference |
| Fine-tuning | 3-5x inference |
| Fine-tuning (QLoRA) | 10-20% of inference |
| Training from scratch | Not Recommended |
