from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


# class Protected(Resource):
#     @auth_token_required
#     def get(self):
#         return {"msg": "Authentication failed"}, 200
#
#     @auth_token_required
#     @roles_required('admin')
#     def post(self):
#         return {"msg": "This resource is protected an only accessible for the admin role"}, 201


class SecretResource(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return {
            'logged_in_as': current_user
}
