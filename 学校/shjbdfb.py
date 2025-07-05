import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, classification_report, adjusted_rand_score
import chardet
with open('seeds.csv', 'rb') as f:
    result = chardet.detect(f.read(10000))  # 读取前10000字节检测

df = pd.read_csv('seeds.csv', delimiter='|',
                 skipinitialspace=True,
                 encoding=result['encoding'])
# 1. 数据加载与预处理
# 假设数据文件为seeds.csv（根据您提供的表结构）
df = pd.read_csv('seeds.csv', delimiter='|', skipinitialspace=True)
df = df.dropna()  # 删除空值

# 分离特征和标签
X = df.iloc[:, :-1].values  # 所有特征列
y_true = df.iloc[:, -1].values  # 种类标签

# 特征标准化（K-Means对尺度敏感）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. K-Means聚类
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

# 3. 与实际种类对比
# 创建标签映射（聚类结果 -> 实际种类）
cluster_to_species = {}
for i in range(3):
    # 获取当前聚类中的真实标签
    cluster_labels = y_true[clusters == i]
    # 找出该聚类中最常见的种类
    species = pd.Series(cluster_labels).mode()
    cluster_to_species[i] = species

# 将聚类标签转换为预测种类
y_pred = np.array([cluster_to_species[c] for c in clusters])

# 4. 评估指标
print("聚类结果评估:")
print("=" * 50)
print(f"调整兰德指数 (ARI): {adjusted_rand_score(y_true, y_pred):.4f}")
print("\n分类报告:")
print(classification_report(y_true, y_pred))
print("\n混淆矩阵:")
print(confusion_matrix(y_true, y_pred))

# 5. 可视化结果
# 使用PCA降维到2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(15, 6))

# 子图1：真实种类分布
plt.subplot(121)
for species in np.unique(y_true):
    plt.scatter(X_pca[y_true == species, 0], 
                X_pca[y_true == species, 1], 
                label=species, alpha=0.7)
plt.title('真实种类分布 (PCA降维)')
plt.xlabel('主成分 1')
plt.ylabel('主成分 2')
plt.legend()

# 子图2：聚类结果分布
plt.subplot(122)
for cluster in range(3):
    plt.scatter(X_pca[clusters == cluster, 0], 
                X_pca[clusters == cluster, 1], 
                label=f'Cluster {cluster} ({cluster_to_species[cluster]})',
                alpha=0.7)
plt.scatter(kmeans.cluster_centers_[:, 0], 
            kmeans.cluster_centers_[:, 1], 
            s=200, marker='X', c='black', label='聚类中心')
plt.title('K-Means聚类结果 (PCA降维)')
plt.xlabel('主成分 1')
plt.legend()

plt.tight_layout()
plt.savefig('clustering_result.png', dpi=300)
plt.show()

# 6. 输出聚类详细信息
results_df = df.copy()
results_df['Cluster'] = clusters
results_df['Predicted_Species'] = y_pred

print("\n前10个样本的聚类结果:")
print(results_df[['种类', 'Cluster', 'Predicted_Species']].head(10))
