
class BaseClientException(Exception):
    pass


class MaxRetriesExceeded(BaseClientException):
    pass


class InvalidShopifyResource(BaseClientException):
    pass
