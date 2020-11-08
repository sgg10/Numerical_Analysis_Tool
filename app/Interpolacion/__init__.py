from flask import Blueprint

interpolacion = Blueprint('interpolaciones', __name__, url_prefix='/api/interpolacion')

from . import routes