FROM python:3.6

RUN apt-get update -y

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get --allow-unauthenticated -y update
RUN apt-get --allow-unauthenticated install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

WORKDIR /app

RUN apt-get install redis-server -y

COPY app/requirements.txt .
RUN pip3 install -r requirements.txt

COPY app/browser.py .
RUN chmod +x browser.py

COPY app/web.py .
COPY app/templates/ templates
COPY app/cert.pem .
COPY app/key.pem .

ENTRYPOINT echo "bind $DB_HOST" | redis-server - --port $DB_PORT & gunicorn --bind 0.0.0.0:4000 web:app --workers 10 --certfile=cert.pem --keyfile=key.pem & python3 -u browser.py

RUN apt-get clean \
  && rm -rf \
    /tmp/* \
    /usr/share/doc/* \
    /var/cache/* \
    /var/lib/apt/lists/* \
    /var/tmp/*
