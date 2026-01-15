.PHONY: up down restart stop attach

up:
	docker-compose up -d

down:
	docker-compose down

restart:
	docker restart library-web-1 library-db-1

stop:
	docker stop library-web-1 library-db-1

logs:
	docker attach library-web-1