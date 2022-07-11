from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/cors")
@cross_origin()
def hello_world_cors():
    return "Hello, Cross Origin World!"

@app.after_request
def add_security_headers(resp):
    """
    Allow use of developer console from "hello world" page to send requests
    https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
    https://stackoverflow.com/questions/63290047/flask-csp-content-security-policy-best-practice-against-attack-such-as-cross
    """
    resp.headers['Content-Security-Policy']='default-src \'self\' http://*; connect-src *;'
    return resp
