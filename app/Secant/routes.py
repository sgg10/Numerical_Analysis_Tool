from . import secant
from ..Methods.Open.Secant import Secant

@secant.route('/<x0>&<x1>&<tolerance>&<iteration>&<function>')
def secant_method(x0, x1, tolerance, iteration, function):
  return Secant(x0, x1, tolerance, iteration, function).run()