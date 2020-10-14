from . import eliminaciongausiana
from ..Methods.Eliminacion import Gaussiana, Parcial, Total

@eliminaciongausiana.route('/simple/<n>&<A>')
def metodoEliminacionGaussiana(n, A):
  return Gaussiana.EliminacionGaussiana(n, A).run()

@eliminaciongausiana.route('/parcial/<n>&<A>')
def metodoEliminacionGaussianaParcial(n, A):
  return Parcial.EliminacionGaussianaPivoteoParcial(n, A).run()

@eliminaciongausiana.route('/total/<n>&<A>')
def metodoEliminacionGaussianaTotal(n, A):
  return Total.EliminacionGaussianaPivoteoTotal(n, A).run()
