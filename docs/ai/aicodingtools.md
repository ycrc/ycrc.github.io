# AI coding tools

## YCRC Support Options
Due to the exposure risks associated with API coding tools like Claude Code, the YCRC does not formally support 
researchers who wish to use AI coding tools, such as Claude Code, to aid in their workflow development. It is possible
to attach agents to your coding environments (VSCode, etc) while in the cluster, but it comes with the following risk.

## Coding Agents
AI-driven programs that write code and take actions on your behalf, are increasing in popularity and efficacy. 
Coding agents are useful and exciting, and their use is permitted on YCRC clusters. However, these programs are 
powerful and rapidly changing tools that come with many potential risks that you may be unfamiliar with. 
These risks include the possibility that the agent might:

- expose your or your lab group's data
- take actions on your behalf, including editing, moving, or deleting files, submitting or canceling your Slurm jobs, or any other action you are allowed to take on the system
- expose your security credentials
- execute arbitrary, perhaps malicious, code. 

Because of coding agents' enhanced capabilities, it is important to follow the best practices recommended by the 
organizations that created the agents, as well as by independent entities.

## Expose data
AI coding agents send code and data to the company that runs them, e.g., OpenAI, Anthropic, Microsoft, or Google. 
The service may log or retain your code and data, which may be added to the AI training set, depending on the provider
 and your account settings. Experiments have shown that many LLMs can be coaxed to resurface their training data or 
leak code snippets (as an extreme example, in the past, some LLMs would reproduce complete [Harry Potter books](https://arxiv.org/abs/2601.02671) 
when prompted by the book's first sentence). A less obvious issue is that coding agents can transmit any data readable
 by your user. On a local laptop, there is a concerning amount of data exposure for your own data. On a cluster, this 
means the agent can also expose any data you have read access to, such as your labmates through the 'project' directory, 
shared data sets, or user-facing systems files. 

## Perform undesirable actions
A coding agent acts on your behalf with your full set of permissions. This means it can do anything you are allowed to 
do, including editing file contents, changing file permissions, and deleting your (or your lab group's) data. It might 
install unknown software, alter shared conda environments, or commit to shared git repos. It can submit or cancel Slurm 
jobs or consume significant allocation, priority, or shared resources by submitting expensive or excessive jobs. Because 
many cluster workflows rely on shared scripts, environments, or repositories, unintended changes can propagate to other 
users without their knowledge. Reports of coding agents deleting production databases, ignoring explicit instructions 
not to read certain files, and many other stories proliferate on the internet. Although these are rare, extreme 
examples, it is important to be aware of what is possible. Proper safeguards will reduce the risk of their occurrence.

## Leak credentials
Coding agents may read configuration files, environment variables, or hidden files that contain credentials 
(e.g., SSH keys, API tokens, cloud credentials, or Slurm configuration). If exposed, these credentials could allow 
others to access your cluster resources or external services.

## Execute unknown code
A coding agent can go much further than simply running bash commands as you. It could, in theory, generate or download 
code and run it, including malicious code. Coding agents are susceptible to prompt injection attacks, in which an 
agent is tricked into reading malicious instructions that it then dutifully executes. It could install keyloggers, 
install backdoors, or perform any other malicious activity you can imagine if a bad actor compromised your account.

Although these potential hazards are serious, they represent worst-case scenarios. If you follow best practices while 
operating a coding agent, you will significantly reduce your risk. All coding agents describe best practices for their 
agents. For example, Anthropic, which produces Claude Code, has the document [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices). 
Ignoring best practices or making light of them will increase your risk of something unfortunate happening to you or 
to your lab mates. Please use these powerful tools wisely and with full knowledge of the risks involved.
