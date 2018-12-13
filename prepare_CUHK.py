'''
=================================
用来处理并读取CUHK3数据集
reference: http://docs.h5py.org/en/latest/quick.html#install

---------------------------------
@inproceedings{li2014deepreid,
  title={DeepReID: Deep Filter Pairing Neural Network for Person Re-identification},
  author={Li, Wei and Zhao, Rui and Xiao, Tong and Wang, Xiaogang},
  booktitle={CVPR},
  year={2014}
}
---------------------------------
=================================
'''
import pandas as pd
import numpy as np
import torch
import scipy.io as sio
import h5py

path='/home/liangzi/cuhk03_release/cuhk-03.mat'  #数据集存放的地址
cuhk03=h5py.File(path,'r')
#print(list(cuhk03.keys())) #查看结构
name1=list(cuhk03.keys())
# 所得结果为： ['#refs#', 'detected', 'labeled', 'testsets']
# the cuhk03 is a group(in other words,a dictionary),
# but the detected is a data set(in other words,a numpy array)

refs=cuhk03[name1[0]]
detected=cuhk03[name1[1]]
labeled=cuhk03[name1[2]]
testsets=cuhk03[name1[3]]
#print(detected.shape) # the shape is : (1,5)
#print(detected.dtype) # the type is : object
print(detected[0][1])
print(cuhk03.name)



