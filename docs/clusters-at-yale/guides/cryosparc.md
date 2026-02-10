# CryoSPARC on the YCRC Clusters

## Install

As of February, 2026, the YCRC is transitioning to a new CryoSPARC workflow. If you would like to use this program on the clusters, please [contact us](/#get-help). 

!!!warning
     For now (February 2026) please avoid installing CryoSPARC 5.0 or later on the clusters.
     It contains a breaking change to our cluster management scripts. We are working on a solution.

!!!warning
     If you are installing a version of CryoSPARC older than 4.4.0, add the additional line

     ``` bash
     --cudapath $cuda_path \
     ```

     after the --ssdpath line.

## Run (2/10/2026 - Experimental)

*For beta testers provided with our `cryosparc-cluster-master.sh` script*: here is a preliminary description and walk-through on how to use it.

Please note, in contrast to our previous cryosparc workflow, the new method *does not use GPU's in the batch script*. Required resources for the script `cryosparc-cluster-master.sh` are minimal and should not be modified. The only change to the #SBATCH directives that may be needed are the running time and partition. Also note, 'worker' nodes are no longer part of this workflow.

To use the new cryosparc workflow, please use the the following steps:

1. **To start your cryosparc server**, submit the 'cryosparc-cluster-master.sh' script using `sbatch cryosparc-cluster-master.sh`. With the script, you may (optionally) change the '#SBATCH -t <time>' and '#SBATCH -p <partition>' directive lines to specify the running time and slurm partition to reflect how long you expect your workflow to take. The default request of 7 days on the 'week' partition, with 1 CPU and 8GB of RAM, should be fine.

2. **To interact with your cryosparc server**, launch a minimal [OnDemand Remote Desktop](/clusters-at-yale/access/ood-remote-desktop) session; 1 CPU, 8GB RAM on the 'devel' partition should suffice. There is no need to request more time than you expect to use your browser for, as you can always launch another Remote Desktop and get back to where you were with no information loss.

3. **When submitting analysis tasks on your cryosparc server**, please note that you will now have several compute lanes to choose from, including 'cpu', 'gpu' and possibly others. The cryosparc GUI will prompt you to select one of these choices after you first click 'submit job' after building the job.

    Cryosparc will then work through the YCRC slurm system to assign your task to an available YCRC compute node. You may then monitor your job through cryosparc itself, and also through the YCRC slurm tools (i.e. 'User Portal' from the OOD Utilities menu, or by the terminal command 'squeue --me').


## Topaz support (Optional)

[Topaz](https://cb.csail.mit.edu/cb/topaz/) is a pipeline for particle picking in cryo-electron microscopy images using
convolutional neural networks. It can optionally be used from inside CryoSPARC using our cluster module.

### 1. In an interactive cluster session, prepare an executable bash script 'topaz.sh' that loads our topaz module and runs topaz:

```
#!/usr/bin/env bash
if command -v conda > /dev/null 2>&1; then
    conda deactivate > /dev/null 2>&1 || true  # ignore any errors
    conda deactivate > /dev/null 2>&1 || true  # ignore any errors
fi
unset _CE_CONDA
unset CONDA_DEFAULT_ENV
unset CONDA_EXE
unset CONDA_PREFIX
unset CONDA_PROMPT_MODIFIER
unset CONDA_PYTHON_EXE
unset CONDA_SHLVL
unset PYTHONPATH
unset LD_PRELOAD
unset LD_LIBRARY_PATH

module load topaz/0.2.5-fosscuda-2020b
exec topaz $@
```

### 2. Make the topaz.sh script executable:
```
chmod a+x <PATH-TO>/topaz.sh
```
   
### 3. In a running CryoSPARC instance, add the executable '<PATH-TO/topaz.sh' to the General settings:
![](/img/TopazCryosparc.png)

### 4. Consult the [CryoSPARC guide](https://guide.cryosparc.com/processing-data/all-job-types-in-cryosparc/deep-picking/topaz)
for details on using Topaz with CryoSPARC.

## Troubleshoot

If you are unable to start a new CryoSPARC instance, the likeliest reason is leftover files from a previous run that was not shut down properly. Check /tmp and /tmp/${USER} for the existence of a cryosparc*.sock file or a mongo*.sock file.  If they are owned by you, you can just remove them, and CryoSPARC should start normally.  If they are not owned by you, and you have reserved the GPUs, then it is likely due to another user's interrupted job.  Contact YCRC staff for assistance.


If your database won't start and *_you're sure_* there isn't another server running, you can remove lock files and try again.

``` bash
# rm -f $CRYOSPARC_DB_PATH/WiredTiger.lock $CRYOSPARC_DB_PATH/mongod.lock
```
