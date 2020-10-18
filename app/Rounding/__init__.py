from flask import Blueprint

rounding = Blueprint('rounding', __name__, url_prefix='/api/rounding')

from . import routes