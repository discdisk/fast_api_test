FROM tiangolo/uvicorn-gunicorn:python3.8-slim
RUN pip install --no-cache-dir fastapi
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
WORKDIR /api
COPY . /api
