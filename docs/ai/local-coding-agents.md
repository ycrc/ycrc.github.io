# Local coding agents on Bouchet

YCRC provides **secure AI coding assistance for Bouchet using a locally hosted LLM with popular coding-agent interfaces**. Code and prompts sent to the model are processed locally without being sent to external AI providers.

The `local-coding-agents` module provides four coding-agent interfaces backed by the same YCRC-hosted Qwen3.8-27B model. The agents run within a YCRC-configured security boundary while retaining access to common HPC development workflows.

To use, be on a compute node and:

```
module load local-coding-agents
```

## Choosing an agent

All four interfaces use the same local model. They differ primarily in how they plan work, interact with tools, and present results.

| Agent | Description |
| --- | --- |
| Pi | Fast and flexible. Recommended for most users. |
| Copilot | Consistent and structured. |
| Codex | Precise and task-focused. |
| Claude | Thorough and exploratory, but generally slower. |

> **YCRC administrators:** currently use the Claude harness only. Additional administrator-specific configurations are under development.

You can switch between interfaces without changing the underlying model or local-inference architecture.

## Getting started

Coding agents must run on a compute node. First request an interactive allocation, then load the module:

```bash
salloc
module load coding-agents/1.0
```

Start the agent you want to use:

```bash
pi
```

or:

```bash
copilot
codex
claude
```

No account or API key with Anthropic, OpenAI, GitHub, or another commercial AI provider is required for these local agents.

## Where agents can run

Start the agent in a **non-hidden subdirectory** of an allowed storage location, such as your home, project, scratch, or approved PI storage.

For example:

```bash
mkdir -p ~/my-analysis
cd ~/my-analysis
pi
```

The module will refuse to start from locations that do not meet its security requirements. Coding agents should not run on login nodes.

These restrictions limit the agent to the files and directories needed for your work and reduce unintended access to credentials, unrelated projects, and other users' data.

## HPC tools and workflows

The local agents are configured to work with common Bouchet workflows, including:

- Slurm job submission and monitoring
- Software modules
- Conda environments
- R and user-installed R packages
- Git and common command-line development tools
- Internet access from Bouchet when needed for normal development workflows

Each command run by a coding agent starts in a fresh shell. Environment changes such as `module load`, `conda activate`, `export`, and `cd` therefore do not persist into the agent's next command. The agents are provided with YCRC-specific instructions for handling these workflows correctly.

For example, commands that depend on a module should load the module and run the program in the same shell command:

```bash
module load R/<version> && Rscript analysis.R
```

## Security and privacy

The local coding-agent environment is designed to give agents useful access to your research workflow without exposing everything your normal login account can access.

Important protections include:

- **Local AI inference.** Prompts and code sent to Qwen3.8-27B are processed by a YCRC-hosted model rather than a commercial AI provider.
- **Restricted filesystem visibility.** The agent sees its intended working area and selected directories required for supported tools rather than your unrestricted home and shared storage.
- **Credential protection.** Sensitive locations such as SSH credentials are not made available to the agent, and the launcher removes inherited environment variables that may contain credentials or tokens.
- **Shared storage protection.** The agent is restricted from browsing other users' project, scratch, or PI storage simply because your normal account may have group read access.
- **Read-only shared software.** YCRC-managed software under `/apps` is available for use but cannot be modified by the agent.
- **YCRC-specific policies.** The agents receive centrally managed instructions describing Bouchet storage, Slurm, GPU, module, Conda, and R policies.

The security boundary is implemented independently of the language model. The model is not relied upon to remember which parts of the cluster it should or should not access.

## Using coding agents safely

Within its allowed environment, a local coding agent can take many of the same actions you would take in a terminal, including changing files, running programs, installing user software, accessing the network, and interacting with Slurm. This autonomy is intentional.

See [AI Coding Agents](aicodingtools.md#coding-agent-risks) for the risks that apply to coding agents generally. The local module is designed to reduce the agent's access to sensitive or unrelated parts of the cluster, but you should still review important changes, use version control when appropriate, and maintain backups of important data.

## Local agents versus commercial agents

The local module does **not** use the commercial models associated with the Pi, Copilot, Codex, or Claude interfaces. Those programs are being used as coding-agent interfaces to YCRC's local Qwen3.8-27B model.

If you specifically need a commercial model, see [Commercial Coding Agents](commercial-coding-agents.md) for information about YCRC's sandboxed commercial-agent beta and its different data-security considerations.
