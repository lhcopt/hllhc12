#!/bin/bash
if [ $# -lt 1 ]; then
  echo "This script needs as an argument the fortran file which needs to be compiled"
  exit
fi

file=$1

gfortran -m32 -static -O3 -L. $file -lkernlib -o ${file%.f}
