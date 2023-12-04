=== "tensorflow 2.15"

	```bash
	module load miniconda

	conda create -n tf15 python=3.11.*

	pip install tensorflow[and-cuda]
	```

=== "tensorflow 2.14"

	Tensorflow 2.14 does not currently support gpu usage but can be installed using pip for cpu usage.

=== "tensorflow 2.13/2.12"

	```bash
	module load miniconda
	conda create --name tf-condacuda python numpy pandas matplotlib jupyter cudatoolkit=11.8.0 
	conda activate tf-condacuda
	pip install nvidia-cudnn-cu11==8.6.0.163

	# Store system paths to cuda libraries for gpu communication
	mkdir -p $CONDA_PREFIX/etc/conda/activate.d
	echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
	echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

	#install tensorflow
	pip install tensorflow==2.12.*

	```

=== "tensorflow 2.11"

	```bash
	module load miniconda
	conda create --name tf-condacuda python numpy pandas matplotlib jupyter cudatoolkit=11.3.1 cudnn=8.2.1
	conda activate tf-condacuda

	# Store system paths to cuda libraries for gpu communication
	mkdir -p $CONDA_PREFIX/etc/conda/activate.d
	echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

	#install tensorflow
	pip install tensorflow==2.11.*

	```
