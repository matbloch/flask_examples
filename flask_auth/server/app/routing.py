from flask import Blueprint
from flask_restful import Api

from app import application
from .resources import Users, Roles, Auth, Protected

# register blueprint
api_bp = Blueprint('api', __name__)

# create routes
api = Api(api_bp, default_mediatype="application/json")

# users
api.add_resource(Users.UsersAPI, '/users')
api.add_resource(Users.SingleUserAPI, '/users/<int:user_id>')
api.add_resource(Users.UserRoleAPI, '/users/<int:user_id>/roles')
# roles
api.add_resource(Roles.RolesAPI, '/roles')
api.add_resource(Roles.SingleRoleAPI, '/roles/<int:role_id>')
# authentication
api.add_resource(Auth.UserLogin, '/login')
api.add_resource(Auth.TokenRefresh, '/login/refresh')
api.add_resource(Auth.UserLogoutAccess, '/logout/access')
api.add_resource(Auth.UserLogoutRefresh, '/logout/refresh')
# protected resource
api.add_resource(Protected.ProtectedResource, '/protected')
api.add_resource(Protected.ProtectedAdminResource, '/protected/admin')
# register the blueprint
application.register_blueprint(api_bp, url_prefix='/api')