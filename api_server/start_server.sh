source $HOME/.poetry/env
poetry run celery -A mq_task.mq_task worker -l INFO
poetry run uvicorn main:app --reload --host 0.0.0.0