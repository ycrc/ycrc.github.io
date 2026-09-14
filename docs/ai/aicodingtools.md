# AI coding agents

Coding agents are AI-driven tools that can write code, inspect files, run commands, and take actions on your behalf. YCRC provides two approaches for using coding agents on YCRC systems: **local coding agents** and **commercial coding agents**.

## Which option should I use?

| | Local coding agents | Commercial coding agents |
| --- | --- | --- |
| AI model | YCRC-hosted Qwen3.8-27B | Models provided by commercial AI services |
| Inference | Local to YCRC | External provider |
| Coding-agent interfaces | Pi, Copilot, Codex, Claude | Commercial coding-agent tools |
| YCRC sandbox | Yes | Claude only, currently in beta |
| Data guidance | AI prompts and code processing remain local to YCRC | Limited by the approved data classification for the commercial service |
| Best for | Keeping AI prompts and code processing local to YCRC | Workflows that specifically require a commercial model |

### Local coding agents

YCRC's [Local Coding Agents on Bouchet](local-coding-agents.md) provide secure AI coding assistance using a locally hosted LLM with popular coding-agent interfaces. Code and prompts sent to the model are processed locally rather than being sent to external AI providers.

This is the recommended option when you want an agentic coding workflow while keeping AI inference local to YCRC.

### Commercial coding agents

Commercial coding agents use models hosted by external AI providers. Prompts, code, and other content provided to the model leave YCRC and are handled according to the provider and account terms.

YCRC is currently beta-testing a **Claude-only sandbox module** that adds cluster-specific protections around Claude Code. See [Commercial Coding Agents](commercial-coding-agents.md) for current data-classification guidance, the Claude sandbox beta, and the planned Claude Enterprise offering.

## Coding-agent risks

Coding agents are more powerful than ordinary chat interfaces. An agent can inspect files, write code, run commands, and take actions using the permissions available to the user who launched it. These capabilities make coding agents useful, but they also introduce risks that should be understood before using them on shared research systems.

Potential risks include:

- **Data exposure.** An agent may read and transmit data available in its environment. With a commercial agent, prompts, code, or other content sent to the model are processed by an external provider. Even with a local model, an agent with network access could transmit data through other tools or commands, however, the chance is greatly reduced with local models.
- **Unintended changes.** An agent may edit, move, overwrite, or delete files; change permissions; modify environments; commit to repositories; or make other changes available to your account. Therefore, you should always have a backup of your work.
- **Scheduler and resource actions.** An agent may submit, cancel, or modify Slurm jobs and can consume allocation, priority, CPU, GPU, memory, or storage resources available to you.
- **Credential exposure.** Configuration files, hidden files, or environment variables may contain SSH keys, API tokens, cloud credentials, or other secrets. An unrestricted agent may be able to read or transmit them. Our sandboxed agents restrict this.
- **Executing untrusted code.** An agent may generate, download, install, or execute code. This creates many of the same risks as manually running software from an unfamiliar source.
- **Prompt injection.** Instructions embedded in source code, documentation, webpages, downloaded files, or other content can attempt to influence an agent into taking actions you did not intend.
- **Impact on shared work.** On a cluster, your account may have access to shared project files, environments, repositories, or other resources. An unintended agent action can therefore affect collaborators as well as you.

These are capability risks, not predictions that an agent will behave maliciously. YCRC's coding-agent environments are designed to reduce the agent's access to sensitive or unrelated resources and to constrain potentially dangerous actions, but no sandbox or permission system can eliminate every risk.

Use version control and backups where appropriate, review important changes, and pay particular attention whenever an agent asks for approval to perform a sensitive action.

## Security settings in commercial tools

Commercial coding agents also provide their own permission and security controls. If you use a commercial tool outside a YCRC-provided sandbox, review its security documentation and understand what files, tools, and commands it can access.

| Agent | Security documentation |
| --- | --- |
| Claude Code (Anthropic) | [Claude Code security](https://code.claude.com/docs/en/security) |
| Codex (OpenAI) | [Codex security](https://developers.openai.com/codex/security) |
| Gemini CLI (Google) | [Gemini CLI documentation](https://geminicli.com/docs/) |
