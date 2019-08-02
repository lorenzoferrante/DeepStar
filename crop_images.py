from PIL import Image
import os

PATH_TRAIN = 'data/RaFD/train/clothes/'

PATH_TEST = 'data/RaFD/test/clothes/'

for filename in os.listdir(PATH_TRAIN):
    if filename.endswith('.jpg'):
        img = Image.open(PATH_TRAIN + filename)
        crp = img.crop((0, 0, 528, 528))
        crp.save(PATH_TRAIN + filename)
