IMAGE_NAME = shopify-products

build:
	docker build -t $(IMAGE_NAME) .

mark-latest:
	docker tag $(IMAGE_NAME):latest rishabhuk/$(IMAGE_NAME):latest

push: mark-latest
	docker push rishabhuk/$(IMAGE_NAME):latest

run:
	@echo "Running $(IMAGE_NAME) using environment variables from .env"
	docker run --rm --env-file .env rishabhuk/$(IMAGE_NAME):latest

rebuild: clean build run

clean:
	docker rmi -f $(IMAGE_NAME) || true
