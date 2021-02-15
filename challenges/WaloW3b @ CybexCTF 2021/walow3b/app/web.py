#!/usr/bin/python3

from flask import Flask, render_template, request, make_response
from random import randint, choice
from re import search
from time import sleep
from os import environ
from redis import Redis

app = Flask(__name__, template_folder='templates/')
context = ('cert.pem', 'key.pem')

cli = None
while not cli:
    cli = Redis(environ.get("DB_HOST"), int(environ.get("DB_PORT")))

@app.route("/")
def index():
    resp = make_response(render_template("index.html"))
    resp.set_cookie('flag', 'whyisitnothere?', httponly=True, samesite='None', secure=True)
    return resp

@app.route("/walomsg", methods=["GET"])
def walomsg():
    flag_p = request.args.get("flag")
    flag_c = request.cookies.get('flag')
    msg = request.args.get("msg")

    print(flag_p, flag_c, msg)

    if not flag_c or not flag_p or not msg:
        return "Something went wrong..."
    return render_template("check_msg.html", msg=search('[A-Za-z" ]+', msg).group(), check=flag_p in flag_c) # Make sure flag is valid

@app.route("/walocheck", methods=['GET'])
def walocheck_get():
    return render_template("check_url.html")

@app.route("/walocheck", methods=['POST'])
def walocheck_post():
    url = request.form.get('url')
    if url:
        cli.set(str(request.remote_addr), url)
    if randint(1,10) == 1:
        return render_template("check_okay.html")
    return render_template("check_wrong.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, ssl_context=context)
