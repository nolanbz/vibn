from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Api, Resource, reqparse

import start
import setup
import os

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

@app.route("/")
def home():
    return render_template("home.html")


class Video(Resource):

    # username = os.environ.get("USERNAME")
    # password = os.environ.get("PASSWORD")

    # if setup.local():
    #     username = "foobar"
    #     password = "foobaz"

    # users = {username: generate_password_hash(password)}

    # @auth.verify_password
    # def verify_password(self, username, password):
    #     if username in self.users:
    #         return check_password_hash(self.users.get(username), password)
    #     return False

    # @app.route('/')
    # @auth.login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("link")
        args = parser.parse_args()
        id = args['id']
        link = args['link']
        payload = start.getLinks(id, link), 200

        return payload

   
api.add_resource(Video, "/")

app.run(debug=False) 



