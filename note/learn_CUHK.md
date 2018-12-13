# 学习CUHK数据集
## 存储文件格式
cuhk03.mat
## 基本性质
包含1467个不同的行人，有5对摄像头共同采集
## 数据集文件夹结构
CUHK-03
　　├── “detected”── 5 x 1 cell
　　　　　　　├── 843x10 cell
　　　　　　　├── 440x10 cell
　　　　　　　├── 77x10 cell
　　　　　　　├── 58x10 cell
　　　　　　　├── 49x10 cell
　　├── “labeled”── 5 x 1 cell
　　　　　　　├── 843x10 cell
　　　　　　　├── 440x10 cell
　　　　　　　├── 77x10 cell
　　　　　　　├── 58x10 cell
　　　　　　　├── 49x10 cell
　　├── “testsets”── 20 x 1 cell
　　　　　　　├── 100 x 2 double matrix
## 关于mat文件的理解
cell是一种特殊的可以看做用来进行分级的属性。比如这里面，5\*1个cell就表示他有5个cell，
然后每个cell里分别盛放这843\*10个、440*10个等等cell，然后每个cell里才是盛放的真正的文件。
## 子cell分析
首先，对于detected下的5个cell，分别代表摄像机组1、摄像机组2、摄像机组3、摄像机组4、摄像机组5
拍摄得到的图片集。
下面对每一个具体的摄像机下的图片进行分析：
对于每一个子cell，注意到都是一个数字乘以10的形式，比如843*10个cell，此处的命名规则为：
前面的1~843代表的是行人的id索引，前五列和后五列分别代表来自同一组的不同摄像头（即一个摄像机组有
两个摄像头），cell内存放的元素为H×W×3的张量（此张量相当于行人框图像）（类型为uint8），并且个别
图像可能会空缺——即为空集。
## testsets分析
相当于是重复了20次的一个100/*2的double类型的矩阵。
100/*2的double类型的矩阵，里面的100代表了100个测试样本，而列数中，第一个列里的数字代表了摄像
头组的数目索引，第二个列里的数据代表了行人的id索引。
## 目前计划
目前计划使用scipy进行读取，如果无法读取，就使用h5py等工具，总之正在尝试。
### 使用scipy
scipy无法读取，会报错：
```buildoutcfg
NotImplementedError: Please use HDF reader for matlab v7.3 files
```
### 使用h5py
首先利用下列方式进行安装
```bash
pip3 install h5py
#如果报错可以前面加sudo
```
然后使用的代码请见项目中的prepare_CUHK.py文件。






