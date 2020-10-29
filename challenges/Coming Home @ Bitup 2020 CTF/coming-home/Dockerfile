FROM haproxy:1.9.0
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

RUN apt update -y
RUN apt install python python-pip -y

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get install python-gevent -y

COPY app.py .
CMD haproxy -f /usr/local/etc/haproxy/haproxy.cfg & gunicorn --keep-alive 10 -k gevent --bind 127.0.0.1:4000 app:app --workers ${THREADS}
