import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')



for column in df:
   print(column, ' :: ', df[column].isnull().sum())

df['Age'].fillna(df['Age'].median(),inplace=True)

df['Embarked'].value_counts()
df['Embarked'].fillna('S',inplace=True)

del df['Cabin']

print("= Clean data ="*3)

for column in df:
   print(column, ' :: ', df[column].isnull().sum())