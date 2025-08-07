import pandas as pd

# From date
df = pd.DataFrame({'date': pd.to_datetime(['2023-01-01', '2023-06-15'])})
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day']=df['date'].dt.day

print(df)