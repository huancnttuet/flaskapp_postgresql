from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate(db=db)


def init_app(app, **kwargs):
    db.app = app
    db.init_app(app)
    migrate.init_app(app)


from .car import CarsModel
from .score import ScoreModel
from .subject import SubjectModel
from .subject_time import SubjectTimeModel
