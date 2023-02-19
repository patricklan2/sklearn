import numpy as np
from myFrame.datasets import *
from myFrame import *

covMatrixList = np.array([[[1, 0.5], [0.5, 2]],[[5, -0.5],[-0.5, 4]],[[3, -0.5],[-0.5, 4]]])
muList = np.array([[10,6],[-10,-8],[0,0]])
data,label = createMulGaussData(covMatrixList,muList = muList,numList=10000)
# drawDots(data,label,s=5)
# plt.show()


model = GaussClusters(3,100)
model.fit(data)
predict = model.predict(data)
print(predict)

print(model.muList)
drawDots(data,predict,s=1)
drawDots(model.muList,"RED",s=20)
plt.show()