from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.DataFrame({
    'height': [150, 160, 170, 180],
    'weight': [50, 60, 70, 80]
})
# Standardization 
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
print(df_scaled)
