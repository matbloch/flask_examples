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


## API Endpoints

**Role Management**
- `GET /roles` get all role
- `POST /roles` create role
- `GET /roles/<id:role_id>` get specific role
- `DELETE /roles/<id:role_id>` delete specific role

**User Management**
- `GET /users` get all users
- `POST /users/`
- `DELETE /users/`
- `GET /users/<id:user_id>`
- `DELETE /users/<id:user_id>`

**Role Assignment**
- `GET /users/<int:user_id>/roles/` get all roles for user
- `POST /users/<int:user_id>/roles/` add specific role
- `DELETE /users/<int:user_id>/roles/` DELETE specific role


**Authentication**
- `POST /login` Login - get access and refresh tokens
- `POST /login/refresh` Refresh access token
- `POST /logout/access` Revoke access token
- `POST /logout/refresh` Revoke refresh token
