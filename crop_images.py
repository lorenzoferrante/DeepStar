from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True, help='Path to directory to cut') # example 'data/RaFD/train/clothes/'
parser.add_argument('--crop_size', type=int, default=528, help='Size of cropped image') 

args = parser.parse_args()

for filename in os.listdir(args.path):
    if filename.endswith('.jpg'):
        img = Image.open(args.path + filename)
        crp = img.crop((0, 0, args.crop_size, args.crop_size))
        crp.save(args.path + filename)
