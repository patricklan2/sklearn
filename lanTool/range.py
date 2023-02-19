

class BaseRange:
    def isContain(self,value):
        pass

    def equal(self,baseRange):
        pass

class ContinuityRange(BaseRange):
    sup = 0.0
    inf = 0.0
    def __init__(self,inf = 0.0,sup = 100.0):
        self.inf = inf
        self.sup = sup

    def isContain(self,value):
        return self.inf <= value <= self.sup

    def set(self, inf = None,sup = None):
        self.inf = inf if inf is not None else self.inf
        self.sup = sup if sup is not None else self.sup

    def equal(self,continuity):
        if  not isinstance(continuity,ContinuityRange):
            return False
        return continuity.inf == self.inf and continuity.sup == self.sup

class DiscreteRange(BaseRange):
    value = 0.0
    Type = True
    def __init__(self,value = 0.0,Type = True):
        self.value = value
        self.Type = Type

    def isContain(self,value):
        if self.Type:
            return value == self.value
        else:
            return value != self.value

    def set(self,value = None,Type = None):
        self.value = value if value is not None else self.value
        self.Type = Type if Type is not None else self.Type

    def equal(self,discrete):
        if  not isinstance(discrete,DiscreteRange):
            return False
        return discrete.value == self.value and discrete.Type == self.Type

class AllRange(BaseRange):
    def __init__(self):
        pass

    def equal(self,baseRange):
        return isinstance(baseRange,AllRange)

    def isContain(self,value):
        return True

class Range(object):
    rangeList = []
    def __init__(self,*rangeList:BaseRange):
        self.rangeList = list(rangeList)

    def isContain(self,value):
        tip = False
        for _range in self.rangeList:
            if _range.isContain(value):
                tip = True
        return tip

    def unionOne(self,rangeOne:BaseRange):
        for _range in self.rangeList:
            if _range.equal(rangeOne):
                return self
        self.rangeList.append(rangeOne)
        return self

    def union(self,_range):
        if isinstance(_range,Range):
            for r in _range.rangeList:
                self.unionOne(r)
        return self

def RangeTypeC(inf = 0.0,sup = 100.0):
    cont = ContinuityRange(inf,sup)
    return Range(cont)

def RangeTypeD(value = 0.0):
    disc = DiscreteRange(value)
    return Range(disc)







