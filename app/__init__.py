from flask import Flask
from .routes.routes import init_routes

def create_app():
    app = Flask(__name__)

    init_routes(app)
    app.run(debug=True)
    return app