import numpy as np
from myFrame.datasets import *

data,label = loadWatermelon()
d = data.shape[1]
dataNew, labelNew = np.array([]).reshape(-1,d),np.array([])

print(np.repeat(data, np.arange(17),axis=0))