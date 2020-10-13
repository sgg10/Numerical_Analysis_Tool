from . import puntoFijo
from ..Methods.Abiertos.PuntoFijo import PuntoFijo

@puntoFijo.route('/<xa>&<tol>&<iter>&<f>&<g>')
def metodoPuntoFijo(xa, tol, iter, f, g):
  return PuntoFijo(xa, tol, iter, f, g).run()