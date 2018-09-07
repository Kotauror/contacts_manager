import os

class BaseConfig():
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI', 'postgresql://localhost/contacts')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestConfig():
    TESTING = True
