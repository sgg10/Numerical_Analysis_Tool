from flask import Blueprint

multiRoots = Blueprint('multiRoots', __name__, url_prefix='/api/multiRoots')

from . import routes