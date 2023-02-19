import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeRegressor

from myFrame.datasets import *

# noinspection PyShadowingNames
def loadData():
    data =  make_relationship(100,noise=0.05)
    return data[:,0],data[:,1]

data,label = loadData()
data = data.reshape(-1,1)

# noinspection PyShadowingNames
class BoostingTree:
    def __init__(self):
        self.treeList = []

    def append(self,DTModel):
        self.treeList.append(DTModel)

    def predict(self,data):
        result = np.zeros(len(data))
        for treeModel in self.treeList:
            result = result + treeModel.predict(data)
        return result

# modelList = BoostingTree()
# e = np.array(label)
# for i in range(10):
#     model = DecisionTreeRegressor(max_depth=5)
#     model.fit(data,e)
#     modelList.append(model)
#     e = label - modelList.predict(data)
#
# print(e)
# plt.scatter(data,e)
# plt.show()

gradientBoostingRegressor = GradientBoostingRegressor(max_depth=5,n_estimators=10,learning_rate=0.5)
gradientBoostingRegressor.fit(data,label)
predict = gradientBoostingRegressor.predict(data)
plt.scatter(data,predict - label)
plt.show()