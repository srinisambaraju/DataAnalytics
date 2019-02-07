import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans


data = pd.read_csv('D:\Springmobile Backup\Google Drive\Data Science\CountryCluster\\3.01. Country clusters.csv')
print(data)

plt.scatter(data['Longitude'], data['Latitude'])
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.xlim(-100, 150)
plt.ylim(-90, 90)
# plt.show()

# select the features
x = data.iloc[:, 1:3]
print(x)
# The value 2 below is we are doing 2 clusters
kmeans = KMeans(2)
kmeans.fit(x)

identified_clusters = kmeans.fit_predict(x)
print(identified_clusters)

data_with_clusters = data.copy()
data_with_clusters['Clusters'] = identified_clusters
print(data_with_clusters)

plt.scatter(data_with_clusters['Longitude'],data_with_clusters['Latitude'], c=data_with_clusters['Clusters'], cmap='rainbow')
plt.xlim(-150, 150)
plt.ylim(-90, 90)
plt.show()


# run the same thing with 3 clusters
# when you run this you get 3 different clusters, i.e., US and Canada are in one cluster, Genrmany, UK and France are
# in once cluster and Australia is all alone in another cluster
kmeans = KMeans(3)
kmeans.fit(x)

identified_clusters = kmeans.fit_predict(x)
print(identified_clusters)

data_with_clusters = data.copy()
data_with_clusters['Clusters'] = identified_clusters
print(data_with_clusters)

plt.scatter(data_with_clusters['Longitude'],data_with_clusters['Latitude'],c = data_with_clusters['Clusters'],cmap='rainbow')
plt.xlim(-150, 150)
plt.ylim(-90, 90)
plt.show()


