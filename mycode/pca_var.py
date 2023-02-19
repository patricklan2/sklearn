from myFrame import *
from myFrame.datasets import *

# covMatrixList,muList = np.array([[[3,4],[4,9]]]),np.array([[30,40]])
# data,label = createMulGaussData(covMatrixList=covMatrixList,
#                                 muList=muList)

data,label = load_iris()
# pca = PCAByCov(2)
# data,label = pca.fit(data,label)
# tree = TreeClassifier(max_depth=5)
# tree.fit(data,label)
# print(tree.tree)
# predict = tree.predict(data)
# print(predict)
model = Pipe(
    endModel=TreeClassifier(max_depth=5),
    preprocessing=[PCAByCov(2)],
    moreInformation=True
)
model.fit(data,label)
print(model.endModel.tree)
predict = model.predict(data)
print(predict)
for i in model.process:
    print(i)
# drawDots(predict,'green')
drawDots(model.preprocess(data),label,location=221)
drawDots(model.preprocess(data),predict,location=222)
drawBetween(predict,label,location=212)
plt.show()
