from flask import Flask


def create_app():
    from app import models, api

    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345678@localhost:5432/uet_api"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ehcvizsztwxxfy:84d3521c4223cff25a51567d24651252e2cd98d70abaec4f8a4f6fa3d438abcb@ec2-184-72-236-57.compute-1.amazonaws.com:5432/d99nfdrao8b0ah"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    models.init_app(app)
    api.init_app(app)

    return app
