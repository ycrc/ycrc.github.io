# AlphaFold

[AlphaFold](https://github.com/google-deepmind/alphafold3) is a machine learning system
developed by Google DeepMind that predicts a protein’s 3D structure from its amino acid sequence.

As of November 11, 2024, there are two versions of AlphaFold generally available:
[AlphaFold 2](https://github.com/google-deepmind/alphafold2) and [AlphaFold 3](https://github.com/google-deepmind/alphafold3).
Both versions are available as cluster modules, but are run somewhat differently. AlphaFold 3 is the version under the most current development, but version 2 remains available for existing workflows or result consistency.

Note that given the duration and resources usually involved in running AlphaFold, it should generally be executed using [batch scripts](/clusters-at-yale/job-scheduling/#batch-jobs) unless explicitly testing parameter

Additionally, due to the [Idle Resources Policy](/clusters-at-yale/job-scheduling/job_defense/),
AlphaFold jobs should be split into two parts.  The first stage of AlphaFold involves generating
Multiple Sequence Alignments (MSAs), which uses only CPUs.  These MSAs are then used as input
for the model-building step, which uses GPUs. To avoid having your job flagged for idle GPUs,
submit a job for the MSA calculation, and when that is complete, submit another job for modeling.

## AlphaFold 3

AlphaFold 3 on the YCRC clusters has one especially significant difference from AlphaFold 2:
the model parameter [Terms of Use](https://github.com/google-deepmind/alphafold3/blob/main/WEIGHTS_TERMS_OF_USE.md).
BEFORE RUNNING, you must obtain your own copy of the parameters file (not all the datafiles).
This requires registering with [Google](https://forms.gle/svvpY4u2jsHEwWYS6) and agreeing to the above terms of use.
Once you have obtained your copy of the parameters, place the file in a "models" folder in your working folder.

You will need an input sequence file in JSON format:
```
{
  "name": "Job name goes here",
  "modelSeeds": [1, 2],  # At least one seed required.
  "sequences": [
    {"protein": {...}},
    {"rna": {...}},
    {"dna": {...}},
    {"ligand": {...}}
  ],
  "bondedAtomPairs": [...],  # Optional.
  "userCCD": "...",  # Optional, mutually exclusive with userCCDPath.
  "userCCDPath": "...",  # Optional, mutually exclusive with userCCD.
  "dialect": "alphafold3",  # Required.
  "version": 4  # Required.
}
```
See [AlphaFold 3 input documentation](https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md#top-level-structure) for details about the settings. An example of a simple protein 2-copy homomer  input is
```
{
  "name": "2PV7",
  "sequences": [
    {
      "protein": {
        "id": ["A", "B"],
        "sequence": "GMRESYANENQFGFKTINSDIHKIVIVGGYGKLGGLFARYLRASGYPISILDREDWAVAESILANADVVIVSVPINLTLETIERLKPYLTENMLLADLTSVKREPLAKMLEVHTGAVLGLHPMFGADIASMAKQVVVRCDGRFPERYEWLLEQIQIWGAKIYQTNATEHDHNMTYIQALRHFSTFANGLHLSKQPINLANLLALSSPIYRLELAMIGRLFAQDAELYADIIMDKSENLAVIETLKQTYDEALTFFENNDRQGFIDAFHKVRDWFGDYSEQFLKESRQLLQQANDLKQG"
      }
    }
  ],
  "modelSeeds": [1],
  "dialect": "alphafold3",
  "version": 1
}
```

Note that AlphaFold 3 will only run on A100 or better GPUs with at least 80 GB of VRAM by default.

In the event of memory problems on newer L40S cards with 48 GB, add the following environment variables to the relevant alphafold_model\.sh script before the command to run AlphaFold:
```
XLA_PYTHON_CLIENT_PREALLOCATE=false
TF_FORCE_UNIFIED_MEMORY=true
XLA_CLIENT_MEM_FRACTION=3.2
```
### Bouchet
On Bouchet, copy the MSA batch script and model batch script templates below. Then, edit the templates 
to in the indicated locations to specify filenames, paths and any specialized compute resources.
Finally, submit as follows. 

!!!note
    Below we give two methods to submit the second script: either
     (1) wait until the first script finishes; or 
     (2) submit it at the same time as the first script using a [job dependency](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/dependency/)

```sh
# Submit the first stage:
sbatch alphafold_msa.sh

# After the above job completes, submit alphafold_model.sh:
sbatch alphafold_model.sh

# Alternately, you can automate the second submission immediately after you do the first submission.
#  Do this by using the jobid that is reported by the alphafold_msa.sh submission:
sbatch --dependency=afterok:<first_stage_jobid> alphafold_model.sh
```

alphafold_msa\.sh: 

```sh
#!/bin/bash

####################
####################
# Modify the below assignments/directives for your specific job
 
## 1. Edit the below line to name your job:
#SBATCH --job-name=YourMSAJobNameHere

# 2. If needed, modify the below SBATCH directives
#    (the given values should work in most cases):

## General-use partition for CPU-only step
#SBATCH --partition=devel
## Maximum job time in Days-Hours:Minutes:Seconds
#SBATCH --time=2:00:00
## CPUs requested for each "task"; in simplest case the total number of used CPUs
#SBATCH --cpus-per-task=4
## Total memory; can also be expressed as --mem-per-cpu
#SBATCH --mem=32G
#SBATCH --mail-type=ALL

# 3. You need to provide input JSON file with the target protein sequence(s) and constraints
#  Give the name of that file here:
INPUTFILE="fold_input.json"

# 4. Edit below to specify the input folder name containing initial alphafold_input.json
INPUTFOLDER="your_protein_name_input"

# 5. Edit below to specify the output folder name for this (MSA) step:
MSAFOLDER="your_protein_name_msa"

# End of user edited script section
####################
####################

## Clear all loaded software modules, and load AlphaFold module
module reset

## Edit the following line to adjust the AlphaFold module version;
## search available versions via "module avail AlphaFold/"
module load AlphaFold/3.0.1-20251125-foss-2024a-CUDA-12.8.0

# Select full path to working directory
RUNDIR=`readlink -f ${PWD}`

mkdir -p ${RUNDIR}/${INPUT}
mkdir -p ${RUNDIR}/${MSAFOLDER}

# run AlphaFold
  alphafold \
  --jackhmmer_n_cpu=$((SLURM_CPUS_PER_TASK)) \
  --nhmmer_n_cpu=$((SLURM_CPUS_PER_TASK)) \
  --json_path=${INPUTFOLDER}/${INPUTFILE} \
  --model_dir=${RUNDIR}/models \
  --db_dir=$DB_DIR \
  --output_dir=$MSAFOLDER \
  --norun_inference
```

alphafold_model\.sh:

!!!note "Choosing the right GPU partition for alphafold_model\.sh"
    * For special GPU needs such as extra VRAM, please see the
      corresponding hardware specs for various gpu partitions available on
      your cluster via [this link](/clusters)
    * For small proteins that need more gpu runtime, try this:
        #SBATCH --partition=gpu
    * For intermediate sized proteins (VRAM 80-96GB) try this:
        #SBATCH --partition=gpu_h100,gpu_rtx6000
    * For larger proteins (VRAM 141-193GB) try this:
        #SBATCH --partition=gpu_b200,gpu_h200
    * On some cluster partitions, an additional constraint may be needed to request specific GPU types
      as described [here](/clusters-at-yale/job-scheduling/resource-requests/#request-specific-gpu-types).
      For example:
        #SBATCH --constraint "a100-80g"

```sh
#!/bin/bash

####################
####################
# Modify the below assignments/directives for your specific job

## 1. Edit the below line to name your job:
#SBATCH --job-name=YourModelJobNameHere

## 2. If needed, adjust the partition.
##    Note, the default partition provided below (gpu_devel) is fine for
##    short protein sequences (i.e. < 100 AA) with low VRAM needs and < 6 hour runtimes
#SBATCH --partition=gpu_devel

## 3. If needed, increase the number of GPUs (job will likely take longer to start)
#SBATCH --gpus=1

## 4. If needed, adjust other job parameters (max runtime, CPU, memory, mail-type)
## Maximum job time in Days-Hours:Minutes:Seconds
#SBATCH --time=6:00:00
## How many CPUs to give alphafold:
#SBATCH --cpus-per-task=4
## Total memory; can also be expressed as --mem-per-cpu
#SBATCH --mem=80G
#SBATCH --mail-type=ALL

# 5. Edit to specify the output folder you gave for the MSA run
MSAFOLDER="your_protein_msa"

# 6. Enter prefix of output from previous MSA run; e.g., MyPrefix_data.json
# This is given by the 'name:' field from your json input to the MSA step.
MSA="your_protein_name_field"

# 7. Optionally edit to specify name of final output folder for models
OUTPUT="${MSA}_output"

# End of user edited script section
####################
####################

## Clear all loaded software modules, and load AlphaFold module
module reset
## Edit to set desired AlphaFold module version;
## search available versions via "module avail AlphaFold/"
module load AlphaFold/3.0.1-20251125-foss-2024a-CUDA-12.8.0

# Select full path to current working directory
RUNDIR=`readlink -f ${PWD}`
mkdir -p ${RUNDIR}

mkdir -p ${RUNDIR}/${OUTPUT}

# run alphafold
alphafold \
  --jackhmmer_n_cpu=$((SLURM_CPUS_PER_TASK)) \
  --nhmmer_n_cpu=$((SLURM_CPUS_PER_TASK)) \
  --json_path=${MSAFOLDER}/${MSA}/${MSA}_data.json \
  --model_dir=models \
  --db_dir=$ALPHAFOLD_DATA_DIR \
  --output_dir=${MSA}_output \
  --norun_data_pipeline
```

The database location has been set automatically.

### McCleary
On McCleary, AlphaFold is installed in a [container](/clusters-at-yale/guides/containers), which requires
a somewhat more complicated script command for running the split version. Once your scripts are prepared,
submit them with sbatch the same was as described for Bouchet, above.

alphafold_msa\.sh (McCleary version):

```sh
#!/bin/bash

####################
####################
# Modify the below assignments/directives for your specific job
 
#SBATCH --job-name=YourMSAJobNameHere
## General-use partition for CPU-only step
#SBATCH --partition=day
## Maximum job time in Days-Hours:Minutes:Seconds
#SBATCH --time=1-00:00:00
## CPUs requested for each "task"; in simplest case the total number of used CPUs
#SBATCH --cpus-per-task=8
## Total memory; can also be expressed as --mem-per-cpu
#SBATCH --mem-per-cpu=80g
#SBATCH --mail-type=ALL

# Select full path to working directory
RUNDIR=`readlink -f ${PWD}`
cd $RUNDIR

# Edit to specify input folder name and filename for initial json
INPUTFOLDER="af_input"
INPUTFILENAME="alphafold_input.json"

# Edit to specify output folder name for MSA
MSAFOLDER="af_msa"

# End of user edited script section
####################
####################

## Clear all loaded software modules, and load AlphaFold module
module reset
module load AlphaFold/3.0.1

mkdir -p ${RUNDIR}/${INPUT}
mkdir -p ${RUNDIR}/${MSAFOLDER}

# run AlphaFold
apptainer exec \
  --bind $RUNDIR/${INPUTFOLDER}:/root/af_input \
  --bind $RUNDIR/${MSAFOLDER}:/root/af_msa \
  --bind $RUNDIR/models:/root/models \
  --bind $ALPHAFOLD_DATA_DIR:/root/public_databases \
  $EBROOTALPHAFOLD/AlphaFold.sif python /app/alphafold/run_alphafold.py \
  --jackhmmer_n_cpu=$((SLURM_CPUS_PER_TASK)) \
  --nhmmer_n_cpu=$((SLURM_CPUS_PER_TASK)) \
  --json_path=/root/af_input/${INPUTFILENAME} \
  --model_dir=/root/models \
  --db_dir=/root/public_databases \
  --output_dir=/root/af_msa \
  --norun_inference
```

alphafold_model\.sh (McCleary version):

```sh
#!/bin/bash

####################
####################
# Modify the below assignments/directives for your specific job
 
#SBATCH --job-name=YourModelJobNameHere

## General-use partition for accessing GPUs;
## may optionally try gpu_devel, as GPU step often takes < 6 hours
#SBATCH --partition=gpu
## Maximum job time in Days-Hours:Minutes:Seconds
#SBATCH --time=4:00:00
## CPUs requested for each "task"; in simplest case the total number of used CPUs
#SBATCH --cpus-per-task=8
## Total memory; can also be expressed as --mem-per-cpu
#SBATCH --mem=80g
## Must explicitly request GPU resources and number of GPUs
#SBATCH --gpus=1
#SBATCH --mail-type=ALL

# Select full path to current working directory
RUNDIR=`readlink -f ${PWD}`
cd ${RUNDIR}

# Edit to specify name of folder containing output from prior MSA run
MSAFOLDER="af_msa"

# Enter prefix of output from previous MSA run; e.g., MyPrefix_data.json
# This is usually based on the name: field from your initial input.
MSA="MyPrefix"

#Edit to specify name of final output folder for models
OUTPUT="${MSA}_output"

# End of user edited script section
####################
####################

## Clear all loaded software modules, and load AlphaFold module
module reset
module load AlphaFold/3.0.1

mkdir -p ${RUNDIR}/${OUTPUT}

# run alphafold
apptainer exec --nv \
  --bind $RUNDIR/${MSAFOLDER}/${MSA}:/root/af_msa \
  --bind $RUNDIR/${OUTPUT}:/root/af_output \
  --bind $RUNDIR/models:/root/models \
  --bind $ALPHAFOLD_DATA_DIR:/root/public_databases \
  $EBROOTALPHAFOLD/AlphaFold.sif python /app/alphafold/run_alphafold.py \
  --jackhmmer_n_cpu=$((SLURM_CPUS_PER_TASK)) \
  --nhmmer_n_cpu=$((SLURM_CPUS_PER_TASK)) \
  --json_path=/root/af_msa/${MSA}_data.json \
  --model_dir=/root/models \
  --db_dir=/root/public_databases \
  --output_dir=/root/af_output \
  --norun_data_pipeline
```


## AlphaFold 2

To run AlphaFold 2, you will need a sequence file in FASTA format for your macromolecule of interest. Note that this sequence format is different than the JSON format used AlphaFold 3 9which also takes different command flags).

Monomer:
```sh
>sequence_name
<SEQUENCE>
```

Homomer:
```sh
>sequence_1
<SEQUENCE>
>sequence_2
<SEQUENCE>
>sequence_3
<SEQUENCE>
...
```

Heteromer:
```sh
>sequence_1
<SEQUENCE A>
>sequence_2
<SEQUENCE A>
>sequence_3
<SEQUENCE B>
>sequence_4
<SEQUENCE B>
>sequence_5
<SEQUENCE B>
...
```
Copy the MSA batch script and model batch script templates below,
modify for your specific use case, and submit as follows. Below, we describe two methods
to submit the second script: either by waiting to submit until the first script finishes, or
simultaneously with the first script using a 
[job dependency](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/dependency/):

```sh
# Submit the first stage:
sbatch alphafold_msa.sh

# After the above job completes, submit alphafold_model.sh:
sbatch alphafold_model.sh

# Alternately, you can automate the second submission immediately after you do the first submission.
#  Do this by using the jobid that is reported by the alphafold_msa.sh submission.
#  Note also the use of 'afterany' rather than 'afterok', allowing alphafold_msa.sh to
#   'successfully crash':
sbatch --dependency=afterany:<first_stage_jobid> alphafold_model.sh
```

alphafold2_msa.sh

!!!note
    Due to the lack of a GPU, alphafold2_msa.sh will exit ungracefully --i.e., crash-- after creating the needed msa files; while obnoxious, this is harmless

```sh
#!/bin/bash

####################
####################
# Modify the below assignments/directives for your specific job

#SBATCH --job-name=YourMSAJobNameHere
## General-use partition for CPU-only step
#SBATCH --partition=day
## Maximum job time in Days-Hours:Minutes:Seconds
#SBATCH --time=1-00:00:00
## CPUs requested for each "task"; in simplest case the total number of used CPUs
#SBATCH --cpus-per-task=8
## Total memory; can also be expressed as --mem-per-cpu
#SBATCH --mem=80g
#SBATCH --mail-type=ALL

## Choose name for output folder    
export OUTDIR="MyOutputDir"

# End of user edited script section
####################
####################

## Clear all loaded software modules, and load AlphaFold module
module reset
module load AlphaFold/2.3.2-foss-2022b-CUDA-12.1.1

## Provide settings for running various components in parallel
export ALPHAFOLD_HHBLITS_N_CPU=${SLURM_CPUS_PER_TASK}   # defaults to 4 if not set
export ALPHAFOLD_JACKHMMER_N_CPU=${SLURM_CPUS_PER_TASK} # defaults to 8 if not set

## Remove old output folder and recreate for new run
rm -r ${OUTDIR}
mkdir -p ${OUTDIR}

## run AlphaFold
alphafold --output_dir=${OUTDIR} --model_preset=monomer --fasta_paths=YourSequence.fasta --max_template_date=2024-12-31
```

alphafold2_model.sh:

```
#!/bin/bash

####################
####################
# Modify the below assignments/directives for your specific job

#SBATCH --job-name=YourModelJobNameHere
## General-use partition for accessing GPUs
#SBATCH --partition=gpu
## Maximum job time in Days-Hours:Minutes:Seconds
#SBATCH --time=1-00:00:00
## CPUs requested for each "task"; in simplest case the total number of used CPUs
#SBATCH --cpus-per-task=8
## Total memory; can also be expressed as --mem-per-cpu
#SBATCH --mem=80g
## Must explicitly request GPU resources and number of GPUs
#SBATCH --gpus=1
## Require use of certain GPUs with extra memory for AlphaFold
#SBATCH --constraint "a100|rtx5000|a5000|rtx3090"

## Specify name for output folder that contains already-generated MSAs    
export OUTDIR="MyOutputDir"

# End of user edited script section
####################
####################

## Clear all loaded software modules, and load AlphaFold module
module reset
module load AlphaFold/2.3.2-foss-2022b-CUDA-12.1.1

## Provide settings for running various components in parallel
export ALPHAFOLD_HHBLITS_N_CPU=${SLURM_CPUS_PER_TASK}   # defaults to 4 if not set
export ALPHAFOLD_JACKHMMER_N_CPU=${SLURM_CPUS_PER_TASK} # defaults to 8 if not set

## run AlphaFold
alphafold --output_dir=${OUTDIR} --model_preset=monomer --fasta_paths=YourSequence.fasta --max_template_date=2024-12-31
--use_precomputed_msas
```

For a multimer in alphafold2, use a multimer input file and "--model_preset=multimer".

To run multiple sequences one after the other, specify the files as a comma-separated list;
e.g.,

```sh
--fasta_paths=YourSequence1.fasta,YourSequence2.fasta
```

When submitting an AlphaFold job, take into consideration [runtime as a 
function of sequence length](https://github.com/google-deepmind/alphafold?tab=readme-ov-file#alphafold-prediction-speed).

In the event of memory problems, add the following environment variables to alphafold2_model\.sh:
```
TF_FORCE_UNIFIED_MEMORY=1
XLA_PYTHON_CLIENT_MEM_FRACTION=0.5
XLA_PYTHON_CLIENT_ALLOCATOR=platform
```

For further information on running AlphaFold 2, see EMBL-EBI's
[online tutorial](https://www.ebi.ac.uk/training/online/courses/alphafold/).

