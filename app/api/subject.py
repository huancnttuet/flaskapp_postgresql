from flask_restplus import Resource, fields
from app.extensions import Namespace
from app.api import api
from app.services import uet_qldt_api
from app.api.requests import subject as requests
from app.models import db
from app import models as m

subject_ns = Namespace("Subject", path="/subject", description="Môn học")


@subject_ns.route("")
class SubjectSimple(Resource):
    @subject_ns.expect(requests.subject_list_params, validate=True)
    def get(self):
        args = requests.subject_list_params.parse_args()
        termId = args.termId
        page = args.page
        pageSize = args.pageSize
        results = uet_qldt_api.get_list_of_term(termId, pageSize, page)
        return {"count": len(results), "list_subject": results}

    @subject_ns.expect(requests.term_id_list_params, validate=True)
    def post(self):
        args = requests.term_id_list_params.parse_args()
        term_id = args.termId
        page = args.page
        pwd = args.pwd
        if pwd != "ok":
            return "Sai pass"
        num = 0
        results = uet_qldt_api.get_list_of_term(term_id, 5000, page)
        num += len(results)

        for r in results:
            new_subject = m.SubjectModel(r)
            db.session.add(new_subject)
        db.session.commit()
        return {"message": f" {num} rows has been created successfully."}

    @subject_ns.expect(requests.delete_pass_list_params, validate=True)
    def delete(self):
        args = requests.delete_pass_list_params.parse_args()
        pwd = args.pwd
        if pwd != "ok":
            return "Sai pass"
        try:
            num = db.session.query(m.SubjectModel).delete()
            db.session.commit()
            return {"message": "table is deteled"}
        except:
            db.session.rollback()
