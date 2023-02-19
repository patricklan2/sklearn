from math import exp

from lanTool.range import *


class Function:
    func = None
    def __init__(self,Func = None):
        self.func = Func if Func is not None else lambda x:x

    def setFunc(self,Func = None):
        self.func = Func if Func is not None else self.func

    def __getitem__(self, item):
        return self.func(item)


class MulFunction:
    func = None
    def __init__(self,Func = None):
        self.func = Func if Func is not None else lambda x:x

    def setFunc(self,Func = None):
        self.func = Func if Func is not None else self.func

    def __cal__(self, *item):
        return self.func(*item)

class PartitionFunction:
    func = None
    def __init__(self,Dict:dict = None):
        self.Dict = Dict if Dict is not None else dict()
        self.func = self.__getitem__

    def __getitem__(self, item):
        for key,value in self.Dict.items():
            if key.isContain(item):
                return value[item]
        else:
            return 0

if __name__ == '__main__':
    # f = Function(lambda x:90)
    #
    # d = {DiscreteRange(2):Function(lambda x:x**5),ContinuityRange(3,6):Function(lambda x:exp(x)),AllRange():f}
    #
    # pf = PartitionFunction(d)
    # for i in range(10):
    #     print(pf.func(i))

    f = MulFunction(lambda x,y,z:x + y + z)

    print(f.__cal__(2, 3, 4))