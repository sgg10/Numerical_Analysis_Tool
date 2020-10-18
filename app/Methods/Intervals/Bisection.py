from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class Bisection():
  f = Function('fx')

  def __init__(self, xi, xs, tolerance, iteration, function):
    self.xi = float(xi)
    self.xs = float(xs)
    self.tolerance = float(tolerance)
    self.iteration = float(iteration)
    self.function = function
    self.vector = []

  def run(self):
    f = parse_expr(self.function)
    x = Symbol('x')
    fxi = f.subs(x, self.xi)
    fxs = f.subs(x, self.xs)
    if fxi == 0:
      return { 'result': f'{repr(self.xi)} is a root' }
    elif fxs == 0:
      return { 'result': f'{repr(self.xs)} is a root' }
    elif fxi * fxs > 0:
      return { 'result': 'The interval does not contain a root' }
    else:
      xm = (self.xi + self.xs) / 2
      i = 1
      fxm = f.subs(x, xm)
      error = self.tolerance + 1
      self.vector.append([str(i), str(self.xs), str(xm), str(self.xi), str(fxm), str(error)])
      while fxm != 0 and error > self.tolerance and i < self.iteration:
        if fxi * fxm < 0:
          self.xs = xm
          fxs = f.subs(x, self.xs)
          self.vector.append([str(i), str(self.xs), str(xm), str(self.xi), str(fxm), str(error)])
        else:
          self.xi = xm
          fxi = f.subs(x, self.xi)

        xaux = xm
        xm = (self.xi + self.xs) / 2
        fxm = f.subs(x, xm)
        error = abs(xm - xaux)
        i += 1
        self.vector.append([str(i), str(self.xs), str(xm), str(self.xi), str(fxm), str(error)])
      if fxm == 0:
        return { 'result': f'{repr(xm)} is a root', 'iterations': self.vector } 
      elif error < self.tolerance:
        return { 'result': f'{repr(xm)} is an approximate root with a tolerance of: {self.tolerance}', 'iterations': self.vector }  
      else:
        return { 'result': 'maximum number of iterations reached', 'iterations': self.vector } 
