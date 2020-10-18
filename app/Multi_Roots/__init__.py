from flask import Blueprint

multi_roots = Blueprint('multi_roots', __name__, url_prefix='/api/multi_roots')

from . import routes