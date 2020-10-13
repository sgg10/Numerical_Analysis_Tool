from flask import Blueprint

reglaFalsa = Blueprint('reglaFalsa', __name__, url_prefix='/api/reglafalsa')

from . import routes