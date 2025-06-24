import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import GridSearchCV

# 加载数据
data = pd.read_csv('house_data.csv')

# 1. 数据探索与预处理
print("数据预览:")
print(data.head())
print("\n数据统计信息:")
print(data.describe())
print("\n缺失值检查:")
print(data.isnull().sum())

# 可视化房价分布
plt.figure(figsize=(12, 6))
sns.histplot(data['price'], bins=50, kde=True)
plt.title('房价分布直方图')
plt.xlabel('房价')
plt.ylabel('频数')
plt.show()

# 特征选择
features = [
    'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
    'waterfront', 'view', 'condition', 'grade', 'sqft_above',
    'sqft_basement', 'yr_built', 'yr_renovated', 'lat', 'long',
    'sqft_living15', 'sqft_lot15'
]

# 2. 将连续房价转换为分类标签
# 使用分位数法创建5个类别：非常低、低、中等、高、非常高
quantiles = data['price'].quantile([0.2, 0.4, 0.6, 0.8]).values
print("\n分类边界值(分位数):", quantiles)

# 创建分类标签
data['price_category'] = pd.cut(data['price'],
                                bins=[0, quantiles[0], quantiles[1], quantiles[2], quantiles[3], float('inf')],
                                labels=['非常低', '低', '中等', '高', '非常高'])

# 查看分类分布
print("\n房价分类分布:")
print(data['price_category'].value_counts())

plt.figure(figsize=(10, 6))
data['price_category'].value_counts().plot(kind='bar')
plt.title('房价分类分布')
plt.xlabel('类别')
plt.ylabel('数量')
plt.show()

# 3. 特征工程
# 处理翻新年份：如果未翻新，则使用建造年份
data['yr_renovated'] = np.where(data['yr_renovated'] > 0, data['yr_renovated'], data['yr_built'])

# 计算房龄
current_year = 2015  # 根据数据集中的日期
data['house_age'] = current_year - data['yr_built']
data['renovation_age'] = current_year - data['yr_renovated']

# 添加新特征：总房间数
data['total_rooms'] = data['bedrooms'] + data['bathrooms']

# 更新特征列表
features.extend(['house_age', 'renovation_age', 'total_rooms'])

# 4. 准备数据集
X = data[features]
y = data['price_category']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 特征标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. 构建KNN分类模型
# 使用网格搜索寻找最佳K值
param_grid = {'n_neighbors': range(3, 21)}
knn = KNeighborsClassifier()
grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train_scaled, y_train)

# 获取最佳模型
best_k = grid_search.best_params_['n_neighbors']
best_model = grid_search.best_estimator_

print(f"\n最佳K值: {best_k}")
print(f"训练集准确率: {best_model.score(X_train_scaled, y_train):.4f}")

# 6. 模型评估
y_pred = best_model.predict(X_test_scaled)

print("\n测试集准确率:", accuracy_score(y_test, y_pred))
print("\n分类报告:")
print(classification_report(y_test, y_pred))

# 混淆矩阵可视化
plt.figure(figsize=(10, 8))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=best_model.classes_,
            yticklabels=best_model.classes_)
plt.title('混淆矩阵')
plt.xlabel('预测类别')
plt.ylabel('真实类别')
plt.show()

# 7. 特征重要性分析
# 使用KNN的特征权重方法（基于距离的权重）
feature_importance = np.mean(np.abs(best_model.kneighbors(X_train_scaled, n_neighbors=best_k, return_distance=False)), axis=0)
feature_importance = feature_importance / np.sum(feature_importance)

plt.figure(figsize=(12, 8))
sorted_idx = np.argsort(feature_importance)
plt.barh(range(len(sorted_idx)), feature_importance[sorted_idx], align='center')
plt.yticks(range(len(sorted_idx)), np.array(features)[sorted_idx])
plt.title('特征重要性')
plt.xlabel('重要性分数')
plt.tight_layout()
plt.show()

# 8. 随机样本预测展示
sample_indices = np.random.choice(len(X_test), 5, replace=False)
sample_data = X_test.iloc[sample_indices].copy()
sample_data['实际房价类别'] = y_test.values[sample_indices]
sample_data['预测房价类别'] = y_pred[sample_indices]
sample_data['预测正确'] = sample_data['实际房价类别'] == sample_data['预测房价类别']

print("\n随机测试样本预测结果:")
print(sample_data[['bedrooms', 'bathrooms', 'sqft_living', 'house_age',
                   '实际房价类别', '预测房价类别', '预测正确']])