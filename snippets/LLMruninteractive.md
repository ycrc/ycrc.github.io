=== "ollama"

    ```bash
    ###request compute node with GPU (add --Constraint=GPUTYPES if needed)
    salloc --partition=gpu_devel --cpus-per-task=1 --time=4:00:00 --mem=5G --gpus=1  
    
    ###load ollama module if it isn't loaded
    module load ollama

    ####launch server to access models. The & symbol causes the server to run in the background of the allocated node
    ollama serve&

    #####hit enter to proceed for more input
    ###run model of interest, replace llama3.2:3b with model of interest
    ollama run llama3.2:3b

    ###enter prompts
    why is the sky blue?
    ```

=== "huggingface"

    ```bash
    ###request an OOD session using Jupyter notebook using these steps:
    1. Click the first dropdown box (Environment Setup) and select your conda environment with HuggingFace installed. If you can't find it, please refer to the installation instructions above.
    2. Under Partitions, select GPU_devel
    3. If specific GPUs are needed, check the box, select check the box to view more options, and enter your constraint command under Additional job options
    4. Click launch session
    
    At this point, you should now have a running session in OOD. You can then open your notebook and start a new script and load your model like so:

    ###inside the notebook
    ####import necessary python functions
    ###this will vary depending on the model being used. Refer to the huggingface website use this model button for explicit instructions for a model.
    from transformers import pipeline, AutoModelForCausalLLM, AutoTokenizer

    ###set tokenizer and model to download LLM, can replace distilgpt2 with preferred model
    tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
    model = AutoModelForCausalLM.from_pretrained("distilgpt2")

    ###specify task for LLM model, in this case, we are generating text
    generator = pipeline(task="text-generation", model=model, tokenizer=tokenizer)
    
    # Use model to generate text
    generator("Three Rings for the Elven-kings under the sky, Seven for the Dwarf-lords in their halls of stone")
    ```
