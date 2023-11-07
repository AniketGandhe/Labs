# -*- coding: utf-8 -*-
"""Assig4_cluster.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16kwDcQ1UZMTgfHU7zjRPkf7JVhgiXjL-
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing  import MinMaxScaler
from matplotlib import pyplot as plt
# %matplotlib inline

df =pd.read_csv("/content/Mall_Customers.csv")
df.head()

plt.scatter(df.Age,df['Annual Income (k$)'])
plt.xlabel('Age')
plt.ylabel('Income')



km =KMeans(n_clusters=3)
y_predicted =km.fit_predict(df[['Age','Annual Income (k$)']])
y_predicted

df['cluster']=y_predicted
df.head()

km.cluster_centers_

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.Age,df1["Income"],color="green")
plt.scatter(df2.Age,df2["Income"],color="red")
plt.scatter(df3.Age,df3["Income"],color="black")
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color="purple",marker="*")
plt.xlabel("Age")
plt.ylabel("Income")
plt.legend()

scaler = MinMaxScaler()
scaler.fit(df[['Annual Income (k$)']])
df['Annual Income (k$)']=scaler.transform(df[['Annual Income (k$)']])

scaler.fit(df[['Age']])
df['Age']=scaler.transform(df[['Age']])
df.head()

plt.scatter(df.Age,df['Annual Income (k$)'])

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.Age,df1['Annual Income (k$)'],color='green')
plt.scatter(df2.Age,df2['Annual Income (k$)'],color='red')
plt.scatter(df3.Age,df3['Annual Income (k$)'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*')
plt.xlabel('Age')
plt.ylabel('Annual Income (k$)')
plt.legend()

sse =[]
k_rng = range(1,10)
for k in k_rng:
  km =KMeans(n_clusters=k)
  km.fit(df[['Age','Annual Income (k$)']])
  sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)
