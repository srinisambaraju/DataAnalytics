import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.cluster import KMeans


raw_data = pd.read_csv('D:\Springmobile Backup\Google Drive\Data Science\CategoricalClustering\Categorical.csv')
# print(data['Latitude'])

# remove the duplicate index column

data = raw_data.copy()

# data = data.drop(['Unnamed: 0'], axis = 1)


data_mapped = data.copy()

data_mapped['continent'] = data['continent'].map({'North America': 0, 'Europe': 1, 'Asia':2, 'Africa': 3, 'South America': 4,
                                           'Oceania': 5, 'Seven seas (open ocean)': 6, 'Antarctica': 7})
x = data_mapped.iloc[:, 3:4]

# Define KMeans with 4 clusters

kmeans = KMeans(4)

identified_clusters = kmeans.fit_predict(x)

data_with_clusters = data_mapped.copy()

data_with_clusters['Cluster'] = identified_clusters

plt.scatter(data['Longitude'], data['Latitude'], c=data_with_clusters['Cluster'], cmap='rainbow')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

# Define KMeans with 3 clusters

kmeans = KMeans(3)
kmeans.fit(x)
identified_clusters = kmeans.fit_predict(x)

data_with_clusters = data_mapped.copy()

data_with_clusters['Cluster'] = identified_clusters

plt.scatter(data['Longitude'], data['Latitude'], c=data_with_clusters['Cluster'], cmap='rainbow')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

# Define KMeans with 7 clusters

kmeans = KMeans(7)
kmeans.fit(x)
identified_clusters = kmeans.fit_predict(x)

data_with_clusters = data_mapped.copy()

data_with_clusters['Cluster'] = identified_clusters

plt.scatter(data['Longitude'], data['Latitude'], c=data_with_clusters['Cluster'], cmap='rainbow')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

# Define KMeans with 8 clusters

kmeans = KMeans(8)

kmeans.fit(x)
identified_clusters = kmeans.fit_predict(x)


data_with_clusters = data_mapped.copy()

data_with_clusters['Cluster'] = identified_clusters

plt.scatter(data['Longitude'], data['Latitude'], c=data_with_clusters['Cluster'], cmap='rainbow')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()
