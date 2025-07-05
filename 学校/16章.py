import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import adjusted_rand_score, silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

# 1. 数据加载与预处理
data = pd.read_csv('seeds.csv')
X = data.drop('种类', axis=1)  # 特征数据
y = data['种类']  # 真实标签

# 标准化处理
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. K均值聚类
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)
kmeans_ari = adjusted_rand_score(y, kmeans_labels)
kmeans_sil = silhouette_score(X_scaled, kmeans_labels)

# 3. DBSCAN密度聚类
# 通过k-距离图确定最佳eps
from sklearn.neighbors import NearestNeighbors
nn = NearestNeighbors(n_neighbors=5).fit(X_scaled)
distances, _ = nn.kneighbors(X_scaled)
distances = np.sort(distances[:, -1], axis=0)

plt.figure(figsize=(10, 6))
plt.plot(distances)
plt.title('K-Distance Graph for DBSCAN')
plt.xlabel('Data Points')
plt.ylabel('Epsilon')
plt.grid(True)
plt.savefig('k_distance_graph.png')
plt.close()

# 根据曲线拐点选择eps=0.6
dbscan = DBSCAN(eps=0.6, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)
dbscan_ari = adjusted_rand_score(y, dbscan_labels)
dbscan_sil = silhouette_score(X_scaled, dbscan_labels) if len(np.unique(dbscan_labels)) > 1 else -1

# 4. 层次聚类
agg_clustering = AgglomerativeClustering(n_clusters=3, linkage='ward')
agg_labels = agg_clustering.fit_predict(X_scaled)
agg_ari = adjusted_rand_score(y, agg_labels)
agg_sil = silhouette_score(X_scaled, agg_labels)

# 绘制树状图
plt.figure(figsize=(12, 8))
linked = linkage(X_scaled, 'ward')
dendrogram(linked, orientation='top', distance_sort='descending')
plt.title('Hierarchical Clustering Dendrogram')
plt.savefig('dendrogram.png')
plt.close()

# 5. 结果对比与可视化
results = pd.DataFrame({
    'Method': ['K-Means', 'DBSCAN', 'Agglomerative'],
    'ARI': [kmeans_ari, dbscan_ari, agg_ari],
    'Silhouette': [kmeans_sil, dbscan_sil, agg_sil],
    'Clusters': [len(np.unique(kmeans_labels)),
                len(np.unique(dbscan_labels)),
                len(np.unique(agg_labels))]
})

print("="*60)
print("聚类性能对比:")
print(results)
print("="*60)

# 可视化聚类结果
plt.figure(figsize=(18, 5))

# K-Means结果
plt.subplot(131)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans_labels, cmap='viridis')
plt.title(f'K-Means Clustering (ARI={kmeans_ari:.3f})')
plt.xlabel('标准化面积')
plt.ylabel('标准化周长')

# DBSCAN结果
plt.subplot(132)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=dbscan_labels, cmap='viridis')
plt.title(f'DBSCAN Clustering (ARI={dbscan_ari:.3f})')
plt.xlabel('标准化面积')

# 层次聚类结果
plt.subplot(133)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=agg_labels, cmap='viridis')
plt.title(f'Agglomerative Clustering (ARI={agg_ari:.3f})')
plt.xlabel('标准化面积')

plt.tight_layout()
plt.savefig('clustering_comparison.png')
plt.show()

# 6. 特征重要性分析（辅助理解）
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, pd.factorize(y))
importances = rf.feature_importances_
features = X.columns

plt.figure(figsize=(10, 6))
plt.barh(features, importances)
plt.title('Feature Importances for Seed Classification')
plt.xlabel('Importance Score')
plt.tight_layout()
plt.savefig('feature_importance.png')
