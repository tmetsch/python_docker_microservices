FROM ubuntu
MAINTAINER engjoy UG (haftungsbeschraenkt)

# dependecies
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip python-matplotlib

# deploy suricate
ADD /misc /tmp/
ADD /suricate /tmp

RUN pip install -r /tmp/requirements.txt

# install
RUN cd tmp && python setup.py install && cd ..
