# Flask REST

A minimal boilerplate for Restful APIs.

## Local Installation
- Install virtualenv `pip install virtualenv`
- In project directory, create new python environment `virtualenv .env` that is being stored in ".env" folder
- Active env: `.env\Scripts\activate`
	- Deactive env: `.env\Scripts\deactivate.bat`
- Install project dependencies: `pip install -r requirements.txt`


## Docker

## Initialize Database for the first time
**Option A:** Python Shell
- `from server import db`
- `db.create_all()`

**Option B:** Migration Script


## Extending the Database Model

1. Create a migration repository (add it to your version control system)
    - `python app/migrate.py db init`
2. Apply some changes to the database models in `app/models.py`
3. Generate the migration script
    - `python db_app/migrate.py db migrate`
4. Apply the changes to the database
    - `python db_app/migrate.py db upgrade`
