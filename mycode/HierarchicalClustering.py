import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets
from myFrame import *

# noinspection PyShadowingNames
def loadData():
    seed = 20221231
    data,label = datasets.make_blobs(n_samples=2000, # 样本个数
                                     n_features=2, # 维度
                                     centers=5, # 类别数目
                                     cluster_std=1.5, # 方差
                                     center_box=(-10.0, 10.0), #
                                    shuffle=True, random_state=seed)
    return data,label

# data,label = loadData()
# model = AgglomerativeClustering(n_clusters=5,
#                                 affinity='euclidean', # 计算距离的方式：欧几里得
#                                 linkage='complete')
# model.fit(data)
#
# print(model.labels_)
#
# plt.figure(figsize=(10,10))
# plt.scatter(data[:, 0], data[:, 1], c=model.labels_, s=20)
# plt.show()



# data,label = loadData()
#
# # model = HierarchicalClustering(n_clusters=5,
# #                                distType="manhattan",)
# model = HierarchicalClustering(n_clusters=5,
#                                dtype='max')
# model.fit(data)
# predict = model.predict()
# # print(predict)
# drawDots(data,predict)
# # drawDots(model.means[model.means[:, 0] != float('inf')],"RED",s=50)
# plt.show()



