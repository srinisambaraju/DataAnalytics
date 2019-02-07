import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

from sklearn.cluster import KMeans

raw_data = pd.read_csv('D:\Springmobile Backup\Google Drive\Data Science\ChoseNoOfClusters\Countries-exercise.csv')
# print(data['Latitude'])

# remove the duplicate index column

data = raw_data.copy()

plt.scatter(data['Longitude'], data['Latitude'])
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

# select the features, basically from the dataframe extract all the rows i.e., first colon and then selecting only the
# last column as the index is 0 which is the name and the continent index is 3 and you want to extract all the values
# in that column you say from 3rd to 4th

x = data.iloc[:, 1:3]

kmeans = KMeans(4)

kmeans.fit(x)

identified_clusters = kmeans.fit_predict(x)

data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters
# plot the data once again

plt.scatter(data_with_clusters['Longitude'], data_with_clusters['Latitude'], c=data_with_clusters['Cluster'],
            cmap='rainbow')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()


# selecting the number of clusters

# kmeans.inertia_

# Write a loop that calculates and saves the WCSS for any number of clusters from 1 up to 10 (or more if you wish).
wcss = []
no_of_clusters = 11
for i in range(1,no_of_clusters):
    kmeans = KMeans(i)
    kmeans.fit(x)
    wcss_iter = kmeans.inertia_
    wcss.append(wcss_iter)
print(wcss)

# The elbow method

number_of_clusters = range(1, no_of_clusters)
plt.plot(number_of_clusters, wcss)
plt.title('The Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Within-cluster number of squares')
plt.show()

# 2 Clusters

kmeans = KMeans(2)

kmeans.fit(x)

identified_clusters = kmeans.fit_predict(x)

data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters
# plot the data once again

plt.scatter(data_with_clusters['Longitude'], data_with_clusters['Latitude'], c=data_with_clusters['Cluster'],
            cmap='rainbow')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

# 3 Clusters

kmeans = KMeans(3)

kmeans.fit(x)

identified_clusters = kmeans.fit_predict(x)

data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters
# plot the data once again

plt.scatter(data_with_clusters['Longitude'], data_with_clusters['Latitude'], c=data_with_clusters['Cluster'],
            cmap='rainbow')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()
