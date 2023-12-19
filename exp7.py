import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
data = pd.read_csv('Salary_Data.csv')
x=data['YearsExperience'].values.reshape(-1,1)
y=data['Salary'].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=39)
lr=LinearRegression()
lr.fit(x_train,y_train)
v=lr.predict(x_test)
r2score=r2_score(y_test,v)
print(r2score)
plt.scatter(x_test,y_test,color='black')
plt.plot(x_test,v,color='blue',linewidth=1,label='Regression lines')
plt.xlabel('Yearsexperience')
plt.ylabel('salary')
plt.legend()
plt.show()
new_data=np.array([8,95,42]).reshape(-1,1)
nn=lr.predict(new_data)
pp=data.target_names[nn[0]]
print(nn)
