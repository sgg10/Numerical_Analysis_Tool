from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class Incremental_Search:
  f = Function('fx')
  def __init__(self, x0, delta, iteration, function):
    self.x0 = float(x0)
    self.delta = float(delta)
    self.iteration = float(iteration)
    self.function = function

  def run(self):
    f = parse_expr(self.function)
    x = Symbol('x')
    fx0 = f.subs(x, self.x0)
    if fx0 == 0:
      return { 'result': f'{self.x0} is a root' }
    else:
      x1 = self.x0 + self.delta
      i = 1
      fx1 = f.subs(x, x1)
      while fx0*fx1 > 0 and i < self.iteration:
        self.x0 = x1
        fx0 = fx1
        x1 = self.x0 + self.delta
        fx1 = f.subs(x, x1)
        i = i + 1
      if fx1 == 0:
        return { 'result': f'{x1} is a root' }
      elif fx0 * fx1 < 0:
        return { 'result': f'There is a root between {self.x0} and {x1}' }
      else:
        return { 'result': 'Maximum number of iterations reached' }
