from flask import Blueprint

fixedPointIteration = Blueprint('fixedPointIteration', __name__, url_prefix='/api/fixedPointIteration')

from . import routes