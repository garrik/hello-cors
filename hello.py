from flask import Flask

import flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hello", methods = ['POST'])
def hello():
    data = flask.request.form

    name = data['name'] if 'name' in data else "anonymous"

    return f"Hello, {name}!"

# https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
# https://web.dev/csp/
# https://stackoverflow.com/questions/63290047/flask-csp-content-security-policy-best-practice-against-attack-such-as-cross
@app.after_request
def add_security_headers(resp):
    resp.headers['Content-Security-Policy']='default-src \'self\' http://*; connect-src *;'
    return resp