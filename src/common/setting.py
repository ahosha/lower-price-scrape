#Setting
APPLICATION_PORT = 5000
DEBUG = True
API_PRODUCT_SEARCH_PATH = '/product/search'

BESTBUY_STORE_NAME = 'Best Buy'
BESTBUY_KEY = 'pfe9fpy68yg28hvvma49sc89'
BESTBUY_CURRENCY = 'USD'
BESTBUY_PRODUCTS_TAG_NAME = 'products'
BESTBUY_PRICE_TAG_NAME = 'regularPrice'

WALMART_STORE_NAME = 'Walmart'
WALMART_KEY = 'rm25tyum3p9jm9x9x7zxshfa'
WALMART_CURRENCY = 'USD'
WALMART_PRODUCTS_TAG_NAME = 'items'
WALMART_PRICE_TAG_NAME = 'salePrice'

STORES_TO_SCAN = ['Walmart', 'BestBuy']

PRODUCT_NAME_OUTPUT_NAME = 'productName'
PRICE_NAME_OUTPUT_NAME = 'bestPrice'
STORE_NAME_OUTPUT_NAME = 'location'
CURRENCY_OUTPUT_NAME = 'currency'