from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

df = pd.DataFrame({'x': [1, 2, 3, 4]})
print(df)
#polynomial take 1 features as input and return 2 features as output(2nd feature is square of first input )
poly = PolynomialFeatures(degree=2, include_bias=False)
poly2 = poly.fit_transform(df)
print(poly2)