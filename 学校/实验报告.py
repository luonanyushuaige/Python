import openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn import metrics
from sklearn import model_selection
import seaborn as sns

# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 导入数据
Knowledge = pd.read_excel("Knowledge.xlsx", engine="openpyxl")
print(Knowledge.head())


# 拆分数据集
predictors = Knowledge.columns[:-1]
X_train, X_test, y_train, y_test = model_selection.train_test_split(Knowledge[predictors], Knowledge.UNS,
                                                                   test_size=0.25, random_state=1234)
# 最佳k值的选择
K = np.arange(1, np.ceil(np.log2(Knowledge.shape[0]))).astype(int)
accuracy = []
for k in K:
    cv_result = model_selection.cross_val_score(neighbors.KNeighborsClassifier(n_neighbors=k, weights='distance'),X_train, y_train, cv=10, scoring='accuracy')
    accuracy.append(cv_result.mean())
arg_max = np.array(accuracy).argmax()
# 绘制不同k值与平均预测准确率之间的折线图
plt.plot(K, accuracy)
plt.scatter(K, accuracy)
plt.text(K[arg_max], accuracy[arg_max], '最佳k值为%s' % int(K[arg_max]))
plt.show()
# 基于k=6重新构建模型
knn_class = neighbors.KNeighborsClassifier(                                                            n_neighbors=6,                                                             weights='distance')
knn_class.fit(X_train, y_train)
predict = knn_class.predict(X_test)
# 构建混淆矩阵
cm = pd.crosstab(predict, y_test)
print(cm)# 绘制热力图
cm = pd.DataFrame(cm,columns=["High","Low","Middle","Very Low"],                                index=["High","Low","Middle","Very Low"])
sns.heatmap(cm, annot=True, cmap='GnBu')
plt.xlabel(' Real Lable')
plt.ylabel(' Predict Lable')
plt.show()
# 模型整体的预测准确率
acc=metrics.accuracy_score(y_test, predict)
print(acc)    # 0.91
# 分类模型的评估报告
print(metrics.classification_report(y_test, predict))