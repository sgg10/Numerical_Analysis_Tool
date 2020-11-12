from flask import Blueprint

interpolations = Blueprint('interpolations', __name__, url_prefix='/api/interpolations')

from . import routes