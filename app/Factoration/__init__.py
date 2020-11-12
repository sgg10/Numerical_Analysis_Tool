from flask import Blueprint

factoration = Blueprint('factoration', __name__, url_prefix='/api/factoration')

from . import routes