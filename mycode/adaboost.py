from copy import deepcopy

import numpy as np
import sklearn

from myFrame import *
from myFrame.datasets import *


data,label = loadWatermelon()
data,label = Encoding([0,1,2,3,4,5],withLabel=True).fit(data,label)
data = data[:,6:]
epoch = 5
modelType = TreeClassifier(max_depth=1)
model = Adaboost(
    modelType = modelType,
    n_model=10
)
# model = modelType
model.fit(data,label)
predict = model.predict(data)

print(predict)
print(label)
# print(model.tree)
# drawDots(data, model.predict(data),location=131)
# drawDots(data,label,location=133)
# drawDots(data,label == model.predict(data),location=132)
# plt.show()



# data,label = sklearn.datasets.make_blobs(n_samples=10000,
#                             n_features=2,
#                             centers=2,
#                             cluster_std=1.5,
#                             center_box=(-5.0, 5.0),
#                             shuffle=True, random_state=2023)
# data,label = Standard().fit(data,label)


# func = lambda e:np.log((1 / e) - 1) / 2
# x = np.linspace(0, 1,1000)
# plt.plot(x,func(x))
# plt.show()

