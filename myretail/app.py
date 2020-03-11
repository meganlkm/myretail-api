import json
from collections import Mapping

from flask import Flask, request, Response

from myretail.database.db import initialize_db
from myretail.database.models import Price, Product


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://data/myretail'
}
initialize_db(app)


@app.route('/products')
def get_products():
    products = Product.objects().to_json()
    return Response(products, mimetype="application/json", status=200)


@app.route('/products/<id>')
def get_product(id):
    products = Product.objects.get(id=id).to_json()
    return Response(products, mimetype="application/json", status=200)


@app.route('/products', methods=['POST'])
def add_product():
    body = request.get_json()

    # current_price is required
    if 'current_price' not in body:
        return {"ERROR": "Missing current_price"}, 500
    # take the price attribute out of the request to
    # create the Price object and embed it into the Product object
    price = body.pop('current_price')
    # if it's a string convert it to json
    if not isinstance(price, Mapping):
        print("Loading JSON from string")
        price = json.loads(price)
    current_price = Price(**price)

    product = Product(current_price=current_price, **body).save()
    id = product.id
    return {'id': str(id)}, 200


@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    body = request.get_json()
    try:
        Product.objects.get(id=id).update(**body)
        return '', 200
    except Exception as e:
        return {"ERROR": str(e)}, 500


@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    Product.objects.get(id=id).delete()
    return '', 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
