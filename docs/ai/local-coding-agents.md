# Local coding agents on Bouchet

YCRC provides **secure AI coding assistance for Bouchet using a locally hosted LLM with popular coding-agent interfaces**. Code and prompts sent to the model are processed locally without being sent to external AI providers.

The `local-coding-agents` module provides four coding-agent interfaces backed by the same YCRC-hosted Qwen3.8-27B model. The agents run within a YCRC-configured security boundary while retaining access to common HPC development workflows.

To use, be on a compute node and:

```bash
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
module load local-coding-agents/1.0
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

## Extended reasoning

Extended reasoning gives the model more opportunity to work through difficult problems before answering. It is disabled by default because it increases response time and can generate substantially more output, which is usually unnecessary for routine coding work.

There are two ways to use it:

1. **For an entire session:** start the interface with `YCRC_THINKING=1`.
2. **For an individual task:** Claude and Pi can delegate that task to a separate reasoning agent.

### Enable reasoning for a whole session

Set `YCRC_THINKING=1` when starting an interface:

```bash
YCRC_THINKING=1 pi
YCRC_THINKING=1 claude
YCRC_THINKING=1 codex
YCRC_THINKING=1 copilot
```

The interface prints a short confirmation at startup, and the displayed model name gains a `-think` suffix.

The setting applies only to that session. Start the interface normally to return to the default behavior.

Extended reasoning is most useful for tasks such as:

- Debugging behavior with a non-obvious cause
- Reasoning about an algorithm, numerical method, or statistical approach
- Planning a complicated multi-step refactor
- Checking work where a subtle mistake could be costly

For routine editing, file navigation, simple commands, and short questions, the default mode is usually faster and more appropriate.

### Delegate an individual task

Claude and Pi can use a different reasoning mode for an individual delegated task without changing the rest of the session.

Two managed agents are available:

| Agent | Purpose |
| --- | --- |
| `deep-reasoning` | Works through a difficult problem using extended reasoning |
| `quick-task` | Handles simple work without extended reasoning |

How you access them depends on the interface:

| Interface | How to use a managed agent |
| --- | --- |
| Claude | Ask for `deep-reasoning` or `quick-task` directly, or let Claude select one automatically when appropriate. |
| Pi | Ask for `deep-reasoning` or `quick-task` explicitly. Pi does not select them automatically. |

For example:

```text
Use the deep-reasoning agent to work out why this job is being preempted.
```

The delegated task runs in its own context and returns its conclusion to the main session.

This works in either direction:

```text
Normal session
  └─ deep-reasoning → extended reasoning for one difficult task
```

or:

```text
YCRC_THINKING=1 session
  └─ quick-task → normal reasoning mode for one routine task
```

This can be more efficient than enabling extended reasoning for an entire session when only part of the work benefits from it.

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
