from app.models import db
from app import models as m


def get_all(term, type_education):
    s = m.ScoreModel
    q = (
        db.session.query(s)
        .filter(s.term == term and s.type_education == type_education)
        .all()
    )
    return q
