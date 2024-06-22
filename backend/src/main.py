from flask import Flask, jsonify
from database import db_cursor

app = Flask(__name__)

def format_products(data_list: list):

    products = list()

    for product in data_list:
        products.append(
            {
                'id': product[0],
                'name': product[1],
                'category': product[2],
                'description': product[3],
                'image_url': product[4],
                'price': product[5],
                'rating': product[6],
                'date': product[7],
            }
        )
    return products

def format_reviews(data_list: list):
    products = list()

    for review in data_list:
        products.append(
            {
                'id': review[0],
                'product_id': review[1],
                'user': review[2],
                'description': review[3],
                'rating': review[4],
                'date': review[5],
            }
        )
    return products

@app.route('/', methods=['GET'])
def get_products():
    db_cursor.execute('SELECT * FROM products')
    data = db_cursor.fetchall()
    products = format_products(data)
    return products
   

@app.route('/products/<string:category>', methods=['GET'])
def get_products_by_category(category: str):
    db_cursor.execute(f'SELECT * FROM products WHERE category = "{category}"')
    data = db_cursor.fetchall()
    products_by_category = format_products(data)

    if products_by_category:
        return products_by_category
    else:
        return jsonify({'erro': 'Category not found'}), 404

@app.route('/reviews', methods=['GET'])
def get_reviews():
    db_cursor.execute('SELECT * FROM reviews')
    data = db_cursor.fetchall()
    products = format_reviews(data)
    return products

@app.route('/products/<int:id>', methods=['GET'])
def get_product_by_id(id: int):
    db_cursor.execute(f'SELECT * FROM products WHERE id = {id}')
    data = db_cursor.fetchall()
    product_by_id = format_reviews(data)

    if product_by_id:
        return product_by_id
    else:
        return jsonify({'erro': 'Product not found'}), 404

@app.route('/reviews/<product_id>', methods=['GET'])
def get_reviews_by_product_id(product_id: int):
    db_cursor.execute(f'SELECT * FROM reviews WHERE product_id = {product_id}')
    data = db_cursor.fetchall()
    reviews_by_product_id = format_reviews(data)

    if reviews_by_product_id:
        return reviews_by_product_id
    else:
        return jsonify({'erro': "This product doesn't have reviews yet"}), 404

app.run()

