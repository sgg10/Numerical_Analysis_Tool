from flask import Flask
from .Converions import conversions
from .Errors import errors
from .Rounded import rounded
from .Biseccion import biseccion
from .ReglaFalsa import reglaFalsa
from .Newton import newton
from .Secante import secante 
from .PuntoFijo import puntoFijo
from .RaicesMultiples import raicesMultiples
from .BusquedaIncrementales import busquedaIncrementales
from .EliminacionGaussiana import eliminaciongausiana
from .Interpolacion import interpolacion
from .Iterativos import iterativos

def create_app():
  app = Flask(__name__)
  app.register_blueprint(conversions)
  app.register_blueprint(errors)
  app.register_blueprint(rounded)
  app.register_blueprint(biseccion)
  app.register_blueprint(reglaFalsa)
  app.register_blueprint(newton)
  app.register_blueprint(secante)
  app.register_blueprint(puntoFijo)
  app.register_blueprint(raicesMultiples)
  app.register_blueprint(busquedaIncrementales)
  app.register_blueprint(eliminaciongausiana)
  app.register_blueprint(interpolacion)
  app.register_blueprint(iterativos)
  return app