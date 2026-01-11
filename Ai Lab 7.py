# Task 1: Manual K-Means with Plotting
'''
import math
import matplotlib.pyplot as plt

# Dataset
data = [(1.1, 1.1), (1.5, 2.1), (3.1, 4.1), (5.1, 7.1),
        (3.5, 5.1), (4.5, 5.1), (3.5, 4.5)]

# Initial centroids
centroid1 = (1.1, 1.1)
centroid2 = (5.1, 7.1)

# Euclidean Distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Manual K-Means
def k_means(data, centroid1, centroid2, iterations=100):
    for _ in range(iterations):
        cluster1, cluster2 = [], []

        # Assign points to nearest centroid
        for point in data:
            d1 = euclidean_distance(point, centroid1)
            d2 = euclidean_distance(point, centroid2)

            if d1 < d2:
                cluster1.append(point)
            else:
                cluster2.append(point)

        # Update centroids
        centroid1 = (
            sum(x for x, _ in cluster1) / len(cluster1),
            sum(y for _, y in cluster1) / len(cluster1)
        )

        centroid2 = (
            sum(x for x, _ in cluster2) / len(cluster2),
            sum(y for _, y in cluster2) / len(cluster2)
        )

    return cluster1, cluster2, centroid1, centroid2


# Run K-Means
cluster1, cluster2, c1, c2 = k_means(data, centroid1, centroid2)

print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)
print("Final Centroid 1:", c1)
print("Final Centroid 2:", c2)

# ------------ Plotting -------------
plt.figure(figsize=(7, 5))

# Cluster 1 points
x1 = [p[0] for p in cluster1]
y1 = [p[1] for p in cluster1]
plt.scatter(x1, y1, label="Cluster 1", s=80)

# Cluster 2 points
x2 = [p[0] for p in cluster2]
y2 = [p[1] for p in cluster2]
plt.scatter(x2, y2, label="Cluster 2", s=80)

# Plotting final centroids
plt.scatter(c1[0], c1[1], color='red', marker='X', s=200, label="Centroid 1")
plt.scatter(c2[0], c2[1], color='black', marker='X', s=200, label="Centroid 2")

plt.title("Manual K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
'''

'''
# Task 2: K-Means & Agglomerative Clustering with Plotting
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering

# Numeric dataset
data = np.array([
    [1.1, 1.1], [1.5, 2.1], [3.1, 4.1],
    [5.1, 7.1], [3.5, 5.1], [4.5, 5.1], [3.5, 4.5]
])

# ----- K-Means -----
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(data)
kmeans_labels = kmeans.labels_
kmeans_centroids = kmeans.cluster_centers_

print("K-means Labels:", kmeans_labels)
print("K-means Centroids:\n", kmeans_centroids)

# ----- Agglomerative -----
agg = AgglomerativeClustering(n_clusters=2)
agg_labels = agg.fit_predict(data)

print("Agglomerative Labels:", agg_labels)

# -------- Plotting --------
plt.figure(figsize=(14, 5))

# K-means plot
plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1], c=kmeans_labels, s=80)
plt.scatter(kmeans_centroids[:, 0], kmeans_centroids[:, 1],
            marker='X', s=200, color='red')
plt.title("K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# Agglomerative plot
plt.subplot(1, 2, 2)
plt.scatter(data[:, 0], data[:, 1], c=agg_labels, s=80)
plt.title("Agglomerative Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.show()
'''

# Task 2 Part B: Clustering on mushrooms.csv
