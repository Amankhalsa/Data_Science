import pandas as pd
pd.set_option("display.max_columns", None)
df_train =pd.read_csv('train.csv')
# print(df_train.sample(5))
y= df_train["Survived"]
x=df_train.drop(["Survived","PassengerId"],axis=1)
from sklearn.model_selection import train_test_split
# train_test_split()
cf=x_train,x_test, y_train, y_test=train_test_split(x,y,test_size=0.15)
print(cf)