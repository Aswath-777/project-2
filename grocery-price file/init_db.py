import sqlite3

# Connect to (or create) database
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Delete old tables if they exist
cur.execute("DROP TABLE IF EXISTS products")
cur.execute("DROP TABLE IF EXISTS supermarkets")
cur.execute("DROP TABLE IF EXISTS prices")

# Create tables
cur.execute('''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
''')

cur.execute('''
CREATE TABLE supermarkets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    area TEXT
)
''')

cur.execute('''
CREATE TABLE prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    supermarket_id INTEGER,
    price REAL,
    FOREIGN KEY(product_id) REFERENCES products(id),
    FOREIGN KEY(supermarket_id) REFERENCES supermarkets(id)
)
''')

# Insert sample data
cur.execute("INSERT INTO products (name) VALUES ('Rice')")
cur.execute("INSERT INTO products (name) VALUES ('Milk')")

cur.execute("INSERT INTO supermarkets (name, area) VALUES ('Reliance', 'T Nagar')")
cur.execute("INSERT INTO supermarkets (name, area) VALUES ('Big Bazaar', 'T Nagar')")
cur.execute("INSERT INTO supermarkets (name, area) VALUES ('More', 'T Nagar')")

cur.execute("INSERT INTO prices (product_id, supermarket_id, price) VALUES (1, 1, 52.00)")
cur.execute("INSERT INTO prices (product_id, supermarket_id, price) VALUES (1, 2, 49.50)")
cur.execute("INSERT INTO prices (product_id, supermarket_id, price) VALUES (1, 3, 51.00)")

cur.execute("INSERT INTO prices (product_id, supermarket_id, price) VALUES (2, 1, 24.00)")
cur.execute("INSERT INTO prices (product_id, supermarket_id, price) VALUES (2, 2, 26.50)")
cur.execute("INSERT INTO prices (product_id, supermarket_id, price) VALUES (2, 3, 25.00)")

# Save and close
conn.commit()
conn.close()
