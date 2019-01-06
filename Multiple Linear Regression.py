# Multiple linear regresssion

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

startup_data = pd.read_csv('50_Startups.csv')
X = startup_data.iloc[:,:-1].values
Y = startup_data.iloc[:,4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lb_encoder = LabelEncoder()
X[:,3] = lb_encoder.fit_transform(X[:,3])
one_hotencoder = OneHotEncoder(categorical_features = [3])
X = one_hotencoder.fit_transform(X).toarray()

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

y_pred = regressor.predict(X_test) 