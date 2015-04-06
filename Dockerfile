FROM ubuntu
MAINTAINER engjoy UG (haftungsbeschraenkt)

# dependecies
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip python-matplotlib python-pandas

# deploy suricate
ADD /misc /tmp/
ADD /suricate /tmp

RUN pip install -r /tmp/requirements.txt

# install
WORKDIR /tmp
RUN python setup.py install
