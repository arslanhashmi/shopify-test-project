build:
	docker-compose up -d --build

run:
	docker-compose run shopify python -m shopify.py

ssh:
	docker-compose run shopify /bin/bash

test:
	docker-compose run shopify python -m unittests tests