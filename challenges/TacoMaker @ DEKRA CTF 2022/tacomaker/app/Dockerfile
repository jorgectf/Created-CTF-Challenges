FROM python:3.6

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY static/ static/

COPY web.py .
COPY templates/index.html templates/index.html

COPY browser.py .

ENTRYPOINT python3 browser.py & gunicorn --bind 0.0.0.0:4000 web:app --workers $GUNICORN_WORKERS -t $GUNICORN_TIMEOUT