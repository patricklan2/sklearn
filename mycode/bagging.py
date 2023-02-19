import numpy as np
import matplotlib.pyplot as plt
from myFrame import *
from myFrame.datasets import *

data,label = load_iris()
# linear = Pipe(
#     endModel=LinearRegression(),
#     preprocessing=[Standard(),ToClosest(destinations=np.array([0,1,2]))]
# )
# model = Bagging(modelType=linear,n_model=100)
# model.fit(data,label)
# predict = model.predict(data)
# # linear.fit(data,label)
# # predict = linear.predict(data)
# # predict = model.predict(data)
# drawBetween(predict,label)
# plt.show()

model = RandomForest(50,max_depth=2)
model.fit(data,label)
predict = model.predict(data)
drawBetween(predict,label)
plt.show()

