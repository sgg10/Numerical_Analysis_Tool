from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class Newton:
  f = Function('fx')
  df = Function('dfx')
  #comment to try push

  def __init__(self, x0, tol, iteration, function):
    self.x0 = float(x0)
    self.tol = float(tol)
    self.iteration = float(iteration)
    self.function = function
    self.vector = []

  def run(self):
    f = parse_expr(self.function)
    x = Symbol('x')
    df = diff(f, x)
    fx = f.subs(x, self.x0)
    dfx = df.subs(x, self.x0)
    i = 0
    absolute_error = self.tol + 1
    self.vector.append([str(i), str(self.x0), str(fx), str(dfx), "0"])
    while fx != 0 and absolute_error > self.tol and dfx != 0 and i < self.iteration:
      x1 = self.x0 - (fx/dfx)
      fx = f.subs(x, x1)
      dfx = df.subs(x, x1)
      absolute_error = (x1 - self.x0)
      relative_error = absolute_error / x1
      self.x0 = x1
      i += 1
      self.vector.append([str(i), str(self.x0), str(fx), str(dfx), str(relative_error)])
    if fx == 0:
      return { 'result': f'{self.x0} is a root', "iterations": self.vector }
    elif absolute_error < self.tol:
      return { 'result': f'{self.x0} is the approximate root of the function, with a tolerance of: {self.tol}', "iterations": self.vector }
    elif dfx == 0:
      return { 'result': f'{self.x0} is a possible multiple root', "iterations": self.vector }
    else:
      return  { 'result': 'Maximum number of iterations reached', 'iterations': self.vector }