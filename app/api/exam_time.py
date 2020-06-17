from flask_restplus import Resource, fields
from app.extensions import Namespace
from app.api import api
from app.services import uet_qldt_api
from app.api.requests import exam_time as requests
from app.models import db
from app import models as m

exam_time_ns = Namespace("ExamTime", path="/exam-time", description="Lịch thi")


@exam_time_ns.route("")
class ExamTimeSimple(Resource):
    @exam_time_ns.expect(requests.exam_time_list_params, validate=True)
    def get(self):
        args = requests.exam_time_list_params.parse_args()
        mssv = args.mssv
        results = uet_qldt_api.get_exam_time(mssv)
        re = []
        for r in results:
            re.append({
                'id': r[0],
                'student_code': r[1],
                'student_name': r[2],
                'class_name': r[4],
                'dob': r[3],
                'sbd': r[5],
                'course_code': r[6],
                'course_name': r[7],
                'day': r[8],
                'time': r[9],
                'exam_case': r[10],
                'room': r[11],
                'place': r[12],
                'note': r[13]}
            )
        return re
