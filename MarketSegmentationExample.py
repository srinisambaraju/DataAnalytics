import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.cluster import KMeans


raw_data = pd.read_csv('D:\Springmobile Backup\Google Drive\Data Science\MarketingSegmentationExample\\3.12.Example.csv')

print(raw_data)

plt.scatter(raw_data['Satisfaction'], raw_data['Loyalty'])
plt.xlabel('Satisfactory')
plt.ylabel('Loyalty')
plt.show()

# The graph can be divided into 4 parts Low Satisfaction Low loyalty, Low satisfaction high loyalty, High satisfaction
# High loyalty, High satisfaction, Low loyalty


x = raw_data.copy()

# The report below with 2 clusters
kmeans = KMeans(2)
kmeans.fit(x)

clusters = x.copy()
print('Clusters')
print(clusters)
clusters['cluster_pred'] = kmeans.fit_predict(x)

# plot the data with cluster
# once the graph shows up, the clustering shown is weird and not what you expected
# There is a cutoff line of satisfaction value of 6 and everything on the right is one cluster and everything on the
# left is another cluster. The algorithm only considered the Satisfaction as a feature , why? because we didn't
# standardize the variable, the satisfaction values are much higher than Loyalty values i.e., 1- 10 vs -1.5 t0 1.5
# and Kmeans disregarded the loyalty as a feeature
# When ever we cluster on the basis of a single feature, the result will like this graph and it's cut of at a single
# point and this is a way to find something is fishy
# so how can we fix this problem, the way to do is standardizing Satisfaction
plt.scatter(clusters['Satisfaction'], clusters['Loyalty'], c=clusters['cluster_pred'], cmap='rainbow')

plt.xlabel('Satisfactory')
plt.ylabel('Loyalty')
plt.show()

from sklearn import preprocessing
# scales (standardizes with mean 0, and standard deviation of 1 by default) each variable is scaled separately
x_scaled = preprocessing.scale(x)
print(x_scaled[0])

# basically X_scaled contains the standardized 'Satisfaction' and the same values for 'Loyalty'
# it has a mean os 0 and Standard deviation of 1
# since we don't know the number of clusters needed we will use the Elbow method to get that

WCSS = []

for i in range(1,10):
    kmeans = KMeans(i)
    kmeans.fit(x)
    WCSS.append(kmeans.inertia_)
# the above loop will get the WCSS for 1 to 9 cluster solutions

# Lets plot the WCSS clusters vs the number of clusters

plt.plot(range(1,10), WCSS)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# the elbow graph gives you that there are 4 clusters that need to be performed i.e, there is a dip at cluster 2
# dip at cluster 3, dip at cluster 4 and dip at cluster 5, but which one give you the right no of clusters, we need to
# plot the graph for each of those

# test it for 3 clusters
kmeans = KMeans(3)
kmeans.fit(x)

clusters = x.copy()
print('Clusters')
print(clusters)
clusters['cluster_pred'] = kmeans.fit_predict(x)
plt.scatter(clusters['Satisfaction'], clusters['Loyalty'], c=clusters['cluster_pred'], cmap='rainbow')
plt.xlabel('Satisfactory')
plt.ylabel('Loyalty')
plt.show()

# test it for 4 clusters
kmeans = KMeans(4)
kmeans.fit(x)

clusters = x.copy()
print('Clusters')
print(clusters)
clusters['cluster_pred'] = kmeans.fit_predict(x)
plt.scatter(clusters['Satisfaction'], clusters['Loyalty'], c=clusters['cluster_pred'], cmap='rainbow')
plt.xlabel('Satisfactory')
plt.ylabel('Loyalty')
plt.show()

# test it for 5 clusters
kmeans = KMeans(5)
kmeans.fit(x)

clusters = x.copy()
print('Clusters')
print(clusters)
clusters['cluster_pred'] = kmeans.fit_predict(x)
plt.scatter(clusters['Satisfaction'], clusters['Loyalty'], c=clusters['cluster_pred'], cmap='rainbow')
plt.xlabel('Satisfactory')
plt.ylabel('Loyalty')
plt.show()

# as you can see from the graphs that 4 clusters gives you an accurate result

# also when the graph is displayed we still need to name the clusters ourselves. i.e.,
# In unsupervised learning the algorithm will do the magic but WE need to interpret the result

# in the 4th and 5th kmeans we can define the cluster names as
# Alienated , Supporters, Fans, and Roamers
