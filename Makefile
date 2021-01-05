API_SERVER_NAME=video-yolo
SLACK_CLIENT_NAME=slack-client

build:
	git submodule update --init --recursive

run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop ${API_SERVER_NAME} ${SLACK_CLIENT_NAME}
	docker rm -f ${API_SERVER_NAME} ${SLACK_CLIENT_NAME}

in:
	docker exec --name ${API_SERVER_NAME} -it ${API_SERVER_NAME}:1.0 /bin/bash
