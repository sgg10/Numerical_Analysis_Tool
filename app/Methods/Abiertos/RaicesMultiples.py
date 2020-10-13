from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class RaicesMultiples:
  f = Function('fx')
  df = Function('dfx')
  d2f = Function('d2fx')

  def __init__(self, x0, tol, iteraciones, function):
    self.x0 = float(x0)
    self.tol = float(tol)
    self.iteraciones = float(iteraciones)
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
    errorAbs = self.tol + 1
    denominador = dfx**2 - (fx*d2fx)
    self.vector.append([str(i), str(self.x0), str(fx), str(dfx), str(d2fx), str(errorAbs)])
    while fx != 0 and errorAbs > self.tol and denominador != 0 and i < self.iteraciones:
      x1 = (self.x0 - fx*dfx)/(dfx**2 - (fx*d2fx))
      fx = f.subs(x, x1)
      dfx = df.subs(x, x1)
      d2fx = d2f.subs(x, x1)
      errorAbs = abs(x1 - self.x0)
      self.x0 = x1
      i += 1
      self.vector.append([str(i), str(self.x0), str(fx), str(dfx), str(d2fx), str(errorAbs)])
    if fx == 0:
      return { 'result': f'{self.x0} es una raiz', "iters": self.vector }
    elif errorAbs < self.tol:
      return { 'result': f'{self.x0} se aproxima a una raiz de la función, con una tolerancia de: {self.tol}', "iters": self.vector }
    elif dfx == 0:
      return { 'result': f'{self.x0} Es una raiz multiple simple', "iters": self.vector }
    elif d2fx == 0:
      return { 'result': f'{self.x0} Es una raiz multiple de multiplicidad 2', "iters": self.vector }
    else:
      return { 'result': 'Excedio el numero de iteraciones posible', "iters": self.vector }
