from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Api, Resource, reqparse

import start

app = Flask(__name__)
api = Api(app)


class Video(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("link")
        args = parser.parse_args()
        id = args['id']
        link = args['link']
        payload = start.getLinks(id, link), 200

        return payload

   
api.add_resource(Video, "/post")


# @app.route('/post/', methods=['POST'])
# def post_something():
#     parser = reqparse.RequestParser()
#     parser.add_argument("id")
#     parser.add_argument("link")
#     args = parser.parse_args()
#     id = args['id']
#     link = args['link']
#     payload = start.getLinks(id, link), 200

#     return payload

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)