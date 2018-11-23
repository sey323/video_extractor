NAME=venom

build:
	git submodule update --init --recursive
	docker build -t ${NAME}:1.0 .

run:
<<<<<<< HEAD
	python api.py &
	docker run -d --rm -v `pwd`/results:/home/${NAME}/results -v `pwd`/src:/home/${NAME}/src --name ${NAME} -it ${NAME}:1.0 python angelo/run.py
=======
	docker run -d --rm -v `pwd`/results:/home/${NAME}/results -v `pwd`/resources:/home/${NAME}/resources -p 3000:3000 --name ${NAME} -it ${NAME}:1.0 python api.py
>>>>>>> 20f15fff66f19a41d97cd1f8f0fb6620e55be055

stop:
	docker rm -f ${NAME}

in:
	docker run --rm -v `pwd`/results:/home/${NAME}/results -v `pwd`/resources:/home/${NAME}/resources -p 1993:3000 --name ${NAME} -it ${NAME}:1.0 /bin/bash
