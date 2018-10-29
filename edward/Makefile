NAME=edward

run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop ${NAME}
	docker rm -f ${NAME}

log:
	docker-compose logs

in:
	docker exec -it ${NAME} /bin/sh
