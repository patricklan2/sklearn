import numpy as np
from sklearn import datasets


from myFrame import *

# # noinspection PyShadowingNames
# def loadData():
#     seed = 20221231
#     data,label = datasets.make_blobs(n_samples=100, # 样本个数
#                                      n_features=2, # 维度
#                                      centers=3, # 类别数目
#                                      cluster_std=1.2, # 方差
#                                      center_box=(-10.0, 10.0), #
#                                     shuffle=True, random_state=seed)
#     return data,label

# noinspection PyShadowingNames
# def loadData():
#     seed = 20221231
#     data,label = datasets.make_blobs(n_samples=1000, # 样本个数
#                                      n_features=2, # 维度
#                                      centers=5, # 类别数目
#                                      cluster_std=1.5, # 方差
#                                      center_box=(-10.0, 10.0), #
#                                     shuffle=True, random_state=seed)
#     return data,label

# data,label = loadData()
# model = KMean(5,40)
# model.fit(data)
# predict = model.predict(data)
# drawDots(data,label)
# plt.show()