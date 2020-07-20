import logging
import time

import shopify
from pyactiveresource import connection

from client.exceptions import MaxRetriesExceeded, InvalidShopifyResource

logger = logging.getLogger(__name__)


def api_call_with_retry(func, *args, **kwargs):
    """
    Execute the function, and pass in all the arguments / keyword arguments.

    Arguments:
        func: Function that will be executed.
        OR Any positional arguments that would be passed to the function

    Keyword Arguments:
        retries: Number of retries in case of exceptions during the execution(i.e. codes => 429, >500).
        OR Any keyword arguments that would be passed to the function 
    """
    retries = kwargs.pop('retries', 3)
    while retries > 0:
        try:
            return func(*args, **kwargs)
        except connection.ClientError as exc:
            if exc.response.code == 429:
                retry_after = float(exc.response.headers.get('Retry-After', 4))
                logger.info(('Shopify API Rate Limit Exceeded.'
                             'Retrying in %s seconds...'), retry_after)
                time.sleep(retry_after)
                retries -= 1
            else:
                raise
        except connection.ServerError as exc:
            # HTTP error code 5xx (500..599)
            # https://github.com/Shopify/pyactiveresource/blob/v2.2.1/pyactiveresource/connection.py#L23-L31
            retry_after = 4
            logger.info(('Shopify API Response Code %s.'
                         'Retrying in %s seconds...'), exc.code, retry_after)
            time.sleep(retry_after)
            retries -= 1

    raise MaxRetriesExceeded("Max retries exceeded.")


class ApiIterator(shopify.PaginatedIterator):
    """
    This class implements PaginatedIterator which aims to be more memory-efficient 
    by not keeping more than one page in memory at a time. Additionally, this supports 
    retry on failures and rate limits.
    """

    def __iter__(self):
        """Iterate over pages, returning one page at a time."""
        current_page = self.collection
        while True:
            yield current_page
            try:
                current_page = api_call_with_retry(
                    func=current_page.next_page,
                    no_cache=True
                )
            except IndexError:
                return


def api_iterator(resource):
    """
    Take a Resource and return a page iterator. Retry on failures 
    and rate limits are supported.
    """
    if not issubclass(resource, shopify.ShopifyResource):
        raise InvalidShopifyResource(f'{resource} is not a valid shopify resource.')

    return ApiIterator(collection=api_call_with_retry(resource.find))
