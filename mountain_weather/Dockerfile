# Getting image choosen by user and inherit from it. Images is on hub.docker.com

FROM python:3.7-alpine 

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt


RUN apk update
# Installing depencies for postgresql
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r /requirements.txt

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN adduser -D user

USER user
