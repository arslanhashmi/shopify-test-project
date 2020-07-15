build:
	docker-compose up -d --build

stop:
	docker-compose stop

run:
	docker exec -ti shopify.client python run.py

ssh:
	docker exec -ti shopify.client /bin/bash

test:
	docker-compose run shopify python -m unittests tests
