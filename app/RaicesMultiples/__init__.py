from flask import Blueprint

raicesMultiples = Blueprint('raicesMultiples', __name__, url_prefix='/api/raicesmultiples')

from . import routes