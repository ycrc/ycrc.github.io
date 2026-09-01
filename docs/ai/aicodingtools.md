# AI coding tools

## YCRC Support Options
Due to the exposure risks associated with API coding tools like Claude Code, the YCRC does not formally support 
researchers who wish to use AI coding tools to aid in their workflow development. It is possible
to attach agents to your coding environments (VSCode, etc) while in the cluster, but it comes with the following risks.

## Coding Agents
Coding agents, AI-driven programs that write code and take actions on your behalf, are becoming increasingly popular and capable. Although you can use coding agents on YCRC clusters, these tools are evolving quickly and can act with broad authority, introducing risks that may not be immediately obvious. For this reason, it is important to follow established security best practices when using coding agents.
 
These risks include the possibility that the agent might:

- Expose your or your lab group's data
- Take actions on your behalf, including: editing, moving, or deleting files, submitting or canceling your Slurm jobs, or any other action you are allowed to take on the system
- Expose your security credentials
- Execute arbitrary, and perhaps malicious, code. 

### Expose data
AI coding agents send code and data to the company that runs them, e.g., OpenAI, Anthropic, Microsoft, or Google. 
The service may log or retain your code and data, which may be added to the AI training set, depending on the provider
 and your account settings. Experiments have shown that many LLMs can be coaxed to resurface their training data or 
leak code snippets (as an extreme example, in the past, some LLMs would reproduce complete [Harry Potter books](https://arxiv.org/abs/2601.02671) 
when prompted by the book's first sentence). A less obvious issue is that coding agents can transmit any data readable
 by your user. On a local laptop, there is a concerning amount of data exposure for your own data. On a cluster, this 
means the agent can also expose any data you have read access to, such as your labmates through the 'project' directory, 
shared data sets, or user-facing systems files. 

### Perform undesirable actions
A coding agent acts on your behalf with your full set of permissions. This means it can do anything you are allowed to 
do, including editing file contents, changing file permissions, and deleting your (or your lab group's) data. It might 
install unknown software, alter shared conda environments, or commit to shared git repos. It can submit or cancel Slurm 
jobs or consume significant allocation, priority, or shared resources by submitting expensive or excessive jobs. Because 
many cluster workflows rely on shared scripts, environments, or repositories, unintended changes can propagate to other 
users without their knowledge. Reports of coding agents deleting production databases, ignoring explicit instructions 
not to read certain files, and many other stories proliferate on the internet. Although these are rare, extreme 
examples, it is important to be aware of what is possible. Proper safeguards will reduce the risk of their occurrence.

### Leak credentials
Coding agents may read configuration files, environment variables, or hidden files that contain credentials 
(e.g., SSH keys, API tokens, cloud credentials, or Slurm configuration). If exposed, these credentials could allow 
others to access your cluster resources or external services.

### Execute unknown code
A coding agent can go much further than simply running bash commands as you. It could, in theory, generate or download 
code and run it, including malicious code. Coding agents are susceptible to prompt injection attacks, in which an 
agent is tricked into reading malicious instructions that it then dutifully executes. It could install keyloggers, 
install backdoors, or perform any other malicious activity you can imagine if a bad actor compromised your account.

### Security settings
Although these potential hazards are serious, they represent worst-case scenarios. If you follow best security practices while operating a coding agent, you will significantly reduce your risk. Most coding agents describe security settings for their agents. See the table below for examples from common coding agents. Ignoring security or making light of it will increase your risk of something unfortunate happening to you or to your lab mates. Please use these powerful tools wisely and with full knowledge of the risks involved.

| Agent | Security documentation |
| -------- | ----------------------------- |
| Claude Code (Anthropic) | [https://code.claude.com/docs/en/security](https://code.claude.com/docs/en/security) |
| Codex (OpenAI) | [https://developers.openai.com/codex/security](https://developers.openai.com/codex/security) |
| Gemini CLI (Google) | [https://geminicli.com/docs/](https://geminicli.com/docs/). See pages for [Trusted Folders](https://geminicli.com/docs/cli/trusted-folders/), [Tools](https://geminicli.com/docs/tools/), and [Sandboxing](https://geminicli.com/docs/cli/sandbox/). |

## Safe(er) Claude code on YCRC clusters

> We are currently beta-testing a module that makes Claude safer to use on our clusters. If you are interested in testing this module, we would appreciate your feedback. To join the beta testing phase, please email us at research.computing@yale.edu.

YCRC offers a module that mitigates many (but not all) of the risks above and ensures safer use of Claude on our clusters. The design philosophy is that you should not know you are using it. Claude should be able to perform any (safe) operation you want it to, but is prevented from performing any (unsafe) actions you would not want it to. 

The module uses your existing Claude account and settings, so transitioning between your existing install and the module should be seamless. It provides access to common research computing tools, including modules, Conda environments, R, and the scheduler, SLURM, while restricting Claude’s access to sensitive or unrelated areas of the system, such as SSH credentials, other users’ files, and directories outside the intended working environment.

Using the module is the recommended way to use Claude on YCRC systems and will help ensure increased safety for yourself and others. 


### How the module reduces risks

The module increases the safe use of Claude through several approaches.

- Claude can only see your working folder, which prevents unintended data egress or file manipulation.
- Every command is inspected for unsafe behavior. Unsafe commands are flagged or denied, while safe commands are run automatically. This puts an extra layer of scrutiny around each command. It also allows you to focus on potentially dangerous commands while ignoring safe ones.
- On top of inspecting each command, additional permissions constrain potentially destructive actions. Some commands, like `rm`, will always ask for your permission before Claude runs them. Others, like `sudo` or `scancel`, are always denied. If you want to run denied commands (and have permission to do so), you can always run them in a terminal outside of claude.

Together, these constraints reduce the risk of the potentially damaging actions described in the coding agent warning above.

### Using the module

To receive access to the module, join the beta test (see above).

Once you have loaded the module, simply load Claude as you normally do.

```bash
salloc
claude
```

You need to have a Claude account with Anthropic to use the module.

If you have already used claude on the cluster, the module will see your existing authentication, sessions, and other settings. If you have not run claude yet, claude will ask you to authenticate to your account.

The module has a few checks before it can start, designed to limit Claude's potential to take unsafe actions. When launching Claude, you should:

- Start Claude on a compute node. Coding agents can use a surprising amount of resources and should not be run on the login node.
- Start Claude in a non-hidden subdirectory in your home, project, pi storage, or scratch space. This prevents Claude from seeing folders such as `~/.ssh`, your other projects, or those of others in your group.

### Tools and environment available to Claude

Claude should have access to all the tools and environmental settings that you would normally have when using a terminal. Currently, the following tools are enabled.

- Modules
- Conda
- R
- Slurm

If you want Claude to have access to other tools, please let us know, and we can make these available.

The module attempts to scrub any environmental variables that contain sensitive information, such as API keys or security tokens.

### How does the module work?

The module uses several approaches to implement its safety measures, including external and internal techniques to the Claude executable. 

- Before loading, a module launch script checks that Claude is starting in an appropriate folder and scrubs sensitive environment variables.
- Claude runs within an Apptainer container. The container implements functionality that limits visibility to only your work folder and special directories required for tools such as conda or R to function.
- The container has security policies embedded in `/etc/claude-code/managed-settings.json`. This is the settings file that enforces security policies for the claude executable, such as turning on auto-mode or denying certain commands.
- Claude knows it is in a container, which sets important context for coding sessions. Claude's execution environment is documented in `/etc/claude-code/CLAUDE.md` within the container.

### Final note

Although the module significantly increases the safe use of Claude, no solution is perfect. The command inspector might misclassify a command; you might approve a destructive command; a bug in the claude executable or apptainer; or a misconfigured environment might lead to unintended consequences. Even when using this module, please keep in mind the potential dangers described in the warning above.


## Claude Science

[Claude Science](https://www.anthropic.com/news/claude-science-ai-workbench) can be connected to the cluster by establishing a local tunnel to a compute node. The [SSH tunneling for local applications](/clusters-at-yale/access/advanced-config/#ssh-tunneling-for-local-applications) page describes how to open a local tunnel.

After you set up the tunnel, you can connect Claude Science to it. 

Open Claude Science, then click Customize -> Compute -> + Add SSH host. Pick `bouchet-compute`. The connection should work and report "connected". 

You only need to perform this setup once, but the connection won't work unless you have a tunnel open.

Try the connection in a prompt, e.g., "Print the first few lines of ~/myfile.txt on bouchet-compute".

Note that operating coding agents on the clusters comes with some risks, not just to yourself but to others in your lab. Please take a moment to read our warning about AI coding tools at the beginning of this page.