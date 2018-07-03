from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import (jwt_required, get_jwt_identity, get_jwt_claims)
from ..utils import admin_required


class ProtectedResource(Resource):
    @jwt_required
    def get(self):
        ret = {
            'current_identity': get_jwt_identity(),
            'current_roles': get_jwt_claims()
        }
        return ret, 200


class ProtectedAdminResource(Resource):
    @jwt_required
    @admin_required
    def get(self):
        ret = {
            'current_identity': get_jwt_identity(),
            'current_roles': get_jwt_claims()
        }
        return ret, 200

