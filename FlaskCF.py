from flask import Flask
import os

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 8080))


@app.route('/')
def hello_world():
    return 'Hello Cloud Foundry!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

# That's All Folks !!
