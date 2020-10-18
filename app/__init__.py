from flask import Flask
from .Conversions import conversions
from .Errors import errors
from .Rounding import rounding
from .Bisection import bisection
from .False_Position import false_position
from .Newton import newton
from .Secant import secant
from .Fixed_Point_Iteration import fixed_point_iteration
from .Multi_Roots import multi_roots
from .Incremental_Search import incremental_search

def create_app():
  app = Flask(__name__)
  app.register_blueprint(conversions)
  app.register_blueprint(errors)
  app.register_blueprint(rounding)
  app.register_blueprint(bisection)
  app.register_blueprint(false_position)
  app.register_blueprint(newton)
  app.register_blueprint(secant)
  app.register_blueprint(fixed_point_iteration)
  app.register_blueprint(multi_roots)
  app.register_blueprint(incremental_search)
  return app