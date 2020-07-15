import logging
import time

import shopify
from pyactiveresource import connection

from client.config import SHOP_URL

logger = logging.getLogger(__name__)

def api_call_with_retry(func, *args, **kwargs):
    retries = kwargs.pop('retries', 3)
    while retries >= 0:
        try:
            return func(*args, **kwargs)
        except connection.ClientError as exc:
            if exc.response.code == 429:
                retry_after = float(exc.response.headers.get('Retry-After', 4))
                logger.info(('Shopify API Rate Limit Exceeded.'
                             'Retrying in %s seconds...'), retry_after)
                time.sleep(retry_after)
            elif exc.response.code >= 500:
                retries -= 1
            else:
                raise exc

