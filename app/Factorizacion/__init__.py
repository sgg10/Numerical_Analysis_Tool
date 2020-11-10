from flask import Blueprint

factorizacion = Blueprint('factorizacion', __name__, url_prefix='/api/factorizacion')

from . import routes