# learn-fastai

This repository is a collection of my notes and Jupyter notebooks I used during learning fastai

* [Deep Learning for Coders with Fastai and PyTorch (Amazon)](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch/dp/1492045527)
* [Practical Deep Learning for Coders 2020 (Youtube)](https://youtube.com/playlist?list=PLfYUBJiXbdtRL3FMB3GoWHRI8ieU6FhfM)
* [fastbook (github)](https://github.com/fastai/fastbook)

My environment is a LSF cluster of several hundred GPU nodes.  I use Anaconda to manage Python packages in my environment.  I am also using Jupyter notebooks for learning.

[fastai docs](https://docs.fast.ai)

## Environment setup

Create a new Anaconda environment and install the required packages. 

```bash
conda create --name learn-fastai python=3.7 -y
conda activate learn-fastai 
conda install -c fastai -c pytorch fastai -y
conda install -c conda-forge jupyterlab -y
conda install -c anaconda psutil 
conda clean --tarballs
```

To remove this env use the following command:

```bash
conda env remove -n learn-fastai
```

By default, Anaconda installs the packages in the environments in your home directory.  If your home directory is limited in space, you may want to place your environments in a different location.  Also note that the dataloaders of fastai, place the data (by default) in the ```<your home directory>/.fastai``` so you may also want to change that.

To check the size of your home directory:

```bash
du -sh ~
```

### Optional

```bash
conda install -c fastai fastbook
conda install -c conda-forge sentencepiece 
```

## Launching and using a Jupyter Notebook server

Activate the Anaconda environment ```conda activate learn-fastai``` then use the ```launch-jupyter-server.sh``` shell script.  The script launches a LSF job which executes the ```jupyter-server-job.sh``` shell script on the node chosen by LSF.  Once the job launches, use the LSF ```bpeek``` command to get the output of the job which has the jupyter server url.  Use the browser on your local system to point to that url.
