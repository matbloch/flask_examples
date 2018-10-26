# Flask REST API

**API Endpoints**

- `/api/users`
  - `GET` get all users
  - `POST` create a new user

- `/api/users/<int:id>`
  - `GET` get a specific user
  - `PATCH` update a user
  - `DELETE` delete a user

- `/api/tasks`
  - `GET` get all tasks
  - `POST` create a new task

- `/api/tasks/<int:id>`
  - `GET` get a specific task
  - `PATCH` update a task
  - `DELETE` delete a task



**Example**: Updating Relationships

`POST http://localhost:3000/api/tasks/42`

Payload:

```json
{
    "name": "New Task Name",
    "user_ids": [3, 5, 163]
}
```



## Setup

**Install Requirements**

1. pip install virtualenv` install virtualenv
2. `virtualenv .env` init new virtual environment in the folder ".env"
3. `.env\Scripts\activate` activate the environment (`.env\Scripts\deactivate.bat` to deactivate)
4. ``pip install -r requirements.txt`` install dependencies

**Initialize the Database**

1. `python migrate.py db init` initialize the database migration
2. `python migrate.py db migrate` create the migration
3. `python migrate.py db upgrade` upgrade the database

**Run the Server**

- `python run.py`

## Testing

- `python -m pytest test` run tests

  - disable reporting of stdout/stderr/logs completely for failed tests: ` python -m pytest --show-capture=no -p no:warnings`
  - set logging level: `python -m pytest --log-cli-level=ERROR test`



## Misc
### Extending the Database Model

1. Create a migration repository (add it to your version control system)
    - `python migrate.py db init`
2. Apply some changes to the database models in `server/models.py`
3. Generate the migration script
    - `python migrate.py db migrate`
4. Apply the changes to the database
    - `python migrate.py db upgrade`

**Hint**

- Each time you update your models, run `migrate` and `upgrade`