from flask import Flask, render_template
from app import application


@application.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('page/home/index.html', title="Welcome")


@application.errorhandler(404)
def page_not_found(error):
    return render_template('page/errors/404.html', title='Page Not Found'), 404
