import os
import config
from create_app import create_app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = create_app(config.DevelopmentConfig)
db = SQLAlchemy(app)
