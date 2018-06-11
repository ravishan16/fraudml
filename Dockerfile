FROM python:2.7

FROM ubuntu:latest
MAINTAINER Ravishankar Sivasubramaniam "contact@ravishankars.com"
ENV HOME /fraudapp
ENV PATH $PATH:/fraudapp
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install gunicorn
COPY . /fraudapp
COPY runserver.sh /usr/local/bin/
WORKDIR /fraudapp
RUN pip install -r requirements.txt
RUN chmod 755 /fraudapp/runserver.sh
RUN chmod 755 /usr/local/bin/runserver.sh
CMD ["runserver.sh"]

