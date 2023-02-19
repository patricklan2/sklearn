from myFrame import *
from myFrame.datasets import *


data,label = loadWatermelon()
model2 = Pipe(
    endModel=TreeClassifier(typeList=np.array([1,1,1,1,1,1,0,0])),
    preprocessing=[Encoding([0,1,2,3,4,5],withLabel=True)],
    moreInformation=True
)
model2.fit(data,label)
predict = model2.predict(data)
for i in model2.process:
    print(i)

