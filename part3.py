# import pandas as pd
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# import  seaborn as sb
# import  matplotlib as mtl

# df=pd.read_csv("train.csv")
# print(df)
# print("= sample ="*10)
# print(df.sample())
# print("= Cross tab ="*10)
# sr=pd.crosstab(df['Fare'],df['Survived'])

# print(sr)
# print("= M/f ="*10)
# print(df["Fare"])
# print("Survived",df["Survived"])


import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
# df.sample()
#
# sr = pd.crosstab(df['Sex'],df['Survived'])

# print(sr)

ax = sb.countplot(x ='Sex', hue="Survived", palette='Set1', data=df)
ax.set(title='Survivors data',xlabel='Sex',ylabel='Numbers')
plt.show()

fp = sb.factorplot(x='Pclass',y='Survived',hue='Sex',data=df,aspect=0.9,size=3)
# sb.factorplot()
fp_Ebbark = sb.factorplot(x='Embarked',y='Survived',hue='Sex',data=df,aspect=0.9,size=3)

