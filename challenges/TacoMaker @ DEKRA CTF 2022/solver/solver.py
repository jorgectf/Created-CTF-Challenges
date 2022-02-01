from flask import Flask, request
from sys import stderr
from os import environ
import logging
import re

# Disable ALL flask output
logging.getLogger('werkzeug').disabled = True
environ['WERKZEUG_RUN_MAIN'] = 'true'

app = Flask(__name__)
flag = "FLAG{"


@app.route('/solve.png', methods=['GET'])
def get_file():
    global flag
    return open('solver.html').read().replace("FLAGHERE", flag.replace("\\", "\\\\"))


@app.route('/exfil', methods=['POST'])
def exfil():
    print(request.data.decode())
    return ""


@app.route('/setFlag', methods=['POST'])
def setflag():
    global flag
    flag = request.data.decode()
    print("Flag: " + flag)
    return ""


if __name__ == "__main__":
    app.run(port=1337)
