# Group Change

On cluster other than Bouchet or Hopper, when your PI is changed, the primary group of your account on the cluster will also be changed. 
As a result, you will have a new storage space on the cluster which belongs to the new group, including Home, Project, Scratch,
etc.

We will change the primary group of your cluster account to the new group and will move all the files stored in your 
old storage space into the new storage space. However, some local installations most likely will not be able to work 
properly after being moved. In particular, Conda environments and R packages will fail. You need to rebuild them  
in your new space under the new group.

For R packages, you just need to reinstall them with `install.packages()`. 

## Rebuild a Conda Environment after Group Change

We will use an example to illustrate how to rebuild a conda env after group change. Assume the conda env is 
originally installed in `/gpfs/gibbs/project/oldgrp/user123`,
and we want to move it to the project directory of the new group. 

First, find the paths of the conda env stored in your old space that you want to rebuild in the new space.  
Set two environment variables CONDA_ENVS_PATH and CONDA_PKGS_DIRS to the paths.
```bash
module load miniconda
export CONDA_ENVS_PATH=/gpfs/gibbs/project/oldgrp/user123/conda_envs
export CONDA_PKGS_DIRS=/gpfs/gibbs/project/oldgrp/user123/conda_pkgs
conda activate myenv
conda env export > myenv.yml
conda deactivate
```

Now, start a new login session, submit an interactive job, and rebuild the conda env in your new storage space.
When a new session starts, CONDA_ENVS_PATH and CONDA_PKGS_DIRS will be set to the right locations by the system, 
so you don't have to set them explicitly. 
```bash
ssh grace
salloc
module load miniconda
conda env create -f myenv.yml
```
