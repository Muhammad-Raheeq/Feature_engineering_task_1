import pandas as pd


df = pd.DataFrame({
    'city': ['A', 'B', 'A', 'C', 'B'],
    'target': [1, 0, 1, 0, 1]
})
#taking mean by combining two or more variable or keys
mean_encoding = df.groupby('city')['target'].mean()
df['city_encoded'] = df['city'].map(mean_encoding)
print(df['city_encoded'])
print(df)