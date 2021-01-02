# learn-fastai

## Environment setup

```bash
conda create --name learn-fastai python=3.7 -y
conda activate learn-fastai 
conda install -c fastai -c pytorch fastai -y
conda install -c conda-forge jupyterlab -y
conda install -c anaconda psutil 
conda install -c fastai fastbook
conda install -c conda-forge sentencepiece 
conda clean --tarballs
```

To check the size of your home directory:

```bash
du -sh ~
```

To remove the env use the following command:

```bash
conda env remove -n learn-fastai
```
