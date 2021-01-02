#! /bin/bash
rm log.txt
bsub -q x86_6h -R "rusage[mem=10000]" -M 10GB -gpu "num=1:gmodel=TeslaV100_SXM2_32GB:mode=exclusive_process:gmem=32510MB" -o ~/github.ibm.com/cfonze/learn-fastai/log.txt ~/github.ibm.com/cfonze/learn-fastai/jupyter-server-job.sh
