# The first example in the fastai book in Python

from fastai.vision.all import *
print(URLs.PETS)

path = untar_data(URLs.PETS)/'images'
#path = '/u/cfonze/.fastai/data/oxford-iiit-pet/images'
print(path)

def is_cat(x): return x[0].isupper()
dls = ImageDataLoaders.from_name_func(
    path, get_image_files(path), valid_pct=0.2, seed=42, 
    label_func=is_cat, item_tfms=Resize(224))

learn = cnn_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(1)


