from . import factoration
from ..Methods.Factoration import cholesky, doolittle, croult, LUPartial, LUSimple

@factoration.route('/cholesky/<n>&<A>&<B>')
def methodCholesky(n, A, B):
  return cholesky.Cholesky(n, A, B).run()

@factoration.route('/doolittle/<n>&<A>&<B>')
def methodDoolittle(n, A, B):
  return doolittle.Dolittle(n, A, B).run()

@factoration.route('/croult/<n>&<A>&<B>')
def methodCroult(n, A, B):
  return croult.Croult(n, A, B).run()

@factoration.route('/partial_lu/<A>&<b>')
def partialLUMethod(A, b):
  return LUPartial.PartialLU(A, b).run()

@factoration.route('/total_lu/<A>&<b>&<n>')
def totalLUMethod(A, b, n):
  return LUSimple.LU_Simple(A, b, n).run()