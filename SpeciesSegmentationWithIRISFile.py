import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.cluster import KMeans

data = pd.read_csv('D:\Springmobile Backup\Google Drive\Data Science\IRIS Dataset\iris-dataset.csv')

print(data)

plt.scatter(data['sepal_length'],data['sepal_width'])
plt.xlabel('Length of sepal')
plt.ylabel('Width of sepal')
plt.show()


x = data.copy()

kmeans = KMeans(2)
print(kmeans.fit(x))
clusters = x.copy()
clusters['cluster_pred'] = kmeans.fit_predict(x)
plt.scatter(clusters['sepal_length'], clusters['sepal_width'], c=clusters['cluster_pred'], cmap='rainbow')
plt.xlabel('Length of sepal')
plt.ylabel('Width of sepal')
plt.show()

# find the WCSS

from sklearn import preprocessing
# scales (standardizes with mean 0, and standard deviation of 1 by default) each variable is scaled separately
x_scaled = preprocessing.scale(x)
print(x_scaled)

kmeans_scaled = KMeans(2)
kmeans_scaled.fit(x_scaled)

clusters = x.copy()
clusters['cluster_pred'] = kmeans_scaled.fit_predict(x_scaled)
plt.scatter(clusters['sepal_length'], clusters['sepal_width'], c=clusters['cluster_pred'], cmap='rainbow')
plt.xlabel('Length of sepal')
plt.ylabel('Width of sepal')
plt.show()



wcss = []

for i in range(1, 10):
    kmeans = KMeans(i)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
# print(wcss)


# plot the elbow graph

plt.plot(range(1,10), wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()



# 3

kmeans = KMeans(3)
print(kmeans.fit(x))
clusters = x.copy()
clusters['cluster_pred'] = kmeans.fit_predict(x)
plt.scatter(clusters['sepal_length'], clusters['sepal_width'], c=clusters['cluster_pred'], cmap='rainbow')
plt.xlabel('Length of sepal')
plt.ylabel('Width of sepal')
plt.show()

# 4

kmeans = KMeans(4)
print(kmeans.fit(x))
clusters = x.copy()
clusters['cluster_pred'] = kmeans.fit_predict(x)
plt.scatter(clusters['sepal_length'], clusters['sepal_width'], c=clusters['cluster_pred'], cmap='rainbow')
plt.xlabel('Length of sepal')
plt.ylabel('Width of sepal')
plt.show()

# 5
kmeans = KMeans(5)
print(kmeans.fit(x))
clusters = x.copy()
clusters['cluster_pred'] = kmeans.fit_predict(x)
plt.scatter(clusters['sepal_length'], clusters['sepal_width'], c=clusters['cluster_pred'], cmap='rainbow')
plt.xlabel('Length of sepal')
plt.ylabel('Width of sepal')
plt.show()



