from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# setup database
db = SQLAlchemy()
ma = Marshmallow()
# setup migration script
migrate = Migrate()
