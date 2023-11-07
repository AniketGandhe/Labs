import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df =pd.read_csv(" ")

df.head()
x=df["YEAR"]
y=df["ANNUAL"]
plt.title("Temperature in India")
plt.xlabel="Year"
plt.ylabel="Annual avg temp"
plt.scatter(x,y)
x.shape
x=x.reshape(117,1)
x.shape

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x,y)
reg.coef_
reg.intercept_
reg.predict([[2035]])
predicted = reg.predict(x)
#mean absolute error MAE
np.mean(abs(y - predicted))
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y,predicted)

# mean square error MSE
np.mean((y-predicted)**2)
from sklearn.metrics import mean_squared_error
mean_squared_error(y,predicted)

#Rsquare metrics r2
from sklearn.metrics import r2_score
r2_score(y,predicted)

reg.score(x,y)

plt.title("Temperature in INDIA")
plt.xlabel = "Year"
plt.ylabel= "Annual avg Temperature"
plt.scatter(x,y,label="Actual",color = "r", marker = ".")
plt.plot(x,predicted,label="Predicted",color = "g")
plt.legend()

sns.regplot(x="YEAR", y= "ANNUAL ", data =df)



