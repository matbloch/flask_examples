import pytest
from server import create_app
from server import config
from server.extensions import db
from server.models import User


@pytest.fixture(scope='module')
def test_user():
    user = User(name="test user")
    yield user


@pytest.fixture(scope='module')
def test_client():

    flask_app = create_app(config.TestingConfig)
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert user data
    # ...

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
