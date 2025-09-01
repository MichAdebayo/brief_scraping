import csv, sqlite3  # Import necessary modules


# Connect to (or create) the SQLite database 'casto.db'
con = sqlite3.connect('casto.db') 
cur = con.cursor()  # Create a cursor object to execute SQL commands

# Create the 'categories' table with columns: category, is_page_list, url
cur.execute("CREATE TABLE categories (category, is_page_list,url);")

# Read data from 'categories2.csv' and prepare it for insertion
with open('categories2.csv','r') as f:
    dr = csv.DictReader(f)  # Read CSV as dictionary
    to_db = [(i['category'], i['is_page_list'],i['url']) for i in dr]  # Extract relevant fields

# Insert all rows from CSV into the 'categories' table
cur.executemany("INSERT INTO categories (category,is_page_list,url) VALUES (?, ?, ?);", to_db)
con.commit()  # Commit changes to the database

# Create the 'products' table with specified columns
cur.execute("CREATE TABLE products (unique_id,category,subcategory,subsubcategory,subsubsubcategory,title,price,url);")

# Read data from 'products.csv' and prepare it for insertion
with open('products.csv','r') as f:
    dp = csv.DictReader(f)  # Read CSV as dictionary
    to_db = [(i['unique_id'], i['category'], i['subcategory'], i['subsubcategory'], i['subsubsubcategory'], i['title'], i['price'], i['url']) for i in dp]  # Extract relevant fields

# Insert all rows from CSV into the 'products' table
cur.executemany("INSERT INTO products (unique_id,category,subcategory,subsubcategory,subsubsubcategory,title, price,url) VALUES (?, ?, ?, ?,?,?, ?,?);", to_db)
con.commit()  # Commit changes to the database
con.close()  # Close the database connection
