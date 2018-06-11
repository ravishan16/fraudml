# fraudml
Fraud Detection ML Scikit Learn Flask App 
    {% comment %} <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css"> {% endcomment %}


```shell
gunicorn -b 0.0.0.0 -w 4 main:app
```


Fraus Detection Machine Learning App
======================

Flask App, SQLAchemy, SQLite, Gunicorn, Docker, Microservice, Python

[![Build Status](https://travis-ci.org/ravishan16/fraudml.svg?branch=master)](https://travis-ci.org/ravishan16/fraudml)
[![Docker Hub](https://hub.docker.com/public/images/logos/mini-logo.svg)](https://hub.docker.com/r/ravishan/fraudml/)

Setup DB
========

``` python
cd fraudml
python fraudapp/model.py
```

Run Flask Server Local
======================

``` python
cd fraudml
python main.py
```

## Build Docker

``` shell
docker build -t fraudml-docker:0.0.1 .
```

## Run Docker image

``` shell
docker run -d -p 8080:8080 --name fraudapp fraudml-docker:0.0.1
```

## Docker Pull and Run

``` shell
docker run -d -p 8080:8080 --name fraudapp ravishan/fraudml
```

##  Check Docker Status

``` shell
docker ps -all
```

## Check Logs

``` shell
docker logs -tf fraudapp


2017-08-31T18:49:51.237387132Z Running Production Application
2017-08-31T18:49:51.493803743Z [2017-08-31 18:49:51 +0000] [1] [INFO] Starting gunicorn 19.7.1
2017-08-31T18:49:51.496746605Z [2017-08-31 18:49:51 +0000] [1] [INFO] Listening at: http://0.0.0.0:4000 (1)
2017-08-31T18:49:51.496764705Z [2017-08-31 18:49:51 +0000] [1] [INFO] Using worker: sync
2017-08-31T18:49:51.496767590Z [2017-08-31 18:49:51 +0000] [9] [INFO] Booting worker with pid: 9
2017-08-31T18:49:51.602635517Z [2017-08-31 18:49:51 +0000] [14] [INFO] Booting worker with pid: 14
2017-08-31T18:49:51.678074435Z [2017-08-31 18:49:51 +0000] [15] [INFO] Booting worker with pid: 15
2017-08-31T18:49:51.748691820Z [2017-08-31 18:49:51 +0000] [20] [INFO] Booting worker with pid: 20
```
