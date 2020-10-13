from . import biseccion
from ..Methods.Biseccion import Biseccion

@biseccion.route('/<xi>&<xs>&<tol>&<iter>&<function>')
def metodoBiseccion(xi, xs, tol, iter, function):
  return Biseccion(xi, xs, tol, iter, function).run()