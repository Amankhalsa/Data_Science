import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv('train.csv')
 
 
def title(name):
   if '.' in name:
      return name.split(',')[1].split('.')[0].strip()
   else:
      return 'No title Exists'
   
 
unique_titles =set([x for x in df['Name'].map(lambda x: title(x))])
 
print(unique_titles)
 
 
def compact_titles(x):
   title_new= x['Title']
   if title_new in ['Capt','Col','Major']:
      return 'Officer'
   elif title_new in ['Sir','Ms','Jonkheer','Dona','Lady']:
      return 'Royale People'
   elif title_new == 'Mme':
      return 'Mrs'
   elif title_new in ['Mlle','Ms']:
      return 'Miss'
   else:
      return title_new
   
 
df['Title'] = df['Name'].map(lambda x:title(x))
 
df['Title'] = df.apply(compact_titles,axis=1)
 
# print(df.Title.value_counts())
 
df.drop('Name',axis=1,inplace=True)
print(df.sample(20))