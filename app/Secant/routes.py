from . import secant
from ..Methods.Open.Secant import Secant

@secant.route('/<x0>&<x1>&<tol>&<iter>&<function>')
def secantMethod(x0, x1, tol, iter, function):
  return Secant(x0, x1, tol, iter, function).run()