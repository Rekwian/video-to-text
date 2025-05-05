build:
	docker compose build

start:
	bun install
	bun run build
	docker compose up -d --force-recreate --remove-orphans