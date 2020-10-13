from . import secante
from ..Methods.Abiertos.Secante import Secante

@secante.route('/<x0>&<x1>&<tol>&<iter>&<function>')
def metodoSecante(x0, x1, tol, iter, function):
  return Secante(x0, x1, tol, iter, function).run()