from . import gaussianElimination
from ..Methods.Eliminacion import Gaussian, Parcial, Total

@gaussianElimination.route('/simple/<n>&<A>')
def gaussianEliminationMethod(n, A):
  return Gaussian.GaussianElimination(n, A).run()

@gaussianElimination.route('/parcial/<n>&<A>')
def gaussianEliminationMethodParcial(n, A):
  return Parcial.EliminacionGaussianaPivoteoParcial(n, A).run()

@gaussianElimination.route('/total/<n>&<A>')
def gaussianEliminationMethodTotal(n, A):
  return Total.EliminacionGaussianaPivoteoTotal(n, A).run()
