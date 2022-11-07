FROM ubuntu:20.04 as base

RUN mkdir /backend
COPY backend_django_rest_api /backend/

WORKDIR /backend

RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip install -r requirements.txt

CMD python3 manage.py runserver