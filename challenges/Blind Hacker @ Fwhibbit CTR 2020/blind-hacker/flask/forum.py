#!/usr/bin/python3

from flask import *
import re
import jwt
from shellescape import quote
import psycopg2
import pymysql
import random
import string

source = """<html>

<h1> BLIND HACKER ACTUAL FORUM </h1>
<h1> Improved security, changed the engine to keep data and began to listen to rock & roll! </h1>

</html>

"""

def blacklist(string):
    chars = ["^", "$", ">", "<", "+", "LIKE", "like", "%"] # % quitado para que se tenga que calcular primero la length con _.
    for char in chars:
        if char in string:
            return True
    return False

def randomString(stringLength=58):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def check_forumtoken(token):
    conn = pymysql.connect(
        host="mysql_net",
        user="readuser",
        passwd="readuserpassword",
        database="tokenDB"
    )

    cursor = conn.cursor()

    cursor.execute(f"SELECT token FROM forumtokens WHERE token = '{quote(token)}';")
    res = cursor.fetchall()
    conn.commit()
    conn.close()

    if res:
        return True
    return False

def check_indextoken(token):
    conn = pymysql.connect(
        host="mysql_net",
        user="readuser",
        passwd="readuserpassword",
        database="tokenDB"
    )

    cursor = conn.cursor()

    cursor.execute(f"SELECT token FROM indextokens WHERE token = '{quote(token)}';")
    res = cursor.fetchall()
    conn.commit()
    conn.close()

    if res:
        return True
    return False


app = Flask(__name__)

@app.route("/")
def root():
    indextoken = request.args.get("indextoken")

    if not indextoken:
        return source + "Meet token.php and share your indextoken."
    
    if not check_indextoken(indextoken):
        return source + "Invalid indextoken."

    forumtoken = request.args.get("forumtoken")

    if not forumtoken:
        return source + "Meet /token and share your forumtoken."
    
    if not check_forumtoken(forumtoken):
        return source + "Invalid forumtoken."

    auth = request.headers.get('forum_auth')

    if not auth:
        resp = make_response(source + "You were not authed, but I have just sent you a guest permission.")
        resp.headers.extend({"forum_auth" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEzMzciLCJ1c2VybmFtZSI6Imd1ZXN0IiwicGFzc3dvcmQiOiJoNHgwciIsImVtYWlsIjoiZ3Vlc3RAd2hlcmUuZXZlciIsImlzX2FkbWluIjoibm8ifQ.dpWu5YCBeeOBknVGhkPPCz0d30PFABcGIB0aEQEWg5o"})
        return resp
    else:
        return source + "Go to /check to test your authorization."

@app.route("/token")
def tokenize():
    tokennow = randomString()
    conn = pymysql.connect(
        host="mysql_net",
        user="readuser",
        passwd="readuserpassword",
        database="tokenDB"
    )

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO `forumtokens`(`token`) VALUES ('{tokennow}');")
    conn.commit()
    conn.close()

    return f"{source}There you go -> {tokennow}"

@app.route("/check")
def check():    
    indextoken = request.args.get("indextoken")

    if not indextoken:
        return source + "Meet token.php and share your indextoken."
    
    if not check_indextoken(indextoken):
        return source + "Invalid indextoken."

    forumtoken = request.args.get("forumtoken")

    if not forumtoken:
        return source + "Meet /token and share your forumtoken."
    
    if not check_forumtoken(forumtoken):
        return source + "Invalid forumtoken."

    cookie = request.headers.get('forum_auth')
    if not cookie:
        return source + "What are you trying to do?"
    else:
        if re.match(r'^[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_+/=]*$', cookie):
            try:
                decoded = jwt.decode(cookie, "cookie", algorithms = 'HS256')
                username = quote(decoded['username'])
                password = quote(decoded['password'])
                email = quote(decoded['email'])
                is_admin = decoded['is_admin']
            except:
                return source + "1337"*99 + " Wrong authentication " + "1337"*99

            try:
                conn = psycopg2.connect(host="postgresql_net", database="blindhackerdb", user="readuser", password="readuserpassword")
            except Exception:
                return source + "Error connecting to the database, please contact an administrator."
                
            cur = conn.cursor()
            quer = f"SELECT username, password, email, is_admin FROM userinfo WHERE username = '{username}' AND password = '{password}' AND email = '{email}' AND is_admin = '{is_admin}'"
            if blacklist(quer):
                conn.close()
                return f"{source} Guau Guau"
            cur.execute(quer)
            res = cur.fetchall()
            conn.close()
            if res:
                return source + "It's a match!"
            else:
                return f"{source} There was an error, please have a look *carefully* and check everything: {quer}"

        else:
            return source + "1337"*99 + " Nice try " + "1337"*99



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
