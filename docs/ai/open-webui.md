# Open WebUI on Bouchet

!!! warning "Beta"
    Open WebUI is currently in beta. Please report any issues to [research.computing@yale.edu](mailto:research.computing@yale.edu).

Open WebUI is a **chat interface in your browser for the YCRC-hosted model**, available on Bouchet as an [Open OnDemand](../clusters-at-yale/access/ood.md) interactive app. Prompts, uploaded files, and anything the assistant reads on Bouchet are processed by the YCRC-hosted model, currently Qwen3.8-Flash-Next, rather than a commercial AI provider. No account or API key is required.

Beyond answering questions, the assistant is set up for work on Bouchet. It can:

- Answer questions about Bouchet using YCRC's own guidance on Slurm, storage, modules, Conda, GPUs, and more
- Look up your jobs, job efficiency, storage quota, and partition status, and check a job script against the scheduler without submitting it
- Read files in your home, project, and scratch directories
- Run Python on Bouchet, including plots and analysis of your data
- Read uploaded images, PDFs (including scanned documents), Word and Excel files, and scripts
- Transcribe voice input

## Launch Open WebUI

Choose **Open WebUI** from the **Interactive Apps** menu on the Bouchet web portal and follow the instructions for [launching an interactive app](../clusters-at-yale/access/ood.md#launch-an-interactive-app). When the session is running, click **Connect to Open WebUI**. You are signed in automatically as yourself.

The form has the usual job settings plus two for running code:

- **Python environment for code:** the environment the assistant uses to run Python. `Default (YCRC)` includes NumPy, pandas, SciPy, and Matplotlib. Your own Conda environments appear in the list once they have `ipykernel` installed:

    ```bash
    module load miniconda
    conda install -n my_env ipykernel
    ```

    Reload the launch page afterwards. If the environment you choose cannot run code, Open WebUI shows a banner explaining why and uses the default environment instead.

- **Additional modules:** modules to load before your Python environment starts, separated by spaces (for example `R` or `SAMtools`).

Open WebUI does not use GPUs, so GPU partitions are not offered. Under **Check the box to view more options** you can set a Slurm account or add job options such as `--constraint=cpugen:turin`.

!!! note "One session at a time"
    You can run one Open WebUI session at a time, because all your sessions share the same chats and settings. To start a new one, delete the running session from **My Interactive Sessions** first. Closing the browser tab does not end the session.

Your chats, settings, and uploaded files are saved and available in every later session.

## Choose a model

Two versions of the YCRC-hosted model are available from the model menu at the top of the chat:

| Model | Use for |
| --- | --- |
| Qwen3.8-Flash-Next | Most questions. Fast; reasons briefly before answering. |
| Qwen3.8-Flash-Next-think | Difficult problems that benefit from extended reasoning. Slower. |

YCRC occasionally updates the hosted model. The model menu always shows the current model, and existing chats continue with it.

## Ask about your work on Bouchet

The assistant can look up information about your own account. For example:

```text
What jobs do I have running right now?
Did any of my jobs fail or time out in the last 7 days?
How efficiently did job 12345678 use its CPUs and memory?
How much of my home and project quota am I using?
Which GPU partitions have idle GPUs right now?
Is GROMACS installed? Which versions, and how do I load one?
Check this job script before I submit it: ...
What columns are in ~/data/results.csv?
```

These lookups are **read-only**: the assistant can't submit, cancel, or change jobs, and can't create, change, or delete your files. It only sees your own jobs, quota, and files, and it does not read credentials such as SSH keys. When you ask for a job script, it checks the script against the scheduler without submitting it and gives you the script to submit yourself.

## Run code

The **Code Interpreter** switch, in the integrations menu below the message box, lets the assistant write and run Python. It is on by default.

![Tools, Skills, and Code Interpreter menu](/img/ood_open_webui_integrations.png){: .medium}

Code runs on Bouchet, as you, in your session:

- It can **read** your files, so you can ask for analysis of your data directly.
- It can **write only to `~/openwebui-outputs`**. Files the assistant creates (CSV files, figures, scripts) are saved there. When you ask for a file somewhere else, the assistant saves it in `~/openwebui-outputs` and gives you the command to copy it.
- It uses the Python environment and modules you chose when launching. Packages can't be installed from a chat; install them in your own Conda environment and relaunch.
- Plots appear in the chat:

![A plot in the chat](/img/ood_open_webui_plot.png){: .large}

## Upload files

Use the **+** button in the message box to attach files, a screenshot (**Capture**), a webpage, notes, knowledge bases, or earlier chats. You can also drag files into the chat or paste an image.

![The + menu in the message box](/img/ood_open_webui_attach_menu.png){: .medium}

Images (including phone photos), PDFs (including scanned documents), Word and Excel files, CSV files, and scripts can all be read. Large images take up a significant part of the model's working memory for the rest of that chat.

### Knowledge bases

A knowledge base is a collection of documents you can reuse across chats. Create one under **Workspace** > **Knowledge** and upload your documents. Then:

- **For a few documents,** type `#` in the message box and choose the knowledge base. All of its documents are given to the model.
- **For a larger collection,** name the knowledge base in your question (for example, "In my knowledge base 'Lab handbook', what is the procedure for ...?"), or create a custom model with the knowledge base attached (see [Customize the assistant](#customize-the-assistant)). The assistant then searches the documents and reads only the relevant ones. Attaching a large collection with `#` can exceed what the model can read at once.

The search matches words that appear in the documents, so it works best when your question uses the same terms as the documents.

## Voice input

Click the microphone in the message box to dictate. Speech is transcribed on Bouchet, and many languages and accents are supported. Your recordings are not kept; only the transcribed text is saved in the chat. The first transcription in a session can take longer.

To have a reply read aloud, use the speaker icon below it; this uses your browser's built-in voices.

## Customize the assistant

**Chat Controls** (the icon at the top right of a chat) apply to the current chat:

![Chat Controls](/img/ood_open_webui_chat_controls.png){: .medium}

- **System Prompt:** extra instructions for this chat, for example "Answer as a grant reviewer" or "Reply in Spanish".
- **Advanced Params:** for example **Temperature** (lower values give more consistent answers) and **Seed** (repeatable answers). Leave **max_tokens** unset: it includes the model's reasoning, and a low value can produce an empty answer. Settings that only apply to other kinds of models, such as `min_p`, have no effect.

Other ways to customize Open WebUI:

- **Prompts** (**Workspace** > **Prompts**): save prompts you use often and insert them by typing `/`.
- **Custom models** (**Workspace** > **Models**): create a named assistant on top of the YCRC model with its own instructions and knowledge bases. It keeps all of the Bouchet features described on this page.
- **Memory** (**Settings** > **Personalization**): facts the assistant remembers across chats. You can view and delete them there.
- **Settings:** theme, language, and many display options.

Workspace **Tools** and **Functions** (in the Admin Panel) let you add custom Python code to Open WebUI, including add-ons shared online. This code runs as you with full access to your files and is not limited like the Code Interpreter, so **only install code you trust**.

## Use your own models

You can add other model services under **Admin Panel** > **Settings** > **Connections**, using the service's address and your API key. Its models then appear in the model menu.

![Adding a connection](/img/ood_open_webui_add_connection.png){: .medium}

This also works with an [Ollama](ollama.md) server you run in your own Bouchet job.

!!! warning "Services outside YCRC"
    With a service outside YCRC, such as a commercial AI provider, your prompts and uploaded files are sent to that provider. Follow the [data classification guidance for commercial AI services](commercial-coding-agents.md) before sending research data.

When a model from a service outside YCRC wants to look something up on Bouchet or run code, the chat pauses and asks you to **Allow** or **Deny** each step, because the results (for example, the contents of a file) would be sent to that provider. **Deny** answers without the data. To stop being asked in a chat, open the **+** menu, choose **Tool Permissions**, and select **Full access**. This applies to that chat only; new chats ask again. Models hosted by YCRC, and your own models running on Bouchet, never ask.

## Your data

- Your chats, settings, and uploaded files are stored in your home directory (`~/.open-webui`). Only you can see them, and they are available in every session.
- Files the assistant creates are saved in `~/openwebui-outputs`.
- **Temporary Chat** (in the model menu) is not saved.
- To share a chat, use **Download** in the chat's menu (as PDF, text, or JSON). Share links are turned off because they would stop working when your session ends.
- To export all chats, or delete chats or uploaded files, use **Settings** > **Data Controls**.

## Limits and good practice

- **The model is shared by all users.** At busy times responses can be slower, and each user can have a limited number of requests in progress at a time.
- **Check important facts.** The assistant can be wrong, including about policies and limits. Confirm anything important in these docs or with [YCRC](https://docs.ycrc.yale.edu/#get-help).
- **Not available:** web search and image generation.
- Some Admin Panel settings are managed by YCRC and are reset each time you launch, including the connection to the YCRC model, code execution, and the default skills and tools. Changes you make to your own connections, models, and preferences are kept.

## Troubleshoot

### "You already have an Open WebUI session"

Only one session can run at a time. Connect to the existing session from **My Interactive Sessions**, or delete it and launch again.

### "Open WebUI doesn't use GPUs"

GPU partitions and GPU options in **Additional job options** are not available for Open WebUI. Choose a CPU partition and remove the GPU options.

### A banner says your Python environment can't run code

The environment you chose doesn't have `ipykernel`, or the modules couldn't be loaded. Code runs in the default environment until you fix it as the banner describes and relaunch.

### "Your message didn't reach the model"

Send the message again. This can happen if you send a message immediately after opening a chat.

### "Lost connection"

Open WebUI reconnects automatically within a few seconds. If it doesn't, reload the page.

### "This model's maximum context length is ..."

The chat, together with its attachments, is longer than the model can read at once. Start a new chat, or for large knowledge bases use the approach described in [Knowledge bases](#knowledge-bases).
