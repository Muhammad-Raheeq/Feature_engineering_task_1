from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd


df = pd.DataFrame({
    'f1': [1, 2, 3, 4],
    'f2': [2, 3, 4, 5],
    'f3': [5, 4, 3, 2]
})

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
pca = PCA(n_components=2)
pca = pca.fit_transform(df_scaled)
pca2 = pd.DataFrame(pca, columns=['PC1', 'PC2'])

print(pca2)