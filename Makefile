build:
	docker-compose up -d --build

stop:
	docker-compose stop

down:
	docker-compose down

demo:
	docker exec -ti shopify.client python cli.py run -th 50 -tgt tr

ssh:
	docker exec -ti shopify.client /bin/bash

test:
	docker-compose run shopify python -m unittest tests
