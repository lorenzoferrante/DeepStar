from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True, help='Path to directory to resize') # example 'data/RaFD/train/clothes/'
parser.add_argument('--new_size', type=int, default=128, help='Size of output image')

args = parser.parse_args()

for filename in os.listdir(args.path):
    if filename.endswith('.jpg'):
        img = Image.open(args.path + filename)
        img = img.resize((args.new_size, args.new_size), Image.ANTIALIAS)
        img.save(args.path + filename)
