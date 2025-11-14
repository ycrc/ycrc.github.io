=== "tensorflow 2.16+"

    ```bash
    module load miniconda
    conda create -n tf_VERSION python=3.11.*
    pip install tensorflow[and-cuda]==2.x.* ###change x to reflect tensorflow version, i.e., 2.17.*
    
    #tensorflow can't find cuda libraries, need to tell it
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'NVIDIA_DIR=$(dirname $(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)")))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    echo 'for dir in $NVIDIA_DIR/*; do     if [ -d "$dir/lib" ]; then         export LD_LIBRARY_PATH="$dir/lib:$LD_LIBRARY_PATH";     fi; done' 

    ####make changes permanent
    conda deactivate 

    conda activate tf16
    ```

=== "tensorflow 2.15"

    ```bash
    module load miniconda
    conda create -n tf15 python=3.11.*
    pip install tensorflow[and-cuda]==2.15.*
    ```

=== "tensorflow 2.14"

    ```bash
    module load miniconda
    conda create -n tf14 python=3.11.*
    conda activate tf14
    pip install tensorflow==2.14.0 nvidia-cuda-runtime-cu11==11.8.89 nvidia-cublas-cu11==11.11.3.6 nvidia-cufft-cu11==10.9.0.58 nvidia-cudnn-cu11==8.7.0.84 nvidia-curand-cu11==10.3.0.86 nvidia-cusolver-cu11==11.4.1.48 nvidia-cusparse-cu11==11.7.5.86 nvidia-nccl-cu11==2.16.5 nvidia-cuda-cupti-cu11==11.8.87 nvidia-cuda-nvcc-cu11==11.8.89

    # Store system paths to cuda libraries for gpu communication
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

    #deactivate and reactivate environment to permanently keep cuda libraries
    conda deactivate
    conda activate tf14    

    ```

=== "tensorflow 2.13/2.12"

    ```bash
    module load miniconda
    conda create --name tf-condacuda python=3.11.* numpy pandas matplotlib notebook cudatoolkit=11.8.0 
    conda activate tf-condacuda
    pip install nvidia-cudnn-cu11==8.6.0.163

    # Store system paths to cuda libraries for gpu communication
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

    #install tensorflow
    pip install tensorflow==2.12.*
    
    #deactivate and reactivate environment to permanently keep cuda libraries
    conda deactivate
    conda activate tf-condacuda
    ```

=== "tensorflow 2.11"

    ```bash
    module load miniconda
    conda create --name tf-condacuda python=3.10.* numpy pandas matplotlib notebook cudatoolkit=11.3.1 cudnn=8.2.1
    conda activate tf-condacuda

    # Store system paths to cuda libraries for gpu communication
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

    #install tensorflow
    pip install tensorflow==2.11.*

    #deactivate and reactivate environment to permanently keep cuda libraries
    conda deactivate
    conda activate tf-condacuda
    ```
