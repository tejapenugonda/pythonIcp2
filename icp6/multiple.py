import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("weatherHistory.csv")

data=data.drop('Summary',axis=1)

data=data.drop('Daily Summary',axis=1)
data['PrecipType']=pd.get_dummies(data.PrecipType, drop_first=True)

y=data.Temperature
x=data.drop('Temperature',axis=1)

X_train, X_test, y_train, y_test = train_test_split(x,y,random_state=42, test_size=.33)

from sklearn import linear_model
lr1=linear_model.LinearRegression()
model=lr1.fit(X_train,y_train)
print('R-squared',model.score(X_test,y_test))
prediction=model.predict(X_test)
from sklearn.metrics import mean_squared_error
print('RMSE',mean_squared_error(y_test,prediction))