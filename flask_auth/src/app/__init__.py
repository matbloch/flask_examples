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




# provide shell custom context
# @application.shell_context_processor
# def make_shell_context():
#     return {'db': db}
