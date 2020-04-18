from flask import Flask


def create_app():
    from app import models, api

    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:12345678@localhost:5432/uet_api"
    # app.config[
    #     "SQLALCHEMY_DATABASE_URI"
    # ] = "postgres://lxzerkyuvpmqcq:01cfd513d5a5ae92bc3ffd6fd07f34e7ce6c145d805911dc1f51cd2335e0baf2@ec2-3-231-46-238.compute-1.amazonaws.com:5432/d3164254kl09mu"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    models.init_app(app)
    api.init_app(app)

    return app


app = create_app()
