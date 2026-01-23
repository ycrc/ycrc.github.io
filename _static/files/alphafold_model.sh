#!/bin/bash

#SBATCH --job-name=alphafold-model
#SBATCH --partition=gpu
#SBATCH --gpus=1
#SBATCH --constraint "a100|rtx3090|rtx5000|a5000"
#SBATCH --out="slurm-alphafold-model-%j.out"
#SBATCH --time=2-00:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=8G
#SBATCH --mail-type=ALL

module load AlphaFold/2.3.2-foss-2020b-CUDA-11.3.1

export ALPHAFOLD_HHBLITS_N_CPU=${SLURM_CPUS_PER_TASK}
export ALPHAFOLD_JACKHMMER_N_CPU=${SLURM_CPUS_PER_TASK}
OUTPUT_DIR="MyOutputDir"

# run alphafold
alphafold --output_dir=${OUTPUT_DIR} \
                --model_preset=monomer \
                --fasta_paths=YourSequence.fasta \
                --max_template_date 2024-12-31 \
                --use_precomputed_msas
