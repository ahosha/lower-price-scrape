# lower-price-scrape
lower-price-scrape

This repository includes code for a RESTful web service that takes a product name query parameter and return the lowest current available price. The price for comparison is taken by querying and comparing results from Best Buy and Walmart using the supplied API keys. If there are multiple products, the lowest priced product should be returned.

Stores API can be tested on following ->  Best Buy: http://bestbuyapis.github.io/bby-query-builder/#/productSearch . For Walmart:  https://developer.walmartlabs.com/io-docs

Following Python client library were used -> 
    for Walmart API: walmart-api-client 1.0  https://github.com/kronas/python-walmart-api-client.   
    for Best Buy API: BestBuyAPI 0.0.51  https://pypi.org/project/BestBuyAPI/
  
  
BestBuy: 'pfe9fpy68yg28hvvma49sc89'
Walmart: 'rm25tyum3p9jm9x9x7zxshfa'

Lower-price-scraper API description in  Swagger file : Blue_Spurs_Developer_Test_Swagger.yaml (in this repository)

Request

GET /product/search?name=ipad



Response
{
    "productName": "iPad Mini",
    "bestPrice": "150.00",
    "currency": "USD",
    "location": "Walmart"
}
