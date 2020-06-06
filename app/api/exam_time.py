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
        return results
