#!/usr/bin/python3

from flask import Flask, request, redirect, jsonify
from os import environ

app = Flask(__name__)

@app.route("/")
def come_from_home():
    request.environ['wsgi.input_terminated'] = True
    ip = request.headers.get('X-Forwarded-For')
    if ip != "127.0.0.1":
        return redirect("https://www.youtube.com/watch?v=k-ImCpNqbJw&ab_channel=DirtyMoneyVEVO#" + str(ip) + "isNotHome")

    return redirect(environ.get('FLAG'))
