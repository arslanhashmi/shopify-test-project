## Getting started

### Background
This implements wrappers that take in a callback and its any number of parameters and respect the rate limits and retry on failures while the execution of those callbacks.

### Get up and running
```sh
$ git clone git@github.com:arslanhashmi/shopify-test-project.git

$ cd shopify-test-project

# Add .env file
$ touch .env # with following content
 #shopify-test-project/.env
 SHOPIFY_API_KEY=insecure-api-key
 SHOPIFY_API_SECRET=insecure-api-pass
 SHOPIFY_SHOP=awesome-shope-id.myshopify.com/admin/api/2020-07
```
Next, from `shopify-test-project/` dir, setup the environment as follow:
```sh
# First time, One liner to:
# 1. setup the environment 
# 2. run the demo with retries on failure / rate limits
$ make build && make demo

# Next time
$ make demo
```

#### Interested in playing with CLI?
```sh
# ssh into the container
$ make ssh
# check cli --help
$ python cli.py run --help

Usage: cli.py run [OPTIONS]

Options:
  -th, --num_threads INTEGER  Number of threads each executing a target.
                              Valid: >0  [required]

  -tgt, --target TEXT         Target for each thread, valid ones are: ti(i.e.
                              test iterator) / tr(i.e. test retry)  [required]

  --help                      Show this message and exit.


# For example: test api_call_iterator with 30 parallel threads
$ python cli.py run -th 30 -tgt ti

# Cleanup: exit from ssh session and run:
make down  # remove containers / volumes / networks
# Or for later use, just stop them.
make stop
```
###### Demo
![Demo Interaction](./assets/cli.gif)

### Running Tests
```sh
# run unit tests
$ make test
```

### Wrapper's Usage
#### `api_call_with_retry`
```python
from client.wrappers import api_call_with_retry
api_call_with_retry(shopify.Variant.find, retries=5)
```

#### `api_iterator`
```python
import logging

import shopify

from client.wrappers import api_iterator

logger = logging.getLogger(__name__)

for products_page in api_iterator(shopify.Product):
        logger.info("[API ITERATOR] Got %d Products.", len(products_page))

```

---
Yay! That's it. Thanks for following!
