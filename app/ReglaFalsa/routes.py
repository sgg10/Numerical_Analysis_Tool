from . import reglaFalsa
from ..Methods.Intervalos.ReglaFalsa import ReglaFalsa

@reglaFalsa.route('/<xi>&<xs>&<tol>&<iter>&<function>')
def metodoReglaFalsa(xi, xs, tol, iter, function):
  return ReglaFalsa(xi, xs, tol, iter, function).run()