from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class Secant:
  f = Function('fx')

  def __init__(self, x0, x1, tolerance, iteration, function):
    self.x0 = float(x0)
    self.x1 = float(x1)
    self.tolerance = float(tolerance)
    self.iteration = float(iteration)
    self.function = function
    self.vector = []

  def run(self):
    f = parse_expr(self.function)
    x = Symbol('x')
    fx0 = f.subs(x, self.x0)

    if fx0 == 0:
      return { 'result': f'{self.x0} is a root' }
    else:
      fx1 = f.subs(x, self.x1)
      i = 0
      absolute_error = self.tolerance + 1
      denominator = fx1 - fx0
      self.vector.append([str(i), str(self.x0), str(fx0), "0"])
      while fx1 != 0 and absolute_error > self.tolerance and denominator != 0 and i < self.iteration:
        x2 = (self.x1 - fx1 * (self.x1-self.x0)) / denominator
        absolute_error = abs(x2 - self.x1)
        relative_error = absolute_error / x2  
        self.x0 = self.x1
        self.x1  = x2
        fx1 = f.subs(x, self.x1)
        denominator = fx1 - fx0
        i += 1
        self.vector.append([str(i), str(self.x0), str(fx0), str(relative_error)])
      if fx1 == 0:
        return { 'result': f'{self.x1} is a root', "iterations": self.vector }
      elif absolute_error < self.tolerance:
        return  { 'result': f'{self.x1} is an approximate root with a tolerance of: {self.tolerance}', "iterations": self.vector }
      elif denominator == 0:
        return { 'result': f' There is a multi-root {self.x1}', "iterations": self.vector }
      else:
        return { 'result': 'Maximum number of iterations reached', 'iterations': self.vector }
