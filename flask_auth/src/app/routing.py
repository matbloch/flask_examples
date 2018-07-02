from flask import Blueprint
from flask_restful import Api

from app import application, resources

# register blueprint
api_bp = Blueprint('api', __name__)

# create routes
api = Api(api_bp, default_mediatype="application/json")
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserRoles, '/roles')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.UserManageRoles,
                 '/users/<int:user_id>/roles/<int:role_id>',     # post/delete
                 '/users/<int:user_id>/roles'                    # get
                 )
api.add_resource(resources.SecretResource, '/protected')

# register the blueprint
application.register_blueprint(api_bp, url_prefix='/api')