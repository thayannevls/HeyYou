# VERSION 0.1

FROM bamos/openface:latest
MAINTAINER Thayanne <thayannevls@gmail.com>

RUN apt-get update && apt-get install -y

# Python manager packages
RUN DEBIAN_FRONTEND=noninteractive apt-get install --force-yes -yq --no-install-recommends \
    python \
    python-dev \
    python-pip=1.5.4-1

# Python third party modules 
RUN pip install -U pip
RUN pip install numpy
RUN pip install scipy

# Flask
RUN pip install Flask 
RUN pip install Flask-SocketIO #websocket

# Mongodb
RUN pip install pymongo
RUN pip install Flask-PyMongo

EXPOSE 8000 9000 5000