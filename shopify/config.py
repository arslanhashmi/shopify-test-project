import os

SHOPIFY_API_KEY = os.environ['SHOPIFY_API_KEY']
SHOPIFY_API_SECRET = os.environ['SHOPIFY_API_SECRET']
SHOPIFY_SHOP = os.environ['SHOPIFY_SHOP']

SHOP_URL = f"https://{SHOPIFY_API_KEY}:{SHOPIFY_API_SECRET}@{SHOPIFY_SHOP}"