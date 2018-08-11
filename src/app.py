from flask import Flask
from flask_restful import Api
from src.resources.product import Product
from src.common.setting import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Product, API_PRODUCT_SEARCH_PATH)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=APPLICATION_PORT, debug=DEBUG)
