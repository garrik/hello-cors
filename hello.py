from flask import Flask

import flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hello", methods = ['POST'])
def hello():

    content_type = flask.request.headers.get('Content-Type')
    print(f"Content-Type {content_type}")
    content_type = content_type.lower() if content_type is not None else ''

    if content_type.startswith('application/x-www-form-urlencoded'):
        
        data = flask.request.form
        name = data['name'] if 'name' in data else "anonymous"

    elif content_type.startswith('multipart/form-data'):
        
        data = flask.request.form
        name = data['name'] if 'name' in data else "anonymous"

    elif content_type.startswith('application/json'):
        import json

        data = flask.request.get_json() # TODO: check valid json
        name = data['name'] if 'name' in data else "anonymous"

    elif content_type.startswith('text/plain'):
        name = flask.request.data

    else:
        return "content type not accepted", 400

    return f"Hello, {name}!"


# https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
# https://web.dev/csp/
# https://stackoverflow.com/questions/63290047/flask-csp-content-security-policy-best-practice-against-attack-such-as-cross
@app.after_request
def add_security_headers(resp):
    resp.headers['Content-Security-Policy']='default-src \'self\' http://*; connect-src *;'
    return resp