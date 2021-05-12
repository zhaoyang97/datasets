

## 简介

本项目旨在减少收集各种数据集的时间成本，提供各种数据集的配置文件及其获取方式，数据集已开放在Titan_Xp_4的目录/root/commonfile/data
* 可在mmlab系列框架上使用
* 如果用其他框架，任然可以使用本项目的数据集获取方式

<br>
目前已支持以下数据集：

分类
- [x] imagenet

目标检测
- [x] coco
- [x] voc
- [] tct

语义分割
- [x] ade20k
- [x] cityscapes
- [x] pascal context
- [x] ddr
- [x] idrid


## 使用方法
以mmdetection为例，介绍配置coco数据集的方式：

### 1. 在mmdetection的同级目录下创建data文件夹

```plain
pathto
├── data
├── mmdetection
│   ├── mmdet
│   ├── tools
│   ├── configs
│   │   ├── _base_
│   │   │   ├── datasets
```

### 2. 添加配置文件
将[coco_detection.py](detection/coco_detection.py)放到目录pathto/mmdetection/configs/\_base\_/datasets/下

### 3. 传数据集到data目录

TODO 由于内网无法访问rtx 2080 决定把数据集都传到xp4上

scp -P your_port -r root@122.207.108.1:/root/commonfile/data/coco pathto/data/


scp -P 19710 -r root@122.207.82.55:/root/commonfile/data/coco ./


### 其他数据集的获取方式
scp -P your_port -r root@122.207.108.1:/root/commonfile/data/dataset_floder pathto/data/

把your_port换成自己的xp4账号对应的端口,pathto/data/换成第一步中新建的data文件夹目录，各个数据集对应的dataset_floder如下（数据集：对应的dataset_floder）：
* imagenet: imagenet
* coco: coco
* voc: voc0712
* tct: ../TCTAnnotatedData
* ade20k: ade20k
* cityscapes：cityscapes
* pascal context：voc0712
* ddr：DDR  
* idrid: IDRID



## 说明
可能需要修改的地方：
每卡的图像改这个参数：samples_per_gpu

提供的DDR和IDRiD数据集是做过数据增广后的数据集，包括旋转90°、180°、270°、水平翻转、垂直翻转，算上原图一共是6倍。

## 注意事项

### 学习率的设置

#### imagenet
imagenet数据集默认的是8卡、每卡32图，学习率=0.01。学习率的设置：
lr = 0.01 \* [卡数] \* [每卡图像] / (8\*32). <br>
例如用8卡、每卡64图，那么学习率应该设为0.01/2=0.005。

### tct
tct数据集只提供了图像，注释文件需要自己放入对应目录。
TODO 收集tct的注释文件
