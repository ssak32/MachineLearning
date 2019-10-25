# Create KMeans Clustering Model

#Importing matplotlib.pyplot to plot the results
import matplotlib.pyplot as plt

#Importing pandas library to read CSV data file
import pandas as pd

#Reading CSV data file into Python
dataset = pd.read_csv('Movies.csv')
X = dataset.iloc[:, [0, 2]].values

#Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#Importing and Fitting K-Means to dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
y = kmeans.fit_predict(X)

# Plotting results to show the clusters
plt.scatter(X[y == 0, 0], X[y == 0, 1], s = 50, c = 'blue', label = 'Cluster 1')
plt.scatter(X[y == 1, 0], X[y == 1, 1], s = 50, c = 'red', label = 'Cluster 2')
plt.scatter(X[y == 2, 0], X[y == 2, 1], s = 50, c = 'purple', label = 'Cluster 3')
plt.title('Clusters of customers')
plt.xlabel('Production Budgest($M)')
plt.ylabel('Gross Income($M)')
plt.legend()
plt.show()