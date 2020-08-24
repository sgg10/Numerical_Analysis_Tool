from . import conversions
from .methods import *

@conversions.route('/to-base-10/<n>&<base>')
def conver_n_to_base_10(n, base):
  result = conver_to_base_10(n, int(base))
  return {
    'inputs': {
      'n': n,
      'base': base
    },
    'result': result
  }

@conversions.route('/float_point_notation/<n>&<base>&<exp>')
def float_point(n, base, exp):
  return {
    'inputs': {
      'n': n,
      'base': base,
      'exp': exp
    },
    'result': float_point_notation(n, base, exp)
  }