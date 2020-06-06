from flask_restplus import Resource, fields
from app.extensions import Namespace
from app.api import api
from app.services import uet_api, score_service
from app.api.requests import score as requests
from app.models import db
from app import models as m

score_ns = Namespace("Score", path="/score", description="Xem điểm thi")

score = api.model(
    "Score",
    {
        "id": fields.Integer(readonly=True, description="The task unique identifier"),
        "name": fields.String(required=True, description="The task details"),
        "code": fields.String(required=True, description="none"),
        "path": fields.String(required=True, description="none"),
        "time": fields.String(required=True, description="none"),
        "note": fields.String(required=True, description="none"),
    },
)


@score_ns.route("")
class ScoreSimple(Resource):
    @score_ns.expect(requests.score_list_params, validate=True)
    def get(self):
        args = requests.score_list_params.parse_args()
        term = args.term
        type_education = args.type_education
        print(args)
        results = uet_api.get_score(term, type_education)
        results[1] = [[results[1]]]
        return results

    @score_ns.expect(requests.score_post_params, validate=True)
    def post(self):
        args = requests.score_post_params.parse_args()
        term = args.term
        type_education = args.type_education
        pwd = args.pwd
        if pwd != "ok":
            return "Sai pass"
        num = 0
        results = uet_api.get_score(term, type_education)
        num += len(results[0])
        for r in results[0]:
            new_score = m.ScoreModel(r, str(term), str(type_education))
            db.session.add(new_score)
        db.session.commit()
        return {"message": f" {num} rows has been created successfully."}


@score_ns.route("/getListYearTerm")
class GetListYearTermSimple(Resource):
    def get(self):
        results = uet_api.get_list_year_term()
        return {
            "list_year": results[0],
            "list_term": results[3],
            "current_term": results[1],
            "current_year": results[2],
        }


@score_ns.route("/getListTerm")
class GetListTermSimple(Resource):
    @score_ns.expect(requests.list_term_list_params, validate=True)
    def get(self):
        args = requests.list_term_list_params.parse_args()
        year = args.year
        results = uet_api.get_list_term(year)
        return {"count": len(results), "list_term": results}


@score_ns.route("/search")
class SearchSimple(Resource):
    @score_ns.expect(requests.search_list_params, validate=True)
    def get(self):
        args = requests.search_list_params.parse_args()
        text = args.input
        term = args.term
        type_education = args.type_education
        results = uet_api.search(text, term, type_education)
        results[1] = [[results[1]]]
        return results


@score_ns.route("/quickSearch")
class SearchSimple(Resource):
    @score_ns.expect(requests.input_search_list_params, validate=True)
    def get(self):
        args = requests.input_search_list_params.parse_args()
        text = args.input
        results = uet_api.quick_search(text)
        return {"count": len(results), "list_score": results}


@score_ns.route("/getHintInput")
class SearchSimple(Resource):
    @score_ns.expect(requests.input_search_list_params, validate=True)
    def get(self):
        args = requests.input_search_list_params.parse_args()
        text = args.input
        results = uet_api.get_hint_input(text)
        return {"count": len(results), "list_hint": results}


@score_ns.route("/getAll")
class ScoreSimple(Resource):
    @score_ns.expect(requests.score_list_params, validate=True)
    def get(self):
        args = requests.score_list_params.parse_args()
        term = args.term
        type_education = args.type_education

        results = score_service.get_all(str(term), str(type_education))
        scores = []
        for r in results:
            s = r.to_array()
            scores.append(s)
        return scores
