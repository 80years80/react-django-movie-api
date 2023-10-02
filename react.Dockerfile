FROM ubuntu:20.04 as base

RUN mkdir /frontend
COPY /front_end_react_movie_app /frontend/

WORKDIR /frontend

RUN apt-get update
RUN apt-get install npm nodejs
RUN npm install
EXPOSE 3000
RUN npm start