from . import factorizacion
from ..Methods.Factorizacion import cholesky, doolittle, croult

@factorizacion.route('/cholesky/<n>&<A>&<B>')
def metodoCholesky(n, A, B):
  return cholesky.Cholesky(n, A, B).run()

@factorizacion.route('/doolittle/<n>&<A>&<B>')
def metodoDoolittle(n, A, B):
  return doolittle.Dolittle(n, A, B).run()

@factorizacion.route('/croult/<n>&<A>&<B>')
def metodoCroult(n, A, B):
  return croult.Croult(n, A, B).run()