import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.cluster import KMeans


data = pd.read_csv('D:\Springmobile Backup\Google Drive\Data Science\Cluster1\\Countries-exercise1.csv')
# print(data.encode("utf-8"))

plt.scatter(data['Longitude'],data['Latitude'])
plt.show()



x = data.iloc[:, 1:]

print(x)

# define a cluster with 2 means
kmeans = KMeans(2)

kmeans.fit(x)
identified_clusters = kmeans.fit_predict(x)
data_with_clusters = data.copy()
data_with_clusters['Clusters'] = identified_clusters

# print(data_with_clusters)

plt.scatter(data_with_clusters['Longitude'],data['Latitude'], c=data_with_clusters['Clusters'],cmap='rainbow')
plt.show()

# Do a cluster of 7
kmeans = KMeans(7)

kmeans.fit(x)
identified_clusters = kmeans.fit_predict(x)
data_with_clusters = data.copy()
data_with_clusters['Clusters'] = identified_clusters

# print(data_with_clusters)

plt.scatter(data_with_clusters['Longitude'], data['Latitude'], c=data_with_clusters['Clusters'], cmap='rainbow')
plt.show()
