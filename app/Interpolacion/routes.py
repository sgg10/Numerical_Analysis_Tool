from . import interpolacion
from ..Methods.Interpolacion import Larange

@interpolacion.route('/larange/<n>&<x>&<y>')
def metodoInterpolacionLarange(n, x, y):
  return Larange.InterpolacionLarange(n, list(x), list(y)).run()