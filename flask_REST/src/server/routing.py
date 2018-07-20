from flask import Flask, render_template
from .api import api_bp
# the application
from server import application


# register the blueprint
application.register_blueprint(api_bp, url_prefix='/api')

