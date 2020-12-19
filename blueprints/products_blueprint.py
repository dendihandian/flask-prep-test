from flask import Blueprint, jsonify

products_blueprint = Blueprint('products_blueprint', __name__)

@products_blueprint.route('/products')
def product_list():
    return jsonify({'data': [{'id': 1, 'name': 'Cappucinno'}]})