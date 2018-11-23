NAME=venom

build:
	git submodule update --init --recursive
	docker build -t ${NAME}:1.0 .

run:
	python api.py &
	docker run -d --rm -v `pwd`/results:/home/${NAME}/results -v `pwd`/src:/home/${NAME}/src --name ${NAME} -it ${NAME}:1.0 python angelo/run.py

stop:
	docker rm -f ${NAME}

in:
	docker run --rm -v `pwd`/results:/home/${NAME}/results -v `pwd`/src:/home/${NAME}/src -p 1993:3000 --name ${NAME} -it ${NAME}:1.0 /bin/bash

in_win:
	docker run --rm -v ./results/:/home/${NAME}/results -v ./src/:/home/${NAME}/src -p 1993:3000 --name ${NAME} -it ${NAME}:1.0 /bin/bash
