FROM python:3.8-slim

WORKDIR /browser

COPY browser.py .
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT python3 -u browser.py
