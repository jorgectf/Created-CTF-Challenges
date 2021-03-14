FROM python:3.8-slim

RUN apt update -y && apt install gcc libssl-dev -y

WORKDIR /app

COPY app/ .
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT uwsgi --ini app.ini
