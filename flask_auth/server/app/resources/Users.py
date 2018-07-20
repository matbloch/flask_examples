from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token)
from ..models import UserModel, RoleModel
from app import db


class UserRoleAPI(Resource):

    def get(self, user_id):
        the_user = UserModel.find_by_id(user_id)
        if not the_user:
            return {'message': 'User not found'}, 400
        return {'roles': list(map(lambda x: {'name': x.name}, the_user.roles))}, 200

    def post(self, user_id):
        args = reqparse.RequestParser() \
            .add_argument("role_id", type=int, location='json', required=True, help="missing") \
            .parse_args()

        the_user = UserModel.find_by_id(user_id)

        if not the_user:
            return {'message': 'User not found'}, 400

        the_role = RoleModel.find_by_id(args['role_id'])
        if not the_role:
            return {'message': 'Role not found'}, 400

        # commit changes to db
        the_user.add_role(the_role)
        the_user.save_to_db()

        return {
            'message': "Role added."
        }, 200

    def delete(self, user_id):
        args = reqparse.RequestParser() \
            .add_argument("role_id", type=int, location='json', required=True, help="missing") \
            .parse_args()
        the_user = UserModel.find_by_id(user_id)

        if not the_user:
            return {'message': 'User not found'}, 400

        the_role = RoleModel.find_by_id(args['role_id'])
        if not the_role:
            return {'message': 'Role not found'}, 400

        the_user.remove_role(the_role)
        the_user.save_to_db()

        return UserModel.delete_all()


class SingleUserAPI(Resource):
    def get(self, user_id):
        the_user = UserModel.find_by_id(user_id)
        if not the_user:
            return {'message': 'User not found'}, 400
        return {'message': "Username: " + the_user.username}, 200

    def delete(self, user_id):
        the_user = UserModel.find_by_id(user_id)
        if not the_user:
            return {'message': 'User not found'}, 400

        db.session.delete(the_user)
        db.session.commit()
        return {'message': 'User deleted'}, 410


class UsersAPI(Resource):
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
            access_token = create_access_token(identity=new_user)
            refresh_token = create_refresh_token(identity=new_user)
            return {
                'message': 'User {} was created'.format(args['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except Exception as e:
            return {'message': 'Something went wrong'}, 500

    def get(self):
        return UserModel.return_all()

    def delete(self):
        return UserModel.delete_all()
