from flask import Flask
import config

def create_app(app_config):
    app = Flask(__name__, static_folder="../frontend/dist", template_folder="../frontend")
    app.config.from_object(app_config)
    return app
