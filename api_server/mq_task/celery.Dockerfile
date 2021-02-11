FROM arm64v8/ubuntu
RUN apt-get update
RUN apt-get -y install python3 python3-pip
WORKDIR /celery_task
COPY . .
RUN pip3 install -r requirements.txt

ENV MQ_HOST='amqp://guest@192.168.3.9:30003//' LOG_DB_HOST='mongodb://cjh:cjh123@132.145.121.207:27017/mq_tasks?authSource=admin'
EXPOSE 5555
ENTRYPOINT ["sh", "entrypoint.sh"]
# ENTRYPOINT ["bash"]