# DeepStar
From https://github.com/yunjey/stargan

## REQUIREMENTS
- Python 3.5+
- PyTorch 0.4.0+
- TensorFlow 1.3+

## TRAIN
```sh
python3 main.py --mode train \
                --dataset RaFD
                --rafd_crop_size 128 \
                --image_size 128 \
                --c_dim 2 \
                --rafd_image_dir data/RaFD \
                --sample_dir stargan_custom/samples \
                --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models \
                --result_dir stargan_custom/results \
                --model_save_step 30 \
                --num_iters 30
```

## TEST
```sh
python3 main.py --mode test \
                --dataset RaFD \
                --rafd_crop_size 128 \
                --image_size 128 \
                --c_dim 2 \
                --rafd_image_dir data/RaFD/test \
                --sample_dir stargan_custom/samples \
                --log_dir stargan_custom/logs \
                --model_save_dir stargan_custom/models \
                --result_dir stargan_custom/results
```
