import numpy as np
import matplotlib.pyplot as plot

np.random.seed(0)
mu_u = 1.71
sigma_m = 0.056
num_m = 10000
rand_data_m = np.random.normal(mu_u,sigma_m,num_m)
y_m = np.ones(num_m)

mu_w = 1.58
sigma_w = 0.051
num_w = 10000
rand_data_w = np.random.normal(mu_w,sigma_w,num_w)
y_w = np.ones(num_w)

data = np.append(rand_data_m,rand_data_w)
data = data.reshape(-1,1)
y = np.append(y_m,y_w)
print(data)
print(y)

from sklearn.mixture import GaussianMixture
g = GaussianMixture(n_components=2,covariance_type='full',tol=1e-6,max_iter=1000)
g.fit(data)
print(u'类别概率:\t',g.weights_[0])
print(u'均值:\t',g.means_)
print(u'方差:\t',g.covariances_)