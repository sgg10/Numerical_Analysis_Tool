from flask import Blueprint

biseccion = Blueprint('biseccion', __name__, url_prefix='/api/biseccion')

from . import routes