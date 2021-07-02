# import numpy
import os
import pandas as pd
# pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)
# import sklearn
# import matplotlib

df =pd.read_csv("test.csv")


print("Data f printed \n",df)
print("=="*40)
print("Names are \n",df['Name'],"\nAnd age \n",df['Age'])
print("=="*40)
print("Sample========= \n",df.sample())
print("=="*40)

print("Describe======== \n",df.describe())
print("=="*40)

print("Info========= \n",df.info())
print("=="*40)


print("=="*40)
print("Col=========== \n",df.columns)
