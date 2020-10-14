from flask import Blueprint

busquedaIncrementales = Blueprint('busquedaIncrementales', __name__, url_prefix='/api/busquedaincrementales')

from . import routes