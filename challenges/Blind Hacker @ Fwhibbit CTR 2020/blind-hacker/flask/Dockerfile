FROM python:3.6

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY forum.py /app
CMD python3 forum.py
