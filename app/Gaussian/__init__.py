from flask import Blueprint

gaussianElimination = Blueprint('gaussianElimination', __name__, url_prefix='/api/gaussianElimination')

from . import routes