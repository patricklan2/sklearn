from lanTool.counter import Counter
from lanTool import reduce,np


def getMulList(shape):
    result = [1]
    length = len(shape)
    for i in range(1,length):
        result = [k*shape[i] for k in result]
        result.append(1)
    return result

def cut(shapeAndMul,indexList):
    return [[l[index] for index in indexList] for l in shapeAndMul]

def shuffle(shapeAndMul,newList):
    result = [[l[newList[i]] for i in range(len(newList))] for l in shapeAndMul]
    return result[0],result[1]

def create(array):
    array = np.array(array)
    shape = array.shape
    array = array.reshape(-1).tolist()
    return Array(array,shape)

class BaseArray(object):
    def __init__(self,data,shape,**kwargs):
        self.data = data
        self.shape = shape
        self.length = len(self.shape)
        self.size = len(self.data)

    def __str__(self):
        Dict = {'shape': self.shape, 'dimension': self.length, 'size': self.size}
        return str(Dict)

    def package(self,empty=False):
        if empty:
            return {"data":None,"shape":None}
        return {"data":self.data.copy(),"shape":self.data}

    def copy(self):
        return BaseArray(**self.package(False))

    def toNumpy(self):
        array = np.array(self.data)
        return array.reshape(self.shape)

    def location(self,numList:list)->int:
        if len(numList) != self.length:
            raise Exception("wrong size")
        S = 0
        mulList = getMulList(self.shape)
        for i in range(self.length):
            S += mulList[i] * numList[i]
        return S

    def getOne(self,numList:list):
        return self.data[self.location(numList)]

    def set(self,numList:list,value)->None:
        self.data[self.location(numList)] = value

    def forEach(self,*functions):
        data = self.data
        for f in functions:
            data = [f(x) for x in data]
        return {"data":data,"shape":self.shape}

    def get(self,numList:list):
        if len(numList) != self.length:
            raise Exception("wrong size")

        mulList = getMulList(self.shape)
        offset ,shape,leftMulList  = 0,[],[]
        for i in range(self.length):
            if numList[i] == -1:
                shape.append(self.shape[i])
                leftMulList.append(mulList[i])
            else:
                offset += mulList[i] * numList[i]

        counter1, counter2 = Counter(shape, leftMulList), Counter(shape, getMulList(shape))
        data = [0] * counter1.S
        for _ in range(counter1.S):
            sum2, sum1 = counter2.plus(), counter1.plus()
            data[sum2] = self.data[sum1 + offset]
        return {"data":data,"shape":shape}

    def split(self,index):
        List = [-1] * self.length
        result = []
        for i in range(self.shape[index]):
            List[index] = i
            result.append(self.get(List))
        return result

    def transpose(self,numList:list):
        if len(numList) != self.length:
            raise Exception("wrong size")
        newShape,BaseMul = shuffle([self.shape,getMulList(self.shape)],numList)
        counter1,counter2 = Counter(newShape,BaseMul),Counter(newShape,getMulList(newShape))
        data = [0] * counter1.S
        for _ in range(counter1.S):
            sum1 ,sum2 = counter1.plus(),counter2.plus()
            data[sum2] = self.data[sum1]
        return {"data":data,"shape":newShape}

    def _sum(self,List:list):
        group,elseGroup = [cut([self.shape,getMulList(self.shape)],i)for i in List]
        counter1,counter2,counter3 = Counter(group[0],group[1]),Counter(elseGroup[0],elseGroup[1]),Counter(elseGroup[0],getMulList(elseGroup[0]))
        data = [0] * counter3.S
        for _ in range(counter3.S):
            sum2,sum3 = counter2.plus(),counter3.plus()
            for _ in range(counter1.S):
                sum1 = counter1.plus()
                data[sum3] += self.data[sum1+sum2]
        return {"data":data,"shape":elseGroup[0]}

    def sumByIndex(self,indexList:list):
        List = [list(indexList),[i for i in range(self.length) if i not in indexList]]
        return self._sum(List)

    def sumByElse(self,indexList):
        List = [[i for i in range(self.length) if i not in indexList], list(indexList)]
        return self._sum(List)

    def dotHead(self,array,dotType = 'T'):
        if dotType == 'T':
            return self._dotFByT(array,lambda x,y:x*y)
        elif dotType == 'H':
            return self._dotFByH(array,lambda x,y:x*y)

    def _dotFByT(self,array,F):
        index = self.length - array.length
        List = [range(self.length)[:index],range(self.length)[index:]]
        left, right = [cut([self.shape, getMulList(self.shape)], i) for i in List]
        counter1,counter2 = Counter(left[0],left[1]),Counter(right[0],right[1])
        data = [0] * self.size
        for _ in range(counter2.S):
            sum2 = counter2.plus()
            for _ in range(counter1.S):
                sum1 = counter1.plus()
                data[sum1 + sum2] = F(data[sum1 + sum2],self.data[sum2])
        return {"data":data,"shape":self.shape}

    def _dotFByH(self,array,F):
        data = [i for i in self.data]
        M, N = self.size, array.size
        tip = int(M / N)
        for i in range(N):
            for k in range(tip):
                data[tip * i + k] = F(self.data[tip * i + k],array.data[i])
        return {"data":data,"shape":self.shape}

    def sumAll(self):
        return reduce(lambda x,y:x+y,self.data)

    def toP(self):
        S = self.sumAll()
        if S == 0:
            return Array([0 for _ in self.data],self.shape)
        data = [i/S for i in self.data]
        return {"data":data,"shape":self.shape}

class Array(BaseArray):
    def __init__(self,data = None,shape = None):
        super().__init__(data=data,shape = shape)

    def forEach(self,*functions):
        return Array(**super().forEach())

    def get(self,numList):
        return Array(**super().get(numList))

    def transpose(self,numList):
        return Array(**super().transpose(numList))

    def sumByIndex(self,indexList):
        return Array(**super().sumByIndex(indexList))

    def sumByElse(self,indexList):
        print(indexList)
        print(super().sumByElse(indexList))
        return Array(**super().sumByElse(indexList))

    def dotFByT(self,array,F):
        return Array(**super()._dotFByT(array,F))

    def dotFByH(self,array,F):
        return Array(**super()._dotFByH(array,F))

    def dotHead(self,array,dotType = 'T'):
        return Array(**super().dotHead(array,dotType=dotType))

class DictArray(BaseArray):
    def __init__(self,data,shape,attribute,extendAttribute=None,value=None):
        super().__init__(data=data,shape=shape)
        self.attribute = attribute
        if value is None:
            self.value = {i:[] for i in attribute}
        else:
            self.value = value
        if extendAttribute is None:
            self.extendAttribute = []
        else:
            self.extendAttribute = extendAttribute

    def __str__(self):
        return super().__str__() + self.attribute.__str__() + self.extendAttribute.__str__()

    def pack(self,data = None,shape = None,attribute = None,extendAttribute = None,value = None):
        Dict = dict()
        Dict['data'] = self.data if data is None else data
        Dict['shape'] = self.shape if shape is None else shape
        Dict['attribute'] = self.attribute if attribute is None else attribute
        Dict['extendAttribute'] = self.extendAttribute if extendAttribute is None else extendAttribute
        Dict['value'] = self.value if value is None else value
        return Dict

    def insertByIndex(self,index:int,valueName:str)->None:
        self.value[self.attribute[index]].append(valueName)

    def deleteByIndex(self,index,value):
        del self.value[self.attribute[index]][value]

    # def deleteByName(self,name,value):
    #     del self.value[name][value]

    def trans(self,nameList):
        result = []
        for index in range(self.length):
            result.append(self.value[self.attribute[index]].index(nameList[index]))
        return result

    def getIndex(self,nameList:list):
        return [self.attribute.index(name) for name in nameList]

    def setByName(self,nameList,value:int):
        numList = self.trans(nameList)
        super().set(numList,value)

    def getOneBN(self,nameList):
        numList = self.trans(nameList)
        return super().getOne(numList)

    def forEach(self,*functions):
        return DictArray(**self.pack(**super().forEach(*functions)))

    def getBN(self,nameList):
        numList,elseList,groupList = [],[],[]
        for index in range(self.length):
            if nameList[index] in self.attribute:
                numList.append(-1)
                elseList.append(nameList[index])
            else:
                numList.append(self.value[self.attribute[index]].index(nameList[index]))
                groupList.append(nameList[index])
        Dict = super().get(numList)
        Dict['extendAttribute'] = groupList
        Dict['value'] = {k: self.value[k] for k in elseList}
        Dict['attribute'] = elseList
        return DictArray(**Dict)

    def get(self,numList:list):
        elseList, groupList = [], []
        for index in range(self.length):
            if numList[index] == -1:
                elseList.append(self.attribute[index])
            else:
                groupList.append(self.value[self.attribute[index]][numList[index]])
        Dict = super().get(numList)
        Dict['extendAttribute'] = groupList
        Dict['value'] = {k: self.value[k] for k in elseList}
        Dict['attribute'] = elseList
        return DictArray(**Dict)



    def sumByElseBN(self,nameList):
        indexList = self.getIndex(nameList)
        Dict = super().sumByElse(indexList)
        Dict['extendAttribute'] = [k for k in self.attribute if k not in nameList]
        Dict['value'] = {k: self.value[k] for k in nameList}
        Dict['attribute'] = nameList
        return DictArray(**Dict)

    def sumByElse(self,indexList):
        nameList = [self.attribute[i] for i in indexList]
        return self.sumByElseBN(nameList)


    def splitBN(self,name):
        index = self.attribute.index(name)
        return {i:k for i,k in zip(self.value[name],super().split(index))}

    def transposeBN(self,nameList):
        numList = self.getIndex(nameList)
        return self.transpose(numList)

    def transpose(self,numList:list):
        Dict = self.pack(attribute=[self.attribute[index] for index in numList], **super().transpose(numList))
        return DictArray(**Dict)

    def dotHead(self,array,dotType = 'T'):
        Dict = self.pack(**super().dotHead(array,dotType = dotType))
        return DictArray(**Dict)

    def dotBF(self,array,F,dotType = 'T'):
        if dotType == 'T':
            return DictArray(**self.pack(**super()._dotFByT(array,F)))
        elif dotType == 'H':
            return DictArray(**self.pack(**super()._dotFByH(array,F)))

    def toP(self):
        return DictArray(**self.pack(**super().toP()))


if __name__ == '__main__':
    # example = np.array(range(24))
    # example = example.reshape(2,3,4)
    # example = create(example)

    example = DictArray(range(24),[2,3,4],['name2','name3','name4'])
    for _i in range(example.length):
        for _k in range(example.shape[_i]):
            example.insertByIndex(_i,str(_i)+"-"+str(_k))

    print(example.value)

    # b = np.array(range(1,3))
    # b = create(b)
    #
    # print(example.sumByElse([0]))


