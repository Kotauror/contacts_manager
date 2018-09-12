from flask import Flask
import config

def create_app(app_config):
    app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
    app.config.from_object(app_config)
    return app
