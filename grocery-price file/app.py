from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_prices', methods=['GET'])
def get_prices():
    product = request.args.get('product')
    area = request.args.get('area')

    conn = get_db_connection()
    cur = conn.cursor()

    query = '''
        SELECT s.name AS store, p.price
        FROM prices p
        JOIN products pr ON p.product_id = pr.id
        JOIN supermarkets s ON p.supermarket_id = s.id
        WHERE pr.name = ? AND s.area = ?
    '''
    cur.execute(query, (product, area))
    data = cur.fetchall()
    conn.close()

    result = [{'store': row['store'], 'price': row['price']} for row in data]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    product = request.form['product_name']
    area = request.form['area']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT store_name, price FROM products
        WHERE product_name=? AND area=?
    ''', (product, area))
    results = cur.fetchall()
    conn.close()
    if results:
        return render_template('index.html', prices=results, product=product, area=area)
    else:
        flash('Data not found for the given product and area.')
        return redirect(url_for('home'))

# New route to show form
@app.route('/add-product', methods=['GET'])
def add_product_form():
    return render_template('add_product.html')

# New route to handle form submission
@app.route('/add-product', methods=['POST'])
def add_product():
    product_name = request.form['product_name']
    area = request.form['area']
    store_name = request.form['store_name']
    price = request.form['price']

    if not product_name or not area or not store_name or not price:
        flash('Please fill all the fields!')
        return redirect(url_for('add_product_form'))

    try:
        price = float(price)
    except ValueError:
        flash('Please enter a valid number for price.')
        return redirect(url_for('add_product_form'))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO products (product_name, area, store_name, price)
        VALUES (?, ?, ?, ?)
    ''', (product_name, area, store_name, price))
    conn.commit()
    conn.close()
    flash('Product added successfully!')
    return redirect(url_for('add_product_form'))

if __name__ == '__main__':
    app.run(debug=True)
print(app.url_map)
