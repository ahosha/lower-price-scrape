from src.models.stores.base_store import BaseStore
from src.common.setting import *


class ProductModel:
    name = ''
    store = ''
    stores = []

    def __init__(self, name, stores):
        self.name = name
        self.stores = stores if stores is not None else []

    def search(self):
        stores_result = dict()
        for store in self.stores:
            if isinstance(store, BaseStore):
                price = store.find_price(self.name)
                if isinstance(price, float):
                    stores_result[store.name] = price

        min_price, store_to_return = self.calculate_min_price(stores_result)

        return_data = {k: v for k, v in ((PRODUCT_NAME_OUTPUT_NAME, self.name),
                                         (PRICE_NAME_OUTPUT_NAME, min_price[1]),
                                         (STORE_NAME_OUTPUT_NAME, min_price[0]),
                                         (CURRENCY_OUTPUT_NAME, store_to_return[0].currency))}
        return return_data

    def calculate_min_price(self, stores_result):
        min_price = min(stores_result.items(), key=lambda x: x[1])
        store_name = min_price[0]
        store_to_return = [x for x in self.stores if x.name == store_name]
        return min_price, store_to_return
