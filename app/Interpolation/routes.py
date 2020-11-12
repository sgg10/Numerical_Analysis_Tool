from . import interpolations
from ..Methods.Interpolation import Lagrange, NewtonPolynomial, SplineLinear, SplineSquared, SplineCubed

@interpolations.route('/lagrange/<n>&<x>&<y>')
def methodLagrangeInterpolation(n, x, y):
  return Lagrange.LagrangeInterpolation(n, list(x), list(y)).run()

@interpolations.route('/newton/<n>&<tabla>')
def methodNewtonInterpolation(n, table):
  return NewtonPolynomial.NewtonInterpolation(n, list(table)).run()

@interpolations.route('/spline/linear/<n>&<x>&<y>')
def methodSplineLinear(n, x, y):
  return SplineLinear.SplineLinear(n, list(x), list(y)).run()

@interpolations.route('/spline/squared/<x>&<y>')
def methodSplineSquared(x, y):
  return SplineSquared.run(list(x), list(y))

@interpolations.route('/spline/cubed/<x>&<y>')
def methodSplineCubed(x, y):
  return SplineCubed.run(list(x), list(y))