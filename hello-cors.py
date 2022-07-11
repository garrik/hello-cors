from flask import Flask
from flask_cors import CORS, cross_origin
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}

@app.route("/")
def hello_world():
    """
    This endpoint responds to same-origin requests only
    """
    return "Hello, World!"

@app.route("/cors")
@cross_origin()
def hello_world_cors():
    """
    This endpoint responds to cross-origin requests
    """
    return "Hello, Cross Origin World!"

@app.route("/auth")
@auth.login_required
def hello_world_auth():
    """
    This endpoint responds to same-origin requests only when authorized
    """
    return "Hello, {}!".format(auth.current_user())

@app.route('/cors-auth')
@cross_origin()
@auth.login_required
def hello_world_cors_auth():
    """
    This endpoint responds to cross-origin requests only when authorized
    """
    return "Hello, Cross Origin {}!".format(auth.current_user())

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.after_request
def add_security_headers(resp):
    """
    Allow use of developer console from "hello world" page to send requests
    https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
    https://stackoverflow.com/questions/63290047/flask-csp-content-security-policy-best-practice-against-attack-such-as-cross
    """
    resp.headers['Content-Security-Policy']='default-src \'self\' http://*; connect-src *;'
    return resp
