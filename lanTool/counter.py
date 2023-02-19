class Counter:
    counter = None
    limitList = None
    plusList = None
    sum = 0
    S = 0
    State = False
    def __init__(self,numList,plusList = None):
        if len(numList) == 0:
            return
        L = len(numList)
        if plusList is None:
            plusList = [1] * L
        self.limitList = [numList[i] * plusList[i] for i in range(L)]
        self.plusList = plusList
        self.counter = [0]*len(self.limitList)
        self.S = self.mul()
        self.State = True

    def mul(self):
        S = 1
        for i,k in zip(self.limitList,self.plusList):
            S *= i // k
        return S

    def plus(self):
        if self.State is False:
            return
        Sum = self.sum
        self.counter[0] += self.plusList[0]
        self.sum +=self.plusList[0]
        self.up(0)
        return Sum

    def up(self,i):
        if self.counter[i] >= self.limitList[i]:
            self.sum -= self.counter[i]
            self.counter[i] = 0
            if i < len(self.limitList) - 1:
                self.counter[i + 1] += self.plusList[i + 1]
                self.sum += self.plusList[i + 1]
                self.up(i + 1)