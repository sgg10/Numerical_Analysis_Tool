from . import newton
from ..Methods.Open.Newton import Newton

@newton.route('/<x0>&<tolerance>&<iteration>&<function>')
def newton_method(x0, tolerance, iteration, function):
  return Newton(x0, tolerance, iteration, function).run()