run:
	docker run --rm --network=host -it ipmi-discover:latest bash

build:
	docker build --no-cache -t ipmi-discover ./build

.PHONY: run build