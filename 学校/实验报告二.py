import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import cluster
from sklearn import preprocessing
pd.set_option("display.unicode.east_asian_width",True)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
Province = pd.read_excel("Province.xlsx",engine="openpyxl")
print(Province.head())
plt.scatter(Province.Birth_Rate, Province.Death_Rate, c = 'steelblue')
plt.xlabel('Birth_Rate')
plt.ylabel('Death_Rate')
plt.show()
predictors = ['Birth_Rate','Death_Rate']
X = preprocessing.scale(Province[predictors])
X = pd.DataFrame(X)
agnes_min = cluster.AgglomerativeClustering(n_clusters=3, linkage='ward')
agnes_min.fit(X)
Province['agnes_label'] = agnes_min.labels_   #聚类的结果标签
print(Province)

sns.lmplot(x='Birth_Rate', y='Death_Rate', hue='agnes_label', data=Province,
           markers=['d', '^', 'o'], fit_reg=False, legend=False)
plt.xlabel('Birth_Rate')
plt.ylabel('Death_Rate')
plt.show()