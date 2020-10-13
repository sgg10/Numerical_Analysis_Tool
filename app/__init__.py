from flask import Flask
from .Converions import conversions
from .Errors import errors
from .Rounded import rounded
from .Biseccion import biseccion
from .ReglaFalsa import reglaFalsa

def create_app():
  app = Flask(__name__)
  app.register_blueprint(conversions)
  app.register_blueprint(errors)
  app.register_blueprint(rounded)
  app.register_blueprint(biseccion)
  app.register_blueprint(reglaFalsa)
  return app