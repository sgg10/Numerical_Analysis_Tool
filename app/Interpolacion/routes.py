from . import interpolacion
from ..Methods.Interpolacion import Larange, Newton_Dif_Divididas, SplineLineal, SplineCuadratico, SplineCubico

@interpolacion.route('/larange/<n>&<x>&<y>')
def metodoInterpolacionLarange(n, x, y):
  return Larange.InterpolacionLarange(n, list(x), list(y)).run()

@interpolacion.route('/newton/<n>&<tabla>')
def metodoInterpolacionNewton(n, tabla):
  return Newton_Dif_Divididas.InterpolacionNewton(n, list(tabla)).run()

@interpolacion.route('/spline/lineal/<n>&<x>&<y>')
def metodoInterpolacionSplineLineal(n, x, y):
  return SplineLineal.SplineLineal(n, list(x), list(y)).run()

@interpolacion.route('/spline/cuadratico/<x>&<y>')
def metodoInterpolacionSplineCuadratico(x, y):
  return SplineCuadratico.run(list(x), list(y))

@interpolacion.route('/spline/cubico/<x>&<y>')
def metodoInterpolacionSplineCubico(x, y):
  return SplineCuadratico.run(list(x), list(y))