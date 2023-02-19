from func import Function,MulFunction

class Pipe:
    Dict = dict()
    inputList = list()
    outputs = ['output']
    inputs = ['input']

    def __init__(self,inputs = None,outputs = None):
        self.inputs = inputs if inputs is not None else ['input']
        self.outputs = outputs if outputs is not None else ['output']

    def addFunction(self,function,end,*start):
        fun = [function,list(start)]
        self.Dict[end] = fun

    def __cal__(self,string,temp):
        function,inputs = self.Dict[string]
        inputs = [temp[inp] for inp in inputs]
        return function.func(*inputs)

    def cal(self,inputs):
        result = {inp:value for inp,value in zip(self.inputs,inputs)}
        # 初始化栈
        stack = [[output,False] for output in self.outputs]
        while len(stack) !=0:
            print(stack)
            # 出栈
            output,status = stack[len(stack) - 1]
            stack[len(stack) - 1][1] = True
            if status is False:
                #遍历inputs
                tip = True
                for inp in self.Dict[output][1]:
                    # 判断inputs是否求出
                    if inp not in result.keys():
                        tip = False
                        stack.append([inp,False])
                if tip is False:
                    continue
            result[output] = self.__cal__(output,result)
            stack.pop()
        return result







if __name__ == '__main__':
    # p = Pipe()
    # p.addFunction(Function(lambda x:x*5),'mid','input')
    # p.addFunction(Function(lambda x: x*9), 'output', 'mid')

    # p = Pipe(inputs=['in1','in2','in3'])
    # p.addFunction(MulFunction(lambda x,y,z:x+y+z),'mid','in1','in2','in3')
    # p.addFunction(Function(lambda x:x**2),'output','mid')

    # print(p.cal([1, 2, 3]))

    # p = Pipe()
    # p.addFunction(Function(lambda x:x*5),'mid1','input')
    # p.addFunction(Function(lambda x: x * 3), 'mid2', 'input')
    # p.addFunction(Function(lambda x: x * 8), 'mid3', 'input')
    # p.addFunction(MulFunction(lambda x,y,z:x+y+z),'mid','mid1','mid2','mid3')
    # p.addFunction(Function(lambda x:x**2),'output','mid')
    #
    # print(p.cal([1]))

    p = Pipe(inputs=['in1','in2'])
    p.addFunction(Function(lambda x:x*2),'mid','in1')
    p.addFunction(MulFunction(lambda x,y:x+y),'output','in2','mid')

    print(p.cal([3, 6]))