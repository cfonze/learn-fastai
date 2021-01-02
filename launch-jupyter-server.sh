#! /bin/bash
# Launches a LSF job (jupyter-server-job.sh) with 10G of memory, 10G memory limit, V100 GPUs, on the x86_6h queue.

rm log.txt
bsub -q x86_6h -R "rusage[mem=10000]" -M 10GB -gpu "num=1:gmodel=TeslaV100_SXM2_32GB:mode=exclusive_process:gmem=32510MB" -o ~/github.com/cfonze/learn-fastai/log.txt ~/github.com/cfonze/learn-fastai/jupyter-server-job.sh
