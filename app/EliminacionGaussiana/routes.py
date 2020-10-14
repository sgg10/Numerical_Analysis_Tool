from . import eliminaciongausiana
from ..Methods.Eliminacion.Gaussiana import EliminacionGaussiana

@eliminaciongausiana.route('/<n>&<A>')
def metodoBusquedasIncrementales(n, A):
  return EliminacionGaussiana(n, A).run()