from flask import Flask
from flask import jsonify
import os

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 8080))


@app.route('/')
def hello_world():
    return 'Hello Cloud Foundry!'


@app.route('/echo')
def echo():
    return 'Echo!'


@app.route('/pythonapi')
def api():
    response = dict(type='REST', language='Python', version='0.0.1')
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

# That's All Folks !!
