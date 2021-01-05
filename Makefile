API_SERVER_NAME=video-yolo

run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop ${API_SERVER_NAME} 
	docker rm -f ${API_SERVER_NAME}

in:
	docker exec --name ${API_SERVER_NAME} -it ${API_SERVER_NAME}:1.0 /bin/bash
