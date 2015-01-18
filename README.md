# Fig, Docker and Suricate

The tool [fig](http://www.fig.sh/index.html) allows for easy deployment of a 
[dockerized](https://www.docker.com/) development environment for 
[suricate](https://github.com/engjoy/suricate).

Install docker & fig and just run *fig up -d* to get a single user development
environment going.

    $ sudo fig up -d
    Creating suricatedockerfig_mongo_1...
    Creating suricatedockerfig_rabbit_1...
    Creating suricatedockerfig_frontend_1...
    Creating suricatedockerfig_execnode_1...
    $ sudo fig ps
                Name                          Command               State           Ports          
    ----------------------------------------------------------------------------------------------
    suricatedockerfig_execnode_1   python /tmp/execnode.py foo      Up                             
    suricatedockerfig_frontend_1   python /tmp/frontend.py          Up      0.0.0.0:8888->8888/tcp 
    suricatedockerfig_mongo_1      mongod                           Up      27017/tcp, 28017/tcp   
    suricatedockerfig_rabbit_1     /docker-entrypoint.sh rabb ...   Up      5672/tcp               

Go [here](http://localhost:8888/) to access the service. Data is persisted 
using the MongoDB data files in /tmp.

## Useful commands

* fig build
* fig ps
* docker rmi $(docker images -q -f dangling=true)

