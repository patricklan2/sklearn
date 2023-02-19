import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

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

# data = loadData()
data = generatorNormal(-5,5,5,10,10000)
data = np.dot(data,np.array([[1,0],[1,1]]))
model = PCA(n_components=1)
resultData = model.fit_transform(data)

print("主成分的个数:",model.n_components)
print("贡献比:",model.explained_variance_ratio_)
print("特征的方差:",model.explained_variance_)

recover = model.inverse_transform(resultData)

plt.scatter(data[:,0],data[:,1],s=1)
plt.scatter(recover[:,0],recover[:,1],c="RED",s=1)
plt.show()