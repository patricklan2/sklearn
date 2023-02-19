import matplotlib.pyplot as plt

from myFrame.datasets import *
from myFrame import *


# data,label = loadBoston()
# # data = StandardScaler().fit_transform(data)
# model = Pipe(
#     endModel = LinearRegression(recursion=True,n_recursion=1000,lr = 0.12),
#     preprocessing=[Standard()]
# )
# # model = LogicalRegression(recursion=True,n_recursion=1000,lr = 0.00001)
# model.fit(data,label)
# predict = model.predict(data)
# print(getLoss(predict,label))
#
# e = label - predict
# e_sort = np.argsort(e)
# plt.scatter(range(len(predict)),label[e_sort],c="RED",s = 2)
# plt.scatter(range(len(predict)),predict[e_sort],c="GREEN",s = 2)
# plt.plot(range(len(predict)),e[e_sort])
# plt.grid(True)
# plt.show()



# data = np.linspace(-10,0,100000)
# # label = data * 7.5 + np.random.randn(len(data))
# label = data * 7.5 + 10
# # plt.scatter(data,label)
# data = data.reshape(-1,1)
# model = Pipe(
#     endModel=LinearRegression(recursion=False),
#     preprocessing=[Standard()]
# )
# model.fit(data,label)
# predict = model.predict(data)
# plt.plot(range(len(predict)),label)
# plt.plot(range(len(predict)),predict)
# plt.show()
# print(getLoss(predict,label))



# data,label = load_iris()
# model = Pipe(
#     endModel=LinearRegression(recursion=False),
#     preprocessing=[Standard(),
#                    ToClosest(destinations=np.array([0,1,2]))]
# )
# model.fit(data,label)
# predict = model.predict(data)
# print(predict)
# plt.scatter(range(len(predict)),label,c="RED",s = 20)
# plt.scatter(range(len(predict)),predict,c="GREEN",s = 20)
# plt.plot(range(len(predict)),label - predict)
# plt.grid(True)
# plt.show()


# x = np.random.randn(10000).reshape(-1,1) * 3
# y = np.random.randn(10000) * 3
# data = np.insert(x,1,y,axis=1)
# destinations =np.array([[0,3],[-2,-2],[2,-2]])
# model = ToClosest(destinations=destinations,
#                   distType="Manhattan")
# predict = model.reprocessForPredict(data)
# label = model.choose
# plt.scatter(x,y,c=label,s=1)
# plt.grid(True)
# plt.show()

data,label = loadBoston()
linear = LinearRegression()
cross = Pipe(
     endModel = CrossValidation(modelType=linear,epoch=10),
     preprocessing=[Standard(withLabel=True)]
)
model = cross
model.fit(data,label)
predict = model.predict(data)
drawBetween(predict,label)
plt.show()
# print(getLoss(predict, label))
# print(predict)
