import pandas as pd
import matplotlib

dfcat = pd.read_csv('categories.csv')
dfprod = pd.read_csv('products.csv')
price_prod_jardin = dfprod[['price', 'title']][dfprod['category'] == 'jardin-et-terrasse']
max_price_cat = dfprod.loc[dfprod['price'].idxmax()]
# print(price_prod_jardin)
print(max_price_cat)