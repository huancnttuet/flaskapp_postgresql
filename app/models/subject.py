from app.models import db


class SubjectModel(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)
    stt = db.Column(db.String())
    code = db.Column(db.String())
    name = db.Column(db.String())
    dob = db.Column(db.String())
    school_year = db.Column(db.String())
    class_code = db.Column(db.String())
    class_name = db.Column(db.String())
    class_type = db.Column(db.String())
    credit = db.Column(db.String())
    register_type = db.Column(db.String())
    term_id = db.Column(db.String())

    def __init__(self, subject):
        self.stt = subject[0]
        self.code = subject[1]
        self.name = subject[2]
        self.dob = subject[3]
        self.school_year = subject[4]
        self.class_code = subject[5]
        self.class_name = subject[6]
        self.class_type = subject[7]
        self.credit = subject[8]
        self.register_type = subject[9]
        self.term_id = subject[10]

    def __repr__(self):
        return f"<Subject {self.name}>"
