.PHONY: down-build-up

down-build-up:
	docker compose down && docker compose build && docker compose up
