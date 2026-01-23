#!/bin/bash

#SBATCH --job-name=alphafold-msa
#SBATCH --partition=day
#SBATCH --out="slurm-alphafold-msa-%j.out"
#SBATCH --time=1-00:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=8G
#SBATCH --mail-type=ALL

module load AlphaFold/2.3.2-foss-2022b-CUDA-12.1.1

export ALPHAFOLD_HHBLITS_N_CPU=${SLURM_CPUS_PER_TASK}
export ALPHAFOLD_JACKHMMER_N_CPU=${SLURM_CPUS_PER_TASK}
# Choose name for output folder
OUTPUT_DIR="MyOutputDir"
rm -rf ${OUTPUT_DIR}​
mkdir -p ${OUTPUT_DIR}

# run alphafold
alphafold --output_dir=${OUTPUT_DIR} \
                --model_preset=monomer \
                --fasta_paths=YourSequence.fasta \
                --max_template_date 2024-12-31 \
                --msas_only

