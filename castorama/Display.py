# Import pandas for data manipulation 
import pandas as pd

# Load categories data from CSV
dfcat = pd.read_csv('categories.csv')
# Load products data from CSV
dfprod = pd.read_csv('products.csv')

# Filter products in the 'jardin-et-terrasse' category and select price and title columns
price_prod_jardin = dfprod[['price', 'title']][dfprod['category'] == 'jardin-et-terrasse']

# Find the product with the maximum price
max_price_cat = dfprod.loc[dfprod['price'].idxmax()]
# print(price_prod_jardin)  # Uncomment to display filtered products

# Print the product with the highest price
print(max_price_cat)