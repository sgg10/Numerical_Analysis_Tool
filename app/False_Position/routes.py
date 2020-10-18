from . import false_position
from ..Methods.Intervals.False_Position import False_Position

@false_position.route('/<xi>&<xs>&<tolerance>&<iteration>&<function>')
def false_position_method(xi, xs, tolerance, iteration, function):
  return False_Position(xi, xs, tolerance, iteration, function).run()