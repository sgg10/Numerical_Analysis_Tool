from flask import Blueprint

rounded = Blueprint('rounded', __name__, url_prefix='/api/rounded')

from . import routes