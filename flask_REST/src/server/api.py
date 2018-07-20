from flask import Blueprint
from flask_restful import Api

from .resources.Hello import Hello
from .resources.Category import CategoryResource

# register blueprint
api_bp = Blueprint('api', __name__)

# create routes
api = Api(api_bp, default_mediatype="application/json")
api.add_resource(Hello, '/hello')

api.add_resource(CategoryResource, '/category')