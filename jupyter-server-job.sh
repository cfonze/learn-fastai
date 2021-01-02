#! /bin/bash
# Launches the Jupyter notebook server

conda activate learn-fastai
cd /u/cfonze/github.com/cfonze/learn-fastai
jupyter notebook --no-browser --ip=* --port=9898

