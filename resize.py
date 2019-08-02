from PIL import Image
import os

PATH_TRAIN = 'data/RaFD/train/clothes/'
PATH_TEST = 'data/RaFD/test/clothes/'

size = 128, 128

for filename in os.listdir(PATH_TRAIN):
    if filename.endswith('.jpg'):
        img = Image.open(PATH_TRAIN + filename)
        img = img.resize((128, 128), Image.ANTIALIAS)
        img.save(PATH_TRAIN + filename)
