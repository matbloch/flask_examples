from flask import Flask
# application configuration
from . import config

# database stuff
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# setup Flask app
application = Flask(__name__, static_url_path='/static')
application.config.from_object(config.DevelopmentConfig)

# TODO: do we actually need this in debug?
application.jinja_env.auto_reload = True

# setup database
db = SQLAlchemy(application)
migrate = Migrate(application, db)


