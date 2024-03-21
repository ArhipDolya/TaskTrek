DOCKER_COMPOSE_FILE := docker-compose/app.yml
DOCKER_COMPOSE_DB_FILE := docker-compose/db.yml

DOCKER_COMPOSE_CMD := docker-compose -f $(DOCKER_COMPOSE_FILE) -f $(DOCKER_COMPOSE_DB_FILE)

up:
	$(DOCKER_COMPOSE_CMD) up

up-build:
	$(DOCKER_COMPOSE_CMD) up --build

down:
	$(DOCKER_COMPOSE_CMD) down