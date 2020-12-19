from flask import Blueprint, jsonify

products = Blueprint('products', __name__)

@products.route('/products')
def product_list():
    return jsonify({'data': [{'id': 1, 'name': 'Cappucinno'}]})