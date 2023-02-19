import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

# noinspection PyShadowingNames
def drawGrid(start,end,span,matrix,c="GREEN",linewidth=1,**kw):
    x = np.arange(start,end,span)
    k = len(x)
    grid_x, grid_y = np.meshgrid(x, x)
    grid = np.insert(grid_x.reshape(-1, 1), 1, grid_y.flat, axis=1)
    grid_new = np.dot(grid, matrix).reshape(k, k, 2)
    for i in range(k):
        plt.plot(grid_new[:, i, 0], grid_new[:, i, 1], c=c, linewidth=linewidth,**kw)
        plt.plot(grid_new[i, :, 0], grid_new[i, :, 1], c=c, linewidth=linewidth,**kw)


# noinspection PyShadowingNames
def loadData():
    X, Y= datasets.make_regression(n_samples=100, # n_samples：样本个数
                            n_features=1,# n_features：输入数据的维度，这里是1维x轴
                            n_targets=1,# n_targets：输出数据的维度，这里是1为y轴
                            bias=5,# bias：数据偏置大小
                            noise=100,# noise：叠加的噪声大小
                            shuffle=True,
                            random_state=20230102)# random_state：随机种子
    return np.insert(X, 0, Y, axis=1)

# noinspection PyShadowingNames
def generatorNormal(mu1,mu2,sigma1,sigma2,count):
    array = np.random.randn(count, 2)
    array[:,0] = array[:,0] * np.sqrt(sigma1) + mu1
    array[:,1] = array[:,1] * np.sqrt(sigma2) + mu2
    return array

# noinspection PyShadowingNames
def pca(data,k):
    u,s,v = np.linalg.svd(data,full_matrices=0)
    return np.dot(data,v.T[:,0:k]),u,s,v

# noinspection PyShadowingNames
def discoverData(Z,v,k):
    v_reduce = v[:,0:k]
    return np.dot(Z,v_reduce.T)

data = loadData()
data = StandardScaler().fit_transform(data)
Z,s,u,v = pca(data,1)
drawGrid(-5,6,1,v)
discover = discoverData(Z,v,1)
plt.scatter(data[:,0],data[:,1])
plt.scatter(discover[:,0],discover[:,1],c="RED")

plt.show()

