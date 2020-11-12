from . import iterative
from ..Methods.Iterative import GaussSeidel, Jacobi, SOR, Vandermonde

@iterative.route('/gaussseidel/<n>&<A>&<b>&<x0>&<niterations>&<tolerance>')
def methodGaussSeidel(n, A, b, x0, niterations, tolerance):
  return GaussSeidel.GaussSeidel(n, A, b, x0, niterations, tolerance).run()

@iterative.route('/jacobi/<n>&<A>&<b>&<x0>&<niterations>&<tolerance>')
def methodJacobi(n, A, b, x0, niterations, tolerance):
  return Jacobi.Jacobi(n, A, b, x0, niterations, tolerance).run()

@iterative.route('/sor/<n>&<A>&<b>&<x0>&<omega>&<niterations>&<tolerance>')
def methodSOR(n, A, b, x0, omega, niterations, tolerance):
  return SOR.SOR(n, A, b, x0, omega, niterations, tolerance).run()

@iterative.route('/vandermonde/<x>')
def methodVandermonde(x):
  x = x.replace('[', '').replace(']', '').split(',')
  print(x)
  for i in range(len(x)):
    x[i] = float(x[i])
  return Vandermonde.Vandermonde(x).run()
