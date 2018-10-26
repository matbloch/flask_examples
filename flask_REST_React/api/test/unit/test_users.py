from server.models import User
from server.extensions import db


def test_create_user(test_client, init_database):
    test_user = User(name="test user")
    db.session.add(test_user)
    db.session.commit()
    all_users = User.query.all()
    assert len(all_users) != 0
    assert all_users[-1].name \
           == test_user.name


def test_delete_user(test_client, init_database):
    test_user = User(name="dwain_johnson")
    db.session.add(test_user)
    db.session.commit()
    db.session.delete(User.query.filter_by(name="dwain_johnson").first())
    db.session.commit()
    assert(len(User.query.filter_by(name="dwain_johnson").all()) == 0)


def test_update_user_attributes(test_client, init_database):
    test_user = User(name="test user")
    db.session.add(test_user)
    db.session.commit()

    assert (len(User.query.all()) != 0)
    user = User.query.first()
    user.name = "A new user name"
    db.session.commit()
    assert User.query.first().name == user.name

