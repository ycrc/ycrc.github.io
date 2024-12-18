# AlphaFold

[AlphaFold](https://github.com/google-deepmind/alphafold) is a machine learning system
developed by Google DeepMind that predicts a protein’s 3D structure from its amino acid sequence.

As of November 11, 2024, there are two versions of AlphaFold generally available:
AlphaFold 2 and [AlphaFold 3]((https://github.com/google-deepmind/alphafold3).
Both versions are available as cluster modules, but are run somewhat differently.

Note that given the duration and resources usually involved in running AlphaFold,
it should be executed using a [batch script](/clusters-at-yale/job-scheduling/#batch-jobs).

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

Copy or download the [batch script template](/docs/_static/files/alphafold_monomer.sh)
and modify for your specific use case.

```sh
#!/bin/bash
#SBATCH --job-name=YourJobNameHere
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
module purge
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

