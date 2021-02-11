#!/bin/bash
echo "trying to start"
celery -A mq_task worker -l INFO