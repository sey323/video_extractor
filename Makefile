NAME=venom

build:
	git submodule update --init --recursive

run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop ${NAME} angelo
	docker rm -f ${NAME} angelo

in:
	docker exec --name ${NAME} -it ${NAME}:1.0 /bin/bash
