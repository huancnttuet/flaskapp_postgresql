from app.api import api
import flask_restplus as fr
from app.extensions import marshmallow as mm
from app.extensions import RequestParser

exam_time_list_params = RequestParser(bundle_errors=True)
exam_time_list_params.add_argument(
    "mssv", default="17020788", required=False, location="args", type=str
)
