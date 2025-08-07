import pandas as pd
import numpy as np
# feature transformation
df = pd.DataFrame({
    'age': [25, np.nan, 28, 35, np.nan],
    'income': [50000, 60000, np.nan, 80000, 90000]
})
# fill value just like imputer in sklearn
df['age'] = df['age'].fillna(df['age'].mean())
dp=df['age']
print(dp)
# drop row which contain null data(2nd method to handle missing data but use only if misssing data is less than 5%)
df = df.dropna()
print(df)