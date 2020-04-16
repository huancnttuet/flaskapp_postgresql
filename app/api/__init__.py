from flask import Blueprint, url_for
from flask_restplus import Api

api_bp = Blueprint('api', __name__)


class CustomApi(Api):
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        scheme = 'http' if '5000' in self.base_url else 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)


api = CustomApi(
    app=api_bp,
    version='BETA 1.0',
    title='UET Support API',
    validate=False,
    # doc=swagger_doc  # disable Swagger UIs
)


def init_app(app, **kwargs):
    """
    :param flask.Flask app: the app
    :param kwargs:
    :return:
    """
    from .car import car_ns
    from .score import score_ns
    app.register_blueprint(api_bp)
    # api.add_namespace(car_ns)
    api.add_namespace(score_ns)
