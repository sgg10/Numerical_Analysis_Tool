from . import bisection
from ..Methods.Intervals.Bisection import Bisection

@bisection.route('/<xi>&<xs>&<tolerance>&<iteration>&<function>')
def bisection_method(xi, xs, tolerance, iteration, function):
  return Bisection(xi, xs, tolerance, iteration, function).run()