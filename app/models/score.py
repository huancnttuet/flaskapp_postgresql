from app.models import db


class ScoreModel(db.Model):
    __tablename__ = "scores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    code = db.Column(db.String())
    path = db.Column(db.String())
    time = db.Column(db.String())
    note = db.Column(db.String())

    def __init__(self, name, model, doors):
        self.name = name
        self.code = code
        self.path = path
        self.time = time
        self.note = note

    def __repr__(self):
        return f"<Score {self.name}>"

    def to_array(self):

        return [self.name, self.code, self.path, self.time, self.note]

