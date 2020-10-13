from . import newton
from ..Methods.Abiertos.Newton import Newton

@newton.route('/<x0>&<tol>&<iter>&<function>')
def metodoNewton(x0, tol, iter, function):
  return Newton(x0, tol, iter, function).run()