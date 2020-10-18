from flask import Blueprint

false_position = Blueprint('false_position', __name__, url_prefix='/api/false_position')

from . import routes