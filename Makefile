NAME=venom

run:
	docker build -t ${NAME}:1.0 .

stop:
	docker rm -f ${NAME}

in:
	docker run -v results:/home/${NAME}/results -v src:/home/${NAME}/src --name ${NAME} -it ${NAME}:1.0  /bin/bash
