import pandas as pd


df = pd.DataFrame({'age': [18, 25, 35, 45, 55, 65]})
# feature binning (just split the age into different catogaries)
df['old'] = pd.cut(df['age'], bins=[0, 30, 50, 70], labels=['Young', 'Middle', 'Old'])
old=df['old'] 
print(old)
print(df)