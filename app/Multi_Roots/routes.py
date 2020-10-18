from . import multi_roots
from ..Methods.Open.Multi_Roots import Multi_Roots

@multiRoots.route('/<x0>&<tolerance>&<iteration>&<function>')
def multi_root_method(x0, tolerance, iteration, function):
  return Multi_Roots(x0, tolerance, iteration, function).run()