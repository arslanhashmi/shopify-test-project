import logging

import shopify

from client.config import SHOP_URL

logger = logging.getLogger(__name__)

def api_call_with_retry():
    shopify.ShopifyResource.set_site(SHOP_URL)
    logger.info("Shop URL: [%s]", SHOP_URL)

    api_product = shopify.Product.find()[0]
    api_product = shopify.Product.find()[1]
    logger.info(api_product.title)
