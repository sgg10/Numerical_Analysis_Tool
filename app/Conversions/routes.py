from . import conversions
from ..Methods.Conversions import *

@conversions.route('/convert_to_base_10/<n>&<base>')
def convert_to_base_10_method(n, base):
  result = convert_to_base_10(n, int(base))
  return {
    'inputs': {
      'n': n,
      'base': base
    },
    'result': result
  }

@conversions.route('/pointing_float_notation/<n>&<base>&<exp>')
def pointing_float_notation_method(n, base, exp):
  return {
    'inputs': {
      'n': n,
      'base': base,
      'exp': exp
    },
    'result': pointing_float_notation(n, base, exp)
  }

@conversions.route('/convert_decimal_to_binary/<n>')
def convert_decimal_to_binary_method(n):
  return {
    'inputs': {
      'n': n
    },
    'result': convert_decimal_to_binary(n)
  }