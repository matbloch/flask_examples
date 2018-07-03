from flask import Flask
from . import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# setup Flask app
application = Flask(__name__, static_url_path='/static')
application.config.from_object(config.DevelopmentConfig)

# TODO: do we actually need this in debug?
application.jinja_env.auto_reload = True

# setup database
db = SQLAlchemy(application)
migrate = Migrate(application, db)

# jwt auth
jwt = JWTManager(application)

# define routing and models
from . import routing, models


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)

# Create a function that will be called whenever create_access_token
# is used. It will take whatever object is passed into the
# create_access_token method, and lets us define what custom claims
# should be added to the access token.
@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'roles': list(map(lambda x: x.name, user.roles))}

# Create a function that will be called whenever create_access_token
# is used. It will take whatever object is passed into the
# create_access_token method, and lets us define what the identity
# of the access token should be.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username



# provide shell custom context
# @application.shell_context_processor
# def make_shell_context():
#     return {'db': db}
