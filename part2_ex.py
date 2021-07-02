# https://www.kaggle.com/c/titanic

import pandas as pd
#
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

df = pd.read_csv('world.csv')
# df['Age'] = 0
print("= Conutry = "*30)

print(df['Country']," REG ",df['Region'])
# print(df)

print("= Describe = "*30)
print(df.describe())
print("= info = "*30)

print(df.info())
print("= sample = "*30)

print(df.sample())

print("= columns = "*40)
print(df.columns)


"""
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
 
 
df = pd.read_csv('train.csv')
# df['Age'] = 0
del df['Age']
print(df)
 
# print(df.describe())
# print(df.info())
# print(df.sample())
# print(df.columns)
 
 
 
pd.crosstab(df['Sex'],df['Survived'])
"""
