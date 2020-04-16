from app.api import api
import flask_restplus as fr
from app.extensions import marshmallow as mm
from app.extensions import RequestParser

score_doc = api.model("ScoreGetDoc", {
    "term": fr.fields.Integer(example=76),
    "type_education": fr.fields.Integer(example=0),
})


score_list_params = RequestParser(bundle_errors=True)
score_list_params.add_argument(
    'term', default=76, required=False, location='args', type=int)
score_list_params.add_argument(
    'type_education', default=0, required=False, location='args', type=int)

list_term_list_params = RequestParser(bundle_errors=True)
list_term_list_params.add_argument(
    'year', default=5, required=False, location='args', type=int)


class ScoreGetSchema(mm.Schema):
    term = mm.fields.Integer(min=1, required=True)
    type_education = mm.fields.Integer(min=0, required=True)
