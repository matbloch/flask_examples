from flask import Flask
from . import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore

# setup Flask app
application = Flask(__name__, static_url_path='/static')
application.config.from_object(config.DevelopmentConfig)

# TODO: do we actually need this in debug?
application.jinja_env.auto_reload = True

# setup database
db = SQLAlchemy(application)
migrate = Migrate(application, db)

# import user database models
from . import user_model as user_model

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, user_model.User, user_model.Role)
security = Security(application, user_datastore)

# define routing
from . import routing


# Create a user to test with
@application.before_first_request
def create_user():
    db.create_all()
    #user_datastore.create_user(email='user@user.com', password='password')
    db.session.commit()


# provide shell custom context
@application.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': user_model.User}
