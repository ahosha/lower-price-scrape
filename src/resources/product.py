from flask_restful import Resource, reqparse
from src.models.product import ProductModel
from src.models.stores.walmart_store import WalmartStore
from src.models.stores.bestbuy_store import BestbuyStore
from src.common import consts
from src.common.setting import *
from src.common.consts import *


def stores_list_factory(stores):
    """ stores = [WalmartStore(), BestbuyStore()] """
    for store in STORES_TO_SCAN:
        if store == 'Walmart':
            stores.append(WalmartStore())
        elif store == 'Walmart':
            stores.append(BestbuyStore())


def parse_varify_params():
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, help=consts.EMPTY_NAME)
    product_name = parser.parse_args()
    name_value = product_name['name']
    return name_value


class Product(Resource):

    def get(self):
        """get lowest current available price for product"""
        name_value = parse_varify_params()
        stores = []
        stores_list_factory(stores)
        if stores:
            product_model = ProductModel(name_value, stores)
            return product_model.search(), 200
        else:
            return EMPTY_STORES_LIST, 404
