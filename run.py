from flask import Flask
from flask_restplus import Resource, Api, fields
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345678@localhost:5432/cars_api"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ehcvizsztwxxfy:84d3521c4223cff25a51567d24651252e2cd98d70abaec4f8a4f6fa3d438abcb@ec2-184-72-236-57.compute-1.amazonaws.com:5432/d99nfdrao8b0ah"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)

car = api.model('Car', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'name': fields.String(required=True, description='The task details'),
    'model': fields.String(required=True, description='none'),
    'doors': fields.Integer(required=True, description='none'),
})


class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"


@api.route('/cars')
class CarsSimple(Resource):
    def get(self):
        cars = CarsModel.query.all()
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
        new_car = CarsModel(name=data['name'],
                            model=data['model'], doors=data['doors'])
        db.session.add(new_car)
        db.session.commit()
        return {"message": f"car {new_car.name} has been created successfully."}


if __name__ == '__main__':
    app.run()
