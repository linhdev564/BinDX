from flask import Flask
from . import routes

def create_app():
    app = Flask(__name__)

    routes.init_routes(app)

    return app