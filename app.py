from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Api, Resource, reqparse

import start
import json

app = Flask(__name__)

@app.route('/post/', methods=['POST'])
def post_something():
    parser = reqparse.RequestParser()
    parser.add_argument("id")
    parser.add_argument("link")
    args = parser.parse_args()
    id = args['id']
    link = args['link']
    payload = start.getLinks(id, link), 200

    return payload

# A welcome message to test our server
@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)