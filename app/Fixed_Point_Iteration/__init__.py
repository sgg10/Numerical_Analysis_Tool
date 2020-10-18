from flask import Blueprint

fixed_point_iteration = Blueprint('fixed_point_iteration', __name__, url_prefix='/api/fixed_point_iteration')

from . import routes