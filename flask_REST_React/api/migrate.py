import sys
import os

module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)

from flask_script import Manager
from flask_migrate import MigrateCommand

from server import config
from server import create_app, init_extensions


if __name__ == '__main__':

    application = create_app(config.DevelopmentConfig)
    init_extensions(application)

    manager = Manager(application)
    manager.add_command('db', MigrateCommand)

    manager.run()
