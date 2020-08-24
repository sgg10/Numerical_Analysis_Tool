from . import api
from .methods import Errors, Conversions, Rounded

@api.route('/test')
def test():
  return {"msg": "Test"}

@api.route('/methods/errors/absolute/<x>&<x1>')
def absolute_error(x, x1):
  result = Errors.absolute_error(float(x), float(x1))
  return {
    'inputs': {
      'x': x,
      'x1': x1,
    },
    'result': result
  }

@api.route('/methods/errors/limit-value/<x>&<E>')
def limit_value_x(x, E):
  reuslt = Errors.limit_value_x(float(x), float(E))
  return {
    'inputs': {
      'x': x,
      'E': E
    },
    'result': reuslt
  }

@api.route('/methods/errors/relative/<x>&<E>')
def relative_error(x, E):
  result = Errors.relative_error(float(x), float(E))
  return {
    'inputs': {
      'x': x,
      'E': E
    },
    'result': result
  }

@api.route('/methods/errors/relative-without-E/<x>&<x1>')
def relative_without_E(x, x1):
  E = abs(Errors.absolute_error(float(x), float(x1)))
  result = Errors.relative_error(float(x), float(E))
  return {
    'inputs': {
      'x': x,
      'x1': x1
    },
    'result': result
  }

@api.route('/methods/conversions/to-base-10/<n>&<base>')
def conver_to_base_10(n, base):
  result = Conversions.conver_to_base_10(n, int(base))
  return {
    'inputs': {
      'n': n,
      'base': base
    },
    'result': result
  }

@api.route('/methods/conversions/float_point_notation/<n>&<base>&<exp>')
def float_point_notation(n, base, exp):
  return {
    'inputs': {
      'n': n,
      'base': base,
      'exp': exp
    },
    'result': Conversions.float_point_notation(n, base, exp)
  }

@api.route('/methods/rounded/default_round/<n>&<figure>')
def default_round(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': Rounded.default_round(n, figure)
  }

@api.route('/methods/rounded/symmetrical_round_statistics/<n>&<figure>')
def symmetrical_round(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': Rounded.symmetrical_round_statistics(n, figure)
  }

@api.route('/methods/rounded/symmetrical_round_distance/<n>&<figure>')
def symmetrical_round_distance(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': Rounded.symmetrical_round_distance(n, figure)
  }

@api.route('/methods/rounded/excess_round/<n>&<figure>')
def excess_round(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': Rounded.excess_round(n, figure)
  }