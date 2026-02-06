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
