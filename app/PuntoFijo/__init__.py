from flask import Blueprint

puntoFijo = Blueprint('puntoFijo', __name__, url_prefix='/api/puntofijo')

from . import routes