from marshmallow import Schema, fields, ValidationError


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=must_not_be_blank)
    status = fields.Int()
    creation_date = fields.DateTime(dump_only=True)


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=must_not_be_blank)
    description = fields.Str()
    creation_date = fields.DateTime(dump_only=True)
    status = fields.Int(required=True, validate=must_not_be_blank)
    # --- Relationships
    users = fields.Nested(UserSchema, only=('id', 'name',), many=True, dump_only=True)
    user_ids = fields.List(fields.Int, load_only=True, data_key='users')
    # --- Custom serialization attributes
    nr_users = fields.Int(dump_only=True)
