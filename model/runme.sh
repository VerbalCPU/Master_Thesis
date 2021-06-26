#!usr/bin/env bash
# select gpu devices
export CUDA_VISIBLE_DEVICES=0

python -m CHR.main |& tee -a log
 
