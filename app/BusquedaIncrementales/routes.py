from . import busquedaIncrementales
from ..Methods.Intervalos.BusquedaIncrementales import BusquedasIncrementales

@busquedaIncrementales.route('/<x0>&<delta>&<iter>&<function>')
def metodoBusquedasIncrementales(x0, delta, iter, function):
  return BusquedasIncrementales(x0, delta, iter, function).run()