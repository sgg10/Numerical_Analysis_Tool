from . import gaussian_elimination
from ..Methods.Elimination import Gaussian, Partial_Pivot, Total_Pivot

@gaussian_elimination.route('/simple/<n>&<A>')
def gaussian_elimination_method(n, A):
  return Gaussian.Gaussian_Elimination(n, A).run()

@gaussian_elimination.route('/Partial_Pivot/<n>&<A>')
def gaussian_elimination_partial_pivot_method(n, A):
  return Partial_Pivot.Gaussian_Elimination_Partial_Pivot(n, A).run()

@gaussian_elimination.route('/Total_Pivot/<n>&<A>')
def gaussian_elimination_total_pivot_method(n, A):
  return Total_Pivot.Gaussian_Elimination_Total_Pivot(n, A).run()
