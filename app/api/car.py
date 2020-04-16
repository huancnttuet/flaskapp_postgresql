from flask_restplus import Resource, fields
from app.extensions import Namespace
from app.models import db
from app import models as m
from app.api import api, car

car_ns = Namespace('Cars', path='/cars', description='Car api')

car = api.model('Car', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'name': fields.String(required=True, description='The task details'),
    'model': fields.String(required=True, description='none'),
    'doors': fields.Integer(required=True, description='none'),
})


@car_ns.route('')
class CarsSimple(Resource):
    def get(self):
        cars = m.CarsModel.query.all()
        results = [
            {
                "name": car.name,
                "model": car.model,
                "doors": car.doors
            } for car in cars]

        return {"count": len(results), "cars": results}

    @api.expect(car)
    def post(self):

        data = api.payload
        new_car = m.CarsModel(name=data['name'],
                              model=data['model'], doors=data['doors'])
        db.session.add(new_car)
        db.session.commit()
        return {"message": f"car {new_car.name} has been created successfully."}
