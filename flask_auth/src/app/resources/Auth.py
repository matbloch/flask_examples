from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from ..models import UserModel, RoleModel, RevokedTokenModel


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


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


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
