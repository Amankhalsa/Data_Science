# import numpy
import os 
import pandas as pd
# import sklearn required
# import pandas required
# import matplotlib required



df =pd.read_csv("train.csv")
# print(df)
# df=df.size
# print(" x "*10)
print("Df is  printed \n",df)
print("========================================================="*2)

print("Desccribe",df.describe())
print("========================================================="*2)


print("info",df.info())
print("========================================================="*2)
print("sample",df.sample())
print("========================================================="*2)
print("sample",df.columns)

