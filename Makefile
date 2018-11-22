NAME=venom

build:
	git submodule update --init --recursive
	docker build -t ${NAME}:1.0 .

run:
	docker run -d --rm -v `pwd`/results:/home/${NAME}/results -v `pwd`/src:/home/${NAME}/src -p 3000:3000 --name ${NAME}_API -it ${NAME}:1.0 python api.py
	docker run -d --rm --name ${NAME} -it ${NAME}:1.0 python angelo/run.py

stop:
	docker rm -f ${NAME} ${NAME}_API

in:
	docker run --rm -v `pwd`/results:/home/${NAME}/results -v `pwd`/src:/home/${NAME}/src -p 1993:3000 --name ${NAME} -it ${NAME}:1.0 /bin/bash

in_win:
	docker run --rm -v ./results/:/home/${NAME}/results -v ./src/:/home/${NAME}/src -p 1993:3000 --name ${NAME} -it ${NAME}:1.0 /bin/bash
