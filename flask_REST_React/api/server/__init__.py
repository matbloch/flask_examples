from flask import Flask
from . import config, routing

from .extensions import db, ma, migrate

# define database models and routing
from . import routing

# setup flask app
app = Flask(__name__, static_url_path='/static')


def create_app(conf=config.DevelopmentConfig):
    app.config.from_object(conf)
    init_extensions(app)
    routing.register_routes(app)
    return app


def init_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
