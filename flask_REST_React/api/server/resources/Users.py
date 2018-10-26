from flask import request
from flask_restful import Resource
from server.models import User
from server.schemas import UserSchema
from . import *
from server.extensions import db
from marshmallow import ValidationError

users_schema = UserSchema(many=True)
user_schema = UserSchema()


class UserAPI(Resource):

    def get(self, id):
        user = User.query.get(id)
        if not user:
            return api_error_resource_does_not_exist()
        json = user_schema.dump(user)
        return api_response(200, json)

    def patch(self, id):
        user = User.query.get(id)
        if not user:
            return api_error_resource_does_not_exist()

        json_data = request.get_json(force=True)
        if not json_data:
            return api_response_no_input()

        # validate the data
        try:
            result = user_schema.load(json_data, partial=True)
        except ValidationError as err:
            return validation_error(err.messages)

        if result['name']:
            user.name = result['name']

        db.session.commit()
        return api_response(200, data=user_schema.dump(user))

    def delete(self, id):
        user = User.query.get(id)
        if not user:
            return api_error_resource_does_not_exist()

        db.session.delete(user)
        db.session.commit()
        return api_response(204, data=user_schema.dump(user))


class UserListAPI(Resource):

    def get(self):
        users = User.query.all()
        users = users_schema.dump(users)
        return api_response(200, data=users)

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return api_response_no_input()

        # validate the data
        try:
            result = user_schema.load(json_data)
        except ValidationError as err:
            return validation_error(err.messages)

        if User.query.filter_by(name=result['name']).all():
            return api_misc_error("User with this name already exists.", code=409)

        user = User(result['name'])
        db.session.add(user)
        db.session.commit()
        return api_response(204, data=user_schema.dump(user))
