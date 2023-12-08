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
export GFDL_WORK=$PALMER_SCRATCH/gfdl_work
# directory for storing model output
export GFDL_DATA=$GIBBS_PROJECT/gfdl_data
```

## Update the Environment

Open `$HOME/programs/isca/src/extra/env/` and add the following after the first line (the starting with `echo`)

```
module restore isca
conda activate isca
```

## Select an Experiment and Update the Flags

We are using GCC version 10.x for this build, so [a slight modification needs to made to Isca for it to build](https://github.com/wrf-model/WRF/issues/1250). Add the following line to the experiment script (e.g. `$GFDL_BASE/exp/test_cases/held_suarez/held_suarez_test_case.py`), after `cb` is defined (so about line 13 in that file).


```
cb.compile_flags.extend(['-fallow-argument-mismatch', '-fallow-invalid-boz'])
```

## Run Isca

The above commands only need to be run once to set everything up. To use it, you will first always need to run:

```
module restore isca
conda activate isca
```

Then you should be able to compile and launch your ISCA models.