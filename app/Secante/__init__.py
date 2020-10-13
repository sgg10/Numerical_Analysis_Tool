from flask import Blueprint

secante = Blueprint('secante', __name__, url_prefix='/api/secante')

from . import routes