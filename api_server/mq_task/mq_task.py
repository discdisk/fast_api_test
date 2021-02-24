from celery import Celery
from .rec_digit.ocr_model import ocr
import os
mq_host = os.environ.get('MQ_HOST')
log_db_host = os.environ.get('LOG_DB_HOST')
if mq_host and log_db_host:
    app = Celery('tasks', broker=mq_host, backend=log_db_host)

    @app.task
    def rec_digit(jpgtxt: str) -> int:
        return int(ocr(jpgtxt))
