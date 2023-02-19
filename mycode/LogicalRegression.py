import sklearn

from myFrame import *
from myFrame.datasets import *
import matplotlib.pyplot as plt




# data,label = loadWatermelon()
# data,label = Encoding([],withLabel=True).fit(data[:,6:8],label)
# data,label = Standard().fit(data,label)
#
# model = LogicalRegression()
# model.fit(data,label)
# predict = model.predict(data)
# print(predict)
# print(label)
# plt.subplot(121)
# plt.scatter(data[:,0],data[:,1],c=label)
# plt.subplot(122)
# plt.scatter(data[:,0],data[:,1],c=predict)
# # plt.grid(True)
# plt.show()

# x,y = np.random.randn(5000).reshape(-1,1) * 2,np.random.randn(5000) * 2
# example = np.insert(x,1,y,axis=1)
# predict = model.predict(example)
# plt.scatter(x,y,c=predict,)
# plt.grid(True)
# plt.show()

data,label = sklearn.datasets.make_blobs(n_samples=10000,
                            n_features=2,
                            centers=2,
                            cluster_std=1.5,
                            center_box=(-5.0, 5.0),
                            shuffle=True, random_state=2023)
data,label = Standard().fit(data,label)
model = LogicalRegression()
model.fit(data,label)
predict = model.predict(data)
print(predict)
print(label)
plt.subplot(121)
plt.scatter(data[:,0],data[:,1],c=label,s=1)
plt.subplot(122)
plt.scatter(data[:,0],data[:,1],c=predict,s=1)
plt.show()
