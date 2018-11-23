NAME=venom

build:
	git submodule update --init --recursive

run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop ${NAME}_venom_1 ${NAME}_angelo_1
	docker rm -f ${NAME}_venom_1 ${NAME}_angelo_1

in:
	docker run --rm -v `pwd`/results:/home/${NAME}/results -v `pwd`/resources:/home/${NAME}/resources -p 1993:3000 --name ${NAME} -it ${NAME}:1.0 /bin/bash
