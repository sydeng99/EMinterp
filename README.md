# EM interpolation

This repo is for EM interpolation (given **registered** EM images). The method comes from the video frame interpolation algorithm “Video frame interpolation via adaptive separable convolution”.



## Dependencies

- python3 
- pytorch 0.4 (later versions may wrok)
- Numpy
- Scipy
- Cupy



## Docker image

```
docker pull registry.cn-hangzhou.aliyuncs.com/shiyu_666/cuda9.0-cudnn7-devel-ubuntu16.04-torch0.4:v1
```

**installation**

> ```
> cd ./libs/sepconv
> bash install.bash
> pip install attrdict
> pip install tensorboardX
> pip install tifffile
> pip install joblib
> ```



## Training

Training images should be saved as:

> 0001_1.png
>
> 0001_2.png
>
> 0001_3.png
>
> ...
>
> 4000_1.png
>
> 4000_2.png
>
> 4000_3.png

Note that `xxx_1.png, xxx_2.png, xxx_3.png` are consequent registered three images.



The training code should be:

```python
cd ./scripts_interp
python gen_data_txt.py -f ../data/train_data/
python main_ms.py -c=ms_l1loss_decay
```



## Testing

```python
cd ./scripts_interp
python inference_singleImage.py -c=ms_l1loss_decay -id=interp -i1=/PATH/IMAGE1.png -i2=/PATH/IMAGE2.png -o=/PATH/OUTPUT.png
```



## Reference

[1]. Niklaus, S., Mai, L., Liu, F.: Video frame interpolation via adaptive separable convolution. In: 2017 IEEE International Conference on Computer Vision (ICCV). pp. 261–270 (2017)
