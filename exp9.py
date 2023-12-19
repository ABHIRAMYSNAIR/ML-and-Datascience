from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score,classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=39)
d_tree=DecisionTreeClassifier(max_depth=3)
d_tree.fit(x_train,y_train)
v=d_tree.predict(x_test)
accuracy_score=accuracy_score(y_test,v)
print(accuracy_score)
report=classification_report(y_test,v,target_names=iris.target_names)
print(report)
plt.figure(figsize=(10,30))
features=iris.feature_names
target=iris.target_names
plot_tree(d_tree,feature_names=features,class_names=target)
plt.show()

