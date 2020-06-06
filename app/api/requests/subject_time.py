from app.api import api
import flask_restplus as fr
from app.extensions import marshmallow as mm
from app.extensions import RequestParser

subject_time_list_params = RequestParser(bundle_errors=True)
subject_time_list_params.add_argument(
    "termId", default="61", required=False, location="args", type=str
)

term_id_list_params = RequestParser(bundle_errors=True)
term_id_list_params.add_argument(
    "termId", default="61", required=False, location="args", type=str
)
term_id_list_params.add_argument(
    "pwd", default="", required=False, location="args", type=str
)
delete_pass_list_params = RequestParser(bundle_errors=True)
delete_pass_list_params.add_argument(
    "pwd", default="", required=False, location="args", type=str
)
