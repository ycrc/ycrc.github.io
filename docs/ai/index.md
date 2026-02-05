# AI at the Yale Center for Research Computing

This section documents supported workflows for running large language models and related AI tools on YCRC resources.

This documentation builds on existing YCRC documentation, including:

- Interactive and GUI interfaces: [Open OnDemand Remote Desktop](../clusters-at-yale/access/ood.md)
- Resource Scheduling(Interactive and Batch): [Slurm job scheduling](../clusters-at-yale/job-scheduling/index.md)
- Available Programs on YCRC systems: [software modules](../applications/modules.md)
- Resource Monitoring for Users: [Jobstats](../clusters-at-yale/job-scheduling/jobstats.md)

Most of which can be found by attending Intro-to-HPC or viewing the [training video](https://www.youtube.com/watch?v=Wvao_o1ACBQ)
## Scope

Covered workflows:

- Open-source inference using Hugging Face and Ollama
- Interactive usage via OpenWebUI, Terminals, and Jupyter Lab
- GPU monitoring using Jobstats
- Multi-GPU usage on a single node
- Yale-managed access to closed-source models via Clarity
- Recommendations/Warnings on AI coding tools
- vLLM and Flash Attention installation instructions
- Resource recommendations
- Free Resources for Massive Scale Workflows

Future workflows:

- Retrieval-Augmented Generation (RAG)
- Fine-tuning and training

## Navigation guidance

Use the pages below based on your workflow and questions:

- **Where should my workflow run? What are some beginner tips about using LLMs on YCRC systems?**  
  See [Available Resources and Recommendations](resources.md) for guidance on clusters, GPU characteristics, and workflow placement.

- **Are my GPUs actually being used? Have I received an email from Jobstats about not using a GPU?**  
  See [GPU Monitoring with Jobstats](gpu-jobstats.md) for how to validate GPU utilization and memory usage.

- **I want to use Ollama, the YCRC recommended tool for inference**  
  See [Ollama](ollama.md) for supported usage and multi-GPU considerations.

- **I want structured practice and validation examples**  
  See [Exercises](exercises.md) for examples on using Ollama in Jupyter Notebooks.

- **I want to use Hugging Face**  
  See [Hugging Face](huggingface.md) for supported environment setup and AI workflows.

- **I want to use multiple GPUs**  
  See [Multi-GPU Usage in Miniconda Environments](miniconda-multigpu.md) for instructions and common issues.

- **I need more GPUs than the H200s and other GPUs available on YCRC systems**
  See [National AI Research Resource](nairr.md) for information about national free resources (with an application submission) for AI-focused research or
  research using AI tools.

- **I need help installing AI/ML python packages like flash attention or others**  
  See [Common Package installation Methods](pythonpackages.md) for instructions

- **I need access to closed-source models, but I want to make sure my data is secure(Claude, etc)**  
  See [Clarity API](clarity.md) for Yale-managed access and usage guidance.

- **I want to use AI coding tools**  
  See [AI Coding Tools on YCRC Systems](aicodingtools.md) for recommendations and data security concerns.

<!--
- **I want a browser-based, chat-style interface**  
  See [OpenWebUI on Remote Desktop](openwebui.md) for installing and launching OpenWebUI in an OOD session.
-->


<!-- - **Something is not behaving as expected**  
  See [Troubleshooting and Best Practices](troubleshooting.md).-->
