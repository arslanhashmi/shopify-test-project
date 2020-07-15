import logging
from threading import Thread

import shopify

from client.wrappers import api_call_with_retry

logger = logging.getLogger(__name__)

def get_products_page():
    # shopify.ShopifyResource.set_site(SHOP_URL)
    # logger.info("Shop URL: [%s]", SHOP_URL)

    # products_page = shopify.Product.find()
    # print(len(products_page))
    # logger.info("\n".join([
    #     product.title 
    #     for product in products_page
    # ]))
    # shopify.Variant.find()
    pass

def main():
    for _ in range(100):
        t = Thread(target=lambda: api_call_with_retry(
            shopify.Variant.find, 
            retries=5
        ))
        t.start()

if __name__ == "__main__":
   main()
