from flask import Flask
import config

def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)
    return app
