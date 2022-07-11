# test cors

# dependencies
pip3 install --user flask flask-cors flask_httpauth

# test same origin
export FLASK_APP=hello
python3 -m flask run --port 5001 --host=127.0.0.1

# test cross-origin
export FLASK_APP=hello-cors
python3 -m flask run --port 5001 --host=127.0.0.1

# notes
https://stackoverflow.com/questions/38742379/cors-why-my-browser-doesnt-send-options-preflight-request