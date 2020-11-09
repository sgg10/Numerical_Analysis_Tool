from . import iterativos
from ..Methods.Iterativos import GaussSeidel, Jacobi

@iterativos.route('/gaussseidel/<n>&<A>&<b>&<x0>&<niter>&<tol>')
def metodoGaussSeidel(n, A, b, x0, niter, tol):
  return GaussSeidel.GaussSeidel(n, A, b, x0, niter, tol).run()

@iterativos.route('/jacobi/<n>&<A>&<b>&<x0>&<niter>&<tol>')
def metodoJacobi(n, A, b, x0, niter, tol):
  return Jacobi.Jacobi(n, A, b, x0, niter, tol).run()

  'localhost/api/iterativos/gaussseidel/'