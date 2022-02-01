#!/usr/bin/python3

from flask import Flask, render_template, request
from random import randint
from os import environ
from redis import Redis
from urllib.parse import urlparse
from re import match
from socket import gethostbyname

cli = None
while not cli:
    cli = Redis(environ.get("REDIS_HOST"))

app = Flask(__name__, template_folder='templates/')

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", taco_name=request.args.get('taco_name'))


@app.route("/getTaco", methods=["GET"])
def getTaco():

    try:
        ingredient = request.args.getlist('ingredient')[-1]  # bye bye bruteforce
        if str(request.remote_addr) == gethostbyname('selenium') and \
            urlparse(request.referrer).netloc == "tacomaker:4000" and \
                match(ingredient, environ.get("FLAG")):
            
            return "static/taco3.jpg"
    except Exception:
        pass
    
    return "static/" + ["taco1.jpg", "taco2.jpg"][randint(0, 1)] 


@app.route("/suggest", methods=["GET", "POST"])
def suggest():
    url = request.args.get('url') or request.form.get('url')
    if not request.remote_addr == gethostbyname('selenium') and url and url.endswith(".png") and urlparse(url).path.endswith(".png"):
        cli.set(str(request.remote_addr), url)
    return "Successfully suggested to taco reviewers."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
