import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# from sklearn.impute import SimpleImputer

# noinspection PyShadowingNames
def loadData():
    data_watermelon = pd.read_csv("watermelon3_0.csv")
    change = {"是": 0, "否": 1}
    data, label = data_watermelon.values[:, 7:9], LabelEncoder().fit_transform(data_watermelon.values[:, 9])
    label[label == 0] = -1
    return data,label

# noinspection PyShadowingNames
def drawDot(_data,_label,wights):
    plt.scatter(_data[:,0],_data[:,1],c=_label,s=50*len(_data)*wights)

# noinspection PyShadowingNames
class SplitByNum:
    def __init__(self,value,bigger = True,index = 0):
        self.value = value
        self.bigger = bigger
        self.index = index

    def predict(self,data):
        _data = data[:,self.index]
        result = (_data > self.value).astype(int)*2-1
        if self.bigger:
            return result
        else:
            return result * -1

# noinspection PyShadowingNames
class FinalFunction:
    def __init__(self):
        self.Function_list = []
        self.alphas = []

    def append(self,function:SplitByNum,alpha):
        self.Function_list.append(function)
        self.alphas.append(alpha)

    def cal(self,data):
        result = np.array([function.predict(data) for function in self.Function_list])
        return np.dot(self.alphas,result)

    def predict(self,data):
        return (self.cal(data) > 0).astype(int) * 2 - 1

    def __str__(self):
        stringStream = [function.value for function in self.Function_list].__str__()
        stringStream += '\n' + self.alphas.__str__()
        return stringStream

# noinspection PyShadowingNames
def getSplitUnit(_data,label,wights,_index):
    data = _data[:,_index]
    data_sorted = np.sort(data)
    biggest_one,Function = 0,None
    for i in range(len(data)):
        tip = True
        bigger = (data > data_sorted[i]).astype(int) * 2 - 1
        result = np.dot((bigger==label).astype(int),wights)
        if result < 0.5:
            tip ,result = False, 1 - result
        if result > biggest_one:
            biggest_one = result
            Function = SplitByNum((data_sorted[i] + data_sorted[i + 1])/2,tip,_index)
    return Function,biggest_one

# noinspection PyShadowingNames
def getSplit(data,label,wights):
    biggest_one,Function,index = 0,None,None
    for i in range(len(data[0])):
        F,e = getSplitUnit(data,label,wights,i)
        if e >= biggest_one:
            Function,biggest_one,index = F,e,i
    return  Function,biggest_one,index

# noinspection PyShadowingNames
def drawSplit(G:FinalFunction):
    x = np.linspace(0,0.5,3)
    y = np.linspace(0.2,0.8,3)
    for function in G.Function_list:
        if function.index == 0:
            plt.plot(np.ones(len(x)) * function.value, x)
        else:
            plt.plot(y, np.ones(len(y)) * function.value)

# noinspection PyShadowingNames
getAlpha = lambda e:np.log(1/e-1)/2

data,label = loadData()
wight_data = np.ones(len(data))/len(data)
functionG = FinalFunction()
for i in range(15):
    G,e,index = getSplit(data,label,wight_data)
    alpha = getAlpha(1-e)
    functionG.append(G,alpha)
    wight_temp = wight_data*np.exp(G.predict(data) * label * (-alpha))
    wight_data = wight_temp/wight_data.sum()
    predict = functionG.predict(data)
    print("time:",i," acc:",accuracy_score(predict,label))
    print(functionG.cal(data))

    if i%3==0:
        # print(functionG.predict(data))
        plt.subplot(121)
        drawDot(data,label,wight_data)
        drawSplit(functionG)
        plt.subplot(122)
        drawDot(data,predict,wight_data)
        drawSplit(functionG)
        plt.show()