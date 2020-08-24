from . import errors
from ..Methods.Errors import *

@errors.route('/absolute/<x>&<x1>')
def absolute_errors(x, x1):
  result = absolute_error(float(x), float(x1))
  return {
    'inputs': {
      'x': x,
      'x1': x1,
    },
    'result': result
  }

@errors.route('/limit-value/<x>&<E>')
def limits_value_x(x, E):
  reuslt = limit_value_x(float(x), float(E))
  return {
    'inputs': {
      'x': x,
      'E': E
    },
    'result': reuslt
  }

@errors.route('/relative/<x>&<E>')
def relative_errors(x, E):
  result = relative_error(float(x), float(E))
  return {
    'inputs': {
      'x': x,
      'E': E
    },
    'result': result
  }

@errors.route('/relative-without-E/<x>&<x1>')
def relative_without_E(x, x1):
  E = abs(absolute_error(float(x), float(x1)))
  result = relative_error(float(x), float(E))
  return {
    'inputs': {
      'x': x,
      'x1': x1
    },
    'result': result
  }