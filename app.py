from flask import Flask, request
from flask_smorest import Api
from resources.runners import blp as RunnersBlueprint
from db import db
import models

def create_app():
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Runners REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///runners.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        """This creates all of our tables initially. It knows what tables to create
        because we imported db and models"""
        db.create_all()

    # This connects the flask smorest extension to the flask app.
    api = Api(app)
    api.register_blueprint(RunnersBlueprint)
    return app
