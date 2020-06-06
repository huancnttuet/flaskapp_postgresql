from app.api import api
import flask_restplus as fr
from app.extensions import marshmallow as mm
from app.extensions import RequestParser

subject_list_params = RequestParser(bundle_errors=True)
subject_list_params.add_argument(
    "termId", default="028", required=False, location="args", type=str
)
subject_list_params.add_argument(
    "page", default=1, required=False, location="args", type=int
)
subject_list_params.add_argument(
    "pageSize", default=10, required=False, location="args", type=int
)

term_id_list_params = RequestParser(bundle_errors=True)
term_id_list_params.add_argument(
    "termId", default="028", required=False, location="args", type=str
)
term_id_list_params.add_argument(
    "page", default="", required=False, location="args", type=str
)
term_id_list_params.add_argument(
    "pwd", default="", required=False, location="args", type=str
)
delete_pass_list_params = RequestParser(bundle_errors=True)
delete_pass_list_params.add_argument(
    "pwd", default="", required=False, location="args", type=str
)
