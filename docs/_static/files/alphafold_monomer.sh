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
