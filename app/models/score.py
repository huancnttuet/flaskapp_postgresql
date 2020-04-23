from app.models import db


class ScoreModel(db.Model):
    __tablename__ = "scores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    code = db.Column(db.String())
    path = db.Column(db.String())
    time = db.Column(db.String())
    note = db.Column(db.String())
    term = db.Column(db.String())
    type_education = db.Column(db.String())

    def __init__(self, score, term, type_education):
        self.name = score[0]
        self.code = score[1]
        self.path = score[2]
        self.time = score[3]
        self.note = score[4]
        self.term = term
        self.type_education = type_education

    def __repr__(self):
        return f"<Score {self.name}>"

    def to_array(self):

        return [self.name, self.code, self.path, self.time, self.note, self.term, self.type_education]
