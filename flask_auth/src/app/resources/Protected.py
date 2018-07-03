from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import (jwt_required, get_jwt_identity, get_jwt_claims)


class ProtectedResource(Resource):
    @jwt_required
    def get(self):
        ret = {
            'current_identity': get_jwt_identity(),
            'current_roles': get_jwt_claims()
        }
        return ret, 200

