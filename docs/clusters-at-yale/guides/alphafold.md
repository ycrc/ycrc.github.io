# AlphaFold

[AlphaFold](https://github.com/google-deepmind/alphafold) is a machine learning system
developed by Google DeepMind that predicts a protein’s 3D structure from its amino acid sequence.

As of November 11, 2024, there are two versions of AlphaFold generally available:
AlphaFold 2 and [AlphaFold 3](https://github.com/google-deepmind/alphafold3).
Both versions are available as cluster modules, but are run somewhat differently.

Note that given the duration and resources usually involved in running AlphaFold,
it should be executed using [batch scripts](/clusters-at-yale/job-scheduling/#batch-jobs).

Additionally, due to the [Idle Resources Policy](/clusters-at-yale/job-scheduling/job_defense/),
AlphaFold jobs should be split into two parts.  The first stage of AlphaFold involves generating
Multiple Sequence Alignments (MSAs), which uses only CPUs.  These MSAs are then used as input
for the model-building step, which uses GPUs. To avoid having your job flagged for idle GPUs,
submit a job for the MSA calculation, and when that is complete, submit another job for modeling.

## AlphaFold 2

To run AlphaFold 2, you will need a sequence file in FASTA format for your macromolecule of interest.

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
and modify for your specific use case. Both stages can be submitted at the same time using a
[job dependency](https://docs.ycrc.yale.edu/clusters-at-yale/job-scheduling/dependency/)
as follows:

```sh
# Submit the first stage:
sbatch alphafold_msa.sh

# Note the jobid that is reported by the above submission.
# Then if you have set the correct input directories corresponding to the MSA outputs,
# optionally submit the second stage by:
sbatch --dependency=afterok:<first_stage_jobid> alphafold_model.sh
# Note that you can also submit alphafold_model.sh in the normal way after alphafold_msa.sh completes. 
```

alphafold_msa.sh:

```sh
#!/bin/bash
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

## Clear all loaded software modules, and load AlphaFold module
module reset
module load AlphaFold/2.3.2-foss-2022b-CUDA-12.1.1

## Provide settings for running various components in parallel
export ALPHAFOLD_HHBLITS_N_CPU=${SLURM_CPUS_PER_TASK}   # defaults to 4 if not set
export ALPHAFOLD_JACKHMMER_N_CPU=${SLURM_CPUS_PER_TASK} # defaults to 8 if not set
## Choose name for output folder    
export OUTDIR="MyOutputDir"

## Remove old output folder and recreate for new run
rm -r ${OUTDIR}
mkdir -p ${OUTDIR}

## run AlphaFold
alphafold --output_dir=${OUTDIR} --model_preset=monomer --fasta_paths=YourSequence.fasta --max_template_date=2024-12-31
--msas_only
```

alphafold_model.sh:

```
#!/bin/bash
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

## Clear all loaded software modules, and load AlphaFold module
module reset
module load AlphaFold/2.3.2-foss-2022b-CUDA-12.1.1

## Provide settings for running various components in parallel
export ALPHAFOLD_HHBLITS_N_CPU=${SLURM_CPUS_PER_TASK}   # defaults to 4 if not set
export ALPHAFOLD_JACKHMMER_N_CPU=${SLURM_CPUS_PER_TASK} # defaults to 8 if not set
## Specify name for output folder that contains already-generated MSAs    
export OUTDIR="MyOutputDir"

## run AlphaFold
alphafold --output_dir=${OUTDIR} --model_preset=monomer --fasta_paths=YourSequence.fasta --max_template_date=2024-12-31
--use_precomputed_msas
```

For a multimer, use a multimer input file and "--model_preset=multimer".

To run multiple sequences one after the other, specify the files as a comma-separated list;
e.g.,

```sh
--fasta_paths=YourSequence1.fasta,YourSequence2.fasta
```

When submitting an AlphaFold job, take into consideration [runtime as a 
function of sequence length](https://github.com/google-deepmind/alphafold?tab=readme-ov-file#alphafold-prediction-speed).

For further information on running AlphaFold 2, see EMBL-EBI's
[online tutorial](https://www.ebi.ac.uk/training/online/courses/alphafold/).

## AlphaFold 3

AlphaFold 3 on the YCRC clusters is currrently a work in progress.  Note that one signficant change
is the model parameter [Terms of Use](https://github.com/google-deepmind/alphafold3/blob/main/WEIGHTS_TERMS_OF_USE.md).
BEFORE RUNNING, you must obtain your own copy of the parameters file (not all the datafiles).
This requires registering with [Google](https://forms.gle/svvpY4u2jsHEwWYS6) and agreeing to the above terms of use.
Once you have obtained your copy of the parameters, place the file in a "models" folder in your working folder.

### Bouchet
On Bouchet, AlphaFold 3 is launched in a manner similar to 2, but with some modifications to the flags.

alphafold_msa.sh:

```sh
#!/bin/bash
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

## Clear all loaded software modules, and load AlphaFold module
module reset
module load AlphaFold/3.0.1-20251021-foss-2024a-CUDA-12.6.0

# Select full path to working directory
RUNDIR=`readlink -f ${PWD}`

# Edit to specify input folder name containing initial alphafold_input.json
INPUTFOLDER="af_input"

# Edit to specify filename of input JSON file
INPUTFILE="fold_input.json"

# Edit to specify output folder name for MSA
MSAFOLDER="af_msa"

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

alphafold_model.sh:

```sh
#!/bin/bash
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
#SBATCH --constraint "a100-80g"
#SBATCH --mail-type=ALL

## Clear all loaded software modules, and load AlphaFold module
module reset
module load AlphaFold/3.0.1-20251021-foss-2024a-CUDA-12.6.0

# Select full path to current working directory
RUNDIR=`readlink -f ${PWD}`
mkdir -p ${RUNDIR}

# Edit to specify name of folder containing output from prior MSA run
MSAFOLDER="af_msa"

# Edit to specify name of final output folder for models 
OUTPUT="af_output"

# Enter prefix of output from previous MSA run; e.g., MyPrefix_data.json
# This is usually based on the name: field from your initial input.
MSA="2PV7"

#Edit to specify name of final output folder for models
OUTPUT="${MSA}_output"

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
a somewhat more complicated command for running the split version.

alphafold_msa.sh (McCleary version):

```sh
#!/bin/bash
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

## Clear all loaded software modules, and load AlphaFold module
module reset
module load AlphaFold/3.0.1

# Select full path to working directory
RUNDIR=`readlink -f ${PWD}`
cd $RUNDIR

# Edit to specify input folder name and filename for initial json
INPUTFOLDER="af_input"
INPUTFILENAME="alphafold_input.json"

# Edit to specify output folder name for MSA
MSAFOLDER="af_msa"

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

alphafold_model.sh (McCleary version):

```sh
#!/bin/bash
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

## Clear all loaded software modules, and load AlphaFold module
module reset
module load AlphaFold/3.0.1

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

See the [AlphaFold 3 documentation](https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md) for details.

Note that AlphaFold 3 will only run on A100 or better GPUs by default.
To run on sequences up to 1280 on a V100 on McCleary, add to your 'alphafold' command the flag
```sh
--flash_attention_implementation=xla
```
