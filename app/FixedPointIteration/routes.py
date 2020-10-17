from . import fixedPointIteration
from ..Methods.Open.FixedPointIteration import FixedPointIteration

@fixedPointIteration.route('/<xa>&<tolerance>&<iteration>&<f>&<g>')
def fixedPointIterationMethod(xa, tolerance, iteration, f, g):
  return FixedPointIteration(xa, tolerance, iteration, f, g).run()
