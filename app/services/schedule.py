from app.models import db
from app import models as m


def get_schedule(mssv):
    s = m.SubjectModel
    st = m.SubjectTimeModel
    q = (
        db.session.query(s, st)
        .filter(s.code == mssv)
        .filter(s.class_code == st.class_code)
        .all()
    )
    return q
