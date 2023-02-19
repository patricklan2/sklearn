import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

from myFrame import *
from myFrame.datasets import *

# noinspection PyShadowingNames
def loadData():
    seed = 20221231
    data,label = datasets.make_blobs(n_samples=1000, # 样本个数
                                     n_features=2, # 维度
                                     centers=5, # 类别数目
                                     cluster_std=1.5, # 方差
                                     center_box=(-15.0, 15.0), #
                                    shuffle=True, random_state=seed)
    return data,label
data,label = loadData()

model = DensityBasedCluster(minPts=9,mu=1.3)
model.fit(data)
predict = model.predict()
drawDots(data,predict)
plt.show()