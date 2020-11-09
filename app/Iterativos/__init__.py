from flask import Blueprint

iterativos = Blueprint('iterativos', __name__, url_prefix='/api/iterativos')

from . import routes