from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
ch=fetch_california_housing()
# print(ch)
df=pd.DataFrame(data=ch.data,columns=ch.feature_names)
df['target']=ch.target
x=df.drop('target',axis=1)
y=df['target']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=29)
lr=LinearRegression()
lr.fit(x_train,y_train)
v=lr.predict(x_test)
mse=mean_squared_error(y_test,v)
print(mse)
plt.scatter(df['MedInc'],df['target'],color='red',label='datapoints')
plt.plot(y_test,v,color='blue',label='regression lines')
plt.show()