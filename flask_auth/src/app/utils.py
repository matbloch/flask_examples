from functools import wraps

from flask_jwt_extended import (
    verify_jwt_in_request, get_jwt_claims
)


# custom admin group decorator
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if 'admin' not in claims['roles']:
            return {'message': 'Not authorized!'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper
