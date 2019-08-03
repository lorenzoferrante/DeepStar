from PIL import Image
import numpy as np
import argparse
import os
import cv2
import imageio

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True, help='Path to directory to resize') # example 'data/RaFD/train/clothes/'
parser.add_argument('--size', type=int, required=True, help='Size of image (square)') # example 128

args = parser.parse_args()

for filename in os.listdir(args.path):
    if filename.endswith('.jpg') and not (filename.endswith('_flipped.jpg') or filename.endswith('_left_shif.jpg') or filename.endswith('_right_shif.jpg') or filename.endswith('_up.jpg') or filename.endswith('_noise.jpg')):
        img = Image.open(args.path + filename)
        img = np.array(img)


        # FLIP
        flipped_img = np.fliplr(img)
        real_filename, file_extension = os.path.splitext(args.path + filename)
        imageio.imwrite(real_filename + '_flipped' + file_extension, flipped_img)

        # LEFT SHIFT
        for i in range(args.size, 1, -1):
            for j in range(args.size):
                if (i < args.size-5):
                    img[j][i] = img[j][i-5]
                elif (i < args.size-1):
                    img[j][i] = 0
        real_filename, file_extension = os.path.splitext(args.path + filename)
        imageio.imwrite(real_filename + '_left_shif' + file_extension, img)


        # RIGHT SHIFT
        for j in range(args.size):
            for i in range(args.size, 1, -1):
                if (i < args.size-2):
                    img[j][i] = img[j][i-2]
        real_filename, file_extension = os.path.splitext(args.path + filename)
        imageio.imwrite(real_filename + '_right_shif' + file_extension, flipped_img)

        # UP
        for j in range(args.size):
            for i in range(args.size):
                if (j < args.size - 2 and j > 2):
                    img[j][i] = img[j+2][i]
                else:
                    img[j][i] = 0
        real_filename, file_extension = os.path.splitext(args.path + filename)
        imageio.imwrite(real_filename + '_up' + file_extension, flipped_img)

        """
        # NOISE
        noise = np.random.randint(15, size = (args.size, args.size, 3), dtype = 'uint8')

        for i in range(args.size):
            for j in range(args.size):
                for k in range(3):
                    if (img[i][j][k] != 255):
                        img[i][j][k] += noise[i][j][k]
        real_filename, file_extension = os.path.splitext(args.path + filename)
        imageio.imwrite(real_filename + '_noise' + file_extension, flipped_img)
        """