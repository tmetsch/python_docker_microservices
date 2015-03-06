# Docker-compose, Docker and Suricate

The tool [docker-compose](http://docs.docker.com/compose/) allows for easy 
deployment of a [dockerized](https://www.docker.com/) development environment 
for [suricate](https://github.com/engjoy/suricate).

Install docker & docker-compose and just run *docker-compose up -d* to get a
single user development environment going.

    $ sudo docker-compose -p engjoy up -d
    Recreating engjoy_mongo_1...
    Recreating engjoy_rabbit_1...
    Recreating engjoy_frontend_1...
    Recreating engjoy_execnode_1...
    $ sudo docker-compose -p engjoy ps   
          Name                     Command               State           Ports          
    -----------------------------------------------------------------------------------
    engjoy_execnode_1   python /tmp/execnode.py foo      Up                             
    engjoy_frontend_1   python /tmp/frontend.py          Up      0.0.0.0:8888->8888/tcp 
    engjoy_mongo_1      mongod                           Up      27017/tcp, 28017/tcp   
    engjoy_rabbit_1     /docker-entrypoint.sh rabb ...   Up      5672/tcp           

Go [here](http://localhost:8888/) to access the service. Data is persisted 
using the MongoDB data files in /tmp.

## Useful commands

* docker-compose build
* docker-compose ps
* docker rmi $(docker images -q -f dangling=true)

