PWD:= $(shell pwd)

unittest:
	@echo "build test env"; docker build -t test -f Dockerfile.unittest . 
	@docker run -it -w /code -u $(shell id -u):$(shell id -g) -v $(PWD):/code  test pytest -x --pdb

build-common:
	tar -cvf common.tar -C common  .

build-web-service: build-common
	cp common.tar web-service/
	cd web-service; docker build .

build-celery-queue:
	cp common.tar celery-queue/
	docker build -f celery-queue/Dockerfile celery-queue

run: build-celery-queue build-web-service
	docker-compose run

build: build-web-service build-celery-queue