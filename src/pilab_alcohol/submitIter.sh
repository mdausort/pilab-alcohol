#!/bin/bash
#
#SBATCH --job-name=essai
#
#SBATCH --ntasks=8
#SBATCH --time=5:00:00
#SBATCH --mem-per-cpu=8000
#SBATCH --mail-type='FAIL'
#SBATCH --mail-user='manon.dausort@uclouvain.be'

#SBATCH --output='/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/Slurm/slurmJob_'$1'.out'
#SBATCH --error='/CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/Slurm/slurmJob_'$1'.err'

# python /CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/registration.py $1 $2 $3 $4 $5
# python /CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/utils.py $1 $2 $3
python /CECI/proj/pilab/PermeableAccess/alcooliques_As2Z4vF8GNv/Pipeline/analyse.py $1 $2 $3
