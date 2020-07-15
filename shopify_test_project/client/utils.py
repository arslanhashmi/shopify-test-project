import logging

import shopify

from client.wrappers import api_call_with_retry, api_iterator

logger = logging.getLogger(__name__)


def get_product_variant():
    return api_call_with_retry(shopify.Variant.find, retries=5)


def get_products():
    """
    Get shopify products keep one page in memory at time using iterator 
    that also accounts for handling retries on failures and 
    on rate limits.
    """
    for products_page in api_iterator(shopify.Product):
        logger.info("[API ITERATOR] Got %d Products.", len(products_page))
