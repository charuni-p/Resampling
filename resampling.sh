#!/usr/bin/env bash
#PBS -P e14
#PBS -l walltime=0:10:00
#PBS -l mem=7GB
#PBS -q normal
#PBS -l ncpus=1
#PBS -l wd
#PBS -l storage=gdata/e14+gdata/hh5+gdata/ub4
module use /g/data/hh5/public/modules
module load conda/analysis3-20.01
export YEAR=${YEAR:-2002}
python3 slhf.py

