from flask import Blueprint

conversions = Blueprint('conversions', __name__, url_prefix='/api/conversions')

from . import routes