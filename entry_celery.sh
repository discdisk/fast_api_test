#!/bin/bash
echo "trying to start"
~/.poetry/bin/poetry run celery -A api_server.mq_task.mq_task worker -l INFO