from flask_restplus import Resource, fields
from app.extensions import Namespace
from app.api import api
from app.services import schedule
from app.api.requests import schedule as requests
from app.models import db
from app import models as m
import json

schedule_ns = Namespace("Schedule", path="/schedule", description="Thời khóa biểu")


@schedule_ns.route("")
class ScheduleSimple(Resource):
    @schedule_ns.expect(requests.schedule_list_params, validate=True)
    def get(self):
        args = requests.schedule_list_params.parse_args()
        mssv = args.mssv

        results = schedule.get_schedule(mssv)
        subject_times = []
        for r in results:
            st = r[1].to_array()
            subject_times.append(st)

        return subject_times
