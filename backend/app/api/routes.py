from . import api
from .methods import Errors

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