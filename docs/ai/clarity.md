# Clarity API

The YCRC recommends using locallized open-source models on the Cluster or closed-source models on Clarity for research 
purposes due to data exposure risks.

Clarity, managed by ITS, provides Yale-managed access to closed-source language models via a ChatGPT-esque communication interface. Clarity currently provides access to:

- OpenAI models
- Anthropic models
- Google models

A specific list of available models can be seen [here](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform/agents).

## Access

Access is provided for anyone with a NetID.

For further information, please visit [this website](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform)

##Issues/Errors

For issues using Clarity, please visit the [FAQ](https://ai.yale.edu/yales-ai-tools-and-resources/clarity-platform/known-issues) or contact [ITS](https://yale.service-now.com/it?id=get_help)

##API Keys for closed-source models
If you are a researcher that has access to closed-source models via API keys, the YCRC systems will support accessing the model from the clusters
so as to avoid unnecessary data transfers.
However, using API keys generally means that you are using resources provided by the API key provider, and do not need GPU resources from the YCRC system.
When submitting jobs with this workflow, please only request these types of resources:

- Cpus: for moving data
- Memory: for moving data
- Time: to ensure completion of API job 

##Data Exposure Risk

For Clarity, there is little to no data exposure risk. It is a closed system, managed by cloud providers, but where data is contained to within Yale's infrastructure.

For API keys, however, there is significantly more risk:
API keys send code and data to the company that runs them, e.g., OpenAI, Anthropic, Microsoft, or Google. The service may log or retain your code and data, which may be added to the AI training set, depending on the provider and your account settings. Experiments have shown that many LLMs can be coaxed to resurface their training data or leak code snippets (as an extreme example, in the past, some LLMs would reproduce complete [Harry Potter books](https://arxiv.org/abs/2601.02671) when prompted by the book's first sentence). 

Because of this, the YCRC recommends using locallized open-source models on the Cluster or Clarity for research purposes.
