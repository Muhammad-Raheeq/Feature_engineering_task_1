import pandas as pd

# feature transformation
df = pd.DataFrame({
    'gender': ['male', 'female', 'female', 'male']
})
# One hot encoding
encoded = pd.get_dummies(df, columns=['gender'])
print(encoded)
# Label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['encoded'] = le.fit_transform(df['gender'])
ec=df['encoded']
print(ec)
print(df)