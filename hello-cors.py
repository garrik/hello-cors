from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/cors")
#@cross_origin() # perchee errore se lo scommento???
def hello_world_cors():
    return "Hello, Cross Origin World!"

# https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
# https://stackoverflow.com/questions/63290047/flask-csp-content-security-policy-best-practice-against-attack-such-as-cross
@app.after_request
def add_security_headers(resp):
    resp.headers['Content-Security-Policy']='default-src \'self\' http://*; connect-src *;'
    return resp