from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from  sklearn.svm import SVC
cat=['alt.atheism','soc.religion.christian','comp.graphics','sci.med']
news=fetch_20newsgroups(subset="train",categories=cat,shuffle=True,random_state=43)
vectorizer=TfidfVectorizer()
x_train_tfidf = vectorizer.fit_transform(news.data)
y_train_tfidf = news.target
x_train,x_test,y_train,y_test=train_test_split(x_train_tfidf,y_train_tfidf,test_size=0.2,random_state=43)
svm=SVC(kernel='linear',random_state=43)
svm.fit(x_train,y_train)
v=svm.predict(x_test)
accuracy=accuracy_score(y_test,v)
print(accuracy)
report=classification_report(y_test,v,target_names=news.target_names)
print(report)
new_data=['iam a christian','i respect medical field']
new_data_vector=vectorizer.transform(new_data)
new_prediction=svm.predict(new_data_vector)
for i,text in enumerate(new_data):
    pred_cat=news.target_names[new_prediction[i]]
    print(f"{text}",":",f"{pred_cat}")
