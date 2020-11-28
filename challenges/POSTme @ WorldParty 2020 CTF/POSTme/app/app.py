from flask import Flask, request, redirect
from shellescape import quote
from random import choice
from subprocess import getoutput
from os import environ
from string import ascii_letters, digits

app = Flask(__name__)
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def get_random_endpoint():
    return ''.join(choice(digits+ascii_letters) for i in range(40))

def check_ip_bool(ip):
    return ip == "127.0.0.1"

# Random endpoints
random_endpoints = [get_random_endpoint() for i in range(20)]

# Endpoints
@app.route("/")
def index():
        return redirect('/POSTthis')

@app.route('/<string:page>', methods=["POST"])
def dynamic(page):
    try:
        if page == "POSTthis":
            if request.form.get('url'):
                for key in ["dict:", "ftp:", "ftps:", "imap:", "scp:", "ldap:", "data:", "php:", "ssh:", "file:"]:
                    if key in request.form.get('url'):
                        return "Nice try ^^"
                return getoutput(f"curl {quote(request.form.get('url'))} --output - -s")

        if page == "begin":
            if check_ip_bool(request.remote_addr):
                return redirect(video_url + '#' + random_endpoints[0])

        if page in random_endpoints[:len(random_endpoints)-1]:
            if check_ip_bool(request.remote_addr):
                return redirect(video_url + '#' + random_endpoints[random_endpoints.index(page)+1])

        if page == random_endpoints[len(random_endpoints)-1]:
            if check_ip_bool(request.remote_addr):
                return redirect(video_url + '#' + environ.get('FLAG'))

        return redirect(video_url)
    except:
        return redirect(video_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)