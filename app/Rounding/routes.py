from . import rounding
from ..Methods.Rounding import default_rounding, symmetrical_rounding_distance, symmetrical_rounding_statistics, excess_round

@rounding.route('/default_rounding/<n>&<figure>')
def default_rounding_method(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': default_rounding(n, figure)
  }

@rounding.route('/symmetrical_rounding_statistics/<n>&<figure>')
def symmetrical_rounding_statistics_method(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': symmetrical_rounding_statistics(n, figure)
  }

@rounding.route('/symmetrical_rounding_distance/<n>&<figure>')
def symmetrical_rounding_distance_method(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': symmetrical_rounding_distance(n, figure)
  }

@rounding.route('/excess_rounding/<n>&<figure>')
def excess_rounding_method(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': excess_rounding(n, figure)
  }