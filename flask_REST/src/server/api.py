from flask import Blueprint
from flask_restful import Api

from .resources.Hello import Hello

# register blueprint
api_bp = Blueprint('api', __name__)

# create routes
api = Api(api_bp)
api.add_resource(Hello, '/hello')