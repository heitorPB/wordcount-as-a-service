FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10

RUN pip install python-multipart==0.0.5

COPY ./app/ /app
