# FROM arm64v8/python:3.8-buster
FROM python
# RUN apt update && apt ins curl gcc libffi-dev linux-headers musl-dev
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH "~/.poetry/bin:$PATH"
WORKDIR /api
COPY . /api
RUN ~/.poetry/bin/poetry install
ENV MQ_HOST='amqp://guest@192.168.3.9:30003//' LOG_DB_HOST='mongodb://cjh:cjh123@132.145.121.207:27017/mq_tasks?authSource=admin'

EXPOSE 8000