import csv, sqlite3

con = sqlite3.connect('casto.db') 
cur = con.cursor()
cur.execute("CREATE TABLE categories (category,subcategory,subsubcategory,subsubsubcategory,unique_id,url);")

with open('categories.csv','r') as f:
    dr = csv.DictReader(f)
    to_db = [(i['category'], i['subcategory'],i['subsubcategory'], i['subsubsubcategory'],i['unique_id'], i['url']) for i in dr]

cur.executemany("INSERT INTO categories (category,subcategory,subsubcategory,subsubsubcategory,unique_id,url) VALUES (?, ?, ?, ?,?,?);", to_db)
con.commit()

cur.execute("CREATE TABLE products (unique_id,category,subcategory,subsubcategory,subsubsubcategory,title,price,url);")

with open('products.csv','r') as f:
    dp = csv.DictReader(f)
    to_db = [(i['unique_id'], i['category'], i['subcategory'], i['subsubcategory'], i['subsubsubcategory'], i['title'], i['price'], i['url']) for i in dp]

cur.executemany("INSERT INTO products (unique_id,category,subcategory,subsubcategory,subsubsubcategory,title, price,url) VALUES (?, ?, ?, ?,?,?, ?,?);", to_db)
con.commit()
con.close()
