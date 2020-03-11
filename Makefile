build:
	docker-compose build

up:
	docker-compose up --remove-orphans --build

up-debug:
	docker-compose --verbose up --remove-orphans --build
