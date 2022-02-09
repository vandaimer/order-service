FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN apk update

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/
