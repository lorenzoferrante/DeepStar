#!/bin/sh

python3 main.py --mode test \
                --dataset RaFD \
                --rafd_crop_size 64 \
                --image_size 64 \
                --c_dim 2 \
                --rafd_image_dir data/RaFD/test \
                --sample_dir stargan_custom/samples \
                --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models \
                --result_dir stargan_custom/results