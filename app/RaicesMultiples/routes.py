from . import raicesMultiples
from ..Methods.Abiertos.RaicesMultiples import RaicesMultiples

@raicesMultiples.route('/<x0>&<tol>&<iter>&<function>')
def metodoRaicesMultiples(x0, tol, iter, function):
  return RaicesMultiples(x0, tol, iter, function).run()