from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
digits=load_breast_cancer()
x=digits.data
y=digits.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=40)
naive_bayes=GaussianNB()
naive_bayes.fit(x_train,y_train)
v=naive_bayes.predict(x_test)
accuracy_score=accuracy_score(y_test,v)
print(accuracy_score)
report=classification_report(y_test,v)
print(report)
cm=confusion_matrix(y_test,v)
print(cm)
plt.figure(figsize=(8,6))
sb.heatmap(cm,annot=True,cmap='Blues',fmt='g')
plt.show()