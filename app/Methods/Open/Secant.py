from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class Secant:
  f = Function('fx')

  def __init__(self, x0, x1, tol, iterations, function):
    self.x0 = float(x0)
    self.x1 = float(x1)
    self.tol = float(tol)
    self.iterations = float(iterations)
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
      absoluteError = self.tol + 1
      denominator = fx1 - fx0
      self.vector.append([str(i), str(self.x0), str(fx0), "0"])
      while fx1 != 0 and absoluteError > self.tol and denominator != 0 and i < self.iterations:
        x2 = (self.x1 - fx1 * (self.x1-self.x0)) / denominator
        absoluteError = abs(x2 - self.x1)
        relativeError = absoluteError / x2  
        self.x0 = self.x1
        self.x1  = x2
        fx1 = f.subs(x, self.x1)
        denominator = fx1 - fx0
        i += 1
        self.vector.append([str(i), str(self.x0), str(fx0), str(relativeError)])
      if fx1 == 0:
        return { 'result': f'{self.x1} is a root', "iterations": self.vector }
      elif absoluteError < self.tol:
        return  { 'result': f'{self.x1} is an approximate root with a tolerance of: {self.tol}', "iterations": self.vector }
      elif denominator == 0:
        return { 'result': f'there is a multi-root {self.x1}', "iterations": self.vector }
      else:
        return { 'result': 'maximum number of iterations reached', 'iterations': self.vector }
