# Clarity Platform

[Clarity](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform) is Yale's centrally managed generative AI platform. It provides a web-based chat interface to models from providers including OpenAI, Anthropic, and Google.

For YCRC users, Clarity is most useful when you need capabilities that are not provided by YCRC's locally hosted models, or when your data requires a Yale-approved service with a higher data classification. For workflows that need to operate directly on files, software, or jobs on a cluster, see the YCRC documentation for [AI coding agents](aicodingtools.md) and [Local LLMs](resources.md).

## When Clarity may be useful

Clarity provides several capabilities that differ from YCRC's local AI services:

- **Multiple commercial model families** through a single Yale-managed interface. The available models change over time; see Yale's [Agents](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform/agents) page for the current list.
- **Support for higher-risk data and Yale-managed data protections.** Clarity is approved for low-, moderate-, and most high-risk data. Yale's Clarity configuration prevents prompts and conversations from being used to train the underlying AI models, and Clarity applies defined retention and deletion practices to chat data. ePHI and data subject to external obligations, such as Data Use Agreements, have additional requirements. Review Yale's [Clarity security guidance](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform/security) and [privacy statement](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform/clarity-privacy-statement) before using restricted data.
- **Custom Agents** for approved use cases. These can use a custom system prompt, uploaded knowledge sources, and user-specific access controls. See Yale's [Custom Agents](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform/custom-agents) documentation.
- **Managed retrieval from uploaded files.** Custom Agents can use uploaded files as knowledge sources, providing a managed retrieval-augmented generation (RAG) workflow without requiring you to build and host your own retrieval system.
- **API access for approved use cases.** A Clarity Custom Agent can be accessed programmatically through the Clarity API. Yale also provides Portkey for use cases that require more direct API access to commercial models. These should not be treated as equivalent from a data-protection perspective: Clarity provides Yale-managed protections governing how submitted data is handled by the underlying AI services, while Portkey does not provide the same agreement for downstream model-provider data handling. Use Portkey only for data appropriate to the approved Portkey use case. See Yale's [API documentation](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform/api) for the differences, request process, and current pricing.

Clarity is primarily a managed AI platform rather than an HPC service. It does not replace cluster resources for computation, large-scale data processing, or software environments.

## Data protection and retention

A major distinction between Clarity and direct access to commercial models is the data-handling arrangement. Yale states that data submitted through Clarity is not provided to the underlying model providers to further train or improve their models. This protection is one reason Clarity is approved for higher data classifications than many direct commercial AI services.

Clarity still retains data within Yale's infrastructure. Chats with no activity are automatically deleted after six months. If you manually delete a conversation, it becomes inaccessible in the user interface and the conversation, files, and related artifacts are permanently purged from the platform after 30 days. Limited usage records are retained for aggregate reporting. See the [Clarity Privacy Statement](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform/clarity-privacy-statement) for the authoritative retention details.

Portkey is a separate API gateway for direct access to models hosted through providers such as Azure, AWS, and Google Cloud. Do **not** assume that using Portkey gives a workflow the same downstream model-provider data protections as Clarity. Data sent through Portkey should be limited to the classification and use case specifically approved for that workflow.

## Access

The standard Clarity chat interface is available to current Yale faculty, staff, and students. Custom Agent creation and API access require an approved use case, and sponsored students can request access with faculty sponsorship.

See the [Clarity Platform](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform) documentation for current access instructions and features.

## Using Clarity APIs from YCRC systems

YCRC systems can make outbound API requests for approved Clarity or other commercial API workflows. The model inference occurs on the remote service, so these jobs generally do **not** require YCRC GPUs.

Request only the cluster resources needed by your application, such as CPU, memory, and runtime. Do not request a GPU solely to make API calls to a remotely hosted model.

API credentials should be treated as secrets. Do not place API keys in source code, Git repositories, job scripts that will be shared, or other locations where they may be exposed.

!!! note
    Approval to use a particular Yale AI service or API does not automatically mean that every dataset may be sent to it. Follow the data classification, Data Use Agreement, ePHI, and other requirements applicable to your data and approved use case.

## Limitations

Clarity is not intended to replace YCRC's local LLM and coding-agent services. In particular, the standard Clarity chat interface does not directly operate on your cluster filesystem, submit Slurm jobs, manage software environments, or interact with your running HPC workflows.

Clarity also currently has no general internet browsing or voice interface. Features and available models change frequently, so consult Yale's [Clarity documentation](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform) for the current platform capabilities rather than relying on a fixed model or feature list here.

## Support

Clarity is managed by Yale's AI Platform Services team rather than YCRC. For Clarity-specific questions, known issues, Custom Agent requests, or API access, use the support resources linked from the [Clarity Platform documentation](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform).
