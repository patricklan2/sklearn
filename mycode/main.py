import numpy as np
import matplotlib.pyplot as plt
from myFrame import load_iris

if __name__ == '__main__':
    data,label = load_iris()
    print(data.shape)
    print(label.shape)

# noinspection PyShadowingNames
def generatorNormal(mu1,mu2,sigma1,sigma2,count):
    array = np.random.randn(count, 2)
    array[:,0] = array[:,0] * np.sqrt(sigma1) + mu1
    array[:,1] = array[:,1] * np.sqrt(sigma2) + mu2
    return array

# noinspection PyShadowingNames
def drawPlot(group,x):
    plt.plot(x,group[1]/group[0]*x,linewidth=2,c="ORANGE")

def drawGrid(start,end,span,matrix,c="GREEN",linewidth=1,**kw):
    x = np.arange(start,end,span)
    k = len(x)
    grid_x, grid_y = np.meshgrid(x, x)
    grid = np.insert(grid_x.reshape(-1, 1), 1, grid_y.flat, axis=1)
    grid_new = np.dot(grid, matrix.T).reshape(k, k, 2)
    for i in range(k):
        plt.plot(grid_new[:, i, 0], grid_new[:, i, 1], c=c, linewidth=linewidth,**kw)
        plt.plot(grid_new[i, :, 0], grid_new[i, :, 1], c=c, linewidth=linewidth,**kw)

# noinspection PyShadowingNames
def draw(matrix):
    plt.scatter(matrix[:,0],matrix[:,1],s=1)

# np.random.normal(0,1,10000) 生成10000个符合（mu=0，方差=1）的一维高斯分布
# np.random.random(6) 生成6个0~1的随机数
# np.random.randn(100000) 等效np.random.normal(0,1,100000)
# np.random.randn(10000,2) 生成二维高斯分布
# np.random.choice([0, 1], size=N, p=p) 从[0,1]中按p的概率选N个
# np.var(normal) #求方差
#
# corrcoef = np.corrcoef(array,rowvar=False)
# cov = np.cov(array,rowvar=False)
# eigenvalues, eigenvectors = np.linalg.eig(cov)
#
# np.corrcoef 相关系数
# np.cov(array) 协方差
# np.correlate
# eigenvalues, eigenvectors = np.linalg.eig(array) 特征值与特征向量
# u, s, v = np.linalg.svd(array, full_matrices=0) 奇异值分解（SVD）
# np.linalg.det 行列式
#
#
# sklearn
# StandardScaler().fit_transform(data) 归一化






