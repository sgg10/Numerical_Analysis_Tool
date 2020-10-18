from . import fixed_point_iteration
from ..Methods.Open.Fixed_Point_Iteration import Fixed_Point_Iteration

@fixed_point_iteration.route('/<xa>&<tolerance>&<iteration>&<f>&<g>')
def fixed_point_iteration_method(xa, tolerance, iteration, f, g):
  return Fixed_Point_Iteration(xa, tolerance, iteration, f, g).run()
