.PHONY: down-build-up, prod-down-up

down-build-up:
	docker compose down && docker compose build && docker compose up

prod-down-up:
	docker compose -f docker-compose.prod.yml down && docker compose -f docker-compose.prod.yml up
