from flask import Blueprint

eliminaciongausiana = Blueprint('eliminaciongausiana', __name__, url_prefix='/api/eliminaciongausiana')

from . import routes