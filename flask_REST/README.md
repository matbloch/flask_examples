# Flask REST

A minimal boilerplate for Restful APIs.

## Setup

### Local
- Install virtualenv `pip install virtualenv`
- In project directory, create new python environment `virtualenv .env` that is being stored in ".env" folder
- Active env: `.env\Scripts\activate`
	- Deactive env: `.env\Scripts\deactivate.bat`
- Install project dependencies: `pip install -r requirements.txt`


### Docker

## Database Model

- `class Comment` ORM for Comment Table
- `class Category` ORM for Category Table
- `CategorySchema`/`CommentSchema` used for Validation

## Initialize Database for the first time
**Option A:** Python Shell
- `from server import db`
- `db.create_all()`

**Option B:** Migration Script


## Extending the Database Model

1. Create a migration repository (add it to your version control system)
    - `python web/migrate.py db init`
2. Apply some changes to the database models in `app/models.py`
3. Generate the migration script
    - `python web/migrate.py db migrate`
4. Apply the changes to the database
    - `python web/migrate.py db upgrade`

**Hint**
- Each time you update your models, run `migrate` and `upgrade`