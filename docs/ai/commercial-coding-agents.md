# Commercial coding agents

Commercial coding agents use models hosted by external AI providers. Unlike YCRC's [Local Coding Agents on Bouchet](local-coding-agents.md), prompts, code, and other content provided to a commercial model leave YCRC for processing by that provider.

This page focuses on **data exposure and approved data use** for commercial coding agents. For the broader operational risks of coding agents, including file changes, credential access, command execution, Slurm actions, and prompt injection, see [AI Coding Agents](aicodingtools.md#coding-agent-risks).

## Data classification

Commercial coding agents must only be used with data appropriate for the approved service and account type.

| Service | Approved data |
| --- | --- |
| Claude Enterprise, when available | Low-risk and medium-risk data |
| Other commercial coding agents | Low-risk data only |

Until Claude Enterprise is available, commercial coding agents should be used only with **low-risk data**.

The approval for medium-risk data will apply specifically to the managed **Claude Enterprise** service when it becomes available. It does not extend to personal Claude accounts or to other commercial coding agents.

## Data exposure

Commercial coding agents send prompts and related context to the company operating the model, such as Anthropic, OpenAI, Microsoft, or Google. Depending on the tool, configuration, account type, and provider terms, that context may include source code, command output, file contents, or other information made available to the agent.

Do not assume that a commercial agent sends only the text you type into the prompt. Coding agents may gather additional context from files or tools while completing a task.

Provider retention, logging, training, and privacy practices vary by service and account type. Use only data permitted for the specific commercial service you are using.

## Claude sandbox beta

> YCRC is currently beta-testing a sandbox module for **Claude Code** on Bouchet and McCleary. If you are interested in testing the module, please email us at research.computing@yale.edu.

The current sandbox module supports **Claude Code only**. It is being developed in anticipation of broader Claude Enterprise availability and is intended to provide a safer way to use Claude on YCRC clusters.

The sandbox does not change where Claude performs inference: prompts and model context are still sent to Anthropic. Its purpose is to reduce what Claude can access and change on the cluster.

The module uses your existing Claude account and settings. It provides access to common research-computing tools, including modules, Conda environments, R, and Slurm, while restricting Claude's access to sensitive or unrelated areas of the system.

### Sandbox controls

The general operational risks of coding agents are described on the [AI Coding Agents](aicodingtools.md#coding-agent-risks) page. The Claude sandbox adds cluster-specific controls around what Claude can see and do.

- Claude can see the intended working directory and selected supporting directories required for supported tools, rather than unrestricted home and shared storage.
- Commands are evaluated against configured safety policies. Some operations can run automatically, some require approval, and others are denied.
- Sensitive locations such as SSH credentials are excluded from Claude's environment.
- The launcher removes inherited environment variables that may contain credentials or security tokens.
- YCRC-managed software and other protected locations are exposed only as needed and with appropriate restrictions.

These controls limit Claude's cluster access, but they do not change the data classification of the commercial service itself.

### Using the beta module

To receive access to the module, join the beta test by contacting YCRC.

Run Claude on a compute node and start it from a non-hidden subdirectory in your home, project, PI, or scratch storage. For example:

```bash
salloc
claude
```

You need a Claude account with Anthropic to use the current beta module.

If you have already used Claude on the cluster, the module can use your existing authentication, sessions, and settings. If you have not used Claude before, it will ask you to authenticate.

The module will refuse to start in locations that do not meet its security requirements.

### Tools and environment available to Claude

The sandbox supports common YCRC workflows, including:

- Modules
- Conda
- R
- Slurm

If you need an additional tool or workflow, contact YCRC so it can be evaluated and added safely.

### How the module works

The module combines controls outside and inside the Claude executable:

- A launch script checks that Claude is starting from an approved working location and removes sensitive inherited environment variables.
- Claude runs inside an Apptainer container that limits filesystem visibility while exposing the directories needed for supported workflows.
- Managed Claude settings enforce YCRC command and permission policies.
- YCRC-specific instructions describe the execution environment and supported cluster workflows to Claude.

The sandbox controls Claude's cluster environment. Separately, the commercial service's approved data classification determines what data may be sent to the model.

## Claude Enterprise

YCRC anticipates making Claude Enterprise available for coding-agent workflows. When available, the managed Claude Enterprise service will be approved for **low-risk and medium-risk data**.

The existing sandbox work is intended to complement that service by limiting what the coding agent can access and change on YCRC systems. Data classification and sandboxing address different risks: Claude Enterprise determines what data may be sent to the provider, while the sandbox limits the agent's authority on the cluster.

Other commercial coding agents remain approved for **low-risk data only**.

## Claude Science

[Claude Science](https://www.anthropic.com/news/claude-science-ai-workbench) can be connected to the cluster by establishing a local tunnel to a compute node. The [SSH tunneling for local applications](/clusters-at-yale/access/advanced-config/#ssh-tunneling-for-local-applications) page describes how to open a local tunnel.

After you set up the tunnel, connect Claude Science to it through **Customize → Compute → + Add SSH host** and select `bouchet-compute`.

You only need to perform this setup once, but the connection will not work unless you have a tunnel open.

For example, you can test the connection with a prompt such as: "Print the first few lines of `~/myfile.txt` on `bouchet-compute`."

Claude Science is a commercial Anthropic service, so the same data-classification guidance above applies.
