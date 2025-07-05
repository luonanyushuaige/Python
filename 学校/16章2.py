from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

# Select the features for clustering
features = data_decoded[['面积', '周长', '紧致性', '长度', '宽度', '偏斜度', '籽粒长度']]

# K-Means Clustering
# We need to decide the number of clusters, we can use the number of unique species as a starting point
num_clusters = len(label_encoder.classes_)
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans_clusters = kmeans.fit_predict(features)

# Calculate the adjusted Rand index to compare the K-Means clusters with the actual species
kmeans_ari = adjusted_rand_score(data_decoded['种类编码'], kmeans_clusters)

# Density Clustering (DBSCAN)
from sklearn.cluster import DBSCAN

# DBSCAN does not require the number of clusters to be specified beforehand
# We will use default parameters for now, but in practice, these should be tuned
dbscan = DBSCAN()
dbscan_clusters = dbscan.fit_predict(features)

# Calculate the adjusted Rand index to compare the DBSCAN clusters with the actual species
dbscan_ari = adjusted_rand_score(data_decoded['种类编码'], dbscan_clusters)

# Hierarchical Clustering
from sklearn.cluster import AgglomerativeClustering

# We will use the same number of clusters as the number of unique species
hierarchical = AgglomerativeClustering(n_clusters=num_clusters)
hierarchical_clusters = hierarchical.fit_predict(features)

# Calculate the adjusted Rand index to compare the Hierarchical clusters with the actual species
hierarchical_ari = adjusted_rand_score(data_decoded['种类编码'], hierarchical_clusters)

# Results
clustering_results = {
    'K-Means': kmeans_ari,
    'DBSCAN': dbscan_ari,
    'Hierarchical': hierarchical_ari
}

clustering_results
