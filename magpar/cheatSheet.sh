#!/bin/bash
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=8
#SBATCH --partition=batch
#SBATCH -J simulation_name
#SBATCH -o simulation_name.%J.out
#SBATCH -e simulation_name.%J.err
#SBATCH --mail-user=your_mail
#SBATCH --mail-type=ALL
#SBATCH --time=72:00:00
#SBATCH --mem=250G

# load virtualmicromagnetics with singularity
module load singularity/3.6

# Enable mpi 
module load openmpi/4.0.3
# Enable infiniband
export OMPI_MCA_btl=openib
export OMPI_MCA_btl_openib_allow_ib=1
#export SINGULARITYENV_MAGPAR_USE=""
#export SINGULARITYENV_OMP_NUM_THREADS=1

# replace "1seg" with the name of your simulation

#echo Mesh generation with gmsh 3.0.6
# use gmsh 3.0.6!!!
/path/to/gmsh-3.0.6-Linux64/bin/gmsh -3 1seg.geo -format msh2 -algo del3d -optimize_lloyd 100 -o 1seg.msh &> gmeshing.txt
#echo done!

# -algo: Select mesh algorithm (meshadapt, del2d, front2d, delquad, del3d, front3d, mmg3d, pack)
# del3d has worked best with cylinders

#echo Converting to inp with magpar tools...

# Change the second line of .msh file ($MeshFormat) from 
# 2.2 0 8
# to
# 2.1 0 8
vi ./1seg.msh -c ':2 s/2.2 0 8/2.1 0 8/ | wq'

singularity exec /path/to/virtualmicromagnetics /opt/magpar/magpar-0.9/src/tools/gmsh/gmshtoucd.py 1seg.msh &> toInp.txt
#echo done!

echo You can inspect mesh in paraview using the MeshQuality filter

# Edit your allopt.txt and .krn files

echo Runnig magpar
# run magpar as 
mpirun -np 8 -N 8 singularity exec /home/morenoja/magparSimuFiles/virtualmicromagnetics /opt/magpar/magpar-0.9/src/magpar.exe &> magparOut.txt
# notice that there is no reference to "project" .krn and .inp should have the same name
echo simulation complete!

echo Postprocessing...
# if there was a sampling line in your allopt.txt
singularity exec /path/to/virtualmicromagnetics /opt/magpar/magpar-0.9/src/tools/shutil/mkdat.sh 1seg.0001.datmsh *.d
# will create dat files with values sampled (NOT AVERAGED) through that line

# To build the inp to visualize the magnetization in paraview:
singularity exec /path/to/virtualmicromagnetics /opt/magpar/magpar-0.9/src/tools/shutil/mkinp.sh 1seg.0001.femsh *.gz
echo done!

