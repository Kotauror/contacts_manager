import os
import create_app, config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = create_app.create_app(app_config=config.DevelopmentConfig)
db = SQLAlchemy(app)
