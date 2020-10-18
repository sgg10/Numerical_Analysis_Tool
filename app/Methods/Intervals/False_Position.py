from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class False_Position:
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
    elif fxi * fxs < 0:
      xm = (self.xi - (fxi * (self.xi - self.xs))) / (fxi-fxs)
      fxm = f.subs(x, xm)
      i = 1
      error = self.tolerance + 1
      self.vector.append([str(i), str(self.xs), str(xm), str(self.xi), str(fxm), str(error)])
      while fxm != 0 and error > self.tolerance and i < self.iteration:
        if fxi * fxm < 0:
          self.xs = xm
          fxs = f.subs(x, self.xi)
          self.vector.append([str(i), str(self.xs), str(xm), str(self.xi), str(fxm), str(error)])
        else:
          self.xi = xm
          fxi = f.subs(x, self.xi)
        xaux = xm
        xm = (self.xi - (fxi * (self.xi - self.xs))) / (fxi-fxs)
        fxm = f.subs(x, xm)
        error = abs(xm - xaux)
        i += 1
        self.vector.append([str(i), str(self.xs), str(xm), str(self.xi), str(fxm), str(error)])
      if fxm == 0:
        return { 'result': f'{repr(xm)} is a root', 'iterations': self.vector }
      elif error < self.tolerance:
        return { 'result': f'{repr(xm)} is an approximate root with a toleranceeration of: {self.tolerance}', 'iterations': self.vector }
      else:
        return { 'result': 'Maximum number of iterations reached', 'iterations': self.vector }
    else:
      return { 'result': 'The interval entered does not meet the requirements to find the root, change parameters or use a different method' }