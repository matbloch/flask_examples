# Flask Authentication API


## Setup

**Create The Database**
- `python app/migrate.py db init`
- `python app/migrate.py db migrate`
- `python app/migrate.py db upgrade`

**Add Users Manually**
- open Python shell
- `from app import db`
- `from app.user_model import UserModel`
- `admin = UserModel(username='admin', email='admin@example.com')`
- `guest = UserModel(username='guest', email='guest@example.com')`
- `db.session.add(admin)`
- `db.session.add(guets)`
- `db.session.commit()`
- Test entries: `UserModel.query.all()`
