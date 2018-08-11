from src.models.stores.base_store import BaseStore
from bestbuy import BestBuyProductsAPI
import httplib
import json
import re
from src.common.setting import *


class BestbuyStore(BaseStore):
    """
    to test use : http://bestbuyapis.github.io/bby-query-builder/#/productSearch
    """
    name = BESTBUY_STORE_NAME
    key = BESTBUY_KEY
    currency = BESTBUY_CURRENCY

    def find_price(self, product_name):

        bb_prod = BestBuyProductsAPI(self.key)
        price_list = []
        search_string = self.compose_search_string(product_name)
        search_response = bb_prod.search(search_string, format="json")
        if search_response:
            json_responce = json.loads(search_response)
            products = json_responce[BESTBUY_PRODUCTS_TAG_NAME]
            for item in products:
                price_list.append(item[BESTBUY_PRICE_TAG_NAME])
            min_price = min(price_list)
            return min_price
        else:
            return "N/A"

    def compose_search_string(self, product_name):
        words = re.split('\s+', product_name)
        search_string = '('
        for word in words:
            search_string += 'search ='
            search_string += word
            search_string += '&'
        search_string = search_string[:-1]
        search_string += ')'
        return search_string
