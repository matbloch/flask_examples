from flask_restful import Resource, reqparse
from ..models import RoleModel
from app import db


class SingleRoleAPI(Resource):

    def get(self, role_id):
        the_role = RoleModel.find_by_id(role_id)
        if not the_role:
            return {'message': 'Role not found'}, 400

        return {'message': 'The role: ' + the_role.name}, 200

    def delete(self, role_id):
        the_role = RoleModel.find_by_id(role_id)
        if not the_role:
            return {'message': 'Role not found'}, 400

        db.session.delete(the_role)
        db.session.commit()
        return {'message': 'Role deleted'}, 410


class RolesAPI(Resource):
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

    def get(self):
        return {'roles': list(map(lambda x: x.name, RoleModel.query.all()))}



