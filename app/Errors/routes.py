from . import errors
from ..Methods.Errors import *

@errors.route('/absolute_error/<x>&<x1>')
def absolute_error_method(x, x1):
  result = absolute_error(float(x), float(x1))
  return {
    'inputs': {
      'x': x,
      'x1': x1,
    },
    'result': result
  }

@errors.route('/limit_value_x/<x>&<E>')
def limit_value_x_method(x, E):
  result = limit_value_x(float(x), float(E))
  return {
    'inputs': {
      'x': x,
      'E': E
    },
    'result': result
  }

@errors.route('/relative_error/<x>&<E>')
def relative_error_method(x, E):
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