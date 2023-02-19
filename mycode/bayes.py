from sklearn import naive_bayes as nb
from sklearn.datasets import load_iris

from myFrame import *

# data,label = loadWatermelon()
# model = Pipe(
#     endModel=NaiveBayes(isContinuousList=[1,1,1,1,1,1,0,0]),
#     preprocessing=[Encoding(changeList=[0,1,2,3,4,5],withLabel=True)]
# )
# model.fit(data,label)
# predict = model.predict(data)

iris = load_iris()
data = iris.data
label = iris.target

model1 = nb.MultinomialNB()
model1.fit(data,label)
predict1 = model1.predict(data)
print(acc(predict1,label))
# drawBetween(predict1,label,location=121)
drawDots(data,predict1,location=121)

model=NaiveBayes()
model.fit(data,label)
predict = model.predict(data)
print(acc(predict,label))
# drawBetween(predict,label,location=122)
drawDots(data,predict,location=122)
plt.show()
