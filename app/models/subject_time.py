from app.models import db


class SubjectTimeModel(db.Model):
    __tablename__ = "subject_times"

    id = db.Column(db.Integer, primary_key=True)
    stt = db.Column(db.String())
    class_code_1 = db.Column(db.String())
    class_name = db.Column(db.String())
    credit = db.Column(db.String())
    class_code = db.Column(db.String())
    teacher = db.Column(db.String())
    student_total = db.Column(db.String())
    session = db.Column(db.String())
    day = db.Column(db.String())
    lession = db.Column(db.String())
    classroom = db.Column(db.String())
    note = db.Column(db.String())

    def __init__(self, subject):
        self.stt = subject[0]
        self.class_code_1 = subject[1]
        self.class_name = subject[2]
        self.credit = subject[3]
        self.class_code = subject[4]
        self.teacher = subject[5]
        self.student_total = subject[6]
        self.session = subject[7]
        self.day = subject[8]
        self.lession = subject[9]
        self.classroom = subject[10]
        self.note = subject[11]

    def __repr__(self):
        return f"<SubjectTime {self.class_name}>"

    def serialize(self):
        return {
            "subject_name": self.class_name,
            "credit": self.credit,
            "class_code": self.class_code,
            "teacher": self.teacher,
            "student_total": self.student_total,
            "day_time": self.session,
            "day_week": self.day,
            "lesson": self.lession,
            "room": self.classroom,
            "note": self.note,
        }

    def to_array(self):
        st = SubjectTimeModel
        return [
            self.class_name,
            self.credit,
            self.class_code,
            self.teacher,
            self.student_total,
            self.session,
            self.day,
            self.lession,
            self.classroom,
            self.note,
        ]
