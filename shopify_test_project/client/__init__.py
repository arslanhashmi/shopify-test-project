import logging

import shopify

from .config import SHOP_URL

logging.basicConfig(level=logging.INFO)
shopify.ShopifyResource.set_site(SHOP_URL)
