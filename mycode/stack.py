import numpy as np
import matplotlib.pyplot as plt

from myFrame import *
from myFrame.datasets import *

from sklearn.datasets import *
from sklearn.svm import SVC


data,label = make_moons(n_samples=1000,noise=0.13,random_state=20230109)

stack = Stack(
    modelTypeList=[
        TreeClassifier(max_depth=5),
        SVC()
    ]
)
modelList = (
    Pipe(
        endModel=stack,
        preprocessing=[ToClosest(destinations=np.array([0,1]))]
    ),
    TreeClassifier(max_depth=5),
    SVC()
)

for index,model in enumerate(modelList):
    model.fit(data, label)
    predict = model.predict(data)
    print(model.__class__.__name__,":",acc(label,predict))
    drawDots(data, predict,location=(3,2,2 * index + 1))
    drawBetween(predict, label,location=(3,2,2 * index + 2))

plt.show()