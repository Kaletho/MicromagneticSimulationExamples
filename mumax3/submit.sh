#!/bin/bash -l
#SBATCH -N 1
#SBATCH --partition=batch
#SBATCH -J coRelax 
#SBATCH -o coRelax.%J.out
#SBATCH -e coRelax.%J.err
#SBATCH --mail-user=your_email@whatever.com
#SBATCH --mail-type=ALL
#SBATCH --time=05:00:00
#SBATCH --mem=1G
#SBATCH --gres=gpu:1
#SBATCH --constraint=[rtx2080ti]

module load mumax/3.10

#run the application:
mumax3 ./coRelax.mx3

#convert results to vtk files
mumax3-convert -vtk binary ./coRelax.out/*.ovf

#delete the ovf files, I don't use them
rm ./coRelax.out/*.ovf
