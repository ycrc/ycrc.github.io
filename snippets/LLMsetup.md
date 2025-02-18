=== "huggingface"

    ```bash
    ###Miniconda requires uses to be on a compute node. You can either use salloc (below) or start an OOD remote desktop session
    ###requests 2 cpus for 1 hour and 32 GB of memory on the devel partition
    salloc --partition=devel --cpus-per-task=2 --time=1:00:00 --mem=32G ###requests 2 cpus for 1 hour and 32 GB of memory on the devel partition
    module load miniconda
    conda create --name huggingface python=3.11.* transformers accelerate tokenizers datasets jupyter jupyterlab

    ###need pytorch installed to use huggingface    
    conda activate huggingface    
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

    ###load into jupyter notebook application on OOD
    module reset
    ycrc_conda_env.sh update
    ```

=== "ollama"

    ```bash
    ###Create directory to store executable
    mkdir ollama
    cd ollama
    curl -L https://ollama.com/download/ollama-linux-amd64.tgz -o ollama-linux-amd64.tgz
    tar -xvf ollama-linux-amd64.gz
    ###turn ollama into executable
    chmod +x bin/ollama
    ```
