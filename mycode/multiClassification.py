from copy import deepcopy
from myFrame import *
from myFrame.datasets import *
import numpy as np
import matplotlib.pyplot as plt


data,label = load_iris()
model = MultiClassification(
    modelType=TreeClassifier(max_depth=2)
)
drawDots(data,label)
plt.show()
model.fit(data,label)
# print(model.getPossibility(data))
predict = model.predict(data)
drawBetween(predict,label)
plt.show()
print(predict)