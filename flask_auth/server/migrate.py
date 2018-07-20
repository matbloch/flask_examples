from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import application, db

migrate = Migrate(application, db)
manager = Manager(application)
manager.add_command('db', MigrateCommand)

# define models
from app.models import *

if __name__ == '__main__':
    """
    Migration
    """
    manager.run()
