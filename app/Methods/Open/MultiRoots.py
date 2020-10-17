from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class MultiRoots:
  f = Function('fx')
  df = Function('dfx')
  d2f = Function('d2fx')

  def __init__(self, x0, tol, iterations, function):
    self.x0 = float(x0)
    self.tol = float(tol)
    self.iterations = float(iterations)
    self.function = function
    self.vector = []

  def run(self):
    f = parse_expr(self.function)
    x = Symbol('x')
    df = diff(f, x)
    d2f = diff(df, x)
    fx = f.subs(x, self.x0)
    dfx = df.subs(x, self.x0)
    d2fx = d2f.subs(x, self.x0)
    i = 0
    abolsuteError = self.tol + 1
    denominator = dfx**2 - (fx*d2fx)
    self.vector.append([str(i), str(self.x0), str(fx), str(dfx), str(d2fx), str(abolsuteError)])
    while fx != 0 and abolsuteError > self.tol and denominator != 0 and i < self.iterations:
      x1 = (self.x0 - fx*dfx)/(dfx**2 - (fx*d2fx))
      fx = f.subs(x, x1)
      dfx = df.subs(x, x1)
      d2fx = d2f.subs(x, x1)
      abolsuteError = abs(x1 - self.x0)
      self.x0 = x1
      i += 1
      self.vector.append([str(i), str(self.x0), str(fx), str(dfx), str(d2fx), str(abolsuteError)])
    if fx == 0:
      return { 'result': f'{self.x0} is a root', "iterations": self.vector }
    elif abolsuteError < self.tol:
      return { 'result': f'{self.x0} is an approximate root with a tolerance of: {self.tol}', "iterations": self.vector }
    elif dfx == 0:
      return { 'result': f'{self.x0} is a single root', "iterations": self.vector }
    elif d2fx == 0:
      return { 'result': f'{self.x0} is a multi-root with a multiplicity of 2', "iterations": self.vector }
    else:
      return { 'result': 'maximum number of iterations reached', "iterations": self.vector }
