# Isca

Isca is a framework used for idealized global circulation modelling.
We recommend that you install it for yourself individually as the code expects to be able to modify its source code files.
It is relatively straighforward to install into a conda environment as described below.


## Install Isca

Install it for just your user as a Python [conda](/clusters-at-yale/guides/python/#conda-based-python-environments) environment called "isca".

```
module load netCDF-Fortran/4.5.3-gompi-2020b

module load miniconda  

module save isca  
mkdir ~/programs  
cd ~/programs  
git clone https://www.github.com/execlim/isca.git
conda create -n isca python=3.7

conda activate isca

conda install tqdm  

cd isca/src/extra/python  
pip install -e .
```

Then add the following to your `.bashrc` file

```
# Isca

# directory of the Isca source code
export GFDL_BASE=$HOME/programs/isca
# "environment" configuration for grace
export GFDL_ENV=gfortran
# temporary working directory used in running the model
export GFDL_WORK=$LOOMIS_SCRATCH/gfdl_work
# directory for storing model output
export GFDL_DATA=$LOOMIS_PROJECT/gfdl_data

```

## Run Isca

The above commands only need to be run once to set everything up. To use it, you will first always need to run:

```
module restore isca
conda activate isca
```

Then you should be able to compile and launch your ISCA models.