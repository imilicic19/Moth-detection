import os
import random
import splitfolders

data_path = "images"
output_path = 'moth_images_splited'

splitfolders.ratio(data_path, output=output_path,
    seed=1337, ratio=(.75, .15, .1), group_prefix=None, move=False) 

