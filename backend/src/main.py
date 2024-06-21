from flask import Flask, jsonify
from db import Products

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return Products

@app.route('/products/<category>', methods=['GET'])
def get_products_by_category(category: str):
    products_by_category = list(filter(lambda product :  product['category'] == category.capitalize(), Products))
    if products_by_category:
        return products_by_category
    else:
        return jsonify({'erro': 'Categoria não encontrada'}), 404
    

app.run()
