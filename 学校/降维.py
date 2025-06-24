import numpy as np
import pandas as pd

a =np.array([[30,65,70],[80,95,10],[50,90,60]])
print (np.median(a, axis = 0))
print (np.std(a, axis = 0))
b=pd.DataFrame(a)
def StandarScale(data):
                s_sc=(data-data.mean())/(data.std())
                return s_sc
c=StandarScale(b)
print(c)
print(c.cov())#协方差矩阵

R=np.linalg.det(b)
#print(b)
#特征值和特征向量
f = np.linalg.eig(b)
# print(f)
#特征值
print(f[0])
# print(f[1])