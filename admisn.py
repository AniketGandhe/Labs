import pandas as pd
import seaborn as sns
df= pd.read_csv(" Admission")
df.columns
df.shape
df.head()

from sklearn.preprocessing import Binarizer
bi = Binarizer(threshold = 0.75)
df["Chance of Admit"]=bi.fit_transform(df[["Chance of Admit"]])
df.head()
x= df.drop("Chance of Admit", axis =1)
y=df["Chance of Admit"]

y=y.astype('int')
sns.countplot(x=y)
y.value_counts()

from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test=tts(x,y,random_state=0,test_size=0.25)
x_train.shape
x_test.shape
