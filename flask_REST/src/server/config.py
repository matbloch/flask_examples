import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    # security token
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True
    # database settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_dev.db')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    # database settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    pass

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

