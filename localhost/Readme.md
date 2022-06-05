docker-compose -f docker-compose-initial.yml up

http://localhost:8086/api/rawdata

http://localhost:8086/dashboard/

curl -H Host:whoami.docker.localhost http://127.0.0.1:8085

docker-compose -f docker-compose-initial.yml up --scale whoami=2
