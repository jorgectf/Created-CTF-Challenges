FROM python:3.6

WORKDIR /app

COPY app/requirements.txt .
RUN pip3 install -r requirements.txt

COPY app/app.py .
ENTRYPOINT python3 app.py