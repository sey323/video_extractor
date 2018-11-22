NAME=venom

build:
	git submodule update --init --recursive
	docker build -t ${NAME}:1.0 .

run:
	docker run -d --rm -v `pwd`/results:/home/${NAME}/results -v `pwd`/resources:/home/${NAME}/resources -p 3000:3000 --name ${NAME} -it ${NAME}:1.0 python api.py

stop:
	docker rm -f ${NAME}

in:
	docker run --rm -v `pwd`/results:/home/${NAME}/results -v `pwd`/resources:/home/${NAME}/resources -p 1993:3000 --name ${NAME} -it ${NAME}:1.0 /bin/bash
