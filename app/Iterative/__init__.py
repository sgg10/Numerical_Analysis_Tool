from flask import Blueprint

iterative = Blueprint('iterative', __name__, url_prefix='/api/iterative')

from . import routes