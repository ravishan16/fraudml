FROM ubuntu:latest
MAINTAINER Ravishankar Sivasubramaniam "contact@ravishankars.com"
ENV HOME /fraudapp
ENV PATH $PATH:/fraudapp
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y gunicorn
COPY . /fraudapp
WORKDIR /fraudapp
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["gunicorn","-w","4", "-b", "0.0.0.0:8080","-t","180", "main:app"]