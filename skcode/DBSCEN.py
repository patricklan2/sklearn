import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io
from sklearn.cluster import DBSCAN
from sklearn import datasets

# noinspection PyShadowingNames
def loadData():
    seed = 20221231
    data,label = datasets.make_blobs(n_samples=1000, # 样本个数
                                     n_features=2, # 维度
                                     centers=5, # 类别数目
                                     cluster_std=1, # 方差
                                     center_box=(-10.0, 10.0), #
                                    shuffle=True, random_state=seed)
    return data

data = loadData()

model = DBSCAN(eps=0.8,
               min_samples=5,
               metric='euclidean', # 计算距离的方式：欧几里得
               )
model.fit(data)
print(model.labels_)

plt.figure(figsize=(10,10))
plt.scatter(data[:, 0], data[:, 1], c=model.labels_,s=10)
plt.show()