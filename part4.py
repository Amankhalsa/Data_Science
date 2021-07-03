# Correcting 
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
     
df = pd.read_csv('train.csv')
     
     
     
graph = sb.FacetGrid(df, col='Survived')
graph.map(plt.hist,'Fare', bins=5)
     
df.loc[df['Fare']>400,'Fare'] = df['Fare'].median()
plt.show()