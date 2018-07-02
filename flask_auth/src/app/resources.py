from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from app.models import UserModel, RoleModel, RevokedTokenModel


# class Protected(Resource):
#     @auth_token_required
#     def get(self):
#         return {"msg": "Authentication failed"}, 200
#
#     @auth_token_required
#     @roles_required('admin')
#     def post(self):
#         return {"msg": "This resource is protected an only accessible for the admin role"}, 201


class UserRoles(Resource):
    def post(self):
        args = reqparse.RequestParser() \
            .add_argument("name", type=str, location='json', required=True, help="missing") \
            .add_argument("description", type=str, location='json', required=False, help="missing") \
            .parse_args()
        if RoleModel.find_by_name(args['name']):
            return {'message': 'Role {} already exists'.format(args['name'])}

        new_role = RoleModel(name=args['name'], description=args['description'])

        try:
            new_role.save_to_db()
            return {
                'message': 'Role {} was created'.format(args['name']),
            }
        except:
            return {'message': 'Something went wrong'}, 500


class UserManageRoles(Resource):

    def post(self, user_id, role_id):

        args = reqparse.RequestParser() \
            .add_argument("name", type=str, location='args', required=True, help="missing") \
            .add_argument("description", type=str, location='args', required=True, help="missing") \
            .parse_args()

        the_user = UserModel.find_by_id(user_id)

        if not the_user:
            return {'message': 'User not found'}, 401

        the_role = RoleModel.find_by_id(role_id)
        if not the_role:
            return {'message': 'Role not found'}, 401

        # commit changes to db
        the_user.add_role(the_role)
        the_user.save_to_db()

        return {
            'message': "Role added."
        }

    def get(self, user_id, **kwargs):
        the_user = UserModel.find_by_id(user_id)

        if not the_user:
            return {'message': 'User not found'}, 401

        return {'roles': list(map(lambda x: {'name': x.name}, the_user.roles))}


class UserRegistration(Resource):
    def post(self):
        args = reqparse.RequestParser() \
            .add_argument("username", type=str, location='json', required=True, help="The username") \
            .add_argument("password", type=str, location='json', required=True, help="The password") \
            .parse_args()

        if UserModel.find_by_username(args['username']):
            return {'message': 'User {} already exists'.format(args['username'])}

        new_user = UserModel(
            username=args['username'],
            password=UserModel.generate_hash(args['password'])
        )

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity=args['username'])
            refresh_token = create_refresh_token(identity=args['username'])
            return {
                'message': 'User {} was created'.format(args['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        args = reqparse.RequestParser() \
            .add_argument("username", type=str, location='json', required=True, help="The username") \
            .add_argument("password", type=str, location='json', required=True, help="The password") \
            .parse_args()

        current_user = UserModel.find_by_username(args['username'])

        if not current_user:
             return {'message': 'UserModel {} doesn\'t exist'.format(args['username'])}, 401

        if UserModel.verify_hash(args['password'], current_user.password):
            access_token = create_access_token(identity=args['username'])
            refresh_token = create_refresh_token(identity=args['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        else:
            return {'message': 'Wrong credentials'}, 401


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()

    def delete(self):
        return UserModel.delete_all()


class SecretResource(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return {
            'logged_in_as': current_user
}