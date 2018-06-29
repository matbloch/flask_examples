# Flask Database Integration with SQLAlchemy

**Configuration**
- SQLLite


## Deployment

**With Docker**
- Build the docker image: `docker build . -t "flask_db"`
- Run the docker image: `docker run --rm -ti -p 8080:8080 flask_db`
- open http://localhost:8080

## Extending the Database Model

1. Create a migration repository (add it to your version control system)
    - `python app/migrate.py db init`
2. Apply some changes to the database models in `app/models.py`
3. Generate the migration script
    - `python db_app/migrate.py db migrate`
4. Apply the changes to the database
    - `python db_app/migrate.py db upgrade`

### "Manual" Database Queries
- Open console and run `python` prompt
- Import the database and the models:
```bash
>>> from app import db
>>> from app.models import User
```

**Adding a New User**
```bash
>>> u = User(username='John', email='johm@wayne.com')
>>> db.session.add(u)
>>> db.session.commit()
```

**Listing All Users**
```bash
>>> users = User.order_by(User.username.desc()).all()
>>> print(users)
```

**Delete User**
```bash
>>> u = User.query.get(1)
>>> db.session.delete(u)
>>> db.session.commit()
```
