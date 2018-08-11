from src.models.stores.base_store import BaseStore
from walmart_api_client import WalmartApiClient
from src.common.setting import *


def build_params(product_name):
    params = {
        "query": product_name,
        "format": "json"
    }
    return params


def get_min_price(price_list, search_response):
    products = search_response[WALMART_PRODUCTS_TAG_NAME]
    for item in products:
        price_list.append(item[WALMART_PRICE_TAG_NAME])
    min_price = min(price_list)
    return min_price


class WalmartStore(BaseStore):
    name = WALMART_STORE_NAME
    key = WALMART_KEY
    currency = WALMART_CURRENCY

    def find_price(self, product_name):
        walmart = WalmartApiClient(self.key)
        params = build_params(product_name)
        price_list = []
        search_response = walmart.search(params)
        if search_response:
            min_price = get_min_price(price_list, search_response)
            return min_price
        else:
            return "N/A"
