from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from .resources.Users import \
    UserAPI, UserListAPI
from .resources.Tasks import \
    TaskAPI, TaskListAPI

# register blueprint
api_bp = Blueprint('api', __name__)

# create routes
api = Api(api_bp, default_mediatype="application/json")

api.add_resource(UserListAPI, '/users')
api.add_resource(UserAPI, '/users/<int:id>')

api.add_resource(TaskListAPI, '/tasks')
api.add_resource(TaskAPI, '/tasks/<int:id>')


def register_routes(app):
    # allow CORS requests
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    # register the blueprint
    app.register_blueprint(api_bp, url_prefix='/api')
