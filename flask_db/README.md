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
    - `python db_manager/migrate.py db init`
2. Apply some changes to the database models in `app/models.py`
3. Generate the migration script
    - `python db_manager/migrate.py db migrate`
4. Apply the changes to the dabase
    - `python db_manager/migrate.py db upgrade`


