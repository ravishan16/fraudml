FROM python:2.7-alpine
MAINTAINER Ravishankar Sivasubramaniam "contact@ravishankars.com"

RUN addgroup -S flaskuser && adduser -S -g flaskuser flaskuser

#ADD . /flaskapp
ENV HOME /fraudapp
ENV PATH $PATH:/fraudapp


WORKDIR /fraudapp
COPY requirements.txt /fraudapp/
COPY runserver.sh /fraudapp/
COPY config.py /fraudapp/
COPY main.py /fraudapp/

RUN pip install gunicorn
RUN pip install -r requirements.txt

COPY fraudapp /fraudapp/fraudapp
COPY runserver.sh /usr/local/bin/

RUN chmod 755 /fraudapp/runserver.sh
RUN chmod 755 /usr/local/bin/runserver.sh

RUN echo "Listing"
RUN ls -ltr /fraudapp
RUN ls -ltr /fraudapp/fraudapp


RUN pwd
#RUN python manage.py db init
#RUN python manage.py db migrate
#RUN python manage.py db upgrade
EXPOSE 4000

CMD ["runserver.sh"]
#ENTRYPOINT ["python"]
#CMD ["manage.py","runserver"]
