from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
iris=load_iris()
print(iris)
x=iris.data
kmeans=KMeans(n_clusters=3,random_state=39)
kmeans.fit(x)
c_labels=kmeans.labels_
print(c_labels)
centroid=kmeans.cluster_centers_
plt.scatter(x[:,0],x[:,1],c=c_labels,cmap='viridis',marker='o',edgecolors='black',label='cluster')
plt.scatter(centroid[:,0],centroid[:,1],marker='*',s=200,c='red',label='centroid')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('KMeans cluster')
plt.legend()
plt.show()