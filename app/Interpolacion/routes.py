from . import interpolacion
from ..Methods.Interpolacion import Larange, Newton_Dif_Divididas

@interpolacion.route('/larange/<n>&<x>&<y>')
def metodoInterpolacionLarange(n, x, y):
  return Larange.InterpolacionLarange(n, list(x), list(y)).run()

@interpolacion.route('/newton/<n>&<tabla>')
def metodoInterpolacionNewton(n, tabla):
  return Newton_Dif_Divididas.InterpolacionNewton(n, list(tabla)).run()