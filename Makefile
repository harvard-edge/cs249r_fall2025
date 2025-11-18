.PHONY: serve build clean install

# Serve the site locally with live reload
serve:
	docker compose up

# Build the static site
build:
	docker compose run --rm jekyll jekyll build

# Clean generated files
clean:
	docker compose run --rm jekyll jekyll clean

# Install dependencies
install:
	docker compose run --rm jekyll bundle install

# Stop the server
stop:
	docker compose down

# Open the site in browser
open:
	open http://localhost:4000

