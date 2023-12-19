from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=39,shuffle=True,stratify=None)
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
v=knn.predict(x_test)
accuracy_score=accuracy_score(y_test,v)
print(accuracy_score)
report=classification_report(y_test,v)
print(report)
plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', marker='o', s=50)
plt.title("KNN Decision Boundaries")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()