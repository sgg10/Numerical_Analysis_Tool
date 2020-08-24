from . import rounded
from ..Methods.Rounded import default_round, symmetrical_round_distance, symmetrical_round_statistics, excess_round

@rounded.route('/default_round/<n>&<figure>')
def defaults_round(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': default_round(n, figure)
  }

@rounded.route('/symmetrical_round_statistics/<n>&<figure>')
def symmetrical_round(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': symmetrical_round_statistics(n, figure)
  }

@rounded.route('/symmetrical_round_distance/<n>&<figure>')
def symmetrical_round_distances(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': symmetrical_round_distance(n, figure)
  }

@rounded.route('/excess_round/<n>&<figure>')
def excess_rounds(n, figure):
  return {
    'inputs': {
      'n': n,
      'figure': figure 
    },
    'result': excess_round(n, figure)
  }