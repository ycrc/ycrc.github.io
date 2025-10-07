# Large Language Models (LLMs) on Research Computing Hardware

The YCRC's research computing infrastructure can be used to run localized version of LLM models. 

Running LLMs locally has the following advantages:

 - User data inputted into model is more secure as local LLM models don't have online access and aren't sharing inputted information with any public entity.
 - Localized LLMs provide users with the flexibility to control which model/version is implemented, increasing research efficiency
 - YCRC GPUs are free of charge and can currently run models up to 320 GB of vRAM.

## GPU availability on YCRC Resources

Once you have your LLM program setup, you can run the models on any of our GPU partitions (gpu_devel, gpu, and gpu_scavenge for McCleary and Grace, or gpu and scavenge for Milgram).

The YCRC clusters have a variety of GPUs available to be used for LLMs. Depending on the GPU used, the amount of memory (vRAM) can vary significantly. Depending on the process, a researcher's desired LLM model may not run without a large enough GPU.
LLMs are designed to automatically detect multiple GPUs on the same node and all of the HPC's GPU nodes contain four GPUs. This means that if a researcher requests 4 a100-80g GPUs, they will receive 320 GB of GPU memory (80 GB x 4).

In depth details about the type of GPUs, number of nodes with GPUs, memory capabilities, and GPU architecture can be found at the respective webpages for [McCleary](https://docs.ycrc.yale.edu/clusters/mccleary/), [Grace](https://docs.ycrc.yale.edu/clusters/grace/), and [Milgram](https://docs.ycrc.yale.edu/clusters/milgram/).
Navigate down to the header, Public Partitions, and choose the gpu or gpu_devel partition to see available hardware.

A quick summary of maximum GPU memory available on a single node and total number of other GPUs available  for each cluster is also displayed here:

| Cluster      | Largest GPU  | Maximum vRam (Four GPUs) | Total Available  | Number of other GPUs available |
|--------------|--------------|--------------------------|------------------|--------------------------------|
| Bouchet      | h200         | 560 GB                   | 80               | 40                             |
| Grace        | a100-80g     | 320 GB                   | 16               | 132                            |
| McCleary     | a100-80g     | 320 GB                   | 12               | 92                             |
| Milgram      | h100         | 320 GB                   | 12               | 8                              | 

It is important to note the number of GPUs that are available on the cluster. Our largest GPUs only account for 30% of the GPU capability on the YCRC research computing infrastructure.
The YCRC's hardware operates on a scheduling based system where users request resources and wait in a queue until said resources are available. 
**Requesting larger GPUs will have longer wait time due to increased demand among researchers**. Therefore, it is suggested to start a research process with a lower precision model that
can fit on smaller GPUs. This will provide quicker access to resources and a faster troubleshooting method. Once confident in the operation of the research process, researchers can upgrade their model precision/size for more accurate results if necessary while avoiding wasting resources/time on failed jobs.

## Choose a local LLM

There are hundreds of different LLMs available for download in both [huggingface](https://huggingface.co/models) and [ollama](https://ollama.com/search).
Each of which use a specific amount of vRAM (GPU memory). These models usually have this naming format - Model_Name_#B where #B represents the number of parameters the
model was trained on, i.e., 7B = 7 Billion parameters. For inference (direct communication with the model like ChatGPT), then only enough vRAM to load the model is required. This table displays the general vRAM requirements for common parameters without any quantization:

| Parameter Size      | Inference vRAM (GB)  |
|---------------------|----------------------|
| 7B                  | ~10-16               |
| 13B                 | ~20-24               |
| 30B                 | ~40-60               |
| 70B                 | ~80+                 |
| 305B                | ~400+                |

Researchers can find the specific vRAM needed by clicking on the model of interest on the respective huggingface or ollama model page. These pages also include additional
information about what the model is for. 

Additionally, each of these models have been trained on a specific set of parameters. Instead of using general purpose models like llama3.3:70B, researchers may find better
success in searching for models in their specific field (law, chemistry, etc). Researchers can enter their subject of interest on the ollama or huggingface model page and find
models specific to their field. These models have the additional advantage of normally being smaller than the general purpose models, which will give greater flexibility
to resource requirements.

If you are unsure how much vRAM you need to load a model, you could launch the model on a larger GPU and use our job monitoring application, [jobstats](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/jobstats/) to see how much vRAM you are using.
### What about Retrieval Augmented Generation(RAG) and Fine-Tuning?

If interested in doing more complex methods with LLM such as RAG or fine-tuning, then additional vRAM will be required. This table displays general vRAM requirements for said methods:

| Method              | additional vRAM (GB) |
|---------------------|----------------------|
| Inference           | 0                    |
| RAG                 | ~10(<30B)-30+        |
| Fine-tuning         | 3 - 5x inference     |
| Fine-tuning(QLoRA)  | 10-20% inference     |
| create from scratch | 1000s

The key things to note in the table above are:

 - any additional modification to LLMs will require additional vRAM on GPUs
 - researchers should avoid the high cost of traditional fine-tuning and use cost-effective methods such as [QLoRA](https://medium.com/@amodwrites/a-definitive-guide-to-qlora-fine-tuning-falcon-7b-with-peft-78f500a1f337)
 - creating models from scratch isn't a feasible approach and likely won't compare to existing models available for download

##Running LLMs on the cluster

Now that we have selected our model and understand what our resource requirements are, we can finally move on to actually running the LLM of interest.

Researchers can run LLMs using interactive or batch submissions. The key differences between interactive submissions and batch submissions can be found in our [Intro to HPC video](https://www.youtube.com/watch?v=SaiXaC0jRjE)
Starting at the 37 minute mark of the video.

It is recommended to start your research with interactive sessions and then once common bugs have been eliminated, to move to batch submissions where stronger resources are available.

By default, Slurm provisions GPU requests with available GPUs having the lowest vRAM. LLMs often require more vRAM than the smallest GPU available, so they won't run on the GPU Slurm provides by default.

For example, say your LLM needs 16 GB of vRAM and you request a single GPU. If the smallest available GPU in your partition has 11 GB (e.g., an rtx2080ti), Slurm may give you this GPU by default. This would cause your job to fail due to a lack of vRAM.

In this case, you can specify GPUs with more vRAM using the `--constraint` flag. In the example above, you could specify rtx5000 or v100 GPUs, which have more vRAM.


```bash
#####interactive
salloc --partition gpu_devel --constraint="rtx5000|v100"

#####submission script
#SBATCH --constraint="rtx5000|v100"
```

if you are using ollama, you are now ready to go. We have ollama as a module, so you can simply type:

```bash
module load ollama
```

and Ollama will be ready to run on the allocated GPUs. Please scroll down to Interactive submissions to see how to run Ollama.

##Installing HuggingFace to run LLMs

Users can use HuggingFace inside of a miniconda environment/jupyter notebook.

```bash
###Miniconda requires uses to be on a compute node. You can either use salloc (below) or start an OOD remote desktop session
###requests 2 cpus for 1 hour and 32 GB of memory on the devel partition
salloc --partition=devel --cpus-per-task=2 --time=1:00:00 --mem=32G ###requests 2 cpus for 1 hour and 32 GB of memory on the devel partition
module load miniconda
conda create --name huggingface python=3.11.* transformers accelerate tokenizers datasets jupyter jupyterlab

###need pytorch installed to use huggingface
conda activate huggingface
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124 --force

###load into jupyter notebook application on OOD
module reset
ycrc_conda_env.sh update
```

### Interactive Submissions

To run HuggingFace interactively, it is recommended to use our Jupyter Notebook application on [Open on Demand](https://docs.ycrc.yale.edu/clusters-at-yale/access/ood/). However, you could also run inside a python script with similar syntax
For Ollama, using a terminal is the cleanest method to run an interactive session. The steps for running both methods are below:

--8<-- "snippets/LLMruninteractive.md"

###Batch submissions

Once your research is ready for batch submissions, there are only some small modifications required to convert your process.

For HuggingFace, you can employ a method called [papermill](https://docs.ycrc.yale.edu/clusters-at-yale/access/ood-jupyter/) under the header of Command-Line Execution of Jupyter Notebooks.

For Ollama, you can submit an inference request like so:

```bash
#######launch the ollama server, the & tells it to run in the background, allowing the script to continue
module reset
module load ollama

ollama serve &

######make slurm wait 10 seconds before advancing in the script, this gives the necessary time to launch the LLM server
######this time may need updating for larger models, llama 3.3:70b requires 60 seconds for example
sleep 10

######runs the LLM model 3.1 with the prompt, why is the sky blue and passes the response into a file called response.txt
ollama run llama3.1 why is the sky blue > response.txt
```

For Ollama, it is necessary to output the prompts response into a separate file because Slurm is unable to convert some of the symbols that are outputted in the traditional .out file from a batch submission.
