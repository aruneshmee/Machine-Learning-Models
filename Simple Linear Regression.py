import pandas as pd
import matplotlib.pyplot as plt

Salary_data = pd.read_csv('Salary_Data.csv')
X = Salary_data.iloc[:,:-1].values
Y = Salary_data.iloc[:,1].values

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

y_pred = regressor.predict(X_test)

plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs experience')
plt.xlabel('Exper')
plt.ylabel('salary')
plt.show

plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs experience') 
plt.xlabel('Exper')
plt.ylabel('salary')
plt.show
