from . import iterativos
from ..Methods.Iterativos import GaussSeidel, Jacobi, SOR, Vandermonde

@iterativos.route('/gaussseidel/<n>&<A>&<b>&<x0>&<niter>&<tol>')
def metodoGaussSeidel(n, A, b, x0, niter, tol):
  return GaussSeidel.GaussSeidel(n, A, b, x0, niter, tol).run()

@iterativos.route('/jacobi/<n>&<A>&<b>&<x0>&<niter>&<tol>')
def metodoJacobi(n, A, b, x0, niter, tol):
  return Jacobi.Jacobi(n, A, b, x0, niter, tol).run()

@iterativos.route('/sor/<n>&<A>&<b>&<x0>&<omega>&<niter>&<tol>')
def metodoSOR(n, A, b, x0, omega, niter, tol):
  return SOR.SOR(n, A, b, x0, omega, niter, tol).run()

@iterativos.route('/vandermonde/<x>')
def metodoVandermonde(x):
  x = x.replace('[', '').replace(']', '').split(',')
  print(x)
  for i in range(len(x)):
    x[i] = float(x[i])
  return Vandermonde.Vandermonde(x).run()
